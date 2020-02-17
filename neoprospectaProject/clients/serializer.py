from rest_framework import serializers
from clients.models import Client
# forms.py
class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id','name','age','city')
