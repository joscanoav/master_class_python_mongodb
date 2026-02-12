import os
import pymongo
from dotenv import load_dotenv

# ====================================================================
#  FASE 1: CONEXIÓN A LA NUBE (NO TOCAR, YA ESTÁ LISTO)
# ====================================================================

# 1. Cargamos la contraseña desde el archivo seguro .env
load_dotenv()
uri = os.getenv("MONGO_URI")

print("⏳ Conectando con el servidor de Jorge...")

try:
    # 2. Creamos el 'Cliente' (el conductor que nos lleva a la nube)
    # OJO 2º ASIR: Esto conecta a un cluster real en AWS (Atlas)
    cliente = pymongo.MongoClient(uri)
    
    # 3. Seleccionamos la Base de Datos y la Colección
    # OJO 1º ASIR: 'instituto_asir' es la carpeta, 'clase_conjunta' es el archivo
    db = cliente["instituto_asir"]
    coleccion = db["clase_conjunta"]
    
    print("✅ ¡CONEXIÓN EXITOSA! El túnel está abierto.")
    print("------------------------------------------")

except Exception as e:
    print(f"❌ Error de conexión: {e}")
    # Si falla, cerramos el programa para no seguir
    exit()


# ====================================================================
#  FASE 2: ZONA DE PROGRAMACIÓN (AQUÍ ES DONDE ESCRIBÍS VOSOTROS)
# ====================================================================

# Instrucciones:
# 1. Cread un menú infinito con while True
# 2. Opción 1: Pedir datos -> Crear Diccionario -> Guardar con insert_one()
# 3. Opción 2: Leer datos con find()

while True:
    # Borra este 'pass' y empieza a programar tu menú aquí abajo 👇
    pass