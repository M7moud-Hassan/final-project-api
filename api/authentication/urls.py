from django.urls import path
from .views import *
urlpatterns=[
    path('verfy_email/<uidb64:uid>/<str:token>',verfy_email,name='verfy_email'),
                path('signup_freelancer/', signup_freeLancer, name='signup_freelancer'),
]