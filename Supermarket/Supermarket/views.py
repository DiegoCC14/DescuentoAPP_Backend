from django.views import View
from django.http import JsonResponse

from .models import Producto as Producto_Model
from .models import Negocios as Negocios_model, Categorias as Categorias_model

import json

class Categorias(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse( [ { 
                        "id":obj_categoria.id,
                        "nombre":obj_categoria.nombre } for obj_categoria in Categorias_model.objects.all()] , safe=False )

class Negocios(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse( [ { 
                        "id":obj_negocio.id,
                        "nombre":obj_negocio.nombre,
                        "coordenadas":obj_negocio.coordenadas,
                        "direccion" : obj_negocio.direccion,
                        "imagen" : str(obj_negocio.imagen) } for obj_negocio in Negocios_model.objects.all()] , safe=False )
    
class Productos_Search(View):
    def get(self, request, *args, **kwargs):
        data_request = json.loads( request.body )
        
        Productos = Producto_Model.objects.all()
        if 'categoria' in data_request.keys():
            Productos = Productos.filter( id_categoria__nombre=data_request['categoria'] )
            
        if 'cadena' in data_request.keys():
            Productos = Productos.filter( nombre__icontains=data_request['cadena'] )
        
        if "page" not in data_request.keys():
            data_request["page"] = 0
        
        Productos = Productos[ 30*data_request["page"] : 30*data_request["page"]+30 ]

        return JsonResponse( [{
                        "id":obj_producto.id,
                        "nombre":obj_producto.nombre,
                        "imagen":str(obj_producto.imagen),
                        "negocio": obj_producto.id_negocio.nombre,
                        "categoria": obj_producto.id_categoria.nombre } for obj_producto in Productos ] , safe=False )