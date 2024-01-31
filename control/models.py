from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Usuario', models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Usuario', models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('Usuario', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empresa(models.Model):
    nomempresa = models.CharField(db_column='nomEmpresa', max_length=255)

    class Meta:
        managed = False
        db_table = 'empresa'

    def __str__(self):
        return self.nomempresa


class Gastosdiarios(models.Model):
    descripcion = models.CharField(max_length=255)
    gasto = models.IntegerField()
    fecha = models.DateField(auto_now_add = True)

    class Meta:
        ordering = [('-id')]
        managed = False
        db_table = 'gastosdiarios'


class Marcas(models.Model):
    nommarca = models.CharField(db_column='nomMarca', max_length=255)

    class Meta:
        managed = False
        db_table = 'marcas'
    
    def __str__(self):
        return self.nommarca.capitalize()


class Mercancia(models.Model):
    idreferencia = models.ForeignKey('Referencia', models.DO_NOTHING, db_column='idReferencia')
    fecha = models.DateField()
    cantidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mercancia'


class Posicion(models.Model):
    nomposicion = models.CharField(db_column='nomPosicion', max_length=255)

    class Meta:
        managed = False
        db_table = 'posicion'

    def __str__(self):
        return self.nomposicion.capitalize()
    


class Referencia(models.Model):
    nomreferencia = models.CharField(db_column='nomReferencia', max_length=255)
    idmarcas = models.ForeignKey(Marcas, models.DO_NOTHING, db_column='idMarcas')
    idubicacion = models.ForeignKey('Ubicacion', models.DO_NOTHING, db_column='idUbicacion')
    numreferencia = models.IntegerField(db_column='numReferencia', blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    idposicion = models.ForeignKey(Posicion, models.DO_NOTHING, db_column='idPosicion')
    idempresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='idEmpresa', blank=True, null=True)
    preciocosto = models.IntegerField(db_column='precioCosto')

    class Meta:
        managed = False
        db_table = 'referencia'
    
    def __str__(self):
        return f'Lado {self.idubicacion} {self.idmarcas} {self.nomreferencia.capitalize()}'


class Ubicacion(models.Model):
    nomubicacion = models.CharField(db_column='nomUbicacion', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ubicacion'
    
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

    class Meta:
        ordering = [('-id')]
        managed = False
        db_table = 'usuario'


class Ventadiaria(models.Model):
    descripcion = models.CharField(max_length=255)
    ventatanque = models.ForeignKey(Referencia, models.DO_NOTHING, db_column='ventaTanque', blank=True, null=True)
    precioventa = models.IntegerField(db_column='precioVenta')
    fecha = models.DateField(auto_now_add = True)

    class Meta:
        ordering = [('-id')]
        managed = False
        db_table = 'ventadiaria'