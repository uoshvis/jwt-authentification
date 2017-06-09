from rest_framework import serializers
from jwtauthapp.models import Member


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('username', 'first_name', 'last_name')
