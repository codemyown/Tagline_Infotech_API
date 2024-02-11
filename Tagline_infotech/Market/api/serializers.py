from rest_framework import serializers
from .models import Product, Purchase
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'password')

        
        
class ProductSerializer(serializers.ModelSerializer):
    user = UserSerializer(many = True,read_only = True)
    class Meta:
        model = Product
        fields = "__all__"
    
class  PurchaseSerializer(serializers.ModelSerializer):
    user = UserSerializer(many = True,read_only = True)
    product = ProductSerializer(many = True,read_only  = True)
    class Meta:
        model = Purchase
        fields = "__all__"
        
        