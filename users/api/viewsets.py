from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from users.api.serializers import UserSerializer
from users.models import User


def check_required_fields(data, required_fields):
    for field in required_fields.keys():
        if not data.get(field):
            raise ValidationError({field: ['%s is required.' % required_fields.get(field)]})


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = ()
    authentication_classes = ()
    http_method_names = ['post']

    @list_route(methods=['POST'])
    def login(self, request):
        data = request.data
        required_fields = {
            'phone': 'Phone Number',
            'password': 'Password',
        }
        check_required_fields(data, required_fields)
        user = authenticate(phone=data.get('phone'), password=data.get('password'))
        if user:
            login(request, user)
            return Response(user.data)
        else:
            raise ValidationError({'__form__': ['Invalid email or password']})

    @list_route(methods=['POST'])
    def logout(self, request):
        logout(request)
        return Response({})