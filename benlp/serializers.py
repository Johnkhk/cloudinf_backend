from rest_framework import serializers
from .models import Summarizer

class SummarizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Summarizer
        fields = ('id', 'context', 'requested_at')