from rest_framework import serializers
from .models import Stock, Account, Holding, Transaction, Watchlist



class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = "__all__"


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"


class HoldingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Holding
        fields = "__all__"


class TransactionSerializer(serializers.ModelSerializer):
    stock = StockSerializer(read_only=True)
    account = serializers.SlugRelatedField(
        read_only=True, slug_field="username"
    )

    class Meta:
        model = Transaction
        fields = "__all__"
    # class Meta:
    #     model = Transaction
    #     fields = ['id', 'account', 'stock', 'amount', 'price', 'type', 'date']


class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watchlist
        fields = "__all__"

# class TransactionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Transaction
#         fields = "__all__"