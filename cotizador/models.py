from django.db import models

# Create your models here.


class Auto(models.Model):
    id_auto = models.AutoField(primary_key=True)  # The composite primary key (id_auto, modelo_id_modelo, modelo_marca_id_marca) found, that is not supported. The first column is selected.
    ano = models.CharField(max_length=45)
    modelo_id_modelo = models.OneToOneField('Modelo', models.DO_NOTHING, db_column='modelo_id_modelo')
    modelo_marca_id_marca = models.OneToOneField('Modelo', models.DO_NOTHING, db_column='modelo_marca_id_marca', to_field='marca_id_marca', related_name='auto_modelo_marca_id_marca_set')

    class Meta:
        managed = False
        db_table = 'auto'
        unique_together = (('id_auto', 'modelo_id_modelo', 'modelo_marca_id_marca'),)
    def __int__(self):
        return self.id_auto


class AutoReemplazo(models.Model):
    id_reemplazo = models.AutoField(primary_key=True)
    cantidad = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'auto_reemplazo'
    def __int__(self):
        return self.id_reemplazo


class Compania(models.Model):
    id_compania = models.AutoField(primary_key=True)
    nombre_compania = models.CharField(max_length=45)
    logo_comapania = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'compania'
    def __str__(self):
        return self.nombre_compania


class Deducible(models.Model):
    id_deducible = models.AutoField(primary_key=True)
    valor_deducible = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'deducible'
    def __int__(self):
        return self.valor_deducible 


class Marca(models.Model):
    id_marca = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'marca'
    def __str__(self):
        return self.marca


class Modelo(models.Model):
    id_modelo = models.AutoField(primary_key=True)  # The composite primary key (id_modelo, marca_id_marca) found, that is not supported. The first column is selected.
    nombre = models.CharField(max_length=45)
    marca_id_marca = models.OneToOneField(Marca, models.DO_NOTHING, db_column='marca_id_marca')

    class Meta:
        managed = False
        db_table = 'modelo'
        unique_together = (('id_modelo', 'marca_id_marca'),)
    def __str__(self):
        return self.nombre


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'producto'
    def __str__(self):
        return self.nombre_producto


class Promocion(models.Model):
    id_promocion = models.AutoField(primary_key=True)
    oferta = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'promocion'
    def __int__(self):
        return self.id_promocion


class TipoDano(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    tipo_dano = models.CharField(max_length=45)
    valor_cobertura = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'tipo_dano'
    def __str__(self):
        return self.tipo_dano


class ValorCotizacion(models.Model):
    id_cotizacion = models.AutoField(primary_key=True)  # The composite primary key (id_cotizacion, auto_reemplazo_id_reemplazo, compania_id_compania, promocion_id_promocion, producto_id_producto, deducible_id_deducible, tipo_dano_id_tipo, auto_id_auto, auto_modelo_id_modelo, auto_modelo_marca_id_marca) found, that is not supported. The first column is selected.
    valor_inicial = models.IntegerField()
    valor_oferta = models.IntegerField()
    auto_reemplazo_id_reemplazo = models.ForeignKey(AutoReemplazo, models.DO_NOTHING, db_column='auto_reemplazo_id_reemplazo')
    compania_id_compania = models.ForeignKey(Compania, models.DO_NOTHING, db_column='compania_id_compania')
    promocion_id_promocion = models.ForeignKey(Promocion, models.DO_NOTHING, db_column='promocion_id_promocion')
    producto_id_producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='producto_id_producto')
    deducible_id_deducible = models.ForeignKey(Deducible, models.DO_NOTHING, db_column='deducible_id_deducible')
    tipo_dano_id_tipo = models.ForeignKey(TipoDano, models.DO_NOTHING, db_column='tipo_dano_id_tipo')
    auto_id_auto = models.ForeignKey(Auto, models.DO_NOTHING, db_column='auto_id_auto')
    auto_modelo_id_modelo = models.ForeignKey(Auto, models.DO_NOTHING, db_column='auto_modelo_id_modelo', to_field='modelo_id_modelo', related_name='valorcotizacion_auto_modelo_id_modelo_set')
    auto_modelo_marca_id_marca = models.ForeignKey(Auto, models.DO_NOTHING, db_column='auto_modelo_marca_id_marca', to_field='modelo_marca_id_marca', related_name='valorcotizacion_auto_modelo_marca_id_marca_set')

    class Meta:
        managed = False
        db_table = 'valor_cotizacion'
        unique_together = (('id_cotizacion', 'auto_reemplazo_id_reemplazo', 'compania_id_compania', 'promocion_id_promocion', 'producto_id_producto', 'deducible_id_deducible', 'tipo_dano_id_tipo', 'auto_id_auto', 'auto_modelo_id_modelo', 'auto_modelo_marca_id_marca'),)
    def __int__(self):
        return self.id_cotizacion
    

class Cotizante(models.Model):
    nombre = models.CharField(max_length= 30)
    ap_pat = models.CharField(max_length= 30)
    ap_mat = models.CharField(max_length=30)
