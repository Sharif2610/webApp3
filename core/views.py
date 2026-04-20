from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'language' :['python','django','react']
    }
    return render(request,'core/home.html',context)
def about(request):
    return render(request,'core/about.html')