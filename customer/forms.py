from django import forms
from .models import *

class buyForm(forms.ModelForm):
    class Meta:
        model = cars_bought
        fields = ['cust_id', 'cust_name', 'cust_phone' , "car_id"]
class soldForm(forms.ModelForm):
    class Meta:
        model = request_sold
        fields = ['id_customer', 'cust_name', "name_car" ,"type_car" ,"manufacture_date_car" , "price_sale_car" , "kilo_car" , "color_car" , "image_car"]
class repairForm(forms.ModelForm):
    class Meta:
        model = request_repairs
        fields = ['cust_id', 'cust_name', "cust_phone" ,"type_repair" ]
class reservForm(forms.ModelForm):
    class Meta:
        model = reservation
        fields = ['id_cust', 'cust_name', "id_car" ,"date_from","date_to", "price"]
class carsForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = ['name', 'type', 'manufacture_date' , 'status' , 'price_sale' , 'price_reserv' , 'kilo' , 'color' , "image","stock","reserv","status_car"]
class driversForm(forms.ModelForm):
    class Meta:
        model = drivers
        fields = ['ID', 'name', 'age' , 'phone' , 'status']
                        
                        
            

                        
                        
