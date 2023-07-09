from django.shortcuts import render

# Create your views here.
def ielts (request):
    # b_data  = blog.objects.all()
    # context = {'user_blog': b_data} 
    return render (request,'ielts.html')