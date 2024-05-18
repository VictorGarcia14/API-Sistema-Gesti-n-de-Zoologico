from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Zoo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    direccion = db.Column(db.String(120))
    animales = db.relationship('Animal', backref='zoo', lazy=True)
    empleados = db.relationship('Empleado', backref='zoo', lazy=True)
    visitas = db.relationship('Visitante', backref='zoo', lazy=True)

class Habitat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    clima = db.Column(db.String(80))
    tamano = db.Column(db.Float)
    animales = db.relationship('Animal', backref='habitat', lazy=True)

class Empleado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    apellido = db.Column(db.String(80), nullable=False)
    posicion = db.Column(db.String(80))
    anos_experiencia = db.Column(db.Integer)
    zoo_id = db.Column(db.Integer, db.ForeignKey('zoo.id'), nullable=False)

class Visitante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    apellido = db.Column(db.String(80), nullable=False)
    cedula = db.Column(db.String(20), unique=True, nullable=False)
    fecha_visita = db.Column(db.DateTime, default=datetime.now)
    zoo_id = db.Column(db.Integer, db.ForeignKey('zoo.id'), nullable=False)

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    especie = db.Column(db.String(80), nullable=False)
    edad = db.Column(db.Integer)
    zoo_id = db.Column(db.Integer, db.ForeignKey('zoo.id'), nullable=False)
    habitat_id = db.Column(db.Integer, db.ForeignKey('habitat.id'), nullable=False)
