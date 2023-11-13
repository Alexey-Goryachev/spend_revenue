# spend_revenue
This is a two endpoint implementation using the Django REST Framework

endpoint http://127.0.0.1:8000/spend-statistics/  - to view the queryset of the SpendStatistic model divided by date and name, with aggregated sums of spend, impressions, clicks, conversion and related revenue values from the RevenueStatistic model.

endpoint http://127.0.0.1:8000/revenue-statistics/ - to view the queryset of the RevenueStatistic model with division by day (date) and name (name), with aggregated sums of revenue values and related spend, impressions, clicks, conversion values from the SpendStatistic model.

Login to admin:

login - admin

pass - password123
