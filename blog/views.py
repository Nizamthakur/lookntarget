from django.shortcuts import render
from .models import blog , Employee

# Create your views here.

# blog view 
def home_page (request):
    b_data  = blog.objects.all()
    context = {'user_blog': b_data} 
    return render (request,'index.html', context)

def employee_details(request):
    employee_data = Employee.objects.all()
   
    return render(request, 'index.html', {'employee': employee_data})
#detailview
def detailblog (request , id ) : 
    b_detail = blog.objects.get(id = id)
    return render  (request , 'blogdetail.html', {'blog': b_detail})

