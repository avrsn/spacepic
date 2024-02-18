from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import SessionZip
from .forms import HomeForm
import requests, base64, zipfile, io, random


# Create your views here
def index(request):
    form = HomeForm()
    context = {"form": form}
    if request.method == 'POST':
        form = HomeForm(request.POST)
        if form.is_valid():
            numpics = form.cleaned_data['num']
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
                    return HttpResponse("response.status_code is not 200 @mbpurdy")

            random_session_id = random.randint(1, 10000)
            session_zip = SessionZip(session_id=random_session_id)

            zip_buffer = io.BytesIO()
            with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
                for i, image in enumerate(zippable):
                    zip_file.writestr(f'image_{i}.jpg', image)
                    
            zip_buffer.seek(0)
            zip_data = base64.b64encode(zip_buffer.read()).decode('utf-8')
            session_zip.file_download.save("pictures", zip_buffer)
            session_zip.save()
             
            context = {
                "zip": zip_data,
                "images": photoset,
                "text": numpics,
                "random_session_id": random_session_id,
                }

            request.session["context_data"] = context
            return HttpResponseRedirect(reverse("index"))
        else:
            template = loader.get_template("photogen/index.html")
            context['form_validation_error_message'] = "Please enter a number between 1 and 5."
            return HttpResponse(template.render(context, request))
    else:
        
        if request.session.get("context_data") is not None:
            template = loader.get_template("photogen/success.html")
            
            context_data = request.session.get("context_data")
            context_data['form'] = HomeForm()

            response = HttpResponse(template.render(context_data, request))
            response.set_cookie('session', context_data["random_session_id"])
            request.session["context_data"] = None
            return response
        else:
            template = loader.get_template("photogen/index.html")
            return HttpResponse(template.render(context, request))
    
def results(request):
    print("my session number:", request.COOKIES.get('session'))
    my_instance = get_object_or_404(SessionZip, session_id=request.COOKIES.get('session'))
    
    response = HttpResponse(my_instance.file_download, content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename=images.zip'
    
    my_instance.delete()
    my_instance.delete_pictures()
    
    return response