from rest_framework import serializers
from .models import *



class carsserializers(serializers.Serializer):
    ID = serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length=50)
    type = serializers.CharField(max_length=50)
    manufacture_date = serializers.DateField()  
    status = serializers.ChoiceField(choices=state)
    price_sale = serializers.DecimalField(max_digits=10, decimal_places=2 ,allow_null=True)
    price_reserv=serializers.DecimalField(max_digits=10, decimal_places=2 ,allow_null=True,default=0)
    kilo = serializers.DecimalField(max_digits=10, decimal_places=2)  
    color = serializers.CharField(max_length=100)
    #image = serializers.ImageField()  
    stock = serializers.IntegerField()
    reserv = serializers.BooleanField(default=False)
    status_car = serializers.BooleanField(default=True)
    def update(self,instance,validate_data):
        instance.status=validate_data.get("status")
        instance.price_sale=validate_data.get("price_sale")
        instance.price_reserv=validate_data.get("price_reserv")
        instance.kilo=validate_data.get("kilo")
        instance.stock=validate_data.get("stock")
        instance.reserv=validate_data.get("reserv")
        instance.status_car=validate_data.get("status_car")
        instance.save()
        return instance
    def delete(self, instance):
        instance.delete() 
        return {"message": "Object deleted successfully"}
class driversserializers(serializers.Serializer):
    ID=serializers.IntegerField()
    name=serializers.CharField(max_length=50)
    age=serializers.IntegerField()
    phone=serializers.IntegerField()
    status = serializers.BooleanField()
    def update(self,instance,validate_data):
        instance.age=validate_data.get("age")
        instance.phone=validate_data.get("phone")
        instance.status=validate_data.get("status")
        instance.save()
        return instance
    def delete(self, instance):
        instance.delete()
        return {"message": "Object deleted successfully"}
class ReservationSerializers(serializers.Serializer):
    id_car = carsserializers
    id = serializers.IntegerField(read_only=True)
    id_cust = serializers.IntegerField()
    cust_name = serializers.CharField(max_length=20)
    # id_car = serializers.ForeignKey()
    id_driver = serializers.PrimaryKeyRelatedField(
        queryset=drivers.objects.all(), allow_null=True, required=False
    )  # Correct way to define a relationship field
    date_from = serializers.DateField()
    date_to = serializers.DateField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2, required=False, default=0)
    statues = serializers.ChoiceField(choices=Li_request, default="Waiting")  
    def update(self, instance, validated_data):
        instance.id_driver = validated_data.get("id_driver")
        instance.statues = validated_data.get("statues")
        instance.save()
        return instance
class request_soldserializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    id_customer=serializers.CharField(max_length=20)
    cust_name=serializers.CharField(max_length=20)
    name_car=serializers.CharField(max_length=50)
    type_car = serializers.CharField(max_length=50)
    manufacture_date_car = serializers.DateField()  
    price_sale_car = serializers.IntegerField()
    kilo_car = serializers.DecimalField(max_digits=10, decimal_places=2, )  
    color_car = serializers.CharField(max_length=100)
    # image_car = serializers.ImageField()
    statues = serializers.ChoiceField(choices=Li_request, default="Waiting")
    def update(self,instance,validate_data):
        instance.statues=validate_data.get("statues")
        instance.save()
        return instance
class request_repairserializers(serializers.Serializer):
    ID =serializers.IntegerField(read_only=True)
    cust_id = serializers.CharField(max_length=20)
    cust_name = serializers.CharField(max_length=30)
    cust_phone= serializers.IntegerField()
    # type_repair=serializers.ForeignKey(repairs,on_delete=models.PROTECT)
    statues = serializers.ChoiceField(choices=Li_request, default="Waiting")
    def update(self,instance,validate_data):
        instance.statues=validate_data.get("statues")
        instance.save()
        return instance




