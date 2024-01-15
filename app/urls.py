from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import CarsUser, CarView, UserRegisterNewCar, DetailCar, UpdateCar, DeleteCar
from users.views import create_user, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', CarView.as_view(), name="cars_list"),  # URL e a view responsavel
    path('user_register_car/', UserRegisterNewCar.as_view(), name="u_register_car"),
    path('create_user/', create_user, name='create_user'),
    path('login/', login_view, name='login_page'),
    path('logout/', logout_view, name='logout_page'),
    path('my_cars/', CarsUser.as_view(), name='cars_user'),
    path('detail_car/<int:pk>/', DetailCar.as_view(), name='detail_car'),  # Define que será recebido um parametro pk(primary-key) do tipo inteiro
    path('update_car/<int:pk>/', UpdateCar.as_view(), name='update_car'),
    path('delete_my_car/<int:pk>/', DeleteCar.as_view(), name='delete_my_car'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
