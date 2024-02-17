from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import SessionZip
from django.template import loader
from .forms import HomeForm
import requests
import base64
import zipfile
import io


# Create your views here.

def index(request):
    template = loader.get_template("photogen/index.html")
    form = HomeForm()
    context = {"form": form}
        
    if request.method == 'POST':
        form = HomeForm(request.POST)
        if form.is_valid():
            numpics = form.cleaned_data['post']

            api_url = 'https://picsum.photos/200'
            photoset = {}
            zippable = []
            for i in range(numpics):
                response = requests.get(api_url)
                if response.status_code == 200:
                    images = response.content

                    base64_image = base64.b64encode(images).decode('utf-8')
                    photoset[f"key_{i}"] = f"data:image/jpeg;base64,{base64_image}"
                    
                    zippable.append(response.content)               

                else:
                    return HttpResponse("FAILED2")


            session_zip = SessionZip(session_id=1)

            zip_buffer = io.BytesIO()
            with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
                for i, image in enumerate(zippable):
                    zip_file.writestr(f'image_{i}.jpg', image)
                    
                    
            zip_buffer.seek(0)
            
            #response = HttpResponse(zip_buffer, content_type='application/zip')
            #response['Content-Disposition'] = 'attachment; filename=images.zip'
           
            session_zip.file_download.save("pictures", zip_buffer)
            session_zip.save()
            
            context = {
                "zip": zip_buffer,
                "images": photoset,
                "form": form,
                "text": numpics
                }

            return HttpResponse(template.render(context, request))
        else:
            
            context['form_validation_error_message'] = "Please enter a number between 1 and 5."
            return HttpResponse(template.render(context, request))
    else:
        return HttpResponse(template.render(context, request)) 
    
def results(request):
    
    my_instance = get_object_or_404(SessionZip, session_id=1)
    
    response = HttpResponse(my_instance.file_download, content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename=images.zip'
    
    return response