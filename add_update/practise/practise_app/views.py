from django.shortcuts import render, HttpResponse,redirect
from .models import Movies
from . forms import Movie_form
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.contrib import messages


# Create your views here.
def main_page(requests):
    a = Movies.objects.all()
    return render(requests,'mainpage.html',{'res':a})
# def detail(requests,id):
#
#     return HttpResponse('This is movie no %s' %id)

def detail(requests,id):
    a = Movies.objects.get(id=id)
    return render(requests,'detail.html',{'res':a})


def add(request):
    if request.method == 'POST':
        name = request.POST['name']
        year = request.POST['year']
        desc = request.POST['desc']
        image = request.FILES['image']
        a = Movies(name=name,desc=desc,year=year,image=image)# tabilelile value=mukalile value
        a.save()
        return redirect('/')
    return render(request, 'add.html')

def update(request, id):
    movie = Movies.objects.get(id=id)
    form = Movie_form(request.POST or None,request.FILES, instance=movie)

    if form.is_valid():
        form.save()
        return redirect('/')
    else:
        form=Movie_form(instance=movie)
    return render(request, 'update.html', {'form': form, 'movie': movie})

def delete(requests,id):
    if requests.method == 'POST':
        place1=Movies.objects.get(id=id)
        place1.delete()
        return redirect('/')
    return render(requests,'delete.html')

class movielistview(ListView):
    model=Movies
    template_name= 'mainpage.html'
    context_object_name = 'res'

class detailview(DetailView):
    model=Movies
    template_name= 'detail.html'
    context_object_name = 'res'

class updateview(UpdateView):
    model = Movies
    template_name = 'update.html'
    context_object_name = 'form' #epozhum form thanne kodukanam
    fields=['name','desc','year','image']
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk': self.object.id})

class deleteview(DeleteView):
    model = Movies
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')

def mailview(request):
    if request.method =='POST':
        sub=request.POST.get('subject')
        msg=request.POST.get('message')
        gmail=request.POST.get('gmail')
        send_mail(sub,msg,gmail,['jasirajaleel2001@gmail.com'],fail_silently=False)
        messages.info(request,'Mail sent sucessfully')
    return render(request,'mailview.html')









