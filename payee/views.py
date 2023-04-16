from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view
from .models import Payee
import jwt, datetime
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

from .serializers import PayeeSerializer
# class RegisterView(APIView):
class AddPayee(APIView):
    def post(self, request):
        permission_classes = [IsAuthenticated]
        serializer = PayeeSerializer(data=request.data)
        print(request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class GetPayee(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request,userId):
        payee = Payee.objects.filter(user=userId).values()
        serializer = PayeeSerializer(payee,many=True)
        return Response(serializer.data)

class UpdatePayee(APIView):
    permission_classes = [IsAuthenticated]
    def patch(self, request,id):
        payee = Payee.objects.get(id=id)
        serializer=PayeeSerializer(instance=payee,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class DeletePayee(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request,id):
        payee = Payee.objects.get(id=id)
        payee.delete()
        return Response("Item Successfully Deleted")


        