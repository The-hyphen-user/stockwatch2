from urllib import request
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
import environ

# from server.stockwatch import serializers
env = environ.Env()
environ.Env.read_env()
apiKey = 'CUKEHSRPBRRPNYX1'


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework import filters
from django.contrib.auth import authenticate, login, logout
from .models import Stock, Account, Watchlist, Holding, Transaction
import requests
import json
from rest_framework.authentication import get_authorization_header
import jwt
from django.contrib.auth.models import User
from django.conf import settings
from .serializers import StockSerializer, WatchlistSerializer, HoldingSerializer, TransactionSerializer
import finnhub

import os
from dotenv import load_dotenv
load_dotenv()
SECRET_KEY = str(os.getenv('FINNHUB_API_KEY'))
finnhub_client = finnhub.Client(api_key=SECRET_KEY)

class TestView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    def get(self, request):
        content = {"message": "Hello, World!"}
        return Response(content)

class PortfolioView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    def get(self, request):
        # token = get_authorization_header(request).decode('utf-8')
        # decoded = jwt.decode(token, settings.SECRET_KEY)
        # print(token)
        # print(self)
        print(request.user)
        # username = request.user.username
        # # username = decoded['username']
        # email = request.user.email
        # password = request.user.password
        # user = authenticate(request, email=email, password=password)
        # if user is not None:
        #     login(request, user)
        #     message = "hello", username
        #     content = {"message": message}
        #     return Response(content)
# user.password, user.balance, user.id, user.watchlist, user.holdings, user.transactions
        account = Account.objects.get(email=request.user.email)
        print(account.username, account.email)
        return JsonResponse({'username': account.username, 'email': account.email, 'balance': account.wealth })

@api_view(['POST', 'DELETE'])
def watchlist(request, ticker):
    if request.method == 'POST':
        #add a stock to the watchlist for user
        account = Account.objects.get(email=request.user.email)
        stock = Stock.objects.get(ticker=ticker)
        #test if stock is already in watchlist
        if Watchlist.objects.filter(account=account, stock=stock).exists():
            return Response("stock already on watchlist", status=status.HTTP_400_BAD_REQUEST)
        else:
            Watchlist.objects.create(stock=stock, account=account)
            return Response("Stock added to watchlist", status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        #remove a stock from the watchlist for user
        account = Account.objects.get(email=request.user.email)
        stock = Stock.objects.get(ticker=ticker)
        Watchlist.objects.filter(stock=stock, account=account).delete()
        return Response("Stock removed from watchlist", status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def getWatchlist(request):
    if request.method == 'GET':
        #get the watchlist for user
        account = Account.objects.get(email=request.user.email)
        watchlist = Watchlist.objects.filter(account=account)
        #return a list of Stock objects
        serializer = WatchlistSerializer(watchlist, many=True)
        #list all stocks linked in watchlist
        stocks = []
        for item in serializer.data:
            stock = Stock.objects.get(id=item['stock'])
            stocks.append(stock)
        #return a list of Stock objects
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def getUserStocks(request):
    if request.method == 'GET':
        account = Account.objects.get(email=request.user.email)
        holdings = Holding.objects.filter(account=account)
        #return a list of Stock objects
        serializer = HoldingSerializer(holdings, many=True)
        #list all stocks linked in holdings
        stocks = []
        for item in serializer.data:
            stock = Stock.objects.get(id=item['stock'])
            stockName = Stock.objects.get(ticker=stock.ticker)
            content = {"ticker": stock.ticker, "name": stockName.name, "amount": item['amount'], "price": getStockPrice(stock.ticker)}
            stocks.append(content)
        return Response(stocks)

@api_view(['POST', 'DELETE'])
def userStocks(request, ticker, amount):
    if request.method == 'POST':
        price = getStockPrice(ticker)
        account = Account.objects.get(email=request.user.email)
        stock = Stock.objects.get(ticker=ticker)
        wealth = account.wealth
        #check if user has enough money to buy stock
        print("price:", price , type(price), "amount:", type(amount), "wealth:", type(wealth))
        if wealth < price * amount:
            return Response("Not enough money to buy stock", status=status.HTTP_400_BAD_REQUEST)
        else:
            account.wealth -= price * amount
            account.save()
        #check if user already owns stock
        if Holding.objects.filter(account=account, stock=stock).exists():
            alreadyOwns = Holding.objects.get(account=account, stock=stock)
            alreadyOwns.amount += amount
            alreadyOwns.save()
        else:
            Holding.objects.create(stock=stock, account=account, amount=amount)
        Transaction.objects.create(stock=stock, account=account, amount=amount, price=price, type="buy")
        return Response("Stock bought", status=status.HTTP_201_CREATED)
    
    elif request.method == 'DELETE':
        account = Account.objects.get(email=request.user.email)
        stock = Stock.objects.get(ticker=ticker)
        price = getStockPrice(ticker)
        wealth = account.wealth
        #check if user owns stock
        if Holding.objects.filter(account=account, stock=stock).exists():
            alreadyOwns = Holding.objects.get(account=account, stock=stock)
            #check if user owns enough stock
            if alreadyOwns.amount < amount:
                return Response("Not enough stock to sell", status=status.HTTP_400_BAD_REQUEST)
            else:
                alreadyOwns.amount -= amount
                alreadyOwns.save()
                account.wealth += price * amount
                account.save()
                Transaction.objects.create(stock=stock, account=account, amount=amount, price=price, type="sell")
                return Response("Stock sold", status=status.HTTP_201_CREATED)
        else:
            return Response("User does not own stock", status=status.HTTP_400_BAD_REQUEST)
    
        
#finnhub api call 60 a minute
def getStockPrice(ticker):
    return finnhub_client.quote(ticker)['c']
        
#alphavantage 5 api calls a min
# def getStockPrice(ticker):
#     url = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={}&apikey={}".format(ticker, apiKey)
#     response = requests.get(url)
#     data = json.loads(response.text)
#     price = data["Global Quote"]["05. price"]
#     name = data["Global Quote"]["01. symbol"]
#     print("price:", price)
#     return float(price)

def UpdateStockPrices():
    import requests
    import json

    # Get the list of all stocks
    stocks = Stock.objects.all()

    # For each stock, get the latest price
    for stock in stocks:
        # Get the stock price
        url = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock.ticker}&apikey={env('ALPHAVANTAGE_API_KEY')}"
        response = requests.get(url)
        data = json.loads(response.text)
        newPrice = data["Global Quote"]["05. price"]
        stock.price = newPrice
        stock.save()

@api_view(['GET'])
def lookup(request, ticker):
    # Get the stock price
    url = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={}&apikey={}".format(ticker, apiKey)
    response = requests.get(url)
    data = json.loads(response.text)
    price = data["Global Quote"]["05. price"]
    name = data["Global Quote"]["01. symbol"]

    # Check if the stock is already in the database
    try:
        stock = Stock.objects.get(ticker=ticker)
    except Stock.DoesNotExist:
        stock = None

    # If the stock is not in the database, add it
    if stock is None:
        stock = Stock(ticker=ticker, name=name, price=price)
        stock.save()

    # Return the stock price
    content = {"price": price, "name": name}
    return Response(content)





class LookupView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    def get(self, request, *args, **kwargs):
        ticker = kwargs.get('ticker')
        # Get the stock price
        url = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={}&apikey={}".format(ticker, apiKey)
        response = requests.get(url)
        data = json.loads(response.text)
        price = data["Global Quote"]["05. price"]
        name = data["Global Quote"]["01. symbol"]

        # Check if the stock is already in the database
        try:
            stock = Stock.objects.get(ticker=ticker)
        except Stock.DoesNotExist:
            stock = None

        # If the stock is not in the database, add it
        if stock is None:
            stock = Stock(ticker=ticker, name=name, price=price)
            stock.save()

        # Return the stock price
        content = {"price": price, "name": name}
        return Response(content)

class SearchView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    def get(self, request, *args, **kwargs):
        query = kwargs.get('query')
        #search for stocks based on name
        Stocks = Stock.objects.filter(name__icontains=query)
        serializer = StockSerializer(Stocks, many=True)
        #use getStockPrice() to get price of each stock
        try:
            for stock in serializer.data[:11]:
                stock['price'] = getStockPrice(stock['ticker'])
        finally:
            return Response(serializer.data)

class TransactionView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    def get(self, request, *args, **kwargs):
        account = Account.objects.get(email=request.user.email)
        transactions = Transaction.objects.filter(account=account)
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)


