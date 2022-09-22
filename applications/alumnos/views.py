from django.urls import reverse_lazy
from django.shortcuts import render

from django.views.generic import (
                                TemplateView,
                                CreateView,
                                ListView,
                                DeleteView,
                                UpdateView,
                                DetailView
                                )


from .forms import AlumnoForm
from .models import Alumno
# Create your views here.




class AlumnoView(TemplateView):
    template_name = "alumnos/index.html"
    
    def get_context_data(self, **kwargs):
        context = super(AlumnoView, self).get_context_data(**kwargs)
        context['form']=AlumnoForm
        context['alumnos']=Alumno.objects.all().order_by('-hora')[:4]
        return context
    
    

class AlumnoCreateView(CreateView):
    form_class=AlumnoForm
    success_url='/'




class AlumnoListView(ListView):
    model = Alumno
    template_name = "alumnos/lista.html"
    context_object_name='lista'
    paginate_by=5
    

class AlumnoDetailView(DetailView):
    model = Alumno
    template_name = "alumnos/detail.html"
    


class AlumnoUpdateView(UpdateView):
    model = Alumno
    template_name = "alumnos/update.html"
    fields=('__all__')
    success_url=reverse_lazy('alumno_app:List')


class AlumnoDeleteView(DeleteView):
    model = Alumno
    success_url=reverse_lazy('alumno_app:List')
