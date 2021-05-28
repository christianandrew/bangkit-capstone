from rest_framework import serializers
from .models import classificationModel


class exportSerializers(serializers.ModelSerializer):
    class Meta:
        model = classificationModel
        fields = '__all__'