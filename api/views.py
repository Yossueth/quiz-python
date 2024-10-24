from rest_framework import generics
from .models import (Clientes,Habitaciones,Reservas,Pagos)
from .serializers import (ClientesSerializer, HabitacionesSerializer,ReservasSerializer,PagosSerializer)


#Clientes

class ClientesListCreate(generics.ListCreateAPIView):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer


class ClientesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer
    
# ---------------------------------------------------------------

#Habitaciones

class HabitacionesListCreate(generics.ListCreateAPIView):
    queryset = Habitaciones.objects.all()
    serializer_class = HabitacionesSerializer


class HabitacionesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Habitaciones.objects.all()
    serializer_class = HabitacionesSerializer
    
# ---------------------------------------------------------------

#Reservas

class ReservasListCreate(generics.ListCreateAPIView):
    queryset = Reservas.objects.all()
    serializer_class = ReservasSerializer


class ReservasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservas.objects.all()
    serializer_class = ReservasSerializer
    
# ---------------------------------------------------------------

#Pagos

class PagosListCreate(generics.ListCreateAPIView):
    queryset = Pagos.objects.all()
    serializer_class = PagosSerializer


class PagosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pagos.objects.all()
    serializer_class = PagosSerializer
    
# ---------------------------------------------------------------