from django.shortcuts import render
from django.http import HttpResponse
from .models import RandomImage
from django.template import loader

# Create your views here.
def index(request):
    # title = "Spacepic<br>"
    # images = RandomImage.objects.order_by("image_num")[:5]
    # #formatted_images = "<br>".join([str(q.image_num) for q in images])
    # formatted_images = "<br>".join([f"{str(q.image_num)} - {q.image_url}" for q in images])
    
    # output = title + "<br>" + formatted_images
    # return HttpResponse(output)
    images = RandomImage.objects.order_by("image_num")[:5]
    template = loader.get_template("photogen/index.html")
    context = {
        "images": images,
        }
    return HttpResponse(template.render(context, request))