from django.urls import include, path
from django.contrib import admin
from spend.views import SpendStatisticsSummary
from revenue.views import RevenueStatisticsSummary  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('spend-statistics/', SpendStatisticsSummary.as_view(), name='spend-statistics-summary'),
    path('revenue-statistics/', RevenueStatisticsSummary.as_view(), name='revenue-statistics-summary'),
]