from flask.app import Flask
import pymysql, json
from pymysql import connections, cursors
from models import Persona

PersonaSchema = Persona.Persona
EstudianteSchema = Persona.Estudiante

def get_connection():
    try:
        config = get_config()
        # operador ternario:
        index = 2 if config[0]['in_production'] else 1

        return pymysql.connect(
            user = config[index]['username'],
            password = config[index]['passw'],
            host = config[index]['host'],
            database = config[index]['database_name']
        )

    except Exception as e:
        print(e)
        raise e

def get_config():
    with open("config.json") as file:
        data = json.load(file)
        return data

def query(sql_query):
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(sql_query)
    except Exception as ex:
        connection.rollback()
    else:
        connection.commit()
        cursor.close()
        connection.close()


def select_query(sql_query, in_json=True):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(sql_query)
    rows = cursor.fetchall()

    if in_json:
        records = json.dumps(tuple(rows), indent=4, sort_keys=True, default=str, ensure_ascii=False)
    else:
        records = rows
    cursor.close()
    connection.close()
    return records


def get_all_students(in_json):
    query = """SELECT 
    p.cedula, p.nombre, p.apellido, p.fechaDacimiento, p.sexo, p.correo, e.añoIngreso, e.creditos
    FROM Personas as p JOIN Estudiantes as e ON p.cedula = e.cedulaEstudiante
    """

    return select_query(query, in_json)

def get_all_profs(in_json):
    query = """SELECT 
    p.cedula, p.nombre, p.apellido, p.fechaDacimiento, p.sexo, p.correo, pr.instituto
    FROM Personas as p JOIN Profesores as pr ON p.cedula = pr.cedulaProf
    """

    return select_query(query, in_json)

def insert_student(student):
    pass


def insert_prof(prof):
    pass

if __name__ == "__main__":
    data = get_all_students(True)
    print(data)
    print(type(data))
    
