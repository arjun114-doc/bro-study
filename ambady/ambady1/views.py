from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def print_hello(request):
    movie_data= {'movies' :[{
        'title': 'Godfather',
        'year' :1990,
        'summary':'story of an undeworld king',
        'success' :False
    },
     {
        'title': 'Titanic',
        'year' :2002,
        'summary':'story of an undeworld king',
        'success' :True
    },{
        'title': 'Goldfish',
        'year' :1999,
        'summary':'story of an undeworld king',
        'success' :False
    }]
    }
    
    return render(request,'hello.html',movie_data)