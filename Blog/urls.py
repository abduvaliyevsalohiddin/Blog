from django.contrib import admin
from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view()),
    path('home/', HomeView.as_view()),
    path('register/', RegisterView.as_view()),
    path('logout/', LogoutView.as_view()),

]
