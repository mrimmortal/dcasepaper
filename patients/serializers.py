from rest_framework import serializers 
from .models import Patient
from .models import Casepaper
 
class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = '__all__'

class CasepaperSerializer(serializers.ModelSerializer):

    class Meta:
        model = Casepaper
        fields = '__all__'
