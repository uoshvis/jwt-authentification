from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
# from rest_framework import permissions
from jwtauthapp.serializers import MemberSerializer
from jwtauthapp.models import Member
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class MemberViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    model = Member
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, )
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def create(self, request):
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        # username = request.data.get('username')
        # email = request.data.get('email')
        # password = request.data.get('password')
        datalist = [first_name, last_name]
        # for item in ['username', 'email', 'password']:
        #     if not request.data.get(item):            

        if '' in datalist:
            respstatus = status.HTTP_406_NOT_ACCEPTABLE
            data = None

        else:
            queryset = Member.objects.create(
                first_name=first_name,
                last_name=last_name,
            )
            serializer = MemberSerializer(queryset)
            data = serializer.data
            respstatus = status.HTTP_201_CREATED
            print(self.serializer_class(queryset).data)
        return Response(self.serializer_class(queryset).data, status=respstatus)

    def list(self, request):
        queryset = Member.objects.all()
        serializer = MemberSerializer(queryset, many=True)
        data = serializer.data
        return Response(data)

    # def retrieve(self, request, pk=None):
    #     queryset = get_object_or_404(MyUsers, pk=pk)
    #     serializer = UserSerializer(queryset)
    #     data = serializer.data
    #     return Response(data)

    # def update(self, request, pk=None):
    #     queryset = get_object_or_404(MyUsers, pk=pk)
    #     serializer = UserSerializer(queryset, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def destroy(self, request, pk=None):
    #     queryset = get_object_or_404(MyUsers, pk=pk)
    #     queryset.delete()
    #     print('DELETED')
    #     return Response(status=status.HTTP_204_NO_CONTENT)


# pass
# accounts
# viewset
# urls
# model
# serializer
# urls for viewset through router.register
