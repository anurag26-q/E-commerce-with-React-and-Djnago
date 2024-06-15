from django.shortcuts import render

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import User,Profile
from .seralizer import RegisterSeralizer,MyTokenObtainPairSerializer

# Create your views here.


class MytokenObtainApiView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    



class RegisterApiView(generics.CreateAPIView):
    serializer_class= RegisterSeralizer
    queryset=User.objects.all()
    permission_classes = (AllowAny,)

    



