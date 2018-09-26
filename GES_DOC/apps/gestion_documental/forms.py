from django.forms import ModelForm
from .models import DocumentoAdmitido


class DocumentoAdmitidoForm(ModelForm):
    class Meta:
        model = DocumentoAdmitido
        fields = [
            'documento',
            'archivo',
            'admitido',
        ]

    def __init__(self, *args, **kwargs):
        super(DocumentoAdmitidoForm, self).__init__(*args, **kwargs)
        self.fields['documento'].empty_label = '-- Seleccione --'

