from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User

class Empresa(models.Model):
    nomempresa = models.CharField(db_column='nomEmpresa', max_length=255)

    def __str__(self):
        return self.nomempresa


class Gastosdiarios(models.Model):
    descripcion = models.CharField(max_length=255)
    gasto = models.IntegerField()
    fecha = models.DateField(auto_now_add = True)


class Marcas(models.Model):
    nommarca = models.CharField(db_column='nomMarca', max_length=255)
    
    def __str__(self):
        return self.nommarca.capitalize()


class Mercancia(models.Model):
    idreferencia = models.ForeignKey('Referencia', models.DO_NOTHING, db_column='idReferencia')
    fecha = models.DateField()
    cantidad = models.IntegerField()


class Posicion(models.Model):
    nomposicion = models.CharField(db_column='nomPosicion', max_length=255)

    def __str__(self):
        return self.nomposicion.capitalize()


class Radiadores(models.Model):
    idmarca = models.ForeignKey(Marcas, models.DO_NOTHING, db_column='idMarca')
    referencia = models.CharField(max_length=255)
    preciocosto = models.IntegerField(db_column='precioCosto')
    precioventa = models.IntegerField(db_column='precioVenta')


class Referencia(models.Model):
    nomreferencia = models.CharField(db_column='nomReferencia', max_length=255)
    idmarcas = models.ForeignKey('Marcas', models.DO_NOTHING, db_column='idMarcas')
    idubicacion = models.ForeignKey('Ubicacion', models.DO_NOTHING, db_column='idUbicacion')
    numreferencia = models.IntegerField(db_column='numReferencia', blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    idposicion = models.ForeignKey(Posicion, models.DO_NOTHING, db_column='idPosicion')
    idempresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='idEmpresa', blank=True, null=True)
    preciocosto = models.IntegerField(db_column='precioCosto')
    
    def __str__(self):
        return f'{self.nomreferencia.capitalize()} lado {self.idubicacion}'


class Ubicacion(models.Model):
    nomubicacion = models.CharField(db_column='nomUbicacion', max_length=100)
    
    def __str__(self):
        return self.nomubicacion.capitalize()


class UsuarioManager(BaseUserManager):
    def create_user(self, documento, nombre, apellido, password = None):

        usuario = self.model(
            documento = documento,
            nombre = nombre,
            apellido = apellido
        )

        usuario.set_password(password)
        usuario.save()
        return usuario
    
    def create_superuser(self, documento, nombre, apellido, password):
        usuario = self.create_user(
            documento = documento,
            nombre = nombre,
            apellido = apellido,
            password = password
        )

        usuario.is_staff = True
        usuario.save()
        return usuario

class Usuario(AbstractBaseUser):
    nombre = models.CharField(max_length = 100)
    apellido = models.CharField(max_length = 100)
    documento = models.CharField('Numero de documento',max_length = 11, unique = True)
    email = models.CharField(max_length = 100, db_column = 'correo', unique = True)
    password = models.CharField(max_length = 100, null = True, blank = True)
    imagen = models.ImageField(upload_to = 'imagen_usuario', db_column = 'imagen', null = True, blank = True)
    registro = models.DateField(auto_now_add = True)
    last_login = models.DateTimeField(auto_now = True, null = True, blank = True)
    is_active = models.BooleanField()
    is_staff = models.BooleanField(default = False)
    objects = UsuarioManager()

    USERNAME_FIELD = 'documento'
    REQUIRED_FIELDS = ['nombre', 'apellido']

    def __str__(self):
        return f'{self.nombre}'

    def has_perm(self,perm,obj = None):
        return True

    def has_module_perms(self,app_label):
        return True
    
    @property
    def is_satff(self):
        return self.is_staff


class Ventadiaria(models.Model):
    descripcion = models.CharField(max_length=255)
    ventatanque = models.ForeignKey(Referencia, models.DO_NOTHING, db_column='ventaTanque', blank=True, null=True)
    precioventa = models.IntegerField(db_column='precioVenta')
    fecha = models.DateField(auto_now_add=True)