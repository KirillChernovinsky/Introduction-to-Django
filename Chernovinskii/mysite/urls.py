from django.urls import path
from . import views

urlpatterns = [
    path('', views.me, name='me', kwargs = {'name':'Kirill', 'age':'16 years old', "interests": 'I love walking and traveling.'} ),
    path('about', views.about, name="about", kwargs = {'geo': "I came from Karelia.", "training": "I've just started studying "
                                                  "and I can't say if I like it yet." ,'grades': " I have good grades."} ),
    path('contacts', views.contacts, name='contacts', kwargs= {'tgcontacts': 'https://t.me/BeLuGa230', 'vk': "Chernovinskij"})
]



