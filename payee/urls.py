from django.urls import path, include
from . import views
from .views import AddPayee, DeletePayee,UpdatePayee,GetPayee


urlpatterns = [
    path('getPayee/<str:userId>', GetPayee.as_view()),
    path('updatePayee/<str:id>', UpdatePayee.as_view()),
    path('deletePayee/<str:id>', DeletePayee.as_view()),
    path('addPayee', AddPayee.as_view()),
]