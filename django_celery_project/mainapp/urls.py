from django.urls import path
from .views import *

urlpatterns = [
    # path('test/', test, name='test'), 
    path('send_mail/', send_mail_to_all, name='send_mail'),
    path('schedulemail/', schedule_mail, name='schedule_mail'),

]