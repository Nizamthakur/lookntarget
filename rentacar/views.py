from django.shortcuts import render
from .models import car , faq
# Create your views here.
def rcar (request):
    # b_data  = blog.objects.all()
    # context = {'user_blog': b_data} 
    return render (request,'rentacar.html')


def View_faq (request): 
    rcar = faq.objects.all()
    context = {'r_car': rcar}
    return render(request, 'rentacar.html', context)