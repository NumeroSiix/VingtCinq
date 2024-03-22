from rest_framework import serializers
from .models import Article, Sale


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['code', 'category', 'name', 'manufacturing_cost']


class SaleSerializer(serializers.ModelSerializer):
    article = ArticleSerializer()

    class Meta:
        model = Sale
        fields = ['date', 'author', 'article', 'quantity', 'unit_selling_price']
