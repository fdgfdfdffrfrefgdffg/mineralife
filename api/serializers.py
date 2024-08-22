from rest_framework import serializers
import customers.models
import kontragent.models
import orders.models
import products.models
import kontragent
import viloyattuman.models
import users.models
import users

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = customers.models.Customer
        fields = "__all__"

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = orders.models.Order
        fields = "__all__"

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = products.models.Product
        fields = "__all__"

class KontragentSerializer(serializers.ModelSerializer):
    class Meta:
        model = kontragent.models.Kontragent
        fields = "__all__"

class ViloyatTumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = viloyattuman.models.ViloyatTuman
        fields = "__all__"

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = users.models.User
        fields = "__all__"
