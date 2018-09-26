from time import strftime
from django.core import serializers
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy

from .models import Admitido
from apps.documentos.models import TipoDocumento
from apps.programas.models import Programa


class IndexTemplateView(TemplateView):
    template_name = 'admitidos/index.html'

    def get(self, request, *args, **kwargs):
        request.session.set_expiry(0)
        request.session.get_expire_at_browser_close()

        if  request.session.get('ID_ADMITIDO', None) and request.session.get('ID_PROGRAMA', None) and request.session.get('ID_PERIODO', None):
            return HttpResponseRedirect(reverse_lazy('SGD_Index'))
        return super(IndexTemplateView, self).get(request, args, kwargs)


def obtener_programas(request):
    data = Programa.objects.all().values('id', 'descripcion')
    list_data = list(data)
    return JsonResponse(list_data, safe=False)


def obtener_tipo_documentos(request):
    data = TipoDocumento.objects.all().values('codigo', 'descripcion')
    list_data = list(data)
    return JsonResponse(list_data, safe=False)


def obtener_sesion_admitido(request):
    if request.is_ajax() and request.method == 'POST':
        try:
            post = request.POST
            anio = strftime("%Y")
            mes = int(strftime("%m"))
            periodo = '01'

            if mes > 6 and mes < 13:
                periodo = '02'

            admitido = Admitido.objects.get(
                programa=post.get('programa', None),
                tipo_documento=post.get('tipo_documento', None),
                numero_identificacion=post.get('identificacion', None),
                anio=anio,
                periodo=periodo
            )

            request.session['ID_ADMITIDO'] = admitido.pk
            request.session['ID_PROGRAMA'] = admitido.programa.pk
            request.session['ID_PERIODO'] = admitido.periodo
        
            return JsonResponse({'ok': True, 'msg': 'Petición Correcta.'})
        except Admitido.DoesNotExist:
            return JsonResponse({'ok': False, 'msg': 'No existe un usuario admitido con los datos suministrados.'})
        except:
            return JsonResponse({'ok': False, 'msg': 'Ocurrio un error en el servidor.'})    
    else:
        return JsonResponse({'ok': False, 'msg': 'Petición no valida.'})
