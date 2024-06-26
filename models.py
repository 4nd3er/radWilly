# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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
    nomempresa = models.CharField(db_column='nomEmpresa', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empresa'


class Gastosdiarios(models.Model):
    descripcion = models.CharField(max_length=255)
    gasto = models.IntegerField()
    fecha = models.DateField()

    class Meta:
        managed = False
        db_table = 'gastosdiarios'


class Marcas(models.Model):
    nommarca = models.CharField(db_column='nomMarca', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'marcas'


class Mercancia(models.Model):
    idreferencia = models.ForeignKey('Referencia', models.DO_NOTHING, db_column='idReferencia')  # Field name made lowercase.
    fecha = models.DateField()
    cantidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mercancia'


class Posicion(models.Model):
    nomposicion = models.CharField(db_column='nomPosicion', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'posicion'


class Radiadores(models.Model):
    idmarca = models.ForeignKey(Marcas, models.DO_NOTHING, db_column='idMarca')  # Field name made lowercase.
    referencia = models.CharField(max_length=255)
    preciocosto = models.IntegerField(db_column='precioCosto')  # Field name made lowercase.
    precioventa = models.IntegerField(db_column='precioVenta')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'radiadores'


class Referencia(models.Model):
    nomreferencia = models.CharField(db_column='nomReferencia', max_length=255)  # Field name made lowercase.
    idmarcas = models.ForeignKey(Marcas, models.DO_NOTHING, db_column='idMarcas')  # Field name made lowercase.
    idubicacion = models.ForeignKey('Ubicacion', models.DO_NOTHING, db_column='idUbicacion')  # Field name made lowercase.
    numreferencia = models.IntegerField(db_column='numReferencia', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.IntegerField(blank=True, null=True)
    idposicion = models.ForeignKey(Posicion, models.DO_NOTHING, db_column='idPosicion')  # Field name made lowercase.
    idempresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='idEmpresa', blank=True, null=True)  # Field name made lowercase.
    preciocosto = models.IntegerField(db_column='precioCosto')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'referencia'


class Ubicacion(models.Model):
    nomubicacion = models.CharField(db_column='nomUbicacion', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ubicacion'


class Usuario(models.Model):
    is_superuser = models.IntegerField()
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    documento = models.CharField(max_length=11)
    correo = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100)
    imagen = models.CharField(max_length=60, blank=True, null=True)
    registro = models.DateField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_active = models.IntegerField()
    is_staff = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usuario'


class Ventadiaria(models.Model):
    descripcion = models.CharField(max_length=255)
    precioventa = models.IntegerField(db_column='precioVenta')  # Field name made lowercase.
    ventatanque = models.ForeignKey(Referencia, models.DO_NOTHING, db_column='ventaTanque', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateField()

    class Meta:
        managed = False
        db_table = 'ventadiaria'
