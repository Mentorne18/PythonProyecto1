from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader

def saludo(request):
    return HttpResponse("Hola Django - Coder")

def segunda_vista(request):
    return HttpResponse("<br><br>Ya entendimos esto, es muy simple :)")

def diaDeHoy(request):
    
        dia = datetime.datetime.now()
        
        documentoDeTexto = f"Hoy es día: <br> {dia}"
        
        return HttpResponse(documentoDeTexto)

def miNombreEs(self, nombre):
    
    documentoDeTexto = f"Mi nombre es: <br><br> {nombre}"
    
    return HttpResponse(documentoDeTexto)

def probandoTemplate(self):
    
    nombre = "Danilo"
    apellido = "Rajcevic"
    
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    lista_notas = [2,2,3,7,2,5]

    
    diccionario = {"nombre": nombre, "apellido": apellido, "fecha": fecha_actual, "notas": lista_notas} # este lo hacemos para enviar el diccionario al contexto
    
    
    
    # miHtml = open(r"C:\Users\USUARIO\Desktop\VisualStudio\PythonProyecto1\Proyecto1\Proyecto1\plantillas\template1.html")
    
    # plantilla = Template(miHtml.read()) #se carga en memoria nuestro documento, template1
    
    # ## OJO importar template y contex con: from django.template import Template, Context
    
    # miHtml.close() #cerramos el archivo. Es una muy buena practica cerrar los archivos despues de usarlos para liberar recursos
    
    # miContexto = Context(diccionario) #En este caso no hay nda ya que no hay parametros, IGUAL hay que crearlo
    # # le enviamos el parametro "diccionario" para que sepa nuestro nombre y apellido
    
    
    plantilla = loader.get_template("template1.html")

    #documento = plantilla.render(miContexto) #Aca renderizamos la plantilla en documento
    
    documento = plantilla.render(diccionario) # ahora va diccionario ya que de esta forma no necesitamos el contexto
    
    return HttpResponse(documento)