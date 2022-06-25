from pipes import Template
from django.http import HttpResponse
from datetime import datetime

from django.template import Template , Context, loader
from vistas.models import Familiar




def inicio(request):
    return HttpResponse('Vista en django')

def ver_fecha(request):
    fecha_actual = datetime.now()
    return HttpResponse(f'Fecha actual : {fecha_actual} ')

def saludo(request,nombre):
    return HttpResponse(f'Hola {nombre}')

def mi_template(request,nombre_fam,edad_fam,fecha_fam):
    
    template1 = loader.get_template('prueba.html')
    
    nombre = 'Lucas'
    apellido = 'Alonso' 
    fechanac = '1993/06/12'
    
    familiar = Familiar(nombre=nombre_fam, edad=edad_fam,fecha_nacimiento=fecha_fam)
    familiar.save()
        
    render1 = template1.render({'nombre': nombre, 'apellido': apellido,'fechanac':fechanac,'familiar': familiar})
    
    return HttpResponse(render1)

def listado_familiares(request):
    
    template = loader.get_template('listado_familiares.html')
    
    lista_familiares = Familiar.objects.all()
    
    render = template.render({'lista': lista_familiares})
    
    return HttpResponse(render)

