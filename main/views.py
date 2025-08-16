from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("صفحه اصلی سایت تدریس خصوصی فیزیک")

def about(request):
    return HttpResponse("درباره مدرس و روش تدریس")

def courses(request):
    return HttpResponse("دوره‌های دبیرستان و دانشگاه")

def blog(request):
    return HttpResponse("مقالات آموزشی فیزیک")

def contact(request):
    return HttpResponse("تماس با مدرس")
from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')
