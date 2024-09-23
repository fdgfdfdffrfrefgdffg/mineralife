from django.urls import path
from api.views import AddCustomer, AddUsers_img, AddAutolar, AddEga, AddKorzinka, AddDastavka, AddXarita, AddDastavkachi, AddTolov, EditCustomer , AddKontragent, AddOrder, AddProduct, AddTuman, AddViloyat, GetTuman, AddUsers, EditKontragent, EditOrder, EditProduct, EditUsers, EditTuman, EditViloyat, RejectOrdersList, DelTolov, EditTolov, EditXarita, EditDastavka, GetDastavkaAuto, GetDastavkaSana, GetOrderCustomer, GetOrderTuman, EditDastavkachi, EditAutolar, EditEga, EditUsers_img, CustomerOrderStatsView, GetUser, GetCustomer, LatestThreeObjectsView, AllModelsCount

urlpatterns = [
    path("customers/", AddCustomer .as_view(), name="add  "),
    path("customers/<int:id>/", EditCustomer .as_view(), name="edit  "),
    path("ega/", AddEga.as_view(), name="add  "),
    path("ega/<int:id>/", EditEga.as_view(), name="edit  "),
    path("autolar/", AddAutolar.as_view(), name="add  "),
    path("autolar/<int:id>/", EditAutolar.as_view(), name="edit  "),
    path("korzinka/", AddKorzinka.as_view(), name="add  "),
    path("kontragent/", AddKontragent.as_view(), name="add  "),
    path("kontragent/<int:id>/", EditKontragent.as_view(), name="edit  "),
    path("orders/", AddOrder.as_view(), name="add  "),
    path("orders/<int:id>/", EditOrder.as_view(), name="edit  "),
    path("orders/customer/<int:customer_id>/", GetOrderCustomer.as_view(), name="get  "),
    path("orders/tuman/<str:tuman>/", GetOrderTuman.as_view(), name="get  "),
    path("products/", AddProduct.as_view(), name="add  "),
    path("products/<int:id>/", EditProduct.as_view(), name="edit  "),
    path("users/", AddUsers.as_view(), name="add "),
    path("users/<int:id>/", EditUsers.as_view(), name="edit  "),
    path("users/img/", AddUsers_img.as_view(), name="add  "),
    path("users/img/<int:id>/", EditUsers_img.as_view(), name="edit  "),
    path("viloyat/", AddViloyat.as_view(), name="add  "),
    path("viloyat/<int:id>/", EditViloyat.as_view(), name="edit  "),
    path("tuman/", AddTuman.as_view(), name="add  "),
    path("tuman/<int:id>/", EditTuman.as_view(), name="edit  "),
    path("tolov/", AddTolov.as_view(), name="add  "),
    path("tolov/<int:id>/", EditTolov.as_view(), name="edit  "),
    path("xarita/", AddXarita.as_view(), name="add  "),
    path("xarita/<int:id>/", EditXarita.as_view(), name="edit  "),
    path("tolov/clear/", DelTolov.as_view(), name="edit  "),
    path("tuman/<str:viloyat>/", GetTuman.as_view(), name="edit  "),
    path('inactive-customers/<int:days>/', RejectOrdersList.as_view(), name='inactive- s'),
    path("dastavka/", AddDastavka.as_view(), name="add  "),
    path("dastavka/<int:id>/", EditDastavka.as_view(), name="edit  "),
    path("dastavkachi/", AddDastavkachi.as_view(), name="add  "),
    path("dastavkachi/<int:id>/", EditDastavkachi.as_view(), name="edit  "),
    path("dastavka/auto/<int:auto>/", GetDastavkaAuto.as_view(), name="edit  "),
    path("dastavka/sana/", GetDastavkaSana.as_view(), name="edit  "),
    path("users/user_id/<str:user_id>/", GetUser.as_view(), name="edit  "),
    path("users/customer_id/<str:customer_id>/", GetCustomer.as_view(), name="edit  "),
    path("statistika/", CustomerOrderStatsView.as_view(), name="get  "),
    path('latest-three/', LatestThreeObjectsView.as_view(), name='latest-three-objects'),
    path('objects_count/', AllModelsCount.as_view(), name='object-count'),
]