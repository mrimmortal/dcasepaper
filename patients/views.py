from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, viewsets
from rest_framework.parsers import JSONParser

from .models import Patient,Casepaper
from .serializers import PatientSerializer,CasepaperSerializer


class PatientViewSet(viewsets.ModelViewSet):
     queryset = Patient.objects.all().order_by('name')
     serializer_class = PatientSerializer

class CasepaperViewSet(viewsets.ModelViewSet):
     queryset = Casepaper.objects.all().order_by('cid')
     serializer_class = CasepaperSerializer