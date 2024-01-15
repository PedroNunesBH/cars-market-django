from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import UserRegisterNewCar, CarsUser, CarView
from users.views import create_user, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', CarView.as_view(), name="cars_list"),  # URL e a view responsavel
    path('user_register_car/', UserRegisterNewCar.as_view(), name="u_register_car"),
    path('create_user/', create_user, name='create_user'),
    path('login/', login_view, name='login_page'),
    path('logout/', logout_view, name='logout_page'),
    path('my_cars/', CarsUser.as_view(), name='cars_user'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
