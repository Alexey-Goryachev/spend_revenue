# from django.urls import path
# from .views import SpendStatisticList

# urlpatterns = [
#     path('spend-statistics/', SpendStatisticList.as_view(), name='spend-statistics-list'),
# ]

# from django.urls import path, include
# from .views import SpendViewSet  # Оновлений імпорт
# from rest_framework import routers
from django.urls import path
from .views import SpendStatisticsSummary 

urlpatterns = [
    path('spend-statistics/', SpendStatisticsSummary.as_view(), name='spend-statistics-summary'),
]