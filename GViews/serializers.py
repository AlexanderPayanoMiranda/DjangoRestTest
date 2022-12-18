from rest_framework import serializers
from GViews.models import SampleUser


class SampleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleUser
        fields = ('username', 'email')
