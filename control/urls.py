from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # ! Modulo de Inicio e Interfaz
    path('', views.Home, name='index'),
    path('inicio/', views.Home, name='inicio'),
    path('registro/', views.Registrarse, name='registro'),
    path('logout/', views.Logout, name="logout"),
    path('interfaz/', login_required(views.Interfaz, login_url='inicio'), name='interfaz'),
    # ! Modulo de Inicio e Interfaz
    
    # ! Modulo de Gastos Diarios
    path('gastoDiario/', login_required(views.GastosDiarios.as_view(), login_url = 'inicio'), name="gastoDiario"),
    path('crear_GastoDiario/', login_required(views.crearGastosDiarios.as_view(), login_url = 'inicio'), name="crear_GastoDiario"),
    path('editar_GastoDiario/<int:pk>', login_required(views.editarGastosDiarios.as_view(), login_url = 'inicio'), name="editar_GastoDiario"),
    path('confirmElimGastoDiario/<int:pk>', login_required(views.confirmarEliminarGastosDiarios.as_view(), login_url = 'inicio'), name="confirmElimGastoDiario"),
    path('eliminarGastoDiario/<int:id>', login_required(views.eliminarGastosDiarios), name="eliminarGastoDiario"),
    # ! Modulo de Gastos Diarios

    # ! Modulo de Marcas
    path('marca/', login_required(views.Marcass.as_view(), login_url = 'inicio'), name="marca"),
    path('crear_Marca/', login_required(views.crearMarcas.as_view(), login_url = 'inicio'), name="crear_Marca"),
    path('editar_Marca/<int:pk>', login_required(views.editarMarcas.as_view(), login_url = 'inicio'), name="editar_Marca"),
    path('confirmElimMarca/<int:pk>', login_required(views.confirmarEliminarMarcas.as_view(), login_url = 'inicio'), name="confirmElimMarca"),
    path('eliminarMarca/<int:id>', login_required(views.eliminarMarcas), name="eliminarMarca"),
    # ! Modulo de Marcas

    # ! Modulo de Mercancias
    path('mercancia/', login_required(views.Mercancias.as_view(), login_url = 'inicio'), name="mercancia"),
    path('crear_Mercancia/', login_required(views.crearMercancias.as_view(), login_url = 'inicio'), name="crear_Mercancia"),
    path('editar_Mercancia/<int:pk>', login_required(views.editarMercancias.as_view(), login_url = 'inicio'), name="editar_Mercancia"),
    path('confirmElimMercancia/<int:pk>', login_required(views.confirmarEliminarMercancias.as_view(), login_url = 'inicio'), name="confirmElimMercancia"),
    path('eliminarMercancia/<int:id>', login_required(views.eliminarMercancias), name="eliminarMercancia"),
    # ! Modulo de Mercancias

    # ! Modulo de Referencias
    path('referencia/', login_required(views.Referencias.as_view(), login_url = 'inicio'), name="referencia"),
    path('crear_Referencia/', login_required(views.crearReferencias.as_view(), login_url = 'inicio'), name="crear_Referencia"),
    path('editar_Referencia/<int:pk>', login_required(views.editarReferencias.as_view(), login_url = 'inicio'), name="editar_Referencia"),
    path('confirmElimReferencia/<int:pk>', login_required(views.confirmarEliminarReferencias.as_view(), login_url = 'inicio'), name="confirmElimReferencia"),
    path('eliminarReferencia/<int:id>', login_required(views.eliminarReferencias), name="eliminarReferencia"),
    # ! Modulo de Referencias

    # ! Modulo de Ventas Diarias
    path('ventaDiaria/', login_required(views.VentasDiarias.as_view(), login_url = 'inicio'), name="ventaDiaria"),
    path('crear_VentaDiaria/', login_required(views.crearVentasDiarias.as_view(), login_url = 'inicio'), name="crear_VentaDiaria"),
    path('editar_VentaDiaria/<int:pk>', login_required(views.editarVentasDiarias.as_view(), login_url = 'inicio'), name="editar_VentaDiaria"),
    path('confirmElimVentaDiaria/<int:pk>', login_required(views.confirmarEliminarVentasDiarias.as_view(), login_url = 'inicio'), name="confirmElimVentaDiaria"),
    path('eliminarVentaDiaria/<int:id>', login_required(views.eliminarVentasDiarias), name="eliminarVentaDiaria"),
    # ! Modulo de Ventas Diarias
]