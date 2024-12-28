from django.db import models

# Choices for the status field
state = [("used", "used"), ("new", "new")]
Li_request = [("Confirm", "Confirm"), ("Refuse", "Refuse")]
class Cars(models.Model):
    ID = models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    manufacture_date = models.DateField()  
    status = models.CharField(max_length=5, choices=state)
    price_sale = models.DecimalField(max_digits=10, decimal_places=2 ,null=True)
    price_reserv=models.DecimalField(max_digits=10, decimal_places=2 ,null=True,default=0,blank=True)
    kilo = models.DecimalField(max_digits=10, decimal_places=2)  
    color = models.CharField(max_length=100)
    image = models.ImageField(upload_to="image/%Y-%m-%d")  
    stock = models.IntegerField()
    reserv = models.BooleanField(default=False)
    status_car = models.BooleanField(default=True)
    def __str__(self):
        return self.name +"\t"+ self.type
class drivers(models.Model):
    ID=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    phone=models.IntegerField()
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.name
class reservation(models.Model):
    id = models.AutoField(primary_key=True)
    id_cust=models.IntegerField()
    cust_name=models.CharField(max_length=20)
    id_car=models.ForeignKey(Cars,on_delete=models.PROTECT)
    id_driver=models.OneToOneField(drivers,null=True,on_delete=models.PROTECT,blank=True)
    date_from=models.DateField()
    date_to=models.DateField()
    price=models.DecimalField(max_digits=10 ,decimal_places=2 , null=True , default=0 , blank=True)
    statues = models.CharField(max_length=50 , choices=Li_request , default="Wating")
    def __str__(self):
        return self.cust_name
class request_sold(models.Model):
    id = models.AutoField(primary_key=True)
    id_customer=models.CharField(max_length=20)
    cust_name=models.CharField(max_length=20)
    name_car=models.CharField(max_length=50)
    type_car = models.CharField(max_length=50)
    manufacture_date_car = models.DateField()  
    price_sale_car = models.IntegerField()
    kilo_car = models.DecimalField(max_digits=10, decimal_places=2, )  
    color_car = models.CharField(max_length=100)
    image_car = models.ImageField(upload_to="image/%Y-%m-%d")
    statues = models.CharField(max_length=50 , choices=Li_request , default="Wating")
class cars_bought(models.Model):
    cust_id = models.CharField(max_length=20)
    cust_name = models.CharField(max_length=30)
    cust_phone= models.IntegerField()
    car_id = models.ForeignKey(Cars,on_delete=models.PROTECT)
class repairs(models.Model):
    ID = models.AutoField(primary_key=True)
    type_repair = models.CharField(max_length=50)
    type_car = models.ForeignKey(Cars,on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10 , decimal_places=2)
    image = models.ImageField(upload_to="image/%Y-%m-%d" ,null=True)
    def __str__(self):
        return f"{self.type_repair} for {self.type_car}"
class request_repairs(models.Model):
    ID =models.AutoField(primary_key=True)
    cust_id = models.CharField(max_length=20)
    cust_name = models.CharField(max_length=30)
    cust_phone= models.IntegerField()
    type_repair=models.ForeignKey(repairs,on_delete=models.PROTECT)
    statues = models.CharField(max_length=50 , choices=Li_request , default="Wating")

class mangers(models.Model):
    username =  models.CharField(max_length=20 , primary_key=True)
    password = models.CharField(max_length=20)
    def __str__(self):
        return self.username + self.password 