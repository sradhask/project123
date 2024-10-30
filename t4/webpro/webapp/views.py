from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from . models  import*

# Create your views here.


def user_login(request):
    if 'username' in request.session:
        return redirect(userhome)
    if request.method=="POST":
     email=request.POST['email']
     password=request.POST['password']
     user=authenticate(request,username=email,password=password)
     if user is not None:
          request.session['username']=email
          login(request,user)
          return redirect('userhome')
     return render(request,'userhome.html')
    else:
     return render(request,'login.html')
    

def logout_view(request):
        logout(request)
        if 'username' in request.session:
            request.session.flush()
        return redirect('login')

def register(request):
        if request.method =='POST':
            name=request.POST['name']
            email=request.POST['email']
            password=request.POST['password']
            ConfirmPassword=request.POST['ConfirmPassword']
            try:
                user=User.objects.create_user(username=email,email=email,password=password,ConfirmPassword=ConfirmPassword)
                user.save()
            except:
                messages.error(request, "Email exit.")

                return redirect('register')
            return redirect('login')
        else:
            return render(request,'register.html')
def userhome(request):
    if 'username' in request.session:
     data=Product.objects.all()
    return render(request,"userhome.html",{'data':data})
    return redirect (user_login)


def view_product(request,pk):
        data=Product.objects.filter(pk=pk)
        return render(request,"product.html",{'data':data})
       

def seller(request):
  
     if request.method =='POST':
            email=request.POST['email']
            password=request.POST['password']
          
            try:
                user=User.objects.create_user(username=email,email=email,password=password)
                user.is_staff=True
                user.save()
                messages.success(request,"account created successfully")
            except:
                messages.error(request, "Email exit.")

                return redirect('login')
            
     else:
            return render(request,'seller.html')



def delete_g(request,pk):
    Prodobj=Product.objects.get(pk=pk)
    Prodobj.delete()
    return redirect("seller")

def edit_g(request,pk):
     if request.method =="POST":
          prodobj=Product.objects.get(pk=pk)
          prodobj.objects.filter(pk=pk).update()
          return redirect('seller')
     else:            
          data=Product.objects.get(pk=pk)
          return render(request,'editpro.html',{'data':data})
      
def user_login1(request):

    if request.method=="POST":
     email=request.POST['email']
     password=request.POST['password']
     user=authenticate(request,username=email,password=password,)
     if user is not None:
          request.session['username']=email
          login(request,user)
          return redirect('seller')
    else:
          return render(request,'seller2.html')
    
    

def add_product(request):
    if request.method=="POST":
      image=request.POST["image"]
      name=request.POST["name"]
      Prize=request.POST["prize"]
      offer_prize=request.POST["offer_price"]
      discription=request.POST["discription"]
      size=request.POST["size"]
      return render("seller2.html")
    else:
        return redirect("seller1.html")
      
      
            
 



 