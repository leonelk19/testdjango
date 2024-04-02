from rest_framework import serializers
from .models import market

class marketserializer(serializers.ModelSerializer):
    class Meta:
        model=market
        fields=['id','name','description']