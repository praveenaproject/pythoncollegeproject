from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.
from .models import Department,Branch



def home(request):
    return render(request,'home.html')
def logout(request):

    return redirect('/')

def form(request):
    departmentid=request.GET.get('department',None)

    branch=None
    if departmentid:
        getdepartment=Department.objects.get(id=departmentid)

        branch=Branch.objects.filter(department=getdepartment)

    department = Department.objects.all()

    return render(request,'form.html',locals())
# {'department':department,'branch':branch}


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return render(request,'newpage.html')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')



    return render(request,"login.html")





def register(request):
    if request.method=='POST':
        username=request.POST['username']

        password=request.POST['password']
        cpassword=request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username taken")
                return redirect('register')

            else:
                 user=User.objects.create_user(username=username,password=password)
                 user.save()
                 return redirect('login')

        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')

    return render(request,"register.html")


def newpage(request):
    return render(request, "newpage.html")

def message(request):
    return render(request,"message.html")