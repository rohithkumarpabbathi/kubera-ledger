# 🪙 Kubera Ledger

> *"Where did all my money go?"* — every student, every month, 3 days after pocket money arrives.

Kubera is a money-tracking app for broke-but-ambitious students. It writes down every rupee you spend, so you can't pretend that "just one more biryani" never happened.

## What Kubera does
- 📒 Tracks income, expenses and savings (yes, savings. They exist. We checked.)
- 🎯 Budget plan: Food gets a limit, snacks get a limit, "Other" gets a stern look
- 🐷 Savings goal with a progress ring, plus a coin explosion when you save. You'll feel rich for 2 seconds
- 🤝 Friends tracker: "sent ₹200 to Arun" becomes "Arun owes you ₹200". Now he can't forget
- 📊 A 3D yearly graph, so you can watch your expenses rise like a mountain
- 🙋 Your own account, so nobody sees your 2 AM food orders

---

## Way 1: Use it right here on GitHub (no download!) ☁️

GitHub can't run a Django app on its own, but **Codespaces** gives you a free computer in your browser. You need a GitHub account (you have one, congratulations).

1. At the top of this repo, click the green **Code** button.
2. Open the **Codespaces** tab and click **Create codespace on main**.
3. Wait about a minute while a VS Code appears in your browser. Go make chai.
4. In the terminal at the bottom, type these one at a time:
   ```
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver
   ```
5. A popup says *"Open in Browser"*. Click it. Kubera is alive. 🎉
6. Click **Create an account** and start confessing your spending.

Notes: Codespaces gives a free monthly allowance, so stop it when you're done (Codespaces menu → Stop). Your data lives inside your own codespace, so don't delete it unless you want a fresh start.

> ⚠️ **Owner of the repo only:** add these two lines at the very bottom of `kubera/settings.py` so Codespaces works, then push:
> ```
> ALLOWED_HOSTS = ["localhost", "127.0.0.1", ".app.github.dev"]
> CSRF_TRUSTED_ORIGINS = ["https://*.app.github.dev"]
> ```

---

## Way 2: Run it on your own computer 💻

You need **Python 3.10+** (python.org, tick "Add Python to PATH") and **Git**.

```
git clone https://github.com/rohithkumarpabbathi/kubera-ledger.git
cd kubera-ledger
```
No Git? Click **Code → Download ZIP**, extract it, and open a terminal in the folder.

**Windows**
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

**Mac / Linux**
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open **http://127.0.0.1:8000/** and create an account. Your username is how Kubera greets you: *"Good morning, Rohith"*.

**Next time:** activate the venv, run `python manage.py runserver`, and stop it with Ctrl+C. Your data stays on your computer.

---

## Oops, something broke 🔧
| Problem | Fix |
|---|---|
| `python` not recognized | Install Python and tick "Add Python to PATH". Restart the terminal. |
| PowerShell refuses `activate` | Use Command Prompt (`cmd`). It's less dramatic. |
| Port already in use | `python manage.py runserver 8001` |
| Spending is too high | No fix available. Kubera only reports. 🙃 |

## For the grown-ups
Before hosting this publicly, change `DEBUG`, `SECRET_KEY` and `ALLOWED_HOSTS` in `kubera/settings.py`.

Made with ☕ by a student who wants to save money.
