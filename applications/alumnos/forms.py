from django  import forms
from .models import Alumno


class AlumnoForm(forms.ModelForm):
    """Form definition for Alumno."""

    class Meta:
        """Meta definition for Alumnoform."""

        model = Alumno
        fields = ('__all__')
