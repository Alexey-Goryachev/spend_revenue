from rest_framework.response import Response
from django.db.models import Sum, F
from .models import SpendStatistic
from revenue.models import RevenueStatistic 
from rest_framework import generics
from .serializers import SpendStatisticSerializer

#get  agregation data model spend 
class SpendStatisticsSummary(generics.ListAPIView):
    serializer_class = SpendStatisticSerializer

    def get(self, request):
        spend_stats = SpendStatistic.objects.values('name', 'date')\
            .annotate(
                total_spend = Sum('spend'),
                total_impressions = Sum('impressions'),
                total_clicks = Sum('clicks'),
                total_conversion = Sum('conversion'),
                revenue_id = F('revenue_id'),
            )

        for stat in spend_stats:
            revenue_stat = RevenueStatistic.objects.filter(name=stat['name'], date=stat['date']).first()
            if revenue_stat:
                stat['revenue'] = revenue_stat.revenue

        return Response(spend_stats)
    
    def get_queryset(self):
        return SpendStatistic.objects.all() 