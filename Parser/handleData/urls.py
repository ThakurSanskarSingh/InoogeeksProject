from django.urls import path
from . import views

urlpatterns = [
    # path('parse/', views.parsing, name='parsing')
    path('',views.homePage)
]
