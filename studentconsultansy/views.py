from django.shortcuts import render

# Create your views here.
def s_cun (request):
    # b_data  = blog.objects.all()
    # context = {'user_blog': b_data} 
    return render (request,'studentc.html')