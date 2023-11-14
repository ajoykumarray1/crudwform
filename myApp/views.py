from django.shortcuts import redirect, render
from .models import Employee

# Create your views here.
def home(request):
    employee=Employee.objects.all()
    return render(request,'home.html',{'employee':employee})

def add(request):
    if request.method=="POST":
        img=request.FILES['imag']
        uname=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        phon=request.POST.get('phone')

        emp=Employee(
            pro_pic=img,
            name=uname,
            email=email,
            address=address,
            phone=phon
        )
        emp.save()
        return redirect('home')
    return render(request,'add.html')

def edit(request):
    return render(request,'edit.html')