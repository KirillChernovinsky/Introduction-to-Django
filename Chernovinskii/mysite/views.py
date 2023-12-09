from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def me(request,name,age,interests):
    return HttpResponse(f'My name is {name}. I am {age}. {interests}.')

def about(request,geo,training,grades):
    return HttpResponse(f'{geo}{training}{grades}')

def contacts (request, tgcontacts, vk):
    return HttpResponse(f'Мои контакты: {tgcontacts} и вк: {vk}')

