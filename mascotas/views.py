from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from mascotas.models import Responsable, Mascota
from mascotas.serializers import ResponsableSerializer, MascotaSerializer

# Create your views here.

# Crear mascota

@api_view(['POST', 'PUT'])
def crear_mascota(request):
    datos_mascota_deserializado = MascotaSerializer(data=request.data)

    if datos_mascota_deserializado.is_valid():
        datos_mascota_deserializado.save()

        return Response(datos_mascota_deserializado.data, status = status.HTTP_201_CREATED)
    else:
        return Response(datos_mascota_deserializado.errors, status = status.HTTP_400_BAD_REQUEST)

# Editar cliente

@api_view(['PATCH'])
def modificar_mascota(request):
    mascota_seleccionada = Mascota.objects.get(id=id)
    datos_mascota_deserializado = MascotaSerializer(mascota_seleccionada, data=request.data)

    if datos_mascota_deserializado.is_valid():
        datos_mascota_deserializado.save()
        return Response(datos_mascota_deserializado.data, status = status.HTTP_201_CREATED)
    else:
        return Response(datos_mascota_deserializado.errors, status = status.HTTP_400_BAD_REQUEST)


# Eliminar Cliente

@api_view(['DELETE'])
def eliminar_mascota(request):
    mascota_seleccionada = Mascota.objects.get(id=id)
    mascota_seleccionada.delete()

    try:
        Mascota.objects.filter(id=id).delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    except:
        return Response(status = status.HTTP_404_NOT_FOUND)



# Listar mascotas

@api_view(['GET'])

def listar_mascotas(request):
    try:
        mascotas = Mascota.objects.all()
        serializer = MascotaSerializer(mascotas, many=True)

        return Response(serializer.data, status = status.HTTP_200_OK)

    except:
        return Response(status = status.HTTP_404_NOT_FOUND)




# Listar mascota

@api_view(['GET'])
def listar_mascota(request):
    try:
        mascotas = Mascota.objects.get(id=id)
        serializer = MascotaSerializer(mascotas, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    except:
        return Response(status = status.HTTP_404_NOT_FOUND)



# Crear Responsable

@api_view(['POST', 'PUT'])

def crear_responsable (request):
    datos_responsable_deserializado = ResponsableSerializer(data=request.data)

    if datos_responsable_deserializado.is_valid():
        datos_responsable_deserializado.save()
        return Response(datos_responsable_deserializado.data, status = status.HTTP_201_CREATED)

    else:
        return Response(datos_responsable_deserializado.errors, status = status.HTTP_400_BAD_REQUEST)




# Modificar responsable

@api_view(['PATCH'])
def modificar_responsable (request):
    responsable_seleccionado = Responsable.objects.get(id=id)
    datos_responsable_deserializado = ResponsableSerializer(data=request.data)
    if datos_responsable_deserializado.is_valid():
        datos_responsable_deserializado.save()
        return Response(datos_responsable_deserializado.data, status = status.HTTP_201_CREATED)
    else:
        return Response(datos_responsable_deserializado.errors, status = status.HTTP_400_BAD_REQUEST)




# Eliminar resopnsable

@api_view(['DELETE'])
def eliminar_responsable (request):
    responsable_seleccionado = Responsable.objects.get(id=id)
    responsable_seleccionado.delete()
    try:
        Mascota.objects.filter(id=id).delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    except:
        return Response(status = status.HTTP_404_NOT_FOUND)



# Listar responsable

@api_view(['GET'])
def listar_responsable(request):
    try:
        responsables = Responsable.objects.get(id=id)
        serializer = MascotaSerializer(mascotas, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    except:
        return Response(status = status.HTTP_404_NOT_FOUND)






