from flask import Flask, request, jsonify
from models import db, Zoo, Habitat, Empleado, Visitante, Animal

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///zoologico.db'
db.init_app(app)

@app.route('/zoo', methods=['POST'])
def create_zoo():
    data = request.get_json()
    zoo = Zoo(nombre=data['nombre'], direccion=data['direccion'])
    db.session.add(zoo)
    db.session.commit()
    return jsonify({'id': zoo.id, 'nombre': zoo.nombre, 'direccion': zoo.direccion}), 201

@app.route('/zoo/<int:zoo_id>', methods=['GET'])
def get_zoo(zoo_id):
    zoo = Zoo.query.get_or_404(zoo_id)
    return jsonify({'id': zoo.id, 'nombre': zoo.nombre, 'direccion': zoo.direccion})

@app.route('/zoo', methods=['GET'])
def get_zoo_all():
    zoo = Zoo.query.all()
    return jsonify([{'id': zo.id, 'nombre': zo.nombre, 'direccion': zo.direccion} for zo in zoo])

@app.route('/zoo/<int:zoo_id>', methods=['PUT'])
def update_zoo(zoo_id):
    zoo = Zoo.query.get_or_404(zoo_id)
    data = request.get_json()
    zoo.nombre = data['nombre']
    zoo.direccion = data['direccion']
    db.session.commit()
    return jsonify({'id': zoo.id, 'nombre': zoo.nombre, 'direccion': zoo.direccion})

@app.route('/zoo/<int:zoo_id>', methods=['DELETE'])
def delete_zoo(zoo_id):
    zoo = Zoo.query.get_or_404(zoo_id)
    db.session.delete(zoo)
    db.session.commit()
    return '', 204

@app.route('/animal', methods=['POST'])
def create_animal():
    data = request.get_json()
    zoo=Zoo.query.get(data['zoo_id'])
    habitat=Habitat.query.get(data['habitat_id'])
    if not zoo or not habitat:
    	return jsonify({'mensaje': 'Zoologico o Habitat no existe'})
    animal = Animal(nombre=data['nombre'], especie=data['especie'], edad=data['edad'], zoo_id=data['zoo_id'], habitat_id=data['habitat_id'])
    db.session.add(animal)
    db.session.commit()
    return jsonify({'id': animal.id, 'nombre': animal.nombre,  'edad': animal.edad, 'especie': animal.especie, 'zoo': {'id': zoo.id, 'nombre': zoo.nombre, 'direccion': zoo.direccion}, 'habitat':{'id': habitat.id, 'nombre': habitat.nombre, 'clima': habitat.clima, 'tamaño': habitat.tamano}}), 201

@app.route('/animal/<int:animal_id>', methods=['GET'])
def get_animal(animal_id):
    animal = Animal.query.get_or_404(animal_id)
    zoo=Zoo.query.get(animal.zoo_id)
    habitat=Habitat.query.get(animal.habitat_id)
    return jsonify({'id': animal.id, 'nombre': animal.nombre,  'edad': animal.edad, 'especie': animal.especie, 'zoo': {'id': zoo.id, 'nombre': zoo.nombre, 'dirección': zoo.direccion}, 'habitat':{'id': habitat.id, 'nombre': habitat.nombre, 'clima': habitat.clima, 'tamaño': habitat.tamano}})

@app.route('/animal/<int:animal_id>', methods=['PUT'])
def update_animal(animal_id):
    data=request.get_json()
    animal = Animal.query.get_or_404(animal_id)
    zoo=Zoo.query.get(data['zoo_id'])
    habitat=Habitat.query.get(data['habitat_id'])
    if not zoo or not habitat:
    	return jsonify({'mensaje': 'Zoologico o Habitat no existe'})
    animal.nombre = data['nombre']
    animal.especie = data['especie']
    animal.edad = data['edad']
    animal.zoo_id = data['zoo_id']
    animal.habitat_id = data['habitat_id']
    db.session.commit()
    return jsonify({'id': animal.id, 'nombre': animal.nombre,  'edad': animal.edad, 'especie': animal.especie, 'zoo': {'id': zoo.id, 'nombre': zoo.nombre, 'dirección': zoo.direccion}, 'habitat':{'id': habitat.id, 'nombre': habitat.nombre, 'clima': habitat.clima, 'tamaño': habitat.tamano}})

@app.route('/animal/<int:animal_id>', methods=['DELETE'])
def delete_animal(animal_id):
    animal = Animal.query.get_or_404(animal_id)
    db.session.delete(animal)
    db.session.commit()
    return jsonify({'mensaje': 'Eliminado'}), 204

@app.route('/empleado', methods=['POST'])
def create_empleado():
    data = request.get_json()
    zoo=Zoo.query.get(data['zoo_id'])
    if not zoo:
    	return jsonify({'mensaje': 'Zoologico no existe'})
    empleado = Empleado(nombre=data['nombre'], apellido=data['apellido'], posicion=data['posicion'], anos_experiencia=data['anos_experiencia'], zoo_id=data['zoo_id'])
    db.session.add(empleado)
    db.session.commit()
    return jsonify({'id':empleado.id, 'nombre': empleado.nombre, 'apellido': empleado.apellido, 'posicion': empleado.posicion, 'anos_experiencia': empleado.anos_experiencia, 'zoo_id': empleado.zoo_id}), 201

@app.route('/empleado/<int:empleado_id>', methods=['GET'])
def get_empleado(empleado_id):
    empleado = Empleado.query.get_or_404(empleado_id)
    return jsonify({'id': empleado.id, 'nombre': empleado.nombre, 'apellido': empleado.apellido, 'posicion': empleado.posicion, 'anos_experiencia': empleado.anos_experiencia, 'zoo_id': empleado.zoo_id})

@app.route('/empleado/<int:empleado_id>', methods=['PUT'])
def update_empleado(empleado_id):
    empleado = Empleado.query.get_or_404(empleado_id)
    data = request.get_json()
    empleado.nombre = data['nombre']
    empleado.apellido = data['apellido']
    empleado.posicion = data['posicion']
    empleado.anos_experiencia = data['anos_experiencia']
    empleado.zoo_id = data['zoo_id']
    db.session.commit()
    return jsonify({'id': empleado.id, 'nombre': empleado.nombre, 'apellido': empleado.apellido, 'posicion': empleado.posicion, 'anos_experiencia': empleado.anos_experiencia, 'zoo_id': empleado.zoo_id})

@app.route('/empleado/<int:empleado_id>', methods=['DELETE'])
def delete_empleado(empleado_id):
    empleado = Empleado.query.get_or_404(empleado_id)
    db.session.delete(empleado)
    db.session.commit()
    return jsonify({'mensaje': 'Eliminado'}), 204

@app.route('/visitante', methods=['POST'])
def create_visitante():
    data = request.get_json()
    visitante = Visitante(nombre=data['nombre'], apellido=data['apellido'], cedula=data['cedula'], fecha_visita=data['fecha_visita'], zoo_id=data['zoo_id'])
    db.session.add(visitante)
    db.session.commit()
    return jsonify({'id': visitante.id, 'nombre': visitante.nombre, 'apellido': visitante.apellido, 'cedula': visitante.cedula, 'zoo_id': visitante.zoo_id}), 201

@app.route('/visitante/<int:visitante_id>', methods=['GET'])
def get_visitante(visitante_id):
    visitante = Visitante.query.get_or_404(visitante_id)
    return jsonify({'id': visitante.id, 'nombre': visitante.nombre, 'apellido': visitante.apellido, 'cedula': visitante.cedula, 'fecha_visita': visitante.fecha_visita, 'zoo_id': visitante.zoo_id})

@app.route('/visitante/<int:visitante_id>', methods=['PUT'])
def update_visitante(visitante_id):
    visitante = Visitante.query.get_or_404(visitante_id)
    data = request.get_json()
    visitante.nombre = data['nombre']
    visitante.apellido = data['apellido']
    visitante.cedula = data['cedula']
    db.session.commit()
    return jsonify({'id': visitante.id, 'nombre': visitante.nombre, 'apellido': visitante.apellido, 'cedula': visitante.cedula})

@app.route('/visitante/<int:visitante_id>', methods=['DELETE'])
def delete_visitante(visitante_id):
    visitante = Visitante.query.get_or_404(visitante_id)
    db.session.delete(visitante)
    db.session.commit()
    return jsonify({'mensaje': 'Eliminado'}), 204

@app.route('/habitat', methods=['POST'])
def create_habitat():
    data = request.get_json()
    habitat = Habitat(nombre=data['nombre'], clima=data['clima'], tamano=data['tamano'])
    db.session.add(habitat)
    db.session.commit()
    return jsonify({'id': habitat.id, 'nombre': habitat.nombre, 'clima': habitat.clima, 'tamano': habitat.tamano}), 201

@app.route('/habitat/<int:habitat_id>', methods=['GET'])
def get_habitat(habitat_id):
    habitat = Habitat.query.get_or_404(habitat_id)
    return jsonify({'id': habitat.id, 'nombre': habitat.nombre, 'clima': habitat.clima, 'tamano': habitat.tamano})

@app.route('/habitat/<int:habitat_id>', methods=['PUT'])
def update_habitat(habitat_id):
    habitat = Habitat.query.get_or_404(habitat_id)
    data = request.get_json()
    habitat.nombre = data['nombre']
    habitat.clima = data['clima']
    habitat.tamano = data['tamano']
    db.session.commit()
    return jsonify({'id': habitat.id,'nombre': habitat.nombre, 'clima': habitat.clima, 'tamano': habitat.tamano})

@app.route('/habitat/<int:habitat_id>', methods=['DELETE'])
def delete_habitat(habitat_id):
    habitat = Habitat.query.get_or_404(habitat_id)
    db.session.delete(habitat)
    db.session.commit()
    return jsonify({'mensaje': 'Eliminado'}), 204
