from flask import render_template
from app import app

@app.route('/')
def inicio():
	acciones = ["Accion 1","Accion 2","Accion 3"]
	return render_template('inicio.html', acciones=acciones)