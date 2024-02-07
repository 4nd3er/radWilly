import json
from django.core.serializers import serialize
from datetime import datetime
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import TemplateView, View, UpdateView, CreateView, DeleteView, ListView
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

# ! Modulo de Inicio e Interfaz
def Home(request):
    if request.user.is_authenticated:
        return redirect('interfaz')
    else:
        if request.method == 'POST':
            documento = request.POST.get('documento')
            password = request.POST.get('password')

            user = authenticate(request, documento = documento, password = password)

            if documento == "" and password == "":
                messages.warning(request, 'Digita en los campos correspondientes para el inicio de sesion')
                return render(request, 'inicio_sesion/inicio.html')
            userFilter = Usuario.objects.filter(documento=documento).values_list('is_active', flat=True)
            if user is not None:
                login(request, user)
                return redirect('interfaz')
            elif not userFilter:
                messages.error(request, 'Usuario no registrado en la pagina web, registrate para iniciar sesion')
            else:
                messages.error(request, 'Numero de documento y/o contraseña incorrectos, vuelve a intentarlo')
    return render(request, 'inicio_sesion/inicio.html')

def Registrarse(request):
    # * rol = request.POST.get('rol
    # * initial={'rol: 'rol}
    registro = UsuarioForm()# *initial=initial
    if request.method == 'POST':
        # * contraseña = request.POST.get("contraseña")
        registro = UsuarioForm(request.POST, request.FILES)
        
        if registro.is_valid():
            registro.is_active = 1 # TODO comprobar si sirve
            registro.save()
            messages.success(request,'Te has registrado exitosamente')
            return redirect('inicio')
    return render(request, 'inicio_sesion/registrarse.html', { 'form': registro })

def Interfaz(request):
    return render(request, 'interfaz/interfaces.html')

def Logout(request):
    logout(request)
    return redirect('inicio')
# ! Modulo de Inicio e Interfaz


# ! Modulo de Gastos Diarios
class GastosDiarios(ListView):
    model = Gastosdiarios
    template_name = 'gastosDiarios/gastosDiarios.html'

    def get_queryset(self):
        return self.model.objects.filter(
            Q(fecha__icontains = str(datetime.now()).split(' ')[0])
        )

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto["gastoDiario"] = self.get_queryset()
        return contexto

    def get(self, request, *args, **kwargs):
        if is_ajax(request=request):
                return HttpResponse(serialize('json', self.get_context_data()), 'application/json')
        else:
            return render(request, self.template_name, {'ventaDiaria': self.get_queryset()})

class crearGastosDiarios(CreateView):
    model = Gastosdiarios
    template_name = 'gastosDiarios/crear.html'
    form_class = gastoDiarioForm
    success_url = reverse_lazy('gastoDiario')

    def post(self, request, *args, **kwargs):
        if is_ajax(request=request):
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'no hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se pudo registrar'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('gastoDiario')

class editarGastosDiarios(UpdateView):
    model = Gastosdiarios
    template_name = 'gastosDiarios/editar.html'
    form_class = gastoDiarioForm
    success_url = reverse_lazy('gastoDiario')

    def post(self, request, *args, **kwargs):
        if is_ajax(request=request):
            form = self.form_class(request.POST, instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'no hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se pudo actualizar'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            redirect('gastoDiario')

class confirmarEliminarGastosDiarios(DeleteView):
    model = GastosDiarios
    template_name = 'gastosDiarios/gastosDiarios_confirm_delete.html'
    success_url = reverse_lazy('gastoDiario')

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)

def eliminarGastosDiarios(request, id):
    eliminar = Gastosdiarios.objects.get(id = id)
    eliminar.delete()
    return redirect('gastoDiario')
# ! Modulo de Gastos Diarios


# ! Modulo de Marcas
class Marcass(ListView):
    model = Marcas
    template_name = 'marcas/marcas.html'

    def get_queryset(self):
        return self.model.objects.all().order_by('nommarca')

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto["marca"] = self.get_queryset()
        return contexto

    def get(self, request, *args, **kwargs):
        if is_ajax(request=request):
                return HttpResponse(serialize('json', self.get_context_data()), 'application/json')
        else:
            return render(request, self.template_name, {'marca': self.get_queryset()})

class crearMarcas(CreateView):
    model = Marcas
    template_name = 'marcas/crear.html'
    form_class = marcaForm
    success_url = reverse_lazy('marca')

    def post(self, request, *args, **kwargs):
        if is_ajax(request=request):
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'no hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se pudo registrar'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('referencia')

class editarMarcas(UpdateView):
    model = Marcas
    template_name = 'marcas/editar.html'
    form_class = marcaForm
    success_url = reverse_lazy('marca')

    def post(self, request, *args, **kwargs):
        if is_ajax(request=request):
            form = self.form_class(request.POST, instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'no hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se pudo actualizar'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            redirect('referencia')

class confirmarEliminarMarcas(DeleteView):
    model = Marcas
    template_name = 'marcas/marcas_confirm_delete.html'
    success_url = reverse_lazy('marca')

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)

def eliminarMarcas(request, id):
    eliminar = Marcas.objects.get(id = id)
    eliminar.delete()
    return redirect('marca')
# ! Modulo de Marcas


# ! Modulo de Mercancia
class Mercancias(ListView):
    model = Mercancia
    template_name = 'mercancias/mercancias.html'

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto["mercancia"] = self.get_queryset()
        return contexto

    def get(self, request, *args, **kwargs):
        if is_ajax(request=request):
            return HttpResponse(serialize('json', self.get_context_data()), 'application/json')
        else:
            return render(request, self.template_name, {'mercancia': self.get_queryset()})

class crearMercancias(CreateView):
    model = Mercancia
    template_name = 'mercancias/crear.html'
    form_class = mercanciaForm
    success_url = reverse_lazy('mercancia')

    def post(self, request, *args, **kwargs):
        if is_ajax(request=request):
            form = self.form_class(request.POST)
            if form.is_valid():
                referenciaForm = str(form.cleaned_data['idreferencia'])
                partes = referenciaForm.split(' ', 3)[-1]
                referencia = Referencia.objects.get(nomreferencia=partes)
                cantidadReferenciaForm = form.cleaned_data['cantidad']
                referencia.cantidad += cantidadReferenciaForm
                referencia.save()
                form.save()
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'no hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se pudo registrar'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('referencia')

class editarMercancias(UpdateView):
    model = Mercancia
    template_name = 'mercancias/editar.html'
    form_class = mercanciaForm
    success_url = reverse_lazy('mercancia')

    def post(self, request, *args, **kwargs):
        if is_ajax(request=request):
            form = self.form_class(request.POST, instance = self.get_object())
            if form.is_valid():
                referenciaForm = str(form.cleaned_data['idreferencia'])
                partes = referenciaForm.split(' ', 3)[-1]
                referencia = Referencia.objects.get(nomreferencia=partes)
                mercanciaSaved = self.model.objects.get(id= self.get_object().id).cantidad
                mercanciaForm = int(form.cleaned_data['cantidad'])
                if mercanciaSaved > mercanciaForm:
                    mercanciaSaved -= mercanciaForm
                    referencia.cantidad -= mercanciaSaved
                else:
                    mercanciaForm -= mercanciaSaved
                    referencia.cantidad += mercanciaForm
                referencia.save()
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'no hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se pudo actualizar'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            redirect('referencia')

class confirmarEliminarMercancias(DeleteView):
    model = Mercancia
    template_name = 'mercancias/mercancias_confirm_delete.html'
    success_url = reverse_lazy('mercancia')

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)

def eliminarMercancias(request, id):
    eliminar = Marcas.objects.get(id = id)
    eliminar.delete()
    return redirect('mercancia')
# ! Modulo de Mercancia


# ! Modulo de Referencias
class Radiadores(ListView):
    model = Radiadores
    template_name = 'radiadores/radiadores.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')

        if buscar:
            query = self.model.objects.filter(
                Q(idmarcas__nommarca__icontains = buscar) |
                Q(nomreferencia__icontains = buscar) |
                Q(numreferencia__icontains = buscar) |
                Q(cantidad__icontains = buscar) |
                Q(idubicacion__nomubicacion__icontains = buscar) |
                Q(idposicion__nomposicion__icontains = buscar) |
                Q(idempresa__nomempresa__icontains = buscar) |
                Q(preciocosto__icontains = buscar)
            ).distinct().order_by('id')
        else:
            query = 0
        return query

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto["referencia"] = self.get_queryset()
        contexto["marcas"] = Marcas.objects.all().order_by('nommarca')
        contexto["posiciones"] = Posicion.objects.all().order_by('id')
        return contexto

    def get(self, request, *args, **kwargs):
        if is_ajax(request=request):
                return HttpResponse(serialize('json', self.get_context_data()), 'application/json')
        else:
            return render(request, self.template_name, {'referencia': self.get_queryset(), 'marcas': self.get_context_data()['marcas'], 'posiciones': self.get_context_data()['posiciones']})

class crearRadiadores(CreateView):
    model = Radiadores
    template_name = 'radiadores/crear.html'
    form_class = radiadorForm
    success_url = reverse_lazy('referencia')

    def post(self, request, *args, **kwargs):
        if is_ajax(request=request):
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'no hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se pudo registrar'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('referencia')

class editarRadiadores(UpdateView):
    model = Radiadores
    template_name = 'radiadores/editar.html'
    form_class = radiadorForm
    success_url = reverse_lazy('referencia')

    def post(self, request, *args, **kwargs):
        if is_ajax(request=request):
            form = self.form_class(request.POST, instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'no hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se pudo actualizar'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            redirect('referencia')

class confirmarEliminarRadiadores(DeleteView):
    model = Radiadores
    template_name = 'radiadores/radiadores_confirm_delete.html'
    success_url = reverse_lazy('referencia')

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)

def eliminarRadiadores(request, id):
    eliminar = Referencia.objects.get(id = id)
    eliminar.delete()
    return redirect('referencia')
# ! Modulo de Referencias


# ! Modulo de Referencias
class Referencias(ListView):
    model = Referencia
    template_name = 'referencias/referencias.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')

        if buscar:
            query = self.model.objects.filter(
                Q(idmarcas__nommarca__icontains = buscar) |
                Q(nomreferencia__icontains = buscar) |
                Q(numreferencia__icontains = buscar) |
                Q(cantidad__icontains = buscar) |
                Q(idubicacion__nomubicacion__icontains = buscar) |
                Q(idposicion__nomposicion__icontains = buscar) |
                Q(idempresa__nomempresa__icontains = buscar) |
                Q(preciocosto__icontains = buscar)
            ).distinct().order_by('id')
        else:
            query = 0
        return query

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto["referencia"] = self.get_queryset()
        contexto["marcas"] = Marcas.objects.all().order_by('nommarca')
        contexto["posiciones"] = Posicion.objects.all().order_by('id')
        return contexto

    def get(self, request, *args, **kwargs):
        if is_ajax(request=request):
                return HttpResponse(serialize('json', self.get_context_data()), 'application/json')
        else:
            return render(request, self.template_name, {'referencia': self.get_queryset(), 'marcas': self.get_context_data()['marcas'], 'posiciones': self.get_context_data()['posiciones']})

class crearReferencias(CreateView):
    model = Referencia
    template_name = 'referencias/crear.html'
    form_class = referenciaForm
    success_url = reverse_lazy('referencia')

    def post(self, request, *args, **kwargs):
        if is_ajax(request=request):
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'no hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se pudo registrar'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('referencia')

class editarReferencias(UpdateView):
    model = Referencia
    template_name = 'referencias/editar.html'
    form_class = referenciaForm
    success_url = reverse_lazy('referencia')

    def post(self, request, *args, **kwargs):
        if is_ajax(request=request):
            form = self.form_class(request.POST, instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'no hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se pudo actualizar'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            redirect('referencia')

class confirmarEliminarReferencias(DeleteView):
    model = Referencia
    template_name = 'referencias/referencias_confirm_delete.html'
    success_url = reverse_lazy('referencia')

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)

def eliminarReferencias(request, id):
    eliminar = Referencia.objects.get(id = id)
    eliminar.delete()
    return redirect('referencia')
# ! Modulo de Referencias


# ! Modulo de Ventas Diarias
class VentasDiarias(ListView):
    model = Ventadiaria
    template_name = 'ventasDiarias/ventasDiarias.html'

    def get_queryset(self):
        return self.model.objects.filter(
            Q(fecha__icontains = str(datetime.now()).split(' ')[0])
        )

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto["ventaDiaria"] = self.get_queryset()
        return contexto

    def get(self, request, *args, **kwargs):
        if is_ajax(request=request):
                return HttpResponse(serialize('json', self.get_context_data()), 'application/json')
        else:
            return render(request, self.template_name, {'ventaDiaria': self.get_queryset()})

class crearVentasDiarias(CreateView):
    model = Ventadiaria
    template_name = 'ventasDiarias/crear.html'
    form_class = ventaDiariaForm
    success_url = reverse_lazy('ventaDiaria')

    def post(self, request, *args, **kwargs):
        if is_ajax(request=request):
            form = self.form_class(request.POST)
            if form.is_valid():
                referenciaForm = str(form.cleaned_data['ventatanque'])
                partes = referenciaForm.split(' ', 3)[-1]
                if referenciaForm is not None:
                    referencia = Referencia.objects.get(nomreferencia=partes)
                    referencia.cantidad -= 1
                    referencia.save()
                form.save()
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'no hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se pudo registrar'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('ventaDiaria')

class editarVentasDiarias(UpdateView):
    model = Ventadiaria
    template_name = 'ventasDiarias/editar.html'
    form_class = ventaDiariaForm
    success_url = reverse_lazy('ventaDiaria')

    def post(self, request, *args, **kwargs):
        if is_ajax(request=request):
            form = self.form_class(request.POST, instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'no hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se pudo actualizar'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            redirect('ventaDiaria')

class confirmarEliminarVentasDiarias(DeleteView):
    model = Ventadiaria
    template_name = 'ventasDiarias/ventasDiarias_confirm_delete.html'
    success_url = reverse_lazy('ventaDiaria')

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)

def eliminarVentasDiarias(request, id):
    eliminar = Ventadiaria.objects.get(id = id)
    eliminar.delete()
    return redirect('ventaDiaria')
# ! Modulo de Ventas Diarias