# Generated by Django 4.2 on 2023-05-09 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutoReemplazo',
            fields=[
                ('id_reemplazo', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'auto_reemplazo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Compania',
            fields=[
                ('id_compania', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_compania', models.CharField(max_length=45)),
                ('logo_comapania', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'compania',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Deducible',
            fields=[
                ('id_deducible', models.AutoField(primary_key=True, serialize=False)),
                ('valor_deducible', models.IntegerField()),
            ],
            options={
                'db_table': 'deducible',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_producto', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'producto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Promocion',
            fields=[
                ('id_promocion', models.AutoField(primary_key=True, serialize=False)),
                ('oferta', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'promocion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoDano',
            fields=[
                ('id_tipo', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_dano', models.CharField(max_length=45)),
                ('valor_cobertura', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'tipo_dano',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ValorCotizacion',
            fields=[
                ('id_cotizacion', models.AutoField(primary_key=True, serialize=False)),
                ('valor_inicial', models.IntegerField()),
                ('valor_oferta', models.IntegerField()),
            ],
            options={
                'db_table': 'valor_cotizacion',
                'managed': False,
            },
        ),
    ]
