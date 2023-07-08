from rest_framework import serializers

from app.models import *
class TrainMS(serializers.ModelSerializer):
    class Meta:
        model=Trains
        fields="__all__"