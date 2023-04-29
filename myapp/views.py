from django.shortcuts import render
from rest_framework import viewsets
from myapp.models import Student, StudentMessges
from rest_framework.views import APIView
from rest_framework.response import Response

from myapp.serializers import StudentSerializer, StudentMessagesSerializer

# Create your views here.
class AllInOneView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentApi(APIView):
    def get(self,request,pk=None, format= None):
        id = pk
        if id is not None:
            stu = StudentMessges.objects.get(id=id)   
            myserialiers = StudentMessagesSerializer(stu)
            return Response(myserialiers.data)
         
        stu = StudentMessges.objects.all()
        print(stu)
        myserialiers = StudentMessagesSerializer(stu,many =True) 
        return Response(myserialiers.data)
    


