from django.shortcuts import render
from django.http import HttpResponse
from .models import RandomImage
from django.template import loader
from .forms import HomeForm
import requests
import base64

# Create your views here.
# nasa api key mbpurdy@asu.edu
# T3K8debLg8Ux7vKfbn3w00lTUPTkJuuUog7VbCwE 
def index(request):
    template = loader.get_template("photogen/index.html")
    form = HomeForm()
    context = {"form": form}
    


    # api_url = 'https://picsum.photos/200'

    # response = requests.get(api_url)
    
    # if response.status_code == 200:
    #         data = response.content
    #         return HttpResponse(data, content_type='image/jpeg')
    # else:
    #     return HttpResponse("FAILED")



    
    if request.method == 'POST':
        form = HomeForm(request.POST)
        if form.is_valid():
            numpics = form.cleaned_data['post']
            #images = RandomImage.objects.order_by("image_num")[:5]

            api_url = 'https://picsum.photos/200'
            photoset = {}
            for i in range(numpics):
                response = requests.get(api_url)
                if response.status_code == 200:
                    images = response.content
                    base64_image = base64.b64encode(images).decode('utf-8')
                    photoset[f"key_{i}"] = f"data:image/jpeg;base64,{base64_image}"
                else:
                    return HttpResponse("FAILED2")

            
            context = {
                "images": photoset,
                "form": form,
                "text": numpics
                }

            return HttpResponse(template.render(context, request))
        else:
            return HttpResponse('Form not valid???')
    else:
        return HttpResponse(template.render(context, request))   