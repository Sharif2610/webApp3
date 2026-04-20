from django.shortcuts import render,redirect,get_object_or_404
from . models import Workforce,Department
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('workforce_list')
        else:
            return render(request,'login.html',{'error':'Invalid Username or password'})
    return render(request,'login.html')
def logout_view(request):
    logout(request)
    return redirect('login')
def home(request):
    return render(request,'home.html')
@login_required(login_url='login')
def workforce_list(request):
    workforce = Workforce.objects.all()
    paginator = Paginator(workforce,2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'workforce_list.html',{'workforce':page_obj})
@login_required(login_url='login')
def insert_workforce(request):
    department = Department.objects.all()
    if request.method == 'POST':
        wfno = request.POST.get('wfno')
        wfname = request.POST.get('wfname')
        salary = request.POST.get('salary')
        deptno = request.POST.get('deptno')
        department = Department.objects.get(deptno=deptno)
        Workforce.objects.create(wfno=wfno,wfname=wfname,salary=salary,department=department)
        return redirect('workforce_list')
    return render(request,'insert_workforce.html',{'department':department})
@login_required(login_url='login')
def update_workforce(request,wfno):
    workforce = get_object_or_404(Workforce,wfno=wfno)
    department = Department.objects.all()
    if request.method == 'POST':
        workforce.wfname = request.POST['wfname']
        workforce.salary = request.POST['salary']
        deptno = request.POST['deptno']
        workforce.department = Department.objects.get(deptno=deptno)
        workforce.save()
        return redirect('workforce_list')
    return render(request,'update_workforce.html',{'workforce':workforce,'department':department})
@login_required(login_url='login')
def delete_workforce(request,wfno):
    workforce = get_object_or_404(Workforce,wfno=wfno)
    workforce.delete()
    return redirect('workforce_list')