from rest_framework import generics
from rest_framework.response import Response
from django.db.models import Sum, F
from .models import RevenueStatistic
from .serializers import RevenueStatisticSerializer
from .models import RevenueStatistic
from spend.models import SpendStatistic

#get  agregation data model revenue
class RevenueStatisticsSummary(generics.ListAPIView):
    serializer_class = RevenueStatisticSerializer

    def get(self, request):
        revenue_stats = RevenueStatistic.objects.values('name', 'date')\
            .annotate(
                total_revenue=Sum('revenue'),
                total_spend=Sum('spend__spend'),
                total_impressions=Sum('spend__impressions'),
                total_clicks=Sum('spend__clicks'),
                total_conversion=Sum('spend__conversion'),
                spend_id = F('spend_id'),
            )
        for stat in revenue_stats:
            spend_stat = SpendStatistic.objects.filter(name=stat['name'], date=stat['date']).first()
            if spend_stat:
                stat['spend'] = spend_stat.spend

        return Response(revenue_stats)
    

    def get_queryset(self):
        return RevenueStatistic.objects.all() 
