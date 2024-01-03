from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.http import HttpResponse
from . models import Items,Movies
from . form import Register,additems,Movie_form
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy
from django.core.mail import send_mail


# Create your views here.

def index(request):
    return HttpResponse("Hello World")

def demo1(request):
    return render(request,"base.html")

def add1(request):
    x=int(request.GET["num1"])
    y=int(request.GET["num2"])
    result=x+y
    return render(request,"result.html",{"res":result})
def sum(request):
    return render(request,"add.html")

def color(request):
    return render(request,"color.html")

def index1(request):
    a= Items.objects.all()
    return render(request,"index.html",{"item": a})

def about(request):
    return render(request,"about.html")

def service(request):
    return render(request,"service.html")

def product(request):
    return render(request,"product.html")

def register(request):
    if request.method == "POST":
        form = Register(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('res')
        messages.success(request, 'user created successfully')
    else:
        form = Register()
    return render(request, "register.html", {"con": form})

def res(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user1 = authenticate(username=username, password=password)
            if user1 is not None:
                login(request, user1)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('index')
            else:
                messages.error(request, "Invalid username or password")
    form = AuthenticationForm()
    return render(request, "login.html", {"login_form": form})

def additm(request):
    if request.method == 'POST':
        form1 = additems(request.POST,request.FILES or None)
        if form1.is_valid():
            form1.save()
            return redirect('index')
        messages.success(request,"Add successfully")
    else:
        form = additems()
    return render(request,"form.html",{"form":form})

def logout(request):
    auth.logout(request)
    return redirect('index')

def mainpg(request):
    a=Movies.objects.all()
    return render(request,"movies.html",{"movie": a})

def display(request,id):
    return HttpResponse("This is movie number %s" %id)

def detail(request,id):
    a=Movies.objects.get(id=id)
    return render(request,"detail.html" ,{"detail":a})

def adding(request):
    if request.method == 'POST':
        name = request.POST['name']
        year = request.POST['year']
        description = request.POST['description']
        image1 = request.FILES['img']
        a = Movies(name=name, description=description, year=year, img=image1)
        a.save()
        return redirect('/')
    return render(request,"adding.html")

def update(request,id):
    movie = Movies.objects.get(id=id)
    form = Movie_form(request.POST or None,request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    else:
        form = Movie_form(instance=movie)
    return render(request,"update.html", {"form": form,"movie": movie})

def delete(request,id):
    if request.method == "POST":
        place1 = Movies.objects.get(id=id)
        place1.delete()
        return redirect('/')
    return render(request,"delete.html")

def session(request):
    request.session['sname']="Janu"
    return HttpResponse('user session is set')

def get_session(request):
    s_get=request.session['sname']
    return HttpResponse('welcome '+s_get)

class movielistview(ListView):
    model=Movies
    template_name = "movies.html"
    context_object_name = "movie"

class detail_view(DetailView):
    model=Movies
    template_name = "detail.html"
    context_object_name = "detail"

class updateview(UpdateView):
    model=Movies
    template_name = "update.html"
    context_object_name = "form"
    fields=['name','description','year','img']
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class deleteview(DeleteView):
    model = Movies
    template_name = "delete.html"
    success_url = reverse_lazy('cbvhome')

#without form
def mail(request):
    send_mail("subject","Dear Sir","jasirajaleel2001@gmail.com",['lekshmichinnu68@gmail.com'],fail_silently=False)
    return HttpResponse("Mail sent successfully")

def mail2(request):
    if request.method == "POST":
        sub=request.POST.get("subject")
        body=request.POST.get("body")
        gmail=request.POST.get("from")
        send_mail(sub,body,gmail,["lekshmichinnu68@gmail.com"],fail_silently=False)
        messages.info(request,"message sent successfully")
    return render(request,"mail2.html")