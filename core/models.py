from django.db import models


class Usuarios(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=150)
    rol = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class Cepas(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)
    origen = models.CharField(max_length=255)
    fecha_ingreso = models.DateField()
    descripcion = models.TextField()
    estado = models.CharField(max_length=50)
    imagen_url = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"


class Cultivos(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    cepa = models.ForeignKey(Cepas, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10)
    codigo = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    medio = models.CharField(max_length=100)
    recipiente = models.CharField(max_length=20)
    volumen_ml = models.IntegerField()
    estado = models.CharField(max_length=20)
    imagen_url = models.CharField(max_length=255)
    observaciones = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.codigo


class CultivoOrigen(models.Model):
    cultivo_destino = models.ForeignKey(Cultivos, on_delete=models.CASCADE, related_name='destino')
    cultivo_fuente = models.ForeignKey(Cultivos, on_delete=models.CASCADE, related_name='fuente')
    metodo = models.CharField(max_length=100)
    observaciones = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.cultivo_destino} <- {self.cultivo_fuente}"


class Monotubes(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    cultivo_grano = models.ForeignKey(Cultivos, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=100)
    fecha_inoculacion = models.DateField()
    tipo_sustrato = models.CharField(max_length=100)
    condiciones_iniciales = models.TextField()
    fecha_pinning = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=20)
    imagen_url = models.CharField(max_length=255)
    observaciones = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.codigo


class Cosechas(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    monotube = models.ForeignKey(Monotubes, on_delete=models.CASCADE)
    flush_num = models.IntegerField()
    fecha_cosecha = models.DateField()
    peso_gramos = models.DecimalField(max_digits=10, decimal_places=2)
    imagen_url = models.CharField(max_length=255)
    observaciones = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.monotube} #{self.flush_num}"


class Seguimiento(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    cultivo = models.ForeignKey(Cultivos, on_delete=models.SET_NULL, null=True, blank=True)
    monotube = models.ForeignKey(Monotubes, on_delete=models.SET_NULL, null=True, blank=True)
    fecha = models.DateField()
    descripcion = models.TextField()
    micelio = models.TextField()
    contaminacion = models.TextField()
    accion_tomada = models.TextField()
    imagen_url = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        target = self.cultivo or self.monotube
        return f"{target} - {self.fecha}" if target else str(self.fecha)


class Conservacion(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    cultivo = models.ForeignKey(Cultivos, on_delete=models.CASCADE)
    metodo = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    ubicacion = models.CharField(max_length=100)
    observaciones = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.cultivo} - {self.metodo}"
