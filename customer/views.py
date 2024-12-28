from django.shortcuts import render ,redirect
from django.http import HttpResponse , JsonResponse
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404
from .serializers import *
from rest_framework import viewsets
from datetime import datetime
# Create your views here.
def home(request):
    cars = Cars.objects.filter(ID__in=[1, 2, 3])
    return render(request,"customer/index.html",{"car":cars})
def buy(request):
    cars = Cars.objects.filter(reserv=False)
    message = None  
    message_2 = None  
    message_3 = None  
    sort_by = request.GET.get('sort_by')
    Search = request.GET.get('search')
    name_car = request.GET.get('name_car')
    if  name_car:
        cars = cars.filter(name=name_car)
    if Search:
            cars = cars.filter(name=Search)
            if len(cars) == 0:
             message_3= "NO Cars Found"

    if sort_by == 'price':
        cars = cars.order_by('price_sale')
    elif sort_by == '-price':
        cars = cars.order_by('-price_sale')
    if request.method == 'POST':
        form = buyForm(request.POST)
        if form.is_valid():
            car_id = request.POST.get('car_id')  
            car = get_object_or_404(Cars, ID=car_id) 
            if car.stock > 0:  
                form.save()
                car.stock -= 1 
                car.save() 
                message_2 = "Success We send you an email"
                
            else:
                message = "Sorry, the car is out of stock."
        else:
            print(form.errors)
    return render(request, "customer/buy.html", {"car": cars,  "message": message , "message_2": message_2 ,"message_3":message_3 })
def sold(request):
    massage = None
    if request.method == 'POST':
        form = soldForm(request.POST , request.FILES)
        if form.is_valid():
                cust_id = request.POST.get('id_customer')
                form.save()
                requests_sold = request_sold.objects.filter(id_customer=cust_id) 
                first_request = requests_sold.first()  
                ID = first_request.id 
                massage=f"Success request this ID to review your request:( {str(ID)} )"
        else:
            print(form.errors)
    return render (request, "customer/sold.html", { "message": massage})       
def revew_request(request):
    requests_sold = None 
    req_id = None
    if request.method == 'POST':
        req_id = request.POST.get('request_id') 
    requests_sold = request_sold.objects.filter(id=req_id)  
    if not requests_sold.exists():  
        requests_sold = "1"
    return render(request, "customer/revew_request.html", {"requset": requests_sold})
def revew_reserv(request):
    requests_reserv = None 
    id = None
    if request.method == 'POST':
        id = request.POST.get('id') 
    requests_reserv = reservation.objects.filter(id = id)  
    if not requests_reserv.exists():  
        requests_reserv = "1"
    print(requests_reserv, id)    
    return render(request, "customer/revew_reserv.html", {"requset": requests_reserv})
def reserv_car(request):
    cars = Cars.objects.filter(reserv=True )
    reservations = reservation.objects.all()
    id= len(reservations)+3
    message = None  
    message_2 = None  
    message_3 = None  
    sort_by = request.GET.get('sort_by')
    Search = request.GET.get('search')
    name_car = request.GET.get('name_car')
    if  name_car:
        cars = cars.filter(name=name_car)
    if Search:
            cars = cars.filter(name=Search)
            if len(cars) == 0:
             message_3= "NO Cars Found"
    if sort_by == 'price':
        cars = cars.order_by('price_reserv')
    elif sort_by == '-price':
        cars = cars.order_by('-price_reserv')
    if request.method == 'POST':
            id_cust = request.POST.get("id_cust")
            cust_name = request.POST.get("cust_name")
            car_id = request.POST.get('id_car')  
            date_to = request.POST.get('date_to')  
            date_from = request.POST.get('date_from')  
            car = get_object_or_404(Cars, ID=car_id) 
            price_per_day = car.price_reserv
            if car.status_car !=False:
                date1 = datetime.strptime(date_from, "%Y-%m-%d")  # Adjust format if needed
                date2 = datetime.strptime(date_to, "%Y-%m-%d")
                # Calculate the difference
                time_difference = date2 - date1
                # Extract days, hours, and minutes
                days = time_difference.days
                price=int(price_per_day) * int(days)
                car.status_car = False
                reserv = reservation.objects.create(
                    id = id,
                    id_cust=id_cust,
                    cust_name=cust_name,
                    id_car_id=car_id,
                    date_from=date_from,
                    date_to=date_to,
                    price=price
                )
                message_2 =f"Success request this ID to review your request:( {str(id)} ) \n Total Price is {price}"
                car.save()
            else :
                message = "Sorry this car reserved"
    return render(request, "customer/resrv_car.html", {"car": cars,  "message": message , "message_2": message_2 , "message_3":message_3})
def repair(request):
    cars = Cars.objects.filter(reserv=False)
    repair = repairs.objects.select_related('type_car').all()
    type_car = request.GET.get('type_car')
    message = ""
    if  type_car:
        repair = repair.filter(type_car=type_car)
    if request.method == 'POST':
        form = repairForm(request.POST)
        if form.is_valid():
                form.save() 
                message = "Success We send you an email"
        else:
           print(form.errors)    
    return render ( request, "customer/repair.html",{"data":repair,"car": cars,"message": message})
def manger(request):
    cars = Cars.objects.filter(ID__in=[1, 2, 3])
    return render(request,"Admin/manager.html",{"car":cars})
def add_car(request):
    massage = None
    if request.method == 'POST':
        form = carsForm(request.POST , request.FILES)
        if form.is_valid():
                form.save()
                massage=f"Success add car "
        else:
            print(form.errors)
    return render (request, "Admin/add_car.html", { "message": massage})       
def display_cars(request):
    cars = Cars.objects.all()
    sort_by = request.GET.get('sort_by')
    Search = request.GET.get('search')
    name_car = request.GET.get('name_car')
    # resrv_buy = request.GET.get('resrv_buy')
    if  name_car:
        cars = cars.filter(name=name_car)
    if Search:
            cars = cars.filter(name=Search)
            if len(cars) == 0:
             message_3= "NO Cars Found"
    if sort_by == 'price':
        cars = cars.order_by('price_sale')
    elif sort_by == '-price':
        cars = cars.order_by('-price_sale')
    # if resrv_buy == 'resrv':
    #     cars = cars.filter('reserv=True')
    # elif resrv_buy == 'buy':
    #     cars = cars.filter('reserv=False')
    return render(request,"Admin/display_cars.html",{"car":cars})
def add_driver(request):
    massage = None
    if request.method == 'POST':
        form = driversForm(request.POST , request.FILES)
        if form.is_valid():
                form.save()
                massage=f"Success add driver "
        else:
            print(form.errors)
    return render (request, "Admin/add_driver.html", { "message": massage})       
def login_view(request):
    massage = None
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_name = mangers.objects.filter(username = username)
        if len(user_name) !=0:
            manager_instance = user_name.first()
            user_password = manager_instance.password
            if user_password == password:
                return redirect('manger')
            else :
                massage = "Password wrong"
        else :
               massage = "Username wrong"     
    return render(request, "Admin/login.html" ,{"massage":massage})  # Render the login form for GET requests
class carsviewsets(viewsets.ModelViewSet):
    queryset=Cars.objects.all()
    serializer_class=carsserializers
class driverviewset(viewsets.ModelViewSet):
    queryset=drivers.objects.all()
    serializer_class=driversserializers
class reservationviewsets(viewsets.ModelViewSet):
    queryset=reservation.objects.all()
    serializer_class=ReservationSerializers
class request_soldviewsets(viewsets.ModelViewSet):
    queryset=request_sold.objects.all()
    serializer_class=request_soldserializers
class request_repairviewsets(viewsets.ModelViewSet):
    queryset=request_repairs.objects.all()
    serializer_class=request_repairserializers