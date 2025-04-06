from prisma import Prisma
from datetime import datetime

usuarios = [
    {
        "nombre": "Juan",
        "apellidoPaterno": "Pérez",
        "apellidoMaterno": "Gómez",
        "correo": "juan.perez@email.com",
        "contrasena": "hashed_password_123",
        "genero": "Masculino",
        "telefono": "59171234567",
        "pais": "Bolivia",
        "ciudad": "La Paz",
        "estado": True,
        "imagen": "https://example.com/juan.jpg"
    },
    {
        "nombre": "María",
        "apellidoPaterno": "López",
        "apellidoMaterno": "Fernández",
        "correo": "maria.lopez@email.com",
        "contrasena": "hashed_password_456",
        "genero": "Femenino",
        "telefono": "59171234568",
        "pais": "Bolivia",
        "ciudad": "Cochabamba",
        "estado": True,
        "imagen": "https://example.com/maria.jpg"
    },
    {
        "nombre": "Carlos",
        "apellidoPaterno": "Gutiérrez",
        "apellidoMaterno": "Mendoza",
        "correo": "carlos.gutierrez@email.com",
        "contrasena": "hashed_password_789",
        "genero": "Masculino",
        "telefono": "59171234569",
        "pais": "Bolivia",
        "ciudad": "Santa Cruz",
        "estado": True,
        "imagen": "https://example.com/carlos.jpg"
    },
    {
        "nombre": "Ana",
        "apellidoPaterno": "Rodríguez",
        "apellidoMaterno": "Vargas",
        "correo": "ana.rodriguez@email.com",
        "contrasena": "hashed_password_101",
        "genero": "Femenino",
        "telefono": "59171234570",
        "pais": "Bolivia",
        "ciudad": "Sucre",
        "estado": True,
        "imagen": "https://example.com/ana.jpg"
    },
    {
        "nombre": "Luis",
        "apellidoPaterno": "Martínez",
        "apellidoMaterno": "Salazar",
        "correo": "luis.martinez@email.com",
        "contrasena": "hashed_password_112",
        "genero": "Masculino",
        "telefono": "59171234571",
        "pais": "Bolivia",
        "ciudad": "Potosí",
        "estado": True,
        "imagen": "https://example.com/luis.jpg"
    },
    {
        "nombre": "Sofía",
        "apellidoPaterno": "García",
        "apellidoMaterno": "Torres",
        "correo": "sofia.garcia@email.com",
        "contrasena": "hashed_password_131",
        "genero": "Femenino",
        "telefono": "59171234572",
        "pais": "Bolivia",
        "ciudad": "Oruro",
        "estado": True,
        "imagen": "https://example.com/sofia.jpg"
    },
    {
        "nombre": "Pedro",
        "apellidoPaterno": "Sánchez",
        "apellidoMaterno": "Ruiz",
        "correo": "pedro.sanchez@email.com",
        "contrasena": "hashed_password_415",
        "genero": "Masculino",
        "telefono": "59171234573",
        "pais": "Bolivia",
        "ciudad": "Tarija",
        "estado": True,
        "imagen": "https://example.com/pedro.jpg"
    },
    {
        "nombre": "Elena",
        "apellidoPaterno": "Díaz",
        "apellidoMaterno": "Castro",
        "correo": "elena.diaz@email.com",
        "contrasena": "hashed_password_161",
        "genero": "Femenino",
        "telefono": "59171234574",
        "pais": "Bolivia",
        "ciudad": "Beni",
        "estado": True,
        "imagen": "https://example.com/elena.jpg"
    },
    {
        "nombre": "Jorge",
        "apellidoPaterno": "Hernández",
        "apellidoMaterno": "Morales",
        "correo": "jorge.hernandez@email.com",
        "contrasena": "hashed_password_718",
        "genero": "Masculino",
        "telefono": "59171234575",
        "pais": "Bolivia",
        "ciudad": "Pando",
        "estado": True,
        "imagen": "https://example.com/jorge.jpg"
    },
    {
        "nombre": "Lucía",
        "apellidoPaterno": "Jiménez",
        "apellidoMaterno": "Ortega",
        "correo": "lucia.jimenez@email.com",
        "contrasena": "hashed_password_920",
        "genero": "Femenino",
        "telefono": "59171234576",
        "pais": "Bolivia",
        "ciudad": "La Paz",
        "estado": True,
        "imagen": "https://example.com/lucia.jpg"
    },
    {
        "nombre": "Miguel",
        "apellidoPaterno": "Álvarez",
        "apellidoMaterno": "Santos",
        "correo": "miguel.alvarez@email.com",
        "contrasena": "hashed_password_211",
        "genero": "Masculino",
        "telefono": "59171234577",
        "pais": "Bolivia",
        "ciudad": "Cochabamba",
        "estado": True,
        "imagen": "https://example.com/miguel.jpg"
    },
    {
        "nombre": "Carmen",
        "apellidoPaterno": "Romero",
        "apellidoMaterno": "Delgado",
        "correo": "carmen.romero@email.com",
        "contrasena": "hashed_password_222",
        "genero": "Femenino",
        "telefono": "59171234578",
        "pais": "Bolivia",
        "ciudad": "Santa Cruz",
        "estado": True,
        "imagen": "https://example.com/carmen.jpg"
    },
    {
        "nombre": "Raúl",
        "apellidoPaterno": "Navarro",
        "apellidoMaterno": "Iglesias",
        "correo": "raul.navarro@email.com",
        "contrasena": "hashed_password_233",
        "genero": "Masculino",
        "telefono": "59171234579",
        "pais": "Bolivia",
        "ciudad": "Sucre",
        "estado": True,
        "imagen": "https://example.com/raul.jpg"
    },
    {
        "nombre": "Isabel",
        "apellidoPaterno": "Torres",
        "apellidoMaterno": "Ramírez",
        "correo": "isabel.torres@email.com",
        "contrasena": "hashed_password_244",
        "genero": "Femenino",
        "telefono": "59171234580",
        "pais": "Bolivia",
        "ciudad": "Potosí",
        "estado": True,
        "imagen": "https://example.com/isabel.jpg"
    },
    {
        "nombre": "Fernando",
        "apellidoPaterno": "Domínguez",
        "apellidoMaterno": "Cortés",
        "correo": "fernando.dominguez@email.com",
        "contrasena": "hashed_password_255",
        "genero": "Masculino",
        "telefono": "59171234581",
        "pais": "Bolivia",
        "ciudad": "Oruro",
        "estado": True,
        "imagen": "https://example.com/fernando.jpg"
    }
]
 
roles = [
        {"nombre_rol": "usuario", "descripcion": "usuario"},
        {"nombre_rol": "administrador", "descripcion": "admin"},
        {"nombre_rol": "cultural", "descripcion": "cultural"},
        {"nombre_rol": "academico", "descripcion": "academico"},
        {"nombre_rol": "organizador", "descripcion": "organizador"},
        {"nombre_rol": "controlador", "descripcion": "controlador"},
    ]

categorias = [
        {"nombre_categoria": "Bélico", "descripcion": "Batallas, guerras y conflictos armados"},
        {"nombre_categoria": "Tratados", "descripcion": "Acuerdos diplomáticos y pactos"},
        {"nombre_categoria": "Científico", "descripcion": "Descubrimientos e innovaciones"},
        {"nombre_categoria": "Revoluciones", "descripcion": "Movimientos sociales y políticos"},
        {"nombre_categoria": "Independencia", "descripcion": "Procesos de liberación nacional"}
    ]

usuario_roles = [
    {"id_usuario": 1, "id_rol": 1},
    {"id_usuario": 2, "id_rol": 2},
    {"id_usuario": 3, "id_rol": 3},
    {"id_usuario": 4, "id_rol": 4},
    {"id_usuario": 5, "id_rol": 5},
    {"id_usuario": 6, "id_rol": 6},
    {"id_usuario": 7, "id_rol": 1},
    {"id_usuario": 8, "id_rol": 2},
    {"id_usuario": 9, "id_rol": 3},
    {"id_usuario": 10, "id_rol": 4},
    {"id_usuario": 11, "id_rol": 5},
    {"id_usuario": 12, "id_rol": 6},
    {"id_usuario": 13, "id_rol": 1},
    {"id_usuario": 14, "id_rol": 2},
    {"id_usuario": 15, "id_rol": 3}
]

ubicaciones = [
    {
        "nombre": "Plaza Murillo",
        "latitud": -16.4958,
        "longitud": -68.1335,
        "imagen": "https://example.com/plaza_murillo.jpg",
        "descripcion": "Plaza principal de La Paz donde se encuentra el Palacio de Gobierno"
    },
    {
        "nombre": "Cerro Rico",
        "latitud": -19.6133,
        "longitud": -65.7533,
        "imagen": "https://example.com/cerro_rico.jpg",
        "descripcion": "Famoso cerro de Potosí que fue una de las mayores minas de plata del mundo"
    },
    {
        "nombre": "Salar de Uyuni",
        "latitud": -20.1337,
        "longitud": -67.4891,
        "imagen": "https://example.com/salar_uyuni.jpg",
        "descripcion": "El salar más grande del mundo"
    },
    {
        "nombre": "Tiwanaku",
        "latitud": -16.5547,
        "longitud": -68.6734,
        "imagen": "https://example.com/tiwanaku.jpg",
        "descripcion": "Ruinas arqueológicas de una antigua civilización preincaica"
    },
    {
        "nombre": "Cristo de la Concordia",
        "latitud": -17.3842,
        "longitud": -66.1347,
        "imagen": "https://example.com/cristo_concordia.jpg",
        "descripcion": "Estatua de Cristo más grande que el Cristo Redentor de Río"
    },
    {
        "nombre": "Parque Nacional Madidi",
        "latitud": -12.5,
        "longitud": -68.3333,
        "imagen": "https://example.com/madidi.jpg",
        "descripcion": "Uno de los parques con mayor biodiversidad del mundo"
    },
    {
        "nombre": "Casa de la Libertad",
        "latitud": -19.0476,
        "longitud": -65.2599,
        "imagen": "https://example.com/casa_libertad.jpg",
        "descripcion": "Lugar donde se firmó el Acta de Independencia de Bolivia"
    },
    {
        "nombre": "Valle de la Luna",
        "latitud": -16.5667,
        "longitud": -68.1167,
        "imagen": "https://example.com/valle_luna.jpg",
        "descripcion": "Formaciones rocosas erosionadas que parecen un paisaje lunar"
    },
    {
        "nombre": "Lago Titicaca",
        "latitud": -15.9254,
        "longitud": -69.3354,
        "imagen": "https://example.com/titicaca.jpg",
        "descripcion": "Lago navegable más alto del mundo, compartido con Perú"
    },
    {
        "nombre": "Samaipata",
        "latitud": -18.1803,
        "longitud": -63.8736,
        "imagen": "https://example.com/samaipata.jpg",
        "descripcion": "Sitio arqueológico con el Fuerte de Samaipata"
    },
    {
        "nombre": "Carnaval de Oruro",
        "latitud": -17.9667,
        "longitud": -67.1167,
        "imagen": "https://example.com/carnaval_oruro.jpg",
        "descripcion": "Ubicación principal del famoso carnaval declarado Patrimonio de la Humanidad"
    },
    {
        "nombre": "Jardín Botánico de Santa Cruz",
        "latitud": -17.7667,
        "longitud": -63.1833,
        "imagen": "https://example.com/jardin_botanico.jpg",
        "descripcion": "Importante centro de conservación de flora boliviana"
    },
    {
        "nombre": "Puerta del Sol",
        "latitud": -16.5547,
        "longitud": -68.6734,
        "imagen": "https://example.com/puerta_sol.jpg",
        "descripcion": "Monolito importante de la cultura Tiwanaku"
    },
    {
        "nombre": "Parque Nacional Toro Toro",
        "latitud": -18.1333,
        "longitud": -65.7667,
        "imagen": "https://example.com/toro_toro.jpg",
        "descripcion": "Parque conocido por sus cavernas y huellas de dinosaurios"
    },
    {
        "nombre": "Misiones Jesuíticas de Chiquitos",
        "latitud": -16.2667,
        "longitud": -60.9667,
        "imagen": "https://example.com/misiones.jpg",
        "descripcion": "Conjunto de misiones jesuíticas declaradas Patrimonio de la Humanidad"
    },
    {
        "nombre": "Región Uru-Chipaya",
        "latitud": -19.1,
        "longitud": -68.25,
        "imagen": "https://example.com/uru_chipaya_region.jpg",
        "descripcion": "Región del altiplano occidental boliviano donde habita el pueblo Uru-Chipaya, cerca del Salar de Coipasa."
    },
    {
        "nombre": "Tarabuco",
        "latitud": -19.1833,
        "longitud": -64.9167,
        "imagen": "https://example.com/tarabuco.jpg",
        "descripcion": "Municipio del departamento de Chuquisaca famoso por su feria dominical y tradición textil y cerámica indígena."
    },
    {
        "nombre": "Trinidad",
        "latitud": -14.8333,
        "longitud": -64.9,
        "imagen": "https://example.com/trinidad.jpg",
        "descripcion": "Capital del departamento del Beni, centro de la cultura moxeña y cuna de música barroca en la Amazonía boliviana."
    }
]

eventos_historicos = [
    {
        "nombre": "Independencia de Bolivia",
        "descripcion": "Declaración de independencia del dominio español",
        "fecha_inicio": "1825-08-06T00:00:00Z",
        "fecha_fin": None,
        "tipo": "Independencia",
        "id_ubicacion": 7
    },
    {
        "nombre": "Guerra del Pacífico",
        "descripcion": "Conflicto entre Bolivia, Chile y Perú que resultó en la pérdida del litoral boliviano",
        "fecha_inicio": "1879-02-14T00:00:00Z",
        "fecha_fin": "1884-04-04T00:00:00Z",
        "tipo": "Bélico",
        "id_ubicacion": 3
    },
    {
        "nombre": "Revolución Nacional de 1952",
        "descripcion": "Movimiento revolucionario que llevó a reformas sociales y políticas importantes",
        "fecha_inicio": "1952-04-09T00:00:00Z",
        "fecha_fin": "1952-04-11T00:00:00Z",
        "tipo": "Revoluciones",
        "id_ubicacion": 1
    },
    {
        "nombre": "Fundación de Tiwanaku",
        "descripcion": "Establecimiento de la cultura Tiwanaku, una de las más importantes de la región andina",
        "fecha_inicio": "1500-01-01T00:00:00Z",
        "fecha_fin": "1000-01-01T00:00:00Z",
        "tipo": "Cultural",
        "id_ubicacion": 4
    },
    {
        "nombre": "Descubrimiento del Cerro Rico",
        "descripcion": "Descubrimiento de las minas de plata en Potosí que financiaron el imperio español",
        "fecha_inicio": "1545-04-01T00:00:00Z",
        "fecha_fin": None,
        "tipo": "Científico",
        "id_ubicacion": 2
    },
    {
        "nombre": "Tratado de Paz con Chile",
        "descripcion": "Tratado que puso fin al estado de guerra entre Bolivia y Chile",
        "fecha_inicio": "1904-10-20T00:00:00Z",
        "fecha_fin": None,
        "tipo": "Tratados",
        "id_ubicacion": 1
    },
    {
        "nombre": "Creación del Estado Plurinacional",
        "descripcion": "Refundación de Bolivia como Estado Plurinacional bajo la nueva constitución",
        "fecha_inicio": "2009-01-25T00:00:00Z",
        "fecha_fin": None,
        "tipo": "Político",
        "id_ubicacion": 1
    },
    {
        "nombre": "Guerra del Chaco",
        "descripcion": "Conflicto bélico entre Bolivia y Paraguay por el territorio del Chaco",
        "fecha_inicio": "1932-09-09T00:00:00Z",
        "fecha_fin": "1935-06-12T00:00:00Z",
        "tipo": "Bélico",
        "id_ubicacion": 6
    },
    {
        "nombre": "Revolución Federal de 1899",
        "descripcion": "Conflicto entre federalistas y unitarios que resultó en el traslado de la sede de gobierno a La Paz",
        "fecha_inicio": "1899-01-01T00:00:00Z",
        "fecha_fin": "1899-04-10T00:00:00Z",
        "tipo": "Revoluciones",
        "id_ubicacion": 1
    },
    {
        "nombre": "Fundación de la Universidad Mayor de San Andrés",
        "descripcion": "Creación de una de las universidades más importantes de Bolivia",
        "fecha_inicio": "1830-10-25T00:00:00Z",
        "fecha_fin": None,
        "tipo": "Educativo",
        "id_ubicacion": 1
    },
    {
        "nombre": "Descubrimiento del Gas Natural",
        "descripcion": "Descubrimiento de grandes reservas de gas natural en el oriente boliviano",
        "fecha_inicio": "1996-01-01T00:00:00Z",
        "fecha_fin": None,
        "tipo": "Científico",
        "id_ubicacion": 3
    },
    {
        "nombre": "Marcha por el Territorio y la Dignidad",
        "descripcion": "Marcha indígena que logró el reconocimiento de territorios indígenas",
        "fecha_inicio": "1990-08-15T00:00:00Z",
        "fecha_fin": "1990-09-17T00:00:00Z",
        "tipo": "Social",
        "id_ubicacion": 1
    },
    {
        "nombre": "Creación del Parque Nacional Madidi",
        "descripcion": "Establecimiento de una de las áreas protegidas con mayor biodiversidad del mundo",
        "fecha_inicio": "1995-09-21T00:00:00Z",
        "fecha_fin": None,
        "tipo": "Ambiental",
        "id_ubicacion": 6
    },
    {
        "nombre": "Guerra de la Independencia en Alto Perú",
        "descripcion": "Campañas militares que llevaron a la independencia del Alto Perú (Bolivia)",
        "fecha_inicio": "1809-05-25T00:00:00Z",
        "fecha_fin": "1825-08-06T00:00:00Z",
        "tipo": "Bélico",
        "id_ubicacion": 7
    },
    {
        "nombre": "Primer Grito Libertario de América",
        "descripcion": "Levantamiento en Chuquisaca considerado el primer movimiento independentista en América",
        "fecha_inicio": "1809-05-25T00:00:00Z",
        "fecha_fin": None,
        "tipo": "Revoluciones",
        "id_ubicacion": 7
    }
]

categorias_evento_historico = [
    {"id_evento": 1, "id_categoria": 5},
    {"id_evento": 2, "id_categoria": 1},
    {"id_evento": 3, "id_categoria": 4},
    {"id_evento": 4, "id_categoria": 3},
    {"id_evento": 5, "id_categoria": 3},
    {"id_evento": 6, "id_categoria": 2},
    {"id_evento": 7, "id_categoria": 4},
    {"id_evento": 8, "id_categoria": 1},
    {"id_evento": 9, "id_categoria": 4},
    {"id_evento": 10, "id_categoria": 3},
    {"id_evento": 11, "id_categoria": 3},
    {"id_evento": 12, "id_categoria": 4},
    {"id_evento": 13, "id_categoria": 3},
    {"id_evento": 14, "id_categoria": 1},
    {"id_evento": 15, "id_categoria": 4}
]

eventos_agendables = [
    {
        "nombre": "Feria del Libro de La Paz",
        "descripcion": "Evento anual que reúne a editoriales y autores nacionales e internacionales",
        "fecha_hora": "2023-08-10T10:00:00Z",
        "id_ubicacion": 1,
        "id_organizador": 2,
        "imagen": "https://example.com/feria_libro.jpg"
    },
    {
        "nombre": "Festival Internacional de Cultura",
        "descripcion": "Celebración de la diversidad cultural boliviana con artistas internacionales",
        "fecha_hora": "2023-09-15T18:00:00Z",
        "id_ubicacion": 3,
        "id_organizador": 5,
        "imagen": "https://example.com/festival_cultura.jpg"
    },
    {
        "nombre": "Conferencia sobre Historia Boliviana",
        "descripcion": "Charla con expertos sobre los hitos históricos más importantes del país",
        "fecha_hora": "2023-07-20T16:00:00Z",
        "id_ubicacion": 7,
        "id_organizador": 4,
        "imagen": "https://example.com/conferencia_historia.jpg"
    },
    {
        "nombre": "Taller de Danzas Folklóricas",
        "descripcion": "Aprende las danzas tradicionales de las diferentes regiones de Bolivia",
        "fecha_hora": "2023-08-05T15:00:00Z",
        "id_ubicacion": 2,
        "id_organizador": 3,
        "imagen": "https://example.com/taller_danzas.jpg"
    },
    {
        "nombre": "Exposición de Arte Colonial",
        "descripcion": "Muestra de pinturas y esculturas del periodo colonial en Bolivia",
        "fecha_hora": "2023-09-01T09:00:00Z",
        "id_ubicacion": 5,
        "id_organizador": 1,
        "imagen": "https://example.com/arte_colonial.jpg"
    },
    {
        "nombre": "Semana de la Revolución",
        "descripcion": "Eventos conmemorativos de la Revolución Nacional de 1952",
        "fecha_hora": "2023-04-09T10:00:00Z",
        "id_ubicacion": 1,
        "id_organizador": 6,
        "imagen": "https://example.com/semana_revolucion.jpg"
    },
    {
        "nombre": "Recorrido Guiado por Tiwanaku",
        "descripcion": "Visita guiada por las ruinas arqueológicas con expertos",
        "fecha_hora": "2023-10-12T08:00:00Z",
        "id_ubicacion": 4,
        "id_organizador": 3,
        "imagen": "https://example.com/tiwanaku_tour.jpg"
    },
    {
        "nombre": "Festival Gastronómico Boliviano",
        "descripcion": "Degustación de platos típicos de todas las regiones del país",
        "fecha_hora": "2023-11-20T12:00:00Z",
        "id_ubicacion": 3,
        "id_organizador": 5,
        "imagen": "https://example.com/festival_gastronomico.jpg"
    },
    {
        "nombre": "Concierto de Música Barroca",
        "descripcion": "Interpretación de obras del periodo barroco en las misiones jesuíticas",
        "fecha_hora": "2023-09-30T19:00:00Z",
        "id_ubicacion": 15,
        "id_organizador": 3,
        "imagen": "https://example.com/musica_barroca.jpg"
    },
    {
        "nombre": "Charla sobre Evo Morales",
        "descripcion": "Análisis del gobierno del primer presidente indígena de Bolivia",
        "fecha_hora": "2023-10-25T17:00:00Z",
        "id_ubicacion": 1,
        "id_organizador": 4,
        "imagen": "https://example.com/charla_evo.jpg"
    },
    {
        "nombre": "Exhibición de Textiles Andinos",
        "descripcion": "Muestra de tejidos tradicionales y su significado cultural",
        "fecha_hora": "2023-08-15T10:00:00Z",
        "id_ubicacion": 9,
        "id_organizador": 3,
        "imagen": "https://example.com/textiles_andinos.jpg"
    },
    {
        "nombre": "Foro sobre el Cambio Climático",
        "descripcion": "Discusión sobre los efectos del cambio climático en Bolivia",
        "fecha_hora": "2023-11-05T15:00:00Z",
        "id_ubicacion": 6,
        "id_organizador": 4,
        "imagen": "https://example.com/foro_climatico.jpg"
    },
    {
        "nombre": "Taller de Cocina Boliviana",
        "descripcion": "Aprende a preparar platos típicos como el saice y el silpancho",
        "fecha_hora": "2023-09-10T14:00:00Z",
        "id_ubicacion": 2,
        "id_organizador": 5,
        "imagen": "https://example.com/taller_cocina.jpg"
    },
    {
        "nombre": "Exposición Fotográfica del Salar",
        "descripcion": "Fotografías que capturan la belleza del Salar de Uyuni en diferentes épocas",
        "fecha_hora": "2023-10-01T11:00:00Z",
        "id_ubicacion": 3,
        "id_organizador": 1,
        "imagen": "https://example.com/expo_fotografica.jpg"
    },
    {
        "nombre": "Celebración del Año Nuevo Aymara",
        "descripcion": "Ceremonia tradicional de recibimiento del nuevo año andino",
        "fecha_hora": "2023-06-21T06:00:00Z",
        "id_ubicacion": 4,
        "id_organizador": 3,
        "imagen": "https://example.com/ano_nuevo_aymara.jpg"
    }
]

participantes_evento = [
    {"id_usuario": 1, "id_evento": 1, "estado_asistencia": True},
    {"id_usuario": 2, "id_evento": 2, "estado_asistencia": True},
    {"id_usuario": 3, "id_evento": 3, "estado_asistencia": False},
    {"id_usuario": 4, "id_evento": 4, "estado_asistencia": True},
    {"id_usuario": 5, "id_evento": 5, "estado_asistencia": False},
    {"id_usuario": 6, "id_evento": 6, "estado_asistencia": True},
    {"id_usuario": 7, "id_evento": 7, "estado_asistencia": False},
    {"id_usuario": 8, "id_evento": 8, "estado_asistencia": True},
    {"id_usuario": 9, "id_evento": 9, "estado_asistencia": False},
    {"id_usuario": 10, "id_evento": 10, "estado_asistencia": True},
    {"id_usuario": 11, "id_evento": 11, "estado_asistencia": False},
    {"id_usuario": 12, "id_evento": 12, "estado_asistencia": True},
    {"id_usuario": 13, "id_evento": 13, "estado_asistencia": False},
    {"id_usuario": 14, "id_evento": 14, "estado_asistencia": True},
    {"id_usuario": 15, "id_evento": 15, "estado_asistencia": False}
]

presidentes = [
        {
            "nombre": "Simón",
            "apellido": "Bolívar",
            "imagen": None,
            "periodo_inicio": datetime(1825, 8, 12),
            "periodo_fin": datetime(1825, 12, 29),
            "biografia": "Libertador de América y primer presidente de Bolivia.",
            "partido_politico": "Ninguno",
            "politicas_clave": "Independencia y organización del nuevo Estado",
        },
        {
            "nombre": "Antonio José",
            "apellido": "de Sucre",
            "imagen": None,
            "periodo_inicio": datetime(1825, 12, 29),
            "periodo_fin": datetime(1828, 4, 18),
            "biografia": "Gran Mariscal de Ayacucho, segundo presidente de Bolivia.",
            "partido_politico": "Ninguno",
            "politicas_clave": "Organización administrativa y jurídica",
        },
        {
            "nombre": "Andrés",
            "apellido": "de Santa Cruz",
            "imagen": None,
            "periodo_inicio": datetime(1829, 5, 24),
            "periodo_fin": datetime(1839, 2, 20),
            "biografia": "Confederación Perú-Boliviana y modernización del Estado.",
            "partido_politico": "Conservador",
            "politicas_clave": "Reformas económicas y educativas",
        },
        {
            "nombre": "José Miguel",
            "apellido": "de Velasco",
            "imagen": None,
            "periodo_inicio": datetime(1828, 4, 18),
            "periodo_fin": datetime(1828, 8, 2),
            "biografia": "Presidente interino en varias ocasiones.",
            "partido_politico": "Conservador",
            "politicas_clave": "Gobiernos provisorios",
        },
        {
            "nombre": "Manuel",
            "apellido": "Isidoro Belzu",
            "imagen": None,
            "periodo_inicio": datetime(1848, 12, 15),
            "periodo_fin": datetime(1855, 8, 15),
            "biografia": "Líder populista, defendió a los sectores populares.",
            "partido_politico": "Liberal",
            "politicas_clave": "Defensa del pueblo y reforma económica",
        },
        {
            "nombre": "José",
            "apellido": "Ballivián",
            "imagen": None,
            "periodo_inicio": datetime(1841, 9, 27),
            "periodo_fin": datetime(1847, 12, 23),
            "biografia": "Militar destacado en la batalla de Ingavi.",
            "partido_politico": "Conservador",
            "politicas_clave": "Fortalecimiento militar y defensa territorial",
        },
        {
            "nombre": "Tomás",
            "apellido": "Frías",
            "imagen": None,
            "periodo_inicio": datetime(1872, 11, 27),
            "periodo_fin": datetime(1873, 5, 9),
            "biografia": "Gobernó en dos periodos no consecutivos.",
            "partido_politico": "Liberal",
            "politicas_clave": "Transición y estabilidad institucional",
        },
        {
            "nombre": "Mariano",
            "apellido": "Melgarejo",
            "imagen": None,
            "periodo_inicio": datetime(1864, 12, 28),
            "periodo_fin": datetime(1871, 1, 15),
            "biografia": "Dictador polémico, conocido por su extravagancia.",
            "partido_politico": "Conservador",
            "politicas_clave": "Gobierno autoritario",
        },
        {
            "nombre": "Hilarión",
            "apellido": "Daza",
            "imagen": None,
            "periodo_inicio": datetime(1876, 5, 4),
            "periodo_fin": datetime(1879, 12, 28),
            "biografia": "Presidente durante la Guerra del Pacífico.",
            "partido_politico": "Nacionalista",
            "politicas_clave": "Defensa del litoral boliviano",
        },
        {
            "nombre": "Narciso",
            "apellido": "Campero",
            "imagen": None,
            "periodo_inicio": datetime(1880, 6, 19),
            "periodo_fin": datetime(1884, 8, 15),
            "biografia": "Militar que asumió tras la Guerra del Pacífico.",
            "partido_politico": "Liberal",
            "politicas_clave": "Reconstrucción post-guerra",
        },
        {
            "nombre": "Aniceto",
            "apellido": "Arce",
            "imagen": None,
            "periodo_inicio": datetime(1888, 8, 15),
            "periodo_fin": datetime(1892, 8, 15),
            "biografia": "Impulsó el desarrollo ferroviario.",
            "partido_politico": "Conservador",
            "politicas_clave": "Desarrollo de infraestructura",
        },
        {
            "nombre": "José Manuel",
            "apellido": "Pando",
            "imagen": None,
            "periodo_inicio": datetime(1899, 10, 25),
            "periodo_fin": datetime(1904, 8, 14),
            "biografia": "Lideró la Revolución Federal.",
            "partido_politico": "Liberal",
            "politicas_clave": "Descentralización y federalismo",
        },
        {
            "nombre": "Ismael",
            "apellido": "Montes",
            "imagen": None,
            "periodo_inicio": datetime(1904, 8, 14),
            "periodo_fin": datetime(1909, 8, 12),
            "biografia": "Gobernó en dos periodos, modernizó el país.",
            "partido_politico": "Liberal",
            "politicas_clave": "Educación y relaciones internacionales",
        },
        {
            "nombre": "Germán",
            "apellido": "Busch",
            "imagen": None,
            "periodo_inicio": datetime(1937, 7, 13),
            "periodo_fin": datetime(1939, 8, 23),
            "biografia": "Militar reformista, se suicidó en el cargo.",
            "partido_politico": "Ninguno",
            "politicas_clave": "Nacionalismo económico",
        },
        {
            "nombre": "Víctor Paz",
            "apellido": "Estenssoro",
            "imagen": None,
            "periodo_inicio": datetime(1952, 4, 11),
            "periodo_fin": datetime(1956, 8, 6),
            "biografia": "Líder de la Revolución de 1952.",
            "partido_politico": "MNR",
            "politicas_clave": "Nacionalización y reforma agraria",
        },
        {
            "nombre": "Hernán",
            "apellido": "Siles Zuazo",
            "imagen": None,
            "periodo_inicio": datetime(1982, 10, 10),
            "periodo_fin": datetime(1985, 8, 6),
            "biografia": "Presidió en tiempos de crisis económica.",
            "partido_politico": "MNRI",
            "politicas_clave": "Restauración democrática",
        },
        {
            "nombre": "Hugo",
            "apellido": "Bánzer",
            "imagen": None,
            "periodo_inicio": datetime(1971, 8, 21),
            "periodo_fin": datetime(1978, 7, 21),
            "biografia": "Gobernó como dictador y luego como demócrata.",
            "partido_politico": "ADN",
            "politicas_clave": "Estabilidad y desarrollo",
        },
        {
            "nombre": "Carlos",
            "apellido": "Mesa",
            "imagen": None,
            "periodo_inicio": datetime(2003, 10, 17),
            "periodo_fin": datetime(2005, 6, 9),
            "biografia": "Historiador y periodista, asumió en crisis política.",
            "partido_politico": "MNR",
            "politicas_clave": "Agenda de octubre",
        },
        {
            "nombre": "Evo",
            "apellido": "Morales",
            "imagen": None,
            "periodo_inicio": datetime(2006, 1, 22),
            "periodo_fin": datetime(2019, 11, 10),
            "biografia": "Primer presidente indígena de Bolivia.",
            "partido_politico": "MAS",
            "politicas_clave": "Nacionalización y Estado Plurinacional",
        },
        {
            "nombre": "Luis",
            "apellido": "Arce",
            "imagen": None,
            "periodo_inicio": datetime(2020, 11, 8),
            "periodo_fin": None,
            "biografia": "Actual presidente, exministro de economía.",
            "partido_politico": "MAS",
            "politicas_clave": "Recuperación económica post-pandemia",
        }
    ]


culturas = [
    {
        "nombre": "Carnaval de Oruro",
        "imagen": "https://example.com/carnaval_oruro.jpg",
        "descripcion": "Manifestación cultural folklórica-religiosa más importante de Bolivia, Patrimonio Cultural Inmaterial de la Humanidad.",
        "id_ubicacion": 11
    },
    {
        "nombre": "Cultura Tiwanaku",
        "imagen": "https://example.com/tiwanaku.jpg",
        "descripcion": "Antigua civilización preincaica que se desarrolló en el altiplano boliviano y dejó importantes ruinas arqueológicas.",
        "id_ubicacion": 4
    },
    {
        "nombre": "Música Andina",
        "imagen": "https://example.com/musica_andina.jpg",
        "descripcion": "Expresión artística tradicional que utiliza instrumentos como zampoñas, charangos y quenas.",
        "id_ubicacion": 1
    },
    {
        "nombre": "Danza de la Diablada",
        "imagen": "https://example.com/diablada.jpg",
        "descripcion": "Danza emblemática del Carnaval de Oruro con raíces religiosas y mitológicas.",
        "id_ubicacion": 11
    },
    {
        "nombre": "Misiones Jesuíticas",
        "imagen": "https://example.com/misiones.jpg",
        "descripcion": "Representación del mestizaje cultural entre pueblos indígenas y misioneros europeos.",
        "id_ubicacion": 15
    },
    {
        "nombre": "El Fuerte de Samaipata",
        "imagen": "https://example.com/samaipata_fuerte.jpg",
        "descripcion": "Sitio ceremonial prehispánico tallado en roca, mezcla de cultura andina y amazónica.",
        "id_ubicacion": 10
    },
    {
        "nombre": "Arte Textil Andino",
        "imagen": "https://example.com/textiles.jpg",
        "descripcion": "Tradición milenaria de tejidos coloridos con diseños simbólicos.",
        "id_ubicacion": 1
    },
    {
        "nombre": "Cultura Aymara",
        "imagen": "https://example.com/aymara.jpg",
        "descripcion": "Uno de los pueblos indígenas originarios del altiplano, con idioma, cosmovisión y vestimenta propia.",
        "id_ubicacion": 1
    },
    {
        "nombre": "Cultura Quechua",
        "imagen": "https://example.com/quechua.jpg",
        "descripcion": "Cultura extendida en los valles y tierras altas, herederos del legado incaico.",
        "id_ubicacion": 5
    },
    {
        "nombre": "Cultura Guaraní",
        "imagen": "https://example.com/guarani.jpg",
        "descripcion": "Pueblo indígena del oriente boliviano con lengua y tradiciones propias.",
        "id_ubicacion": 13
    },
    {
        "nombre": "Fiesta de San Juan",
        "imagen": "https://example.com/sanjuan.jpg",
        "descripcion": "Celebración tradicional que incluye fogatas y música para conmemorar el solsticio de invierno.",
        "id_ubicacion": 3
    },
    {
        "nombre": "Ritos de la Pachamama",
        "imagen": "https://example.com/pachamama.jpg",
        "descripcion": "Ceremonias ancestrales de ofrenda a la Madre Tierra, especialmente en agosto.",
        "id_ubicacion": 4
    },
    {
        "nombre": "Cantos en Idioma Uru-Chipaya",
        "imagen": "https://example.com/uru_chipaya.jpg",
        "descripcion": "Expresiones musicales únicas de esta antigua cultura ubicada cerca del Salar de Coipasa.",
        "id_ubicacion": 12 
    },
    {
        "nombre": "La Saya Afroboliviana",
        "imagen": "https://example.com/saya.jpg",
        "descripcion": "Expresión cultural de la comunidad afrodescendiente en los Yungas.",
        "id_ubicacion": 6
    },
    {
        "nombre": "Cerámica de Tarabuco",
        "imagen": "https://example.com/tarabuco.jpg",
        "descripcion": "Reconocida artesanía elaborada por comunidades indígenas del sur del país.",
        "id_ubicacion": 13
    },
    {
        "nombre": "Ch’alla de Carnaval",
        "imagen": "https://example.com/challa.jpg",
        "descripcion": "Ritual andino de agradecimiento a la Pachamama durante las festividades.",
        "id_ubicacion": 1
    },
    {
        "nombre": "Cultura Moxeña",
        "imagen": "https://example.com/moxos.jpg",
        "descripcion": "Pueblo indígena de la región de Beni con tradiciones orales, danzas y música barroca.",
        "id_ubicacion": 14 
    },
    {
        "nombre": "Danza del Caporal",
        "imagen": "https://example.com/caporal.jpg",
        "descripcion": "Danza popular moderna con raíces en el folklore afroboliviano.",
        "id_ubicacion": 11
    },
    {
        "nombre": "Tinku",
        "imagen": "https://example.com/tinku.jpg",
        "descripcion": "Ritual de combate entre comunidades, acompañado de música y danza.",
        "id_ubicacion": 2
    },
    {
        "nombre": "Música Barroca Chiquitana",
        "imagen": "https://example.com/barroco_chiquitos.jpg",
        "descripcion": "Tradición musical heredada de las misiones jesuíticas en la región chiquitana.",
        "id_ubicacion": 15
    }
]


historias = [
    {
        "titulo": "La Leyenda del Cerro Rico",
        "descripcion": "Historia sobre cómo el Cerro Rico de Potosí fue descubierto y su importancia durante la colonia",
        "fecha_inicio": "1545-01-01T00:00:00Z",
        "fecha_fin": "1825-01-01T00:00:00Z",
        "imagen": "https://example.com/leyenda_cerro.jpg",
        "id_ubicacion": 2,
        "id_categoria": 3
    },
    {
        "titulo": "La Rebelión de Túpac Katari",
        "descripcion": "Relato del levantamiento indígena contra el dominio español en el siglo XVIII",
        "fecha_inicio": "1781-03-01T00:00:00Z",
        "fecha_fin": "1782-11-15T00:00:00Z",
        "imagen": "https://example.com/tupac_katari.jpg",
        "id_ubicacion": 4,
        "id_categoria": 4
    },
    {
        "titulo": "El Último Día de la Guerra del Chaco",
        "descripcion": "Narración personal de un soldado boliviano durante el conflicto con Paraguay",
        "fecha_inicio": "1935-06-12T00:00:00Z",
        "fecha_fin": "1935-06-12T00:00:00Z",
        "imagen": "https://example.com/guerra_chaco.jpg",
        "id_ubicacion": 6,
        "id_categoria": 1
    },
    {
        "titulo": "La Fundación de La Paz",
        "descripcion": "Cómo Alonso de Mendoza estableció la ciudad de Nuestra Señora de La Paz",
        "fecha_inicio": "1548-10-20T00:00:00Z",
        "fecha_fin": "1548-10-20T00:00:00Z",
        "imagen": "https://example.com/fundacion_lapaz.jpg",
        "id_ubicacion": 1,
        "id_categoria": 3
    },
    {
        "titulo": "El Misterio de la Puerta del Sol",
        "descripcion": "Teorías sobre el significado y origen del famoso monumento tiwanakota",
        "fecha_inicio": "1500-01-01T00:00:00Z",
        "fecha_fin": "1500-01-01T00:00:00Z",
        "imagen": "https://example.com/puerta_sol_historia.jpg",
        "id_ubicacion": 13,
        "id_categoria": 3
    },
    {
        "titulo": "La Vida en las Misiones Jesuíticas",
        "descripcion": "Cómo vivían los indígenas en las reducciones jesuíticas del oriente boliviano",
        "fecha_inicio": "1696-01-01T00:00:00Z",
        "fecha_fin": "1696-01-01T00:00:00Z",
        "imagen": "https://example.com/misiones_vida.jpg",
        "id_ubicacion": 15,
        "id_categoria": 3
    },
    {
        "titulo": "La Batalla de Ingavi",
        "descripcion": "Relato de la victoria boliviana sobre Perú que consolidó la independencia",
        "fecha_inicio": "1841-11-18T00:00:00Z",
        "fecha_fin": "1841-11-18T00:00:00Z",
        "imagen": "https://example.com/batalla_ingavi.jpg",
        "id_ubicacion": 1,
        "id_categoria": 1
    },
    {
        "titulo": "El Primer Ferrocarril en Bolivia",
        "descripcion": "Cómo se construyó el ferrocarril entre Antofagasta y Oruro y su impacto económico",
        "fecha_inicio": "1873-01-01T00:00:00Z",
        "fecha_fin": "1873-01-01T00:00:00Z",
        "imagen": "https://example.com/ferrocarril_bolivia.jpg",
        "id_ubicacion": 2,
        "id_categoria": 3
    },
    {
        "titulo": "La Masacre de Catavi",
        "descripcion": "Triste episodio de represión contra mineros en 1942 que antecedió a la Revolución Nacional",
        "fecha_inicio": "1942-12-21T00:00:00Z",
        "fecha_fin":  "1942-12-21T00:00:00Z",
        "imagen": "https://example.com/masacre_catavi.jpg",
        "id_ubicacion": 2,
        "id_categoria": 1
    },
    {
        "titulo": "El Origen de los Uru-Chipaya",
        "descripcion": "Relato mítico sobre los ancestros que emergieron de las aguas del lago y fundaron la cultura Uru-Chipaya",
        "fecha_inicio": "1000-01-01T00:00:00Z",
        "fecha_fin": "1000-01-01T00:00:00Z",
        "imagen": "https://example.com/origen_uru_chipaya.jpg",
        "id_ubicacion": 18,
        "id_categoria": 3
    }
]


agenda_usuarios = [
  { "id_usuario": 2, "id_evento_agendable": 2, "fecha_recordatorio": "2025-04-06T09:00:00Z" },
  { "id_usuario": 1, "id_evento_agendable": 1, "fecha_recordatorio": "2025-04-06T09:00:00Z" },
  { "id_usuario": 4, "id_evento_agendable": 4, "fecha_recordatorio": "2025-04-06T09:00:00Z" },
  { "id_usuario": 6, "id_evento_agendable": 6, "fecha_recordatorio": "2025-04-06T09:00:00Z" },
  { "id_usuario": 8, "id_evento_agendable": 8, "fecha_recordatorio": "2025-04-06T09:00:00Z" },
  { "id_usuario": 10, "id_evento_agendable": 10, "fecha_recordatorio": "2025-04-06T09:00:00Z" },
  { "id_usuario": 12, "id_evento_agendable": 12, "fecha_recordatorio": "2025-04-06T09:00:00Z" },
  { "id_usuario": 14, "id_evento_agendable": 14, "fecha_recordatorio": "2025-04-06T09:00:00Z" }
]

multimedia_eventos = [
  { "url": "https://ejemplo.com/imagenes/independencia_bolivia.jpg", "tipo": "imagen", "id_evento_historico": 1 },
  { "url": "https://ejemplo.com/imagenes/guerra_pacifico.jpg", "tipo": "imagen", "id_evento_historico": 2 },
  { "url": "https://ejemplo.com/imagenes/revolucion_1952.jpg", "tipo": "imagen", "id_evento_historico": 3 },
  { "url": "https://ejemplo.com/imagenes/fundacion_tiwanaku.jpg", "tipo": "imagen", "id_evento_historico": 4 },
  { "url": "https://ejemplo.com/imagenes/cerro_rico.jpg", "tipo": "imagen", "id_evento_historico": 5 },
  { "url": "https://ejemplo.com/imagenes/tratado_chile.jpg", "tipo": "imagen", "id_evento_historico": 6 },
  { "url": "https://ejemplo.com/imagenes/estado_plurinacional.jpg", "tipo": "imagen", "id_evento_historico": 7 },
  { "url": "https://ejemplo.com/imagenes/guerra_chaco.jpg", "tipo": "imagen", "id_evento_historico": 8 },
  { "url": "https://ejemplo.com/imagenes/revolucion_federal.jpg", "tipo": "imagen", "id_evento_historico": 9 },
  { "url": "https://ejemplo.com/imagenes/umsa.jpg", "tipo": "imagen", "id_evento_historico": 10 },
  { "url": "https://ejemplo.com/imagenes/gas_natural.jpg", "tipo": "imagen", "id_evento_historico": 11 },
  { "url": "https://ejemplo.com/imagenes/marcha_dignidad.jpg", "tipo": "imagen", "id_evento_historico": 12 },
  { "url": "https://ejemplo.com/imagenes/parque_madidi.jpg", "tipo": "imagen", "id_evento_historico": 13 },
  { "url": "https://ejemplo.com/imagenes/guerra_independencia.jpg", "tipo": "imagen", "id_evento_historico": 14 },
  { "url": "https://ejemplo.com/imagenes/grito_libertario.jpg", "tipo": "imagen", "id_evento_historico": 15 }
]

tipos_documentos = [
  {
    "tipo": "Libro"
  },
  {
    "tipo": "Artículo"
  },
  {
    "tipo": "Tesis"
  },
  {
    "tipo": "Informe"
  },
  {
    "tipo": "Revista"
  },
  {
    "tipo": "Ensayo"
  },
  {
    "tipo": "Ponencia"
  },
  {
    "tipo": "Conferencia"
  },
  {
    "tipo": "Estudio de Caso"
  },
  {
    "tipo": "Documento Histórico"
  },
  {
    "tipo": "Guía Práctica"
  },
  {
    "tipo": "Manual"
  },
  {
    "tipo": "Memoria"
  },
  {
    "tipo": "Artículo Científico"
  },
  {
    "tipo": "Capítulo de Libro"
  }
]


bibliotecas_eventos = [
  {
    "titulo": "Historia de la Independencia de Bolivia",
    "autor": "Autor desconocido",
    "imagen": "https://ejemplo.com/imagenes/independencia_bolivia_libro.jpg",
    "fecha_publicacion": "1825-08-06T00:00:00Z",
    "edicion": "Primera edición",
    "id_tipo": 1,
    "fuente": "Archivo Nacional de Bolivia",
    "enlace": "https://ejemplo.com/libros/independencia_bolivia",
    "eventos_historicos": [{ "id_evento_historico": 1 }]
  },
  {
    "titulo": "La Guerra del Pacífico",
    "autor": "Juan Pérez",
    "imagen": "https://ejemplo.com/imagenes/guerra_pacifico_libro.jpg",
    "fecha_publicacion": "1880-05-15T00:00:00Z",
    "edicion": "Segunda edición",
    "id_tipo": 2,
    "fuente": "Biblioteca Militar",
    "enlace": "https://ejemplo.com/libros/guerra_pacifico",
    "eventos_historicos": [{ "id_evento_historico": 2 }]
  },
  {
    "titulo": "Revolución Nacional de 1952",
    "autor": "Carlos Mendoza",
    "imagen": "https://ejemplo.com/imagenes/revolucion_1952_libro.jpg",
    "fecha_publicacion": "1952-04-09T00:00:00Z",
    "edicion": "Primera edición",
    "id_tipo": 3,
    "fuente": "Editorial Revolución",
    "enlace": "https://ejemplo.com/libros/revolucion_1952",
    "eventos_historicos": [{ "id_evento_historico": 3 }]
  },
  {
    "titulo": "Tiwanaku: La Cultura Andina",
    "autor": "María Salazar",
    "imagen": "https://ejemplo.com/imagenes/tiwanaku_libro.jpg",
    "fecha_publicacion": "1950-01-01T00:00:00Z",
    "edicion": "Tercera edición",
    "id_tipo": 4,
    "fuente": "Museo Nacional de Arqueología",
    "enlace": "https://ejemplo.com/libros/tiwanaku",
    "eventos_historicos": [{ "id_evento_historico": 4 }]
  },
  {
    "titulo": "Cerro Rico: Historia y Riqueza",
    "autor": "Eduardo Romero",
    "imagen": "https://ejemplo.com/imagenes/cerro_rico_libro.jpg",
    "fecha_publicacion": "1550-01-01T00:00:00Z",
    "edicion": "Primera edición",
    "id_tipo": 5,
    "fuente": "Biblioteca del Patrimonio",
    "enlace": "https://ejemplo.com/libros/cerro_rico",
    "eventos_historicos": [{ "id_evento_historico": 5 }]
  },
  {
    "titulo": "Tratado de Paz con Chile: Análisis Histórico",
    "autor": "Sofía Ríos",
    "imagen": "https://ejemplo.com/imagenes/tratado_chile_libro.jpg",
    "fecha_publicacion": "1905-01-01T00:00:00Z",
    "edicion": "Segunda edición",
    "id_tipo": 6,
    "fuente": "Editorial Diplomática",
    "enlace": "https://ejemplo.com/libros/tratado_chile",
    "eventos_historicos": [{ "id_evento_historico": 6 }]
  },
  {
    "titulo": "Bolivia Plurinacional: Historia Contemporánea",
    "autor": "Jorge Gutierrez",
    "imagen": "https://ejemplo.com/imagenes/plurinacional_libro.jpg",
    "fecha_publicacion": "2009-01-25T00:00:00Z",
    "edicion": "Primera edición",
    "id_tipo": 7,
    "fuente": "Editorial Política",
    "enlace": "https://ejemplo.com/libros/plurinacional",
    "eventos_historicos": [{ "id_evento_historico": 7 }]
  },
  {
    "titulo": "Guerra del Chaco: La lucha por el territorio",
    "autor": "Miguel López",
    "imagen": "https://ejemplo.com/imagenes/guerra_chaco_libro.jpg",
    "fecha_publicacion": "1935-06-12T00:00:00Z",
    "edicion": "Primera edición",
    "id_tipo": 8,
    "fuente": "Biblioteca Nacional de Bolivia",
    "enlace": "https://ejemplo.com/libros/guerra_chaco",
    "eventos_historicos": [{ "id_evento_historico": 8 }]
  },
  {
    "titulo": "La Revolución Federal de 1899",
    "autor": "Luis Martínez",
    "imagen": "https://ejemplo.com/imagenes/revolucion_federal_libro.jpg",
    "fecha_publicacion": "1899-01-01T00:00:00Z",
    "edicion": "Primera edición",
    "id_tipo": 9,
    "fuente": "Editorial Histórica",
    "enlace": "https://ejemplo.com/libros/revolucion_federal",
    "eventos_historicos": [{ "id_evento_historico": 9 }]
  },
  {
    "titulo": "Fundación de la Universidad Mayor de San Andrés",
    "autor": "Ana Torres",
    "imagen": "https://ejemplo.com/imagenes/umsa_libro.jpg",
    "fecha_publicacion": "1830-10-25T00:00:00Z",
    "edicion": "Primera edición",
    "id_tipo": 10,
    "fuente": "Biblioteca Universitaria",
    "enlace": "https://ejemplo.com/libros/umsa",
    "eventos_historicos": [{ "id_evento_historico": 10 }]
  },
  {
    "titulo": "Gas Natural en Bolivia: Un Tesoro Descubierto",
    "autor": "Carlos Ríos",
    "imagen": "https://ejemplo.com/imagenes/gas_natural_libro.jpg",
    "fecha_publicacion": "1996-01-01T00:00:00Z",
    "edicion": "Segunda edición",
    "id_tipo": 11,
    "fuente": "Editorial Científica",
    "enlace": "https://ejemplo.com/libros/gas_natural",
    "eventos_historicos": [{ "id_evento_historico": 11 }]
  },
  {
    "titulo": "Marcha por el Territorio y la Dignidad",
    "autor": "Isabel Vargas",
    "imagen": "https://ejemplo.com/imagenes/marcha_dignidad_libro.jpg",
    "fecha_publicacion": "1990-09-17T00:00:00Z",
    "edicion": "Primera edición",
    "id_tipo": 12,
    "fuente": "Biblioteca Social",
    "enlace": "https://ejemplo.com/libros/marcha_dignidad",
    "eventos_historicos": [{ "id_evento_historico": 12 }]
  },
  {
    "titulo": "El Parque Nacional Madidi: Un Paraíso Natural",
    "autor": "Pedro García",
    "imagen": "https://ejemplo.com/imagenes/parque_madidi_libro.jpg",
    "fecha_publicacion": "1995-09-21T00:00:00Z",
    "edicion": "Primera edición",
    "id_tipo": 13,
    "fuente": "Editorial Ambiental",
    "enlace": "https://ejemplo.com/libros/parque_madidi",
    "eventos_historicos": [{ "id_evento_historico": 13 }]
  },
  {
    "titulo": "Guerra de la Independencia en Alto Perú",
    "autor": "Fernando Quiroga",
    "imagen": "https://ejemplo.com/imagenes/guerra_independencia_libro.jpg",
    "fecha_publicacion": "1825-08-06T00:00:00Z",
    "edicion": "Primera edición",
    "id_tipo": 14,
    "fuente": "Archivo Histórico",
    "enlace": "https://ejemplo.com/libros/guerra_independencia",
    "eventos_historicos": [{ "id_evento_historico": 14 }]
  },
  {
    "titulo": "Primer Grito Libertario de América",
    "autor": "Luis Gonzales",
    "imagen": "https://ejemplo.com/imagenes/grito_libertario_libro.jpg",
    "fecha_publicacion": "1809-05-25T00:00:00Z",
    "edicion": "Primera edición",
    "id_tipo": 15,
    "fuente": "Editorial Histórica",
    "enlace": "https://ejemplo.com/libros/grito_libertario",
    "eventos_historicos": [{ "id_evento_historico": 15 }]
  }
]

db = Prisma()
async def seed_usuarios():
    for usuario in usuarios:
        await db.usuario.create(data=usuario)

async def seed_roles():
    for rol in roles:
        await db.rol.create(data=rol)

async def seed_usuario_roles():
    for usuario_rol in usuario_roles:
        await db.usuariorol.create(data=usuario_rol)

async def seed_categorias():
    for categoria in categorias:
        await db.categoria.create(data=categoria)

async def seed_ubicaciones():
    for ubicacion in ubicaciones:
        await db.ubicacion.create(data=ubicacion)

async def seed_eventos_historicos():
    for evento_historico in eventos_historicos:
        await db.eventohistorico.create(data=evento_historico)

async def seed_eventos_historicos_categorias():
    for evento_historico_categoria in categorias_evento_historico:
        await db.categoriaeventohistorico.create(data=evento_historico_categoria)

async def seed_eventos_agendables():
    for evento_agendable in eventos_agendables:
        await db.eventoagendable.create(data=evento_agendable)

async def seed_participantes_evento():
    for participante_evento in participantes_evento:
        await db.participanteevento.create(data=participante_evento)

async def seed_presidentes():
    for presidente in presidentes:
        await db.presidente.create(data=presidente)

async def seed_culturas():
    for cultura in culturas:
        await db.cultura.create(data=cultura)

async def seed_historias():
    for historia in historias:
        await db.historia.create(data=historia)

async def seed_agenda_usuarios():
    for agenda_usuario in agenda_usuarios:
        await db.agendausuario.create(data=agenda_usuario)

async def seed_multimedia_eventos():
    for multimedia_evento in multimedia_eventos:
        await db.multimedia.create(data=multimedia_evento)

async def seed_tipos_documentos():
    for tipo_documento in tipos_documentos:
        await db.tipodocumento.create(data=tipo_documento)

async def seed_bibliotecas_eventos():
    for biblioteca_evento in bibliotecas_eventos:
        document = await db.biblioteca.create({
            "titulo": biblioteca_evento["titulo"],
            "autor": biblioteca_evento["autor"],
            "imagen": biblioteca_evento["imagen"],
            "fecha_publicacion": biblioteca_evento["fecha_publicacion"],
            "edicion": biblioteca_evento["edicion"],
            "fuente": biblioteca_evento["fuente"],
            "enlace": biblioteca_evento["enlace"],
            "id_tipo": biblioteca_evento["id_tipo"],	
        })
        
            
async def main():

    await db.connect()

    await asyncio.gather(
        seed_usuarios(),
        seed_roles(),
        seed_usuario_roles(),
        seed_categorias(),
        seed_ubicaciones(),
        seed_eventos_historicos(),
        seed_eventos_historicos_categorias(),
        seed_eventos_agendables(),
        seed_participantes_evento(),
        seed_presidentes(),
        seed_culturas(),
        seed_historias(),
        seed_agenda_usuarios(),
        seed_multimedia_eventos(),
        seed_tipos_documentos(),
        seed_bibliotecas_eventos(),
    )
    await db.disconnect()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())