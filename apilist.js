/*
http://127.0.0.1:8000/api/token/
http://127.0.0.1:8000/api/stockwatch/portfolio/
http://127.0.0.1:8000/api/stockwatch/watchlist/
http://127.0.0.1:8000/api/stockwatch/watchlist/AAPL
http://127.0.0.1:8000/api/stockwatch/stocks/
http://127.0.0.1:8000/api/stockwatch/stock/GOOG/1
http://127.0.0.1:8000/api/stockwatch/tempdata/
http://127.0.0.1:8000/api/stockwatch/transactions/





Try instead of doing fields = "__all__", 
explicitly say each field and then 
for the ForeignKeys do '{key}__{field}' 
like for TransactionSerializer do 
fields = ['stock__ticket','date',etc] 
to get the ticket field 
*/