from rest_framework import serializers
import customers.models
import kontragent.models
import orders.models
import products.models
import kontragent
import viloyat.models
import tuman.models
import users.models
import korzinka.models
import autolar.models
import ega.models
import users
import dastavkachi.models
import tolov.models
import xarita.models
import dastavka.models

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = customers.models.Customer
        fields = "__all__"

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = orders.models.Order
        fields = "__all__"

class KorzinkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = korzinka.models.Korzinka
        fields = "__all__"

class EgaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ega.models.Ega
        fields = "__all__"

class AutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = autolar.models.Autolar
        fields = "__all__"

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = products.models.Product
        fields = "__all__"

class KontragentSerializer(serializers.ModelSerializer):
    class Meta:
        model = kontragent.models.Kontragent
        fields = "__all__"

class ViloyatSerializer(serializers.ModelSerializer):
    class Meta:
        model = viloyat.models.Viloyat
        fields = "__all__"

class TumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = tuman.models.Tuman
        fields = "__all__"

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = users.models.User
        fields = "__all__"

class TolovSerializer(serializers.ModelSerializer):
    class Meta:
        model = tolov.models.Tolov
        fields = "__all__"

class XaritaSerializer(serializers.ModelSerializer):
    class Meta:
        model = xarita.models.Xarita
        fields = "__all__"

class DastavkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = dastavka.models.Dastavka
        fields = "__all__"

class DastavkachiSerializer(serializers.ModelSerializer):
    class Meta:
        model = dastavkachi.models.Dastavkachi
        fields = "__all__"
