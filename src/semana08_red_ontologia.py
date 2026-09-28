# Importación de librerías necesarias
from pathlib import Path          # Manejo de rutas de archivos y carpetas
import pickle                     # Guardar y cargar objetos de Python (ej. el modelo entrenado)
import sqlite3                    # Base de datos SQLite para registrar evidencia
import networkx as nx             # Librería para crear grafos y ontologías
import matplotlib.pyplot as plt   # Visualización de imágenes
from sklearn.datasets import load_digits          # Dataset de dígitos escritos a mano
from sklearn.model_selection import train_test_split  # División en entrenamiento y prueba
from sklearn.neural_network import MLPClassifier      # Red neuronal multicapa
from sklearn.metrics import accuracy_score            # Métrica de precisión

# Definición de rutas y carpeta de artefactos
ROOT = Path(__file__).resolve().parent.parent
ARTIFACTS = ROOT / "artifacts"
ARTIFACTS.mkdir(parents=True, exist_ok=True)  # Crea la carpeta si no existe

# Cargar dataset de dígitos (cada imagen es 8x8 píxeles)
X, y = load_digits(return_X_y=True)

# Dividir datos en entrenamiento (75%) y prueba (25%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# Definir y entrenar la red neuronal MLP
model = MLPClassifier(hidden_layer_sizes=(64,), max_iter=400, random_state=42)
model.fit(X_train, y_train)  # Ajusta los pesos internos con los datos de entrenamiento

# Predicción sobre el conjunto de prueba
pred = model.predict(X_test)

# Calcular e imprimir la precisión del modelo
print("Accuracy MLP:", round(accuracy_score(y_test, pred), 4))

# Guardar el modelo entrenado en artifacts/modelo_mlp.pkl
with (ARTIFACTS / "modelo_mlp.pkl").open("wb") as file:
    pickle.dump(model, file)

# Crear base de datos SQLite para registrar evidencia de imágenes
with sqlite3.connect(ARTIFACTS / "imagenes.db") as con:
    con.execute(
        "CREATE TABLE IF NOT EXISTS images("
        "id INTEGER PRIMARY KEY, label INTEGER, split TEXT)"
    )
    # ⚠️ Línea de borrado eliminada para conservar registros previos
    # con.execute("DELETE FROM images")  
    con.executemany(
        "INSERT INTO images(id,label,split) VALUES(?,?,?)",
        [(i, int(y[i]), "dataset") for i in range(20)],  # Inserta 20 registros de ejemplo
    )
    con.commit()

# Crear ontología en forma de grafo dirigido
G = nx.DiGraph()
G.add_edges_from([
    ("digito", "cero", {"rel": "tiene_clase"}),
    ("digito", "uno", {"rel": "tiene_clase"}),
    ("digito", "dos", {"rel": "tiene_clase"}),
    ("modelo_mlp", "digito", {"rel": "reconoce"}),
    ("imagen", "digito", {"rel": "representa"}),
    ("prediccion", "digito", {"rel": "asigna_clase"}),
    ("modelo_mlp", "prediccion", {"rel": "produce"}),
])
nx.write_graphml(G, ARTIFACTS / "ontologia.graphml")  # Exporta la ontología a archivo GraphML
print("Relaciones de ontología:", G.number_of_edges())

# Integrar una predicción real con la ontología
ejemplo_id = 15
clase_predicha = int(model.predict([X[ejemplo_id]])[0])  # Predice la clase del ejemplo 15
concepto = f"digito_{clase_predicha}"                    # Crea concepto dinámico (ej. digito_7)
G.add_edge("prediccion_15", concepto, rel="asigna_clase")  # Relación predicción → clase
G.add_edge("imagen_15", "prediccion_15", rel="genera")     # Relación imagen → predicción
print(ejemplo_id, clase_predicha, concepto)

# Generar y guardar imágenes de ejemplo (8x8 píxeles) en artifacts/
for i in range(5):  # Guarda 5 ejemplos
    plt.imshow(X[i].reshape(8, 8), cmap="gray")  # Convierte vector en imagen 8x8
    plt.title(f"Dígito: {y[i]}")                 # Etiqueta real del dígito
    plt.axis("off")                              # Oculta ejes
    plt.savefig(ARTIFACTS / f"digito_{i}.png")   # Guarda archivo PNG
    plt.close()
print("Imágenes guardadas en artifacts/: digito_0.png ... digito_4.png")

# --- Checklist de verificación de artefactos ---
print("\n--- Checklist de artefactos ---")

# Lista de nombres de archivos que deberían existir en la carpeta artifacts
for nombre in ["modelo_mlp.pkl", "imagenes.db", "ontologia.graphml"] + [f"digito_{i}.png" for i in range(5)]:
    ruta = ARTIFACTS / nombre   # Construye la ruta completa del archivo
    # Imprime ✔ si el archivo existe, ✘ si no existe
    print(f"{nombre}: {'✔' if ruta.exists() else '✘'}")

