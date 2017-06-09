from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from authentication.serializers import MemberSerializer
from authentication.models import Member


class MemeberView(APIView):
    """
    Register a new user.
    """
    serializer_class = MemberSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = Member.objects.all()
        serializer = MemberSerializer(queryset, many=True)
        data = serializer.data
        return Response(data)

    # def post(self, request, format=None):
    #     serializer = self.serializer_class(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
