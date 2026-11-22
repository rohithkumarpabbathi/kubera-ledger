from django.conf import settings
from django.db import models


class Transaction(models.Model):
    TYPES = [("expense", "Expense"), ("income", "Income"), ("saving", "Saving")]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="transactions")
    date = models.DateField()
    type = models.CharField(max_length=10, choices=TYPES)
    category = models.CharField(max_length=60)
    note = models.CharField(max_length=200, blank=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date", "-id"]

    def __str__(self):
        return f"{self.user} {self.date} {self.type} {self.category} {self.amount}"


class Budget(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    percents = models.JSONField(default=dict, blank=True)
    goal_name = models.CharField(max_length=100, blank=True)
    goal_target = models.DecimalField(max_digits=12, decimal_places=2, default=0)
