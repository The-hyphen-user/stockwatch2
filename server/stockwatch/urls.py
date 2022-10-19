from django.urls import URLPattern, path
from . import views

from . import tmpdata

urlpatterns = [#already at http://127.0.0.1:8000/api/stockwatch/
    # path("register/",)
    path("tempdata/", tmpdata.addTempData, name="tempdata"),
    path("test/<str:ticker>", views.lookup, name="lookup"),
    path("portfolio/", views.PortfolioView.as_view(), name="portfolio"),
    path("lookup/<str:ticker>", views.LookupView.as_view(), name="test"),
    path("search/<str:query>", views.SearchView.as_view(), name="search"),
    path("watchlist/", views.getWatchlist, name="getWatchlist"),  
    path("watchlist/<str:ticker>", views.watchlist, name="watchlist"),
    # path("holding/<str:ticker>", views.HoldingView.as_view(), name="holding"),
    path("stocks/", views.getUserStocks, name="stocks"),
    path("stock/<str:ticker>/<int:amount>", views.userStocks, name="stock"),
    path("transactions/", views.TransactionView.as_view(), name="transactions"),
    path("realdata/", tmpdata.addRealData, name="realdata"),
]