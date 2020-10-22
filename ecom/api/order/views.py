from json.encoder import JSONEncoder
from django.http import request
from rest_framework import viewsets
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .serializers import OrderSerializers
from .models import Order
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def validate_user_session(id, token):
    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(pk=id)
        if user.session_token == token:
            return True
        return False
    except UserModel.DoesNotExist:
        return False


@csrf_exempt
def add(request, id, token):
    if not validate_user_session(id, token):
        return JsonResponse({'error': 'Please re-login', 'code': '1'})

    if request.method == "POST":
        user_id = id
        transation_id = request.POST['transation_id']
        amount = request.POST['amount']
        products = request.POST['products']

        total_pro = len(products.split(',')[:-1])

        UserModel = get_user_model()

        try:
            user = UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return JsonResponse({'error': 'user Doesn\'t Exists'})

        ordr = Order(user=user, product_name=products,
                     total_products=total_pro, transation_id=transation_id, total_amount=amount)

        ordr.save()

        return JsonResponse({'success': True, 'error': False, 'msg': 'Order Place Successfully'})


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializers
    queryset = Order.objects.all().order_by('product_name')
