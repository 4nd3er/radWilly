# Generated by Django 4.2.6 on 2024-04-01 02:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('documento', models.CharField(max_length=11, unique=True, verbose_name='Numero de documento')),
                ('email', models.CharField(db_column='correo', max_length=100, unique=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('imagen', models.ImageField(blank=True, db_column='imagen', null=True, upload_to='imagen_usuario')),
                ('registro', models.DateField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomempresa', models.CharField(db_column='nomEmpresa', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Gastosdiarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=255)),
                ('gasto', models.IntegerField()),
                ('fecha', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Marcas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nommarca', models.CharField(db_column='nomMarca', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Posicion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomposicion', models.CharField(db_column='nomPosicion', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Referencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomreferencia', models.CharField(db_column='nomReferencia', max_length=255)),
                ('idmarcas', models.ForeignKey(db_column='idMarcas', on_delete=django.db.models.deletion.DO_NOTHING, to='control.marcas')),
                ('numreferencia', models.IntegerField(blank=True, db_column='numReferencia', null=True)),
                ('cantidad', models.IntegerField(blank=True, null=True)),
                ('idposicion', models.ForeignKey(db_column='idPosicion', on_delete=django.db.models.deletion.DO_NOTHING, to='control.posicion')),
                ('idempresa', models.ForeignKey(blank=True, db_column='idEmpresa', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='control.empresa')),
                ('preciocosto', models.IntegerField(db_column='precioCosto')),
            ],
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomubicacion', models.CharField(db_column='nomUbicacion', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ventadiaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=255)),
                ('precioventa', models.IntegerField(db_column='precioVenta')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('ventatanque', models.ForeignKey(blank=True, db_column='ventaTanque', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='control.referencia')),
            ],
        ),
        migrations.AddField(
            model_name='referencia',
            name='idubicacion',
            field=models.ForeignKey(db_column='idUbicacion', on_delete=django.db.models.deletion.DO_NOTHING, to='control.ubicacion'),
        ),
        migrations.CreateModel(
            name='Radiadores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referencia', models.CharField(max_length=255)),
                ('preciocosto', models.IntegerField(db_column='precioCosto')),
                ('precioventa', models.IntegerField(db_column='precioVenta')),
                ('idmarca', models.ForeignKey(db_column='idMarca', on_delete=django.db.models.deletion.DO_NOTHING, to='control.marcas')),
            ],
        ),
        migrations.CreateModel(
            name='Mercancia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('cantidad', models.IntegerField()),
                ('idreferencia', models.ForeignKey(db_column='idReferencia', on_delete=django.db.models.deletion.DO_NOTHING, to='control.referencia')),
            ],
        ),
    ]
