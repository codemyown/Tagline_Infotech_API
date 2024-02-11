from django.shortcuts import render
from rest_framework import generics
from .models import Purchase,Product
from .serializers import ProductSerializer,PurchaseSerializer,UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated,IsAdminUser,BasePermission
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken



class RegisterView(APIView):
    def post(self,request):
        username = request.data['username']
        password = request.data['password']
        
        user = User(username = username)
        user.set_password(password)
        user.save()

        refresh = RefreshToken.for_user(user)
        print(username)
        print(password)

        return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token)
        })







# class WriteByAdminOnlyPermission(BasePermission):
#     def has_permission(self, request, view):
#         user = request.user
#         if request.method == "GET":
#             return True
#         if request.method == "POST" or request.method == "PUT" or request.method == "DELETE":
#             if user.is_superuser:
#                 return True
#         return False



            


class UserListView(generics.ListAPIView,generics.CreateAPIView):

    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class ProductListView(generics.ListAPIView,generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

class ProductUpdateView(generics.UpdateAPIView,generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer   
    
    
class PurchaseListView(generics.ListAPIView,generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    

class PurchaseUpdateView(generics.UpdateAPIView,generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    


    