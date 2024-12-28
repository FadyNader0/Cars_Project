from django.urls import path 
from . import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
urlpatterns=[
    path("",views.home,name="home"),
    path("buy/",views.buy,name="buy"),
    path("sold/",views.sold,name="sold"),
    path("repair/",views.repair,name="repair"),
    path("revew_request/",views.revew_request,name="revew_request"),
    path("reserv_car/",views.reserv_car,name="reserv_car"),
    path("revew_reserv/",views.revew_reserv,name="revew_reserv"),
    path("login/",views.login_view,name="login"),
    path("manger/",views.manger,name="manger"),
    path("manger/add_car/",views.add_car,name="add_car"),
    path("manger/display_cars/",views.display_cars,name="display_cars"),
    path("manger/add_driver/",views.add_driver,name="add_driver"),
]
router.register("manger/cars",views.carsviewsets,basename="cars")
router.register("manger/drivers",views.driverviewset,basename="driver")
router.register("manger/resrvation",views.reservationviewsets,basename="resrvation")
router.register("manger/request_sold",views.request_soldviewsets,basename="request_sold")
router.register("manger/request_repair",views.request_repairviewsets,basename="request_repair")
urlpatterns=urlpatterns+router.urls