from django.db import models

class Clientes(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    apellido =  models.CharField(max_length=100)
    correo = models.CharField(max_length=100,unique=True)
    telefono = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.nombre_cliente
    
class Habitaciones(models.Model):
    numero_habitacion = models.CharField(max_length=100)
    tipo_habitacion  =  models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.numero_habitacion    
    
class Reservas(models.Model):
    id_cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    id_habitacion =  models.OneToOneField(Habitaciones, on_delete=models.CASCADE)
    fecha_checkin  = models.DateField(auto_now_add=True)
    fecha_checkout   = models.DateField()

    def __str__(self):
        return self.fecha_checkin        
    
class Pagos(models.Model):
    id_reserva = models.ForeignKey(Reservas, on_delete=models.CASCADE)
    fecha_pago  =  models.DateField(auto_now_add=True)
    metodo_pago = models.CharField(max_length=100)
    total   = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.fecha_pago                  
