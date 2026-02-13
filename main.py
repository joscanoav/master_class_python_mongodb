import os
import pymongo
from dotenv import load_dotenv

# --- FASE 1: ADMINISTRACIÓN Y CONEXIÓN ---
load_dotenv()
uri = os.getenv("MONGO_URI")

try:
    cliente = pymongo.MongoClient(uri)
    print("✅ CONEXIÓN EXITOSA")
except Exception as e:
    print(f"❌ Error: {e}")

db = cliente["instituto_asir"]
coleccion = db["clase_conjunta"]

# --- FASE 2: LÓGICA ---
while True:
    print("1. Insertar Alumno (Write)")
    print("2. Ver Alumnos (Read)")
    print("3. Salir")

    opcion = input("\n> Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        curso = input("Curso (1º o 2º): ")
        nuevo_alumno = {
            "nombre": nombre,
            "curso": curso,
            "asistente": True
        }
        coleccion.insert_one(nuevo_alumno)
        print("💾 ¡Guardado!")

    elif opcion == "2":
        cursor = coleccion.find()
        for alumno in cursor:
            print(f"- {alumno['nombre']} ({alumno['curso']})")

    elif opcion == "3":
        break