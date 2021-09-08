from flask import Flask, json, jsonify, request
import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345678',
    database='usuarios',
    port=3307,
)

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.post('/usuarios')
def crearUsuario():
    #request => Lo que me envia el cliente
    #response => Lo que le voy a responder
    datos = request.json
    
    cursor = db.cursor()
    
    cursor.execute('''INSERT INTO usuario(nombres, email, contrasena) 
        VALUE(%s, %s, %s)''', (
        datos['nombres'],
        datos['email'],
        datos['contrasena'],
    ))

    db.commit()

    return jsonify({
        "mensaje": "Usuario almacenado correctamente"
    })

@app.get('/usuarios')
def listarUsuarios():
    cursor = db.cursor(dictionary=True)

    cursor.execute('select * from usuario')

    usuarios = cursor.fetchall()

    return jsonify(usuarios)

@app.put('/usuarios/<id>')
def actualizarUsuario(id):
    datos = request.json

    cursor = db.cursor()

    cursor.execute('''UPDATE usuario set nombres=%s, 
        email=%s, contrasena=%s where id=%s''',(
            datos['nombres'],
            datos['email'],
            datos['contrasena'],
            id
        ))

    db.commit()

    return jsonify({
        "mensaje": "Usuario actualizado correctamente"
    })

app.run(debug=True)