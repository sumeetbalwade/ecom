

from django.contrib.auth.models import Permission
from django.http import request
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework import validators
from .serializers import UserSerializers
from .models import CustomUser
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout
import re
import random
from rest_framework.decorators import api_view
# Create your views here.


def get_session_token(length=10):
    return ''.join(random.SystemRandom().choice([chr[i] for i in range(97, 123)]+[str[i] for i in range(10)] for _ in range(length)))


@csrf_exempt
@api_view(['POST'])
def SignIn(request):

    if not request.method == 'POST':
        return JsonResponse({'error': 'Send a Post request with valid parameter by POST Request'})

    username = request.POST['email']
    password = request.POST['password']

    validator = "/[a-z0-9!#$%&'*+ /=?^_`{| }~-]+(?: \.[a-z0-9!  # $%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?/g"

    # if not re.match(validator, username):
    #     return JsonResponse({'error': 'Invalid Email'})

    if len(password) < 3:
        pass

    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(email=username)
        if user.check_password(password):
            usr_dict = UserModel.objects.filter(
                email=username).values().first()
            usr_dict.pop('password')

            if user.session_token != "0":
                user.session_token == "0"
                user.save()
                return JsonResponse({'error': 'Previous Session Exist'})

            token = get_session_token(10)
            user.session_token = token
            user.save()
            login(request, user)
            return JsonResponse({'token': token, 'user': usr_dict})
        else:
            return JsonResponse({'error': 'Invalid Password'})

    except UserModel.DoesNotExist:
        return JsonResponse({'error': 'Invalid Email'})


@api_view(['POST'])
def signout(request, id):
    logout(request)
    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(pk=id)
        user.session_token = "0"
        user.save()
    except UserModel.DoesNotExist:
        return JsonResponse({'error': 'Invalid user id'})

    return JsonResponse({'success': 'Logout Successfully'})


@api_view(['POST'])
class UserViewSet(viewsets.ViewSet):

    queryset = CustomUser.objects.all().order_by('id')
    serializer_class = UserSerializers
    permission_classes_by_action = {'create': [AllowAny]}

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
