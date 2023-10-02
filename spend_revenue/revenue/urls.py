from django.urls import path
from .views import RevenueStatisticsSummary 

urlpatterns = [
    path('revenue-statistics/', RevenueStatisticsSummary.as_view(), name='revenue-statistics-summary'),
]