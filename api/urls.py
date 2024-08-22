from django.urls import path
from api.views import AddCustomer, EditCustomer, AddKontragent, AddOrder, AddProduct, AddViloyatTuman, AddUsers, EditKontragent, EditOrder, EditProduct, EditUsers, EditViloyatTuman, RejectOrdersList

urlpatterns = [
    path("customers/", AddCustomer.as_view(), name="add customer"),
    path("customers/<int:id>/", EditCustomer.as_view(), name="edit customer"),
    path("kontragent/", AddKontragent.as_view(), name="add customer"),
    path("kontragent/<int:id>/", EditKontragent.as_view(), name="edit customer"),
    path("orders/", AddOrder.as_view(), name="add customer"),
    path("orders/<int:id>/", EditOrder.as_view(), name="edit customer"),
    path("products/", AddProduct.as_view(), name="add customer"),
    path("products/<int:id>/", EditProduct.as_view(), name="edit customer"),
    path("users/", AddUsers.as_view(), name="add customer"),
    path("users/<int:id>/", EditUsers.as_view(), name="edit customer"),
    path("viloyatTuman/", AddViloyatTuman.as_view(), name="add customer"),
    path("viloyat/<int:id>/", EditViloyatTuman.as_view(), name="edit customer"),
    path('inactive-customers/<int:days>/', RejectOrdersList.as_view(), name='inactive-customers'),

]