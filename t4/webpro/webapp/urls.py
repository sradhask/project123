
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('register',views.register,name="register"),
    path('',views.user_login,name="login"),
    path('user',views.userhome,name="userhome"),
    path('logout_p',views.logout_view,name="logout_p"),
    path('view/<pk>/', views.view_product, name='view'),
    path('user_login1',views.user_login1,name="user_login1"),
    path('add_product',views.add_product,name="add_product"),
    path('seller',views.seller,name="seller"),
    path('seller1',views.seller1,name='seller1')
    

]



