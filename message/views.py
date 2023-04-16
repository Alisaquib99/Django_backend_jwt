from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view
import jwt, datetime
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

from .models import Message, Requests
from .serializer import Requestserilazer

class Messagefunc(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        new_message = Message(
            name=request.data.get('name'),
            sendedBy= request.user,
            message=request.data.get('message')
        )
        new_message.save()
        return Response({
            "success": True
        })


class Requestfunc(APIView):
    def post(self, request):
        serializer = Requestserilazer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            request_saved = serializer.save()
        return Response({
            "success": True
        })

