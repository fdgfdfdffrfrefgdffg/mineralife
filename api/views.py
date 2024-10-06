from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
import customers.models
import orders.models
import products.models
import users.models
import korzinka.models
import xarita.models
import ega.models
import autolar.models
import tolov.models
from django.utils.dateparse import parse_date
import kontragent.models
import viloyat.models
import dastavka.models
import dastavkachi.models
from django.shortcuts import get_object_or_404
import tuman.models
import users_img.models
from rest_framework import status
from django.utils import timezone
from .serializers import CustomerSerializer, KorzinkaSerializer, OrdersSerializer, ProductsSerializer, UsersSerializer, KontragentSerializer, ViloyatSerializer, TumanSerializer, TolovSerializer, XaritaSerializer, DastavkaSerializer, DastavkachiSerializer, EgaSerializer, AutosSerializer, Users_imgSerializer
import customers
from .serializers import CustomerStatSerializer, OrderStatSerializer

class LatestThreeObjectsView(APIView):
    def get(self, request):
        latest_objects = orders.models.Order.objects.all().order_by('-created_at')[:3]
        serializer = OrdersSerializer(latest_objects, many=True)
        return Response(serializer.data)

class AllModelsCount(APIView):
    def get(self, request):
        orders_count = orders.models.Order.objects.count()
        users_count = users.models.User.objects.count()
        customers_count = customers.models.Customer.objects.count()
        autos_count = autolar.models.Autolar.objects.count()
        products_count = products.models.Product.objects.count()
        return Response({
            "orderss": orders_count,
            "users": users_count,
            "customers": customers_count,
            "autos": autos_count,
            "products": products_count
        })


class CustomerOrderStatsView(APIView):
    def get(self, request, format=None):
        customers1 = customers.models.Customer.objects.all()
        customer_stats = []

        for customer in customers1:
            orders1 = orders.models.Order.objects.filter(customer_id=customer.id).order_by('sana')
            if orders1.exists():
                first_order = orders1.first()
                order_count = orders1.count()
                customer_stats.append({
                    'customer': CustomerStatSerializer(customer).data,
                    'first_order': OrderStatSerializer(first_order).data,
                    'order_count': order_count
                })

        # Buyurtmalar soniga qarab tartiblash
        sorted_customer_stats = sorted(customer_stats, key=lambda x: x['order_count'], reverse=True)

        return Response({
            'customer_count': customers1.count(),
            'customer_stats': sorted_customer_stats
        })


class AddKorzinka(ListCreateAPIView):
    queryset = korzinka.models.Korzinka.objects.all()
    serializer_class = KorzinkaSerializer

class AddCustomer(ListCreateAPIView):
    queryset = customers.models.Customer.objects.all()
    serializer_class = CustomerSerializer

class EditCustomer(RetrieveUpdateDestroyAPIView):
    queryset = customers.models.Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = 'id'

class AddUsers_img(ListCreateAPIView):
    queryset = users_img.models.UsersImg.objects.all()
    serializer_class = Users_imgSerializer

class EditUsers_img(RetrieveUpdateDestroyAPIView):
    queryset = users_img.models.UsersImg.objects.all()
    serializer_class = Users_imgSerializer
    lookup_field = 'id'


class AddEga(ListCreateAPIView):
    queryset = ega.models.Ega.objects.all()
    serializer_class = EgaSerializer

class EditEga(RetrieveUpdateDestroyAPIView):
    queryset = ega.models.Ega.objects.all()
    serializer_class = EgaSerializer
    lookup_field = 'id'


class AddAutolar(ListCreateAPIView):
    queryset = autolar.models.Autolar.objects.all()
    serializer_class = AutosSerializer

class EditAutolar(RetrieveUpdateDestroyAPIView):
    queryset = autolar.models.Autolar.objects.all()
    serializer_class = AutosSerializer
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


class AddDastavka(ListCreateAPIView):
    queryset = dastavka.models.Dastavka.objects.all()
    serializer_class = DastavkaSerializer

class EditDastavka(RetrieveUpdateDestroyAPIView):
    queryset = dastavka.models.Dastavka.objects.all()
    serializer_class = DastavkaSerializer
    lookup_field = 'id'


class AddDastavkachi(ListCreateAPIView):
    queryset = dastavkachi.models.Dastavkachi.objects.all()
    serializer_class = DastavkachiSerializer

class EditDastavkachi(RetrieveUpdateDestroyAPIView):
    queryset = dastavkachi.models.Dastavkachi.objects.all()
    serializer_class = DastavkachiSerializer
    lookup_field = 'id'


class AddKontragent(ListCreateAPIView):
    queryset = kontragent.models.Kontragent.objects.all()
    serializer_class = KontragentSerializer

class EditKontragent(RetrieveUpdateDestroyAPIView):
    queryset = kontragent.models.Kontragent.objects.all()
    serializer_class = KontragentSerializer
    lookup_field = 'id'


class AddViloyat(ListCreateAPIView):
    queryset = viloyat.models.Viloyat.objects.all()
    serializer_class = ViloyatSerializer

class EditViloyat(RetrieveUpdateDestroyAPIView):
    queryset = viloyat.models.Viloyat.objects.all()
    serializer_class = TumanSerializer
    lookup_field = 'id'

class AddTuman(ListCreateAPIView):
    queryset = tuman.models.Tuman.objects.all()
    serializer_class = TumanSerializer

class EditTuman(RetrieveUpdateDestroyAPIView):
    queryset = tuman.models.Tuman.objects.all()
    serializer_class = TumanSerializer
    lookup_field = 'id'

class GetTuman(ListAPIView):
    serializer_class = TumanSerializer

    def get_queryset(self):
        viloyat_id = self.kwargs.get('viloyat')
        return tuman.models.Tuman.objects.filter(viloyat=viloyat_id)

class GetDastavkaAuto(ListAPIView):
    serializer_class = DastavkaSerializer

    def get_queryset(self):
        auto = self.kwargs.get('auto')
        return dastavka.models.Dastavka.objects.filter(auto=auto)

class GetOrderCustomer(ListAPIView):
    serializer_class = OrdersSerializer

    def get_queryset(self):
        customer_id = self.kwargs.get('customer_id')
        return orders.models.Order.objects.filter(customer_id=customer_id)

class GetUser(ListAPIView):
    serializer_class = UsersSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        return  users.models.User.objects.filter(user_id=user_id)

class GetCustomer(ListAPIView):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        customer_name = self.kwargs.get('customer_name')
        return  customers.models.Customer.objects.filter(customer_name=customer_name)

class GetOrderTuman(ListAPIView):
    serializer_class = OrdersSerializer

    def get_queryset(self):
        tuman = self.kwargs.get('tuman')
        return orders.models.Order.objects.filter(tuman=tuman)

class AddTolov(ListCreateAPIView):
    queryset = tolov.models.Tolov.objects.all()
    serializer_class = TolovSerializer

class EditTolov(RetrieveUpdateDestroyAPIView):
    queryset = tolov.models.Tolov.objects.all()
    serializer_class = TolovSerializer
    lookup_field = 'id'

class DelTolov(APIView):
    def post(self, request, *args, **kwargs):
        sana1 = request.data.get('sana1')
        sana2 = request.data.get('sana2')
        
        if not sana1 or not sana2:
            return Response({"error": "Ikkala sana ham kerak"}, status=status.HTTP_400_BAD_REQUEST)
        
        sana1 = parse_date(sana1)
        sana2 = parse_date(sana2)
        
        if not sana1 or not sana2:
            return Response({"error": "Sana formati noto'g'ri"}, status=status.HTTP_400_BAD_REQUEST)
        
        queryset = tolov.models.Tolov.objects.filter(sana__range=[sana1, sana2])
        for query in queryset:
            query.delete()
        return Response("ok", status=status.HTTP_200_OK)

class GetDastavkaSana(APIView):
    def post(self, request, *args, **kwargs):
        sana1 = request.data.get('sana1')
        sana2 = request.data.get('sana2')
        
        if not sana1 or not sana2:
            return Response({"error": "Ikkala sana ham kerak"}, status=status.HTTP_400_BAD_REQUEST)
        
        sana1 = parse_date(sana1)
        sana2 = parse_date(sana2)
        
        if not sana1 or not sana2:
            return Response({"error": "Sana formati noto'g'ri"}, status=status.HTTP_400_BAD_REQUEST)
        
        queryset = dastavka.models.Dastavka.objects.filter(sana__range=[sana1, sana2])
        serializer_data = DastavkaSerializer(queryset, many=True)
        return Response(serializer_data, status=status.HTTP_200_OK)


class AddXarita(ListCreateAPIView):
    queryset = xarita.models.Xarita.objects.all()
    serializer_class = XaritaSerializer

class EditXarita(RetrieveUpdateDestroyAPIView):
    queryset = xarita.models.Xarita.objects.all()
    serializer_class = XaritaSerializer
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
