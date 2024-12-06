from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from . models  import*

# Create your views here.

# for userlogin
def user_login(request):
    if 'username' in request.session:
        return redirect(userhome)
    if request.method=="POST":
     username=request.POST['username']
     password=request.POST['password']
     user=authenticate(request,username=username,password=password)
     if user is not None:
          request.session['username']=username
          login(request,user)
          return redirect('userhome')
     return redirect(request,'user_login')
    else:
     return render(request,'login.html')
    
# for user logout
def logout_view(request):
        logout(request)
        if 'username' in request.session:
            request.session.flush()
        return redirect('login')
# for user registration
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['ConfirmPassword']

        if not username or not email or not password or not confirm_password:
            messages.error(request,'all fields are required.')

        elif confirm_password != password:
            messages.error(request,"password doesnot match")
           
        elif User.objects.filter(email=email).exists():
            messages.error(request,"email already exist")
           
        elif User.objects.filter(username=username).exists():
            messages.error(request,"username already exist")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)    
            user.save()
            messages.success(request,"account created successfully")
            return redirect(request, "user_login")
    else:
        return render(request, 'register.html')
    
    
# for userhome
def userhome(request):
    if 'username' in request.session:
     data=Product.objects.all()
    return render(request,"userhome.html",{'data':data})
    return redirect (user_login)

# for views
def view_product(request,pk):
        data=Product.objects.filter(pk=pk)
        return render(request,"product.html",{'data':data})
       
# for seller registration
def seller(request):
  
     if request.method =='POST':
            email=request.POST['email']
            password=request.POST['password']
            username=request.POST['username']
            ConfirmPassword=request.POST['ConfirmPassword']
          
            if not username or not email or not password or not ConfirmPassword:
                messages.error(request,'all fields are required.')

            elif ConfirmPassword != password:
                messages.error(request,"password doesnot match")
           
            elif User.objects.filter(email=email).exists():
                messages.error(request,"email already exist")
           
            elif User.objects.filter(username=username).exists():
                messages.error(request,"username already exist")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)  
                user.is_staff=True  
                user.save()
                messages.success(request,"account created successfully")
                return redirect(request, "user_login1")
            
     else:
            return render(request,'sellreg.html')
      
# for seller login
def user_login1(request):
    if 'username' in request.session:
        return redirect('seller1')  
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session['username']=username
            login(request, user)
            return redirect('seller1')  
        return redirect("user_login1")
    else:
        return render(request, 'sellerlog.html', {'error': 'Invalid credentials'})

    
# for adding products in to the seller

def add_product(request):
    if request.method == "POST":
        # Capture data from the form
        image = request.FILES.get("image")  # Use request.FILES for image uploads
        name = request.POST["name"]
        prize = request.POST["prize"]
        offer_price = request.POST["offer_price"]
        description = request.POST["description"]
        size = request.POST["size"]

        # Create a new product object and save it to the database
        product = Product(name=name,prize=prize,offer_price=offer_price, size=size,description=description, image=image)
        
        product.save()  # Save the product to the database
        messages.success(request,"product added")    

        # Redirect to the seller page or another page
        return redirect("sellerhome")  # Replace with your actual URL name
    else:
        return render(request, "addpro.html")
    
    
    
    
    

      
      
      
#   for add product     
def seller1(request):
    return render(request,"sellerhome.html")
 
# for display products






# for delete
def delete_g(request,pk):
    Prodobj=Product.objects.get(pk=pk)
    Prodobj.delete()
    return redirect("seller")


# for edit
def edit_g(request,pk):
     if request.method =="POST":
          prodobj=Product.objects.get(pk=pk)
          prodobj.objects.filter(pk=pk).update()
          return redirect('seller')
     else:            
          data=Product.objects.get(pk=pk)
          return render(request,'editpro.html',{'data':data})
 