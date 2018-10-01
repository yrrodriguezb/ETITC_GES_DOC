from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic import CreateView, DeleteView
from django.urls import reverse_lazy
from .models import DocumentoAdmitido, Documento, Admitido
from .forms import DocumentoAdmitidoForm


class DocumentoAdmitidoView(CreateView):
    form_class = DocumentoAdmitidoForm
    template_name = "gestion_documental/index.html"
    success_url = reverse_lazy('SGD_Index')

    def get(self, request, *args, **kwargs):
        if  request.session.get('ID_ADMITIDO', None) and request.session.get('ID_PROGRAMA', None) and request.session.get('ID_PERIODO', None):
            return super(DocumentoAdmitidoView, self).get(request, args, kwargs)
        return HttpResponseRedirect(reverse_lazy('index'))

    def get_context_data(self, **kwargs):
        context = super(DocumentoAdmitidoView, self).get_context_data(**kwargs)
        admitido = Admitido.objects.get(pk=self.request.session.get('ID_ADMITIDO'))
        documentos = DocumentoAdmitido.objects.values_list('documento__id', 'archivo').filter(admitido=admitido)
        archivos = DocumentoAdmitido.objects.filter(admitido=self.request.session.get('ID_ADMITIDO'))
        aprobados = archivos.filter(aprobado=True)[:1]

        aprobado = False
        if len(aprobados) > 0:
            aprobado = aprobados[0].aprobado
        
        context['aprobar'] = Documento.objects.count() == len(archivos)
        context['aprobados'] = aprobado
        context['files'] = archivos
        context['admitido'] = admitido 

        return context


class DocumentoAdmitidoDeleteView(DeleteView):
    model = DocumentoAdmitido
    success_url = reverse_lazy('SGD_Index')


def obtener_lista_documentos(request):
    admitido = Admitido.objects.get(pk=request.session.get('ID_ADMITIDO'))
    documentos = DocumentoAdmitido.objects.values_list('documento__id', 'archivo').filter(admitido=admitido)

    list_value = []
    for x, y in documentos:
        if x not in list_value:
            list_value.append(x)
    
    data = Documento.objects.exclude(id__in=list_value).values('id', 'descripcion')
    list_data = list(data)
    return JsonResponse(list_data, safe=False)


def aprobar_documentos(request):
    admitido = Admitido.objects.get(pk=request.session.get('ID_ADMITIDO'))
    DocumentoAdmitido.objects.filter(admitido=admitido).update(aprobado=True)
    return HttpResponseRedirect(reverse_lazy('SGD_Index'))
