from django.shortcuts import render

# Create your views here.

def inicio(request):
    generos = [
        {
            'nombre': 'Acción',
            'descripcion': 'Películas de adrenalina pura, combates impresionantes, persecuciones intensas y misiones de alto riesgo.',
            'url_name': 'home:accion'
        },
        {
            'nombre': 'Ciencia Ficción',
            'descripcion': 'Historias fascinantes sobre el futuro, viajes en el espacio, realidades alternativas y tecnología avanzada.',
            'url_name': 'home:scifi'
        }
    ]
    return render(request, 'home_maximiliano_gabriel/inicio.html', {'generos': generos})

def genero_accion(request):
    peliculas = [
        {
            'nombre': 'Iron Man',
            'anio': 2008,
            'imagen': 'img/accion/iron_man.jpg',
            'descripcion': 'Un empresario multimillonario construye una armadura blindada de alta tecnología para combatir a criminales.'
        },
        {
            'nombre': 'Hombres de Negro',
            'anio': 1997,
            'imagen': 'img/accion/hombres_de_negro.jpg',
            'descripcion': 'Dos agentes de una organización secreta monitorean y supervisan a los alienígenas que habitan en la Tierra.'
        },
        {
            'nombre': 'Piratas del Caribe',
            'anio': 2003,
            'imagen': 'img/accion/piratas_del_caribe.jpg',
            'descripcion': 'El herrero Will Turner une fuerzas con el peculiar pirata Jack Sparrow para rescatar al amor de su vida.'
        },
        {
            'nombre': 'Top Gun: Maverick',
            'anio': 2022,
            'imagen': 'img/accion/top_gun_maverick.jpg',
            'descripcion': 'Maverick regresa para entrenar a un grupo destacado de jóvenes pilotos para una misión de combate.'
        },
        {
            'nombre': 'El Karate Kid',
            'anio': 1984,
            'imagen': 'img/accion/karate_kid.jpg',
            'descripcion': 'Un joven aprende karate y disciplina gracias a las sabias enseñanzas del maestro Miyagi.'
        },
        {
            'nombre': 'Spider-Man: No Way Home',
            'anio': 2021,
            'imagen': 'img/accion/spiderman_no_way_home.jpg',
            'descripcion': 'Con su identidad desenmascarada, Peter Parker pide ayuda a Doctor Strange, desatando consecuencias multiversales.'
        },
        {
            'nombre': 'Wanted',
            'anio': 2008,
            'imagen': 'img/accion/wanted.jpg',
            'descripcion': 'Un oficinista descubre que su padre era un letal sicario y es reclutado por una antigua hermandad secreta.'
        },
        {
            'nombre': 'Rápidos y Furiosos 9',
            'anio': 2021,
            'imagen': 'img/accion/rapidos_y_furiosos_9.jpg',
            'descripcion': 'Dominic Toretto y su equipo se reúnen para detener una conspiración liderada por su peligroso hermano Jakob.'
        },
        {
            'nombre': 'Capitán América: Civil War',
            'anio': 2016,
            'imagen': 'img/accion/capitan_america_civil_war.jpg',
            'descripcion': 'Las tensiones políticas dividen a los Vengadores en dos bandos liderados por Capitán América e Iron Man.'
        },
        {
            'nombre': 'Matrix',
            'anio': 1999,
            'imagen': 'img/accion/matrix.jpg',
            'descripcion': 'Un programador descubre que la realidad es una compleja simulación y decide luchar por la libertad humana.'
        },
    ]
    return render(request, 'home_maximiliano_gabriel/accion.html', {
        'titulo_genero': 'Películas de Acción',
        'peliculas': peliculas
    })

def genero_scifi(request):
    peliculas = [
        {
            'nombre': 'Interestelar',
            'anio': 2014,
            'imagen': 'img/scifi/interstellar.jpg',
            'descripcion': 'Un grupo de astronautas cruza un agujero de gusano en el espacio buscando un nuevo planeta para la humanidad.'
        },
        {
            'nombre': 'Al filo del mañana',
            'anio': 2014,
            'imagen': 'img/scifi/al_filo_del_manana.jpg',
            'descripcion': 'Un oficial militar queda atrapado en un bucle temporal reviviendo el mismo día de combate alienígena.'
        },
        {
            'nombre': 'WALL-E',
            'anio': 2008,
            'imagen': 'img/scifi/wall_e.jpg',
            'descripcion': 'Un pequeño robot que limpia la basura de la Tierra emprende una aventura espacial que define el futuro humano.'
        },
        {
            'nombre': 'Volver al Futuro',
            'anio': 1985,
            'imagen': 'img/scifi/back_to_the_future.jpg',
            'descripcion': 'Un adolescente viaja a 1955 en un automóvil impulsado por plutonio y debe unir nuevamente a sus padres.'
        },
        {
            'nombre': 'Guardianes de la Galaxia',
            'anio': 2014,
            'imagen': 'img/scifi/guardianes_de_la_galaxia.jpg',
            'descripcion': 'Un (profe pongame un 7)grupo de forajidos espaciales se alía para salvar a la galaxia de un fanático guerrero intergaláctico.'
        },
        {
            'nombre': 'Misión Rescate (The Martian)',
            'anio': 2015,
            'imagen': 'img/scifi/mision_rescate.jpg',
            'descripcion': 'Un botánico dado por muerto en Marte lucha por sobrevivir mientras la NASA organiza una misión de rescate.'
        },
        {
            'nombre': 'Akira',
            'anio': 1988,
            'imagen': 'img/scifi/akira.jpg',
            'descripcion': 'En una futurista Neo-Tokio, un joven miembro de una pandilla de motociclistas desata temibles poderes psíquicos.'
        },
        {
            'nombre': 'El final de la calle Oak',
            'anio': 2026,
            'imagen': 'img/scifi/el_final_de_la_calle_oak.jpg',
            'descripcion': 'Una extraña anomalía cósmica traslada a un vecindario a un entorno desconocido donde deben sobrevivir.'
        },
        {
            'nombre': 'Resident Evil: Noche Cero',
            'anio': 2026,
            'imagen': 'img/scifi/resident_evil_noche_cero.jpg',
            'descripcion': 'Un joven repartidor lucha por escapar de Raccoon City en las primeras horas tras desatarse un misterioso virus desarrollado por la corporacion Umbrella.'
        },
        {
            'nombre': 'El Origen (Inception)',
            'anio': 2010,
            'imagen': 'img/scifi/inception.jpg',
            'descripcion': 'Un talentoso extractor de secretos en el mundo de los sueños asume la peligrosa tarea de implantar una idea.'
        },
    ]
    return render(request, 'home_maximiliano_gabriel/scifi.html', {
        'titulo_genero': 'Películas de Ciencia Ficción',
        'peliculas': peliculas
    })