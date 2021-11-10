from flask import Flask, json, jsonify, request
from flask_cors import CORS
import mysql.connector
from flask_jwt_extended import create_access_token, JWTManager, jwt_required, get_jwt_identity

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345678',
    database='usuarios',
    port=3307,
)

app = Flask(__name__)
CORS(app)
app.config["JWT_SECRET_KEY"] = "ROSCerVALEvinstOmenTrideankLeaRm"
jwt = JWTManager(app)

@app.post('/login')
def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    cursor = db.cursor(dictionary=True, buffered=True)

    cursor.execute('''select * from usuarios 
        where email = %s and contrasena = %s ''', (email, password,))

    usuario = cursor.fetchone()

    if not usuario:
        return jsonify({
            "message": "Datos de acceso invalidos"
        })
    
    token = create_access_token(identity=usuario['id'])

    return jsonify({
        "token": token
    })

@app.route('/')
def index():
    return 'Hello World'

@app.post('/usuarios')
def crearUsuario():
    #request => Lo que me envia el cliente
    #response => Lo que le voy a responder
    datos = request.json
    
    cursor = db.cursor()
    
    cursor.execute('''INSERT INTO usuarios(nombres, apellidos, email, contrasena) 
        VALUE(%s, %s, %s, %s)''', (
        datos['nombres'],
        datos['apellidos'],
        datos['email'],
        datos['contrasena'],
    ))

    db.commit()

    return jsonify({
        "mensaje": "Usuario almacenado correctamente"
    })

@app.get('/usuarios')
@jwt_required()
def listarUsuarios():
    usuario = get_jwt_identity()
    print(usuario)
    cursor = db.cursor(dictionary=True)

    cursor.execute('select * from usuarios')

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