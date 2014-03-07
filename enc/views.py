import json
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, render_to_response

# Create your views here.
from enc.models import Encuesta, Imagen
from encuestas.settings import SERVER_DOMAIN


def encuesta(request):
    if Encuesta.objects.filter(vigente=True).exists():
        enc = Encuesta.objects.filter(vigente=True)[:1].get()
        response = HttpResponse(enc.datos)
        response['content_type'] = 'application/json; charset=utf-8'

        return response
    else:
        return HttpResponse(json.dumps({"error":"No existe encuesta"}), mimetype="application/json")

def imagen(request, id):
    if Imagen.objects.filter(id=id).exists():
        img = Imagen.objects.get(pk=id)
        try:
            f = open(str(img.archivo.file), "rb")
            return HttpResponse(f.read(), mimetype="image/jpeg")
        except IOError:
            raise Http404
    else:
        raise Http404


def index(request):
    return render_to_response("index.html",{"SERVER_URL": SERVER_DOMAIN})