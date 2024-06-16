from django.shortcuts import render
import random
import shortuuid 

from rest_framework.response import Response
from rest_framework import  status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import User,Profile
from .seralizer import RegisterSeralizer,MyTokenObtainPairSerializer,UserSeralizer

# Create your views here.


class MytokenObtainApiView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    



class RegisterApiView(generics.CreateAPIView):
    serializer_class= RegisterSeralizer
    queryset=User.objects.all()
    permission_classes = (AllowAny,)
def generate_otp(length=7):
        uuid_key = shortuuid.uuid()
        unique_key = uuid_key[0:7]
        # otp = ''.join([str(random.randint(0, 9)) for _ in range(length)])
        return unique_key
class PasswordEmailVerify(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSeralizer
    
    def get_object(self):
        email = self.kwargs['email']
        user = User.objects.get(email=email)
        
        if user:
            user.otp = generate_otp()
            print('user',user)
            user.save()
            uidb64= user.pk
            otp = user.otp

            link = f"http://localhost:5173/create-new-password?otp={otp}&uidb64={uidb64}"
            print("link ",link)
        return user

class PasswordChangeView(generics.CreateAPIView):
     permission_classes = (AllowAny,)
     serializer_class = UserSeralizer

     def create(self, request, *args, **kwargs):
          payload = request.data
          otp= payload.get('otp')
          uidb64= payload.get('uidb64')
        #   reset_token = payload.get('reset_token')
          password = payload.get('password')

          user = User.objects.get(id=uidb64,otp=otp)
          if user:
               user.set_password(password)
            #    user.res = ''
               user.otp = ''
               user.save()
               return Response({'message':'password changed successfully'}, status=status.HTTP_201_CREATED)
          else:
               return Response({'message':'invalid otp'}, stats=status.HTTP_400_BAD_REQUEST)

          
            

    



