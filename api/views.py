from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
import customers.models
import orders.models
import products.models
import users.models
import kontragent.models
import viloyattuman.models
from rest_framework import status
from django.utils import timezone
from .serializers import CustomerSerializer, OrdersSerializer, ProductsSerializer, UsersSerializer, KontragentSerializer, ViloyatTumanSerializer
import customers
# Create your views here.

class AddCustomer(ListCreateAPIView):
    queryset = customers.models.Customer.objects.all()
    serializer_class = CustomerSerializer

class EditCustomer(RetrieveUpdateDestroyAPIView):
    queryset = customers.models.Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = 'id'


class AddOrder(ListCreateAPIView):
    queryset = orders.models.Order.objects.all()
    serializer_class = OrdersSerializer

class EditOrder(RetrieveUpdateDestroyAPIView):
    queryset = orders.models.Order.objects.all()
    serializer_class = OrdersSerializer
    lookup_field = 'id'


class AddProduct(ListCreateAPIView):
    queryset = products.models.Product.objects.all()
    serializer_class = ProductsSerializer

class EditProduct(RetrieveUpdateDestroyAPIView):
    queryset = products.models.Product.objects.all()
    serializer_class = ProductsSerializer
    lookup_field = 'id'


class AddUsers(ListCreateAPIView):
    queryset = users.models.User.objects.all()
    serializer_class = UsersSerializer

class EditUsers(RetrieveUpdateDestroyAPIView):
    queryset = users.models.User.objects.all()
    serializer_class = UsersSerializer
    lookup_field = 'id'


class AddKontragent(ListCreateAPIView):
    queryset = kontragent.models.Kontragent.objects.all()
    serializer_class = KontragentSerializer

class EditKontragent(RetrieveUpdateDestroyAPIView):
    queryset = kontragent.models.Kontragent.objects.all()
    serializer_class = KontragentSerializer
    lookup_field = 'id'


class AddViloyatTuman(ListCreateAPIView):
    queryset = viloyattuman.models.ViloyatTuman.objects.all()
    serializer_class = ViloyatTumanSerializer

class EditViloyatTuman(RetrieveUpdateDestroyAPIView):
    queryset = viloyattuman.models.ViloyatTuman.objects.all()
    serializer_class = ViloyatTumanSerializer
    lookup_field = 'id'

class RejectOrdersList(APIView):
    def get(self, request, days):
        # Hozirgi vaqtni olish
        now = timezone.now()
        # Berilgan kundan boshlab vaqtni hisoblash
        past_date = now - timezone.timedelta(days=int(days))
        
        # Berilgan kundan oldin buyurtma bergan mijozlarni topish
        old_orders = orders.models.Order.objects.filter(sana_vaqt__lt=past_date).values('customer_id', 'fio').distinct()
        
        # Yaqin kunlarda buyurtma bergan mijozlarni topish
        recent_orders =  orders.models.Order.objects.filter(sana_vaqt__gte=past_date).values('customer_id').distinct()
        
        # Yaqin kunlarda buyurtma bergan mijozlarni chiqarib tashlash
        inactive_customers = old_orders.exclude(customer_id__in=recent_orders)
        
        # Inactive mijozlarning barcha buyurtmalarining statusini False qilish
        for customer in inactive_customers:
            orders.models.Order.objects.filter(customer_id=customer['customer_id']).update(status=False)
        
        return Response(inactive_customers, status=status.HTTP_200_OK)
