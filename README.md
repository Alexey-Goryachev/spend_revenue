# spend_revenue


endpoint http://127.0.0.1:8000/spend-statistics/  - для просмотру queryset моделі SpendStatistic з поділом по дням (date) та назвою (name), з агрегованими сумами значень spend, impressions, clicks, conversion та пов'язаними значеннями revenue з моделі RevenueStatistic.

endpoint http://127.0.0.1:8000/revenue-statistics/ - для просмотру queryset моделі RevenueStatistic з поділом по дням (date) та назвою (name), з агрегованими сумами значень revenue та пов'язаними значеннями spend, impressions, clicks, conversion з моделі SpendStatistic.

Вход в админку:
Login - admin
pass - password123
