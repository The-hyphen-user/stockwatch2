from requests import Response
from .models import Stock
from rest_framework import response


def addTempData(request):
    print("Adding temp data")
    Stock.objects.create(
        ticker="AAPL",
        name="Apple",
        price=0.00,
    )
    Stock.objects.create(
        ticker="MSFT",
        name="Microsoft",
        price=0.00,
    )
    Stock.objects.create(
        ticker="AMZN",
        name="Amazon",
        price=0.00,
    )
    Stock.objects.create(
        ticker="GOOG",
        name="Google",
        price=0.00,
    )
    Stock.objects.create(
        ticker="TSLA",
        name="Tesla",
        price=0.00,
    )
    Stock.objects.create(
        ticker="NFLX",
        name="Netflix",
        price=0.00,
    )
    print("Done adding temp data")
    return Response("Done adding temp data")

import json
def addRealData(request):
    print("Adding real data")
    json_data = open('./stockdata.json').read()
    data = json.loads(json_data)
    Stock.objects.all().delete()
    for stock in data:
        print('stock',stock.get('displaySymbol'),stock.get('displaySymbol') )

        Stock.objects.create(
            ticker=stock.get('displaySymbol'),
            name=stock.get('description'),
            price=0.00,
        )
    print("Done adding real data")
    return Response(200)
