from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import Datas
# Create your views here.
def home(request):
    return render(request,'home.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/success')
        else:
            messages.info(request, 'Invalid userid or password')
    return render(request, 'login.html')
def success(request):
    return render(request,'success.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['confirm-password']
        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'user already exist')

            else:
                user = User.objects.create_user(username=username,password=password)
                user.save();
                return redirect('/login')
        else:
            messages.info(request, 'Password is not matching')
    return render(request, 'register.html')

def forms(request):
    return render(request,'forms.html')
def save(request):
    if request.method=='POST':

        name = request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phoneno = request.POST.get('phoneno')
        mailid = request.POST.get('mailid')
        address= request.POST.get('address')
        department= request.POST.get('department')
        course= request.POST.get('courses')
        purpose = request.POST.get('purpose')
        notebook = request.POST.get('notebook')
        pen = request.POST.get('pen')
        record = request.POST.get('record')
        uniform = request.POST.get('uniform')
        exampaper = request.POST.get('exampaper')

        datas = Datas(name=name,dob=dob,age=age,gender=gender,phoneno=phoneno,mailid=mailid,address=address,department=department,course=course,purpose=purpose,notebook=notebook,pen=pen,record=record,uniform=uniform,exampaper=exampaper)
        datas.save();
        return redirect('/logout')

    return render(request,'forms.html')

def logout(request):
    auth.logout(request)
    return render(request,'save.html')
