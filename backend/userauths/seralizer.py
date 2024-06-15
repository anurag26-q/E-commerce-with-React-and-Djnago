from django.contrib.auth.password_validation import validate_password


from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import Token


from .models import User,Profile



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['email'] = user.email
        token['full_name'] = user.full_name

        try:
            token['vendor_id']= user.vendor.id
        except:
            token['vendor_id']=0
        return token
    

class RegisterSeralizer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True ,validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password','full_name','phone']
    
    def validate(self, attrs):
       if attrs.get('password') != attrs.get('confirm_password'):
          raise serializers.ValidationError("confirm_password in not match")
       return attrs
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            full_name=validated_data['full_name'],
            phone=validated_data['phone']
        )
        email_username,phone = user.email.split('@')
        user.username = email_username
        user.set_password(validated_data['password'])
        user.save()
        return user






class UserSeralizer(serializers.ModelSerializer):
    class Meta:
       model = User
       fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):    
    class Meta:
       model = Profile
       fields = '__all__'
    
    def to_representation(self, instance):
        data = super(ProfileSerializer, self).to_representation(instance)
        data['user'] = UserSeralizer(instance.user).data
        return data