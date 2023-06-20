from dataclasses import fields
from rest_framework import serializers

from communities.models import Community

class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = ['id', 'name', 'description']