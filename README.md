# Post
  # Zoo
    http://victor1403.pythonanywhere.com/zoo
    Parámetros: JSON {"nombre": valor, "direccion": valor}
  # Habitat
    http://victor1403.pythonanywhere.com/habitat
    Parámetros: JSON {"nombre": valor, "tamano": valor, "clima": valor}
  # Empleado
    http://victor1403.pythonanywhere.com/empleado
    Parametros: JSON {"nombre": valor, "apellido": valor, "posicion": valor, "anos_experiencia": valor, "zoo_id": valor}
  # Visitante
    http://victor1403.pythonanywhere.com/visitante
    Parametros: JSON {"nombre": valor, "apellido": valor, "cedula": valor, "zoo_id": valor}
  # Animal
    http://victor1403.pythonanywhere.com/animal
    Parametros: JSON {"nombre": valor, "edad": valor, "especie": valor, "zoo_id": valor, "habitat_id": valor}
# Get
  # Zoo
    http://victor1403.pythonanywhere.com/zoo
  # Habitat
    http://victor1403.pythonanywhere.com/habitat
  # Empleado
    http://victor1403.pythonanywhere.com/empleado
  # Visitante
    http://victor1403.pythonanywhere.com/visitante
  # Animal
    http://victor1403.pythonanywhere.com/animal
    
# Put

  # Zoo
    http://victor1403.pythonanywhere.com/zoo/{{zoo_id}}
    Parámetros: JSON {"nombre": valor, "direccion": valor}
  # Habitat
    http://victor1403.pythonanywhere.com/habitat/{{habitat_id}}
    Parámetros: JSON {"nombre": valor, "tamano": valor, "clima": valor}
  # Empleado
    http://victor1403.pythonanywhere.com/empleado/{{empleado_id}}
    Parametros: JSON {"nombre": valor, "apellido": valor, "posicion": valor, "anos_experiencia": valor, "zoo_id": valor}
  # Visitante
    http://victor1403.pythonanywhere.com/visitante/{{visitante_id}}
    Parametros: JSON {"nombre": valor, "apellido": valor, "cedula": valor, "zoo_id": valor}
  # Animal
    http://victor1403.pythonanywhere.com/animal/{{animal_id}}
    Parametros: JSON {"nombre": valor, "edad": valor, "especie": valor, "zoo_id": valor, "habitat_id": valor}
    
# Delete
  # Zoo
    http://victor1403.pythonanywhere.com/zoo/{{zoo_id}}
  # Habitat
    https://argenisrrazaga.pythonanywhere.com/cursos/{{id_curso}}
  # Empleado
  
http://victor1403.pythonanywhere.com/empleado/{{empleado_id}}
  # Visitante

http://victor1403.pythonanywhere.com/visitante/{{visitante_id}}
  # Animal
http://victor1403.pythonanywhere.com/animal/{{animal_id}}
