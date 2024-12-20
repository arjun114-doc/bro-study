from django.shortcuts import render
from django.shortcuts import redirect

from . models import MovieInfo

from . forms import MovieForm
# Create your views here.
def create(request):
    frm=MovieForm()
    if request.POST:
        frm=MovieForm(request.POST,request.FILES)
        if frm.is_valid:
            frm.save()
            return redirect('create')
        
    else:
        frm=MovieForm()
        
    return render(request,'create.html',{'frm':frm})
def edit(request,pk):
    isinstance_to_be_edited=MovieInfo.objects.get(pk=pk)
    if request.post:
        frm=MovieForm(request.POST,instance=isinstance_to_be_edited)
        if frm.is_valid():
            isinstance_to_be_edited.save()
    else:
        frm=MovieForm(instance=isinstance_to_be_edited)
    return render(request,'create.html',{'frm':frm})

def delete(request,pk):
    isinstance=MovieInfo.objects.get(pk=pk)
    isinstance.delete()
    
    movie_set=MovieInfo.objects.all()
    
    return render(request,'list.html',{'movies':movie_set})


def list(request):
    movie_set=MovieInfo.objects.all()
    print(movie_set)
    return render(request,'list.html',{'movies':movie_set})