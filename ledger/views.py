import datetime
import json
from decimal import Decimal, InvalidOperation

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods, require_POST

from .models import Budget, Transaction

TYPES = {"expense", "income", "saving"}


def _state(user):
    b, _ = Budget.objects.get_or_create(user=user)
    entries = [
        {"id": t.id, "date": t.date.isoformat(), "type": t.type, "cat": t.category,
         "note": t.note, "amt": float(t.amount)}
        for t in user.transactions.all()
    ]
    return {"entries": entries,
            "bud": {"total": float(b.total), "pct": b.percents,
                    "goal": {"name": b.goal_name, "target": float(b.goal_target)}}}


def signup(request):
    form = UserCreationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        login(request, form.save())
        return redirect("index")
    return render(request, "registration/signup.html", {"form": form})


@login_required
def index(request):
    name = request.user.first_name or request.user.username.capitalize()
    return render(request, "ledger/index.html", {"state": _state(request.user), "name": name})


@login_required
@require_POST
def add_transaction(request):
    try:
        d = json.loads(request.body)
        amt = Decimal(str(d["amt"]))
        date = datetime.date.fromisoformat(d["date"])
        if d["type"] not in TYPES or amt <= 0:
            raise ValueError
    except (ValueError, KeyError, TypeError, InvalidOperation):
        return JsonResponse({"error": "invalid"}, status=400)
    t = Transaction.objects.create(
        user=request.user, date=date, type=d["type"], amount=amt,
        category=str(d.get("cat", ""))[:60], note=str(d.get("note", ""))[:200])
    return JsonResponse({"id": t.id})


@login_required
@require_http_methods(["DELETE"])
def delete_transaction(request, pk):
    get_object_or_404(Transaction, pk=pk, user=request.user).delete()
    return JsonResponse({"ok": True})


@login_required
@require_POST
def save_budget(request):
    try:
        d = json.loads(request.body)
        total = Decimal(str(d.get("total") or 0))
        goal = d.get("goal") or {}
        target = Decimal(str(goal.get("target") or 0))
        pct = {str(k): float(v) for k, v in (d.get("pct") or {}).items()}
    except (ValueError, TypeError, InvalidOperation, AttributeError):
        return JsonResponse({"error": "invalid"}, status=400)
    b, _ = Budget.objects.get_or_create(user=request.user)
    b.total, b.percents = max(total, 0), pct
    b.goal_name, b.goal_target = str(goal.get("name", ""))[:100], max(target, 0)
    b.save()
    return JsonResponse({"ok": True})
