from flask import Flask, render_template, send_from_directory, Response
import json
import database as db
from models import Persona

PersonaSchema = Persona.Persona
EstudianteSchema = Persona.Estudiante

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
	return render_template("index.html")


@app.route('/api/v1/get_all_students', methods = ['GET'])
def get_all_students():
    try:
        return str(db.get_all_students(True))
    except Exception as e:
        return None

@app.route("/api/v1/insert_person", methods=["POST"])
def insert_person():
    pass


@app.route("/api/v1/get_all_profs", methods=["GET"])
def get_all_profs():
    pass

@app.route("/api/v1/insert_prof", methods=["POST"])
def insert_prof():
    pass

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404errorPage.html")

@app.route('/public/<path:path>', methods=["GET"])
def send_static_files(path):
    return send_from_directory('public', path)

if __name__ == '__main__':
    app.run(port = 3000, debug = True)

# le indicamos el puerto (3000 en este caso) y si estamos el modo debugger o no

