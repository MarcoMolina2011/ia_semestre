# importaciones necesarias
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics.pairwise import cosine_similarity

# rutas y cargas de documentos
DATA_DIR = Path("data")
KB_PATH = DATA_DIR / "base_conocimiento.txt"
REPORTS_DIR = Path("reports")
REPORT_PATH = REPORTS_DIR / "semana05.md"

def load_documents() -> list[str]:
    docs = [line.strip() for line in KB_PATH.read_text(encoding="utf-8").splitlines() if line.strip()]
    if len(docs) < 8:
        raise ValueError("data/base_conocimiento.txt debe contener al menos 8 entradas.")
    return docs

# Definir reglas expertas (mínimo 5)
RULES = [
    (lambda q: "dns" in q or "internet" in q, "revisar_conectividad"),
    (lambda q: "caliente" in q or "temperatura" in q, "revisar_ventilacion"),
    (lambda q: "sesion" in q or "cuenta" in q, "revisar_acceso"),
    (lambda q: "lento" in q or "memoria" in q, "revisar_rendimiento"),
    (lambda q: "bloqueado" in q or "permiso" in q, "revisar_seguridad"),
]
# Entrenamiento del clasificador (mínimo 15 ejemplos)
TRAIN_X = [
    "equipo muy caliente",
    "se cae internet",
    "no puedo iniciar sesion",
    "ventilador bloqueado",
    "cuenta bloqueada",
    "app lenta",
    "error de impresora",
    "pantalla azul",
    "red lenta",
    "sistema no arranca",
    "cpu sobrecargado",
    "memoria insuficiente",
    "disco lleno",
    "usuario sin permisos",
    "router desconectado"
]
TRAIN_Y = [
    "hardware",
    "red",
    "seguridad",
    "hardware",
    "seguridad",
    "rendimiento",
    "hardware",
    "hardware",
    "red",
    "hardware",
    "rendimiento",
    "rendimiento",
    "rendimiento",
    "seguridad",
    "red"
]

classifier = make_pipeline(
    TfidfVectorizer(),
    LogisticRegression(max_iter=1000, random_state=42),
)
classifier.fit(TRAIN_X, TRAIN_Y)

# Función answer(query) con trazabilidad 
DOCS = load_documents()
vectorizer = TfidfVectorizer()
doc_matrix = vectorizer.fit_transform(DOCS)

def answer(query: str) -> dict:
    q = query.lower()
    fired = [name for condition, name in RULES if condition(q)]
    similarities = cosine_similarity(vectorizer.transform([q]), doc_matrix)[0]
    best_index = int(similarities.argmax())
    label = str(classifier.predict([q])[0])
    return {
        "reglas": fired,
        "evidencia": DOCS[best_index],
        "similitud": float(similarities[best_index]),
        "clase": label,
    }
 # Función para generar reporte Markdown
def write_report(rows: list[tuple[str, dict]]) -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    lines = ["# Semana 05 - Sistema híbrido", ""]
    for i, (query, result) in enumerate(rows, start=1):
        lines += [
            f"## Consulta {i}",
            f"- Entrada: {query}",
            f"- Reglas: {', '.join(result['reglas']) or 'ninguna'}",
            f"- Evidencia: {result['evidencia']}",
            f"- Similitud: {result['similitud']:.3f}",
            f"- Clase: {result['clase']}",
        ]
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")

# Ejecutar consultas de prueba
if __name__ == "__main__":
    rows = []
    for query in [
        "El equipo está caliente",
        "Internet se cae y aparece error DNS",
        "No puedo iniciar sesión con mi cuenta"
    ]:
        result = answer(query)
        rows.append((query, result))
    write_report(rows)
    print("Reporte generado en reports/semana05.md")
