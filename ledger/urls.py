from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("api/transactions/", views.add_transaction),
    path("api/transactions/<int:pk>/", views.delete_transaction),
    path("api/budget/", views.save_budget),
]
