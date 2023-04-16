# from rest_framework.response import Response
# from .models import User
# from rest_framework.views import APIView
# from rest_framework.exceptions import AuthenticationFailed
# import jwt, datetime
# # from rest_framework.authtoken.views import ObtainAuthToken
# # from rest_framework.authtoken.models import Token
# from rest_framework import status
# # from rest_framework.authentication import TokenAuthentication # get user
# from rest_framework.permissions import IsAuthenticated
# # from django.contrib.auth import authenticate, login
# from django.http import HttpResponse 
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView
# from rest_framework_simplejwt.tokens import AccessToken, RefreshToken


# from .models import User
# from .serializers import Userserializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view
from .serializers import Userserializer
from .models import User
import jwt, datetime
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

class login(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed('user not found!')
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')
        tokenr = TokenObtainPairSerializer().get_token(user)  
        tokena = AccessToken().for_user(user)
        tokena['email'] = user.email
        response = Response()
        response.set_cookie(key='jwt', value=tokena, httponly=True)
        response.data = {
            'id':user.id,
            'email':user.email,
            'accessToken':str(tokena),
            'refreshToken': str(tokenr)
        }
        return response
# USER LOGIN
# class login(ObtainAuthToken):
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             # print(f'====================={Token}')
#             token, created =  Token.objects.get_or_create(user=serializer.validated_data['user'])
#             # return Response({'token': token.key})
#             print(token)
#             response = Response()  
#             response.set_cookie('token',f'Token {token.key}',samesite='Lax')
#             return Response({'token': f'Token {token.key}'})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# USER LOGIN
class GetUser(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        # print(request.user)
        user = User.objects.get(username__iexact=request.user)
        serializer = Userserializer(user, many=False)
        # print(serializer.data)
        return Response({
            'user': serializer.data
        })
class Register(APIView):
    def post(self, request):
        serializer = Userserializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        tokenr = TokenObtainPairSerializer().get_token(user)  
        tokena = AccessToken().for_user(user)
        tokena['email'] = user.email
        response = Response()
        response.data = {
            'user':serializer.data,
            'accessToken':str(tokena),
            'refreshToken': str(tokenr)
        }
        return response
# class Register(APIView):
#     def post(self, request):
#         first_name=request.data['first_name']
#         if first_name.isalpha():
#             serializer = Userserializer(data=request.data)
#             print(request.data)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response("first_name cannot contain numbers")
# class wish(APIView):
#     def get(self, request):
#         print("hello")
#         return Response(print('hello'))