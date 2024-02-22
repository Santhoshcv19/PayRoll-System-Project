from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from services.models import Employee
from .serializer import EmployeeSerializer

class EmployeeView(APIView):
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success"})
        else:
            return Response(serializer.errors, status=400)
