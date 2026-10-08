from django.shortcuts import render

# Create your views here.

def inicio(request):
    generos = [
        {
            'nombre': 'Acción',
            'descripcion': 'Películas de combates, persecuciones intensas y rescates extremos.',
            'url_name': 'home:accion'
        },
        {
            'nombre': 'Ciencia Ficción',
            'descripcion': 'Historias futuristas, viajes en el espacio y tecnología avanzada.',
            'url_name': 'home:scifi'
        }
    ]
    return render(request, 'home_maximiliano_gabriel/inicio.html', {'generos': generos})

def genero_accion(request):
    return render(request, 'home_maximiliano_gabriel/accion.html')

def genero_scifi(request):
    return render(request, 'home_maximiliano_gabriel/scifi.html')