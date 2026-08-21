from dataclasses import dataclass
from pathlib import Path
import csv, re, unicodedata

ROOT = Path(__file__).resolve().parent.parent
CSV_FILE = ROOT / "data" / "casos_ia.csv"
REPORT_FILE = ROOT / "reports" / "semana03.md"

@dataclass(frozen=True)
class Category:
    name: str
    keywords: tuple[str, ...]

# Categorías principales
CATEGORIES = [
    Category("Visión por computador", ("imagen","imagenes","foto","fotografia","camara","rostro","peaton","senal")),
    Category("Procesamiento de lenguaje natural", ("texto","comentario","comentarios","correo","chatbot","contrato","nombres")),
    Category("Aprendizaje automático predictivo", ("predecir","probabilidad","demanda","fraude","sensores")),
    Category("Sistemas de recomendación", ("recomendar","preferencias","historial","sugerir")),
    Category("Búsqueda y optimización", ("ruta","horario","optimizar","combinacion optima","capacidad maxima")),
    Category("Sistemas expertos", ("diagnostico","reglas","politicas","credito")),
    Category("Robótica y sistemas autónomos", ("robot","dron","vehiculo autonomo","obstaculos")),
]

# Cinco reglas de ejemplo. Cada estudiante debe reemplazarlas o ampliarlas
# con cinco reglas propias y justificar el cambio en reports/semana03.md.
CUSTOM_RULES = {
    "Visión por computador": ("matricula", "sensor"),
    "Procesamiento de lenguaje natural": ("sentimiento", "usuario"),
    "Aprendizaje automático predictivo": ("falla", "red"),
    "Sistemas expertos": ("sintoma", "proyecto"),
    "Robótica y sistemas autónomos": ("trayectoria", "seguridad"),
}

# Referencia manual (categorías esperadas para los 20 casos)
MANUAL_REFERENCE = [
    "Visión por computador",
    "Procesamiento de lenguaje natural",
    "Aprendizaje automático predictivo",
    "Búsqueda y optimización",
    "Sistemas de recomendación",
    "Aprendizaje automático predictivo",
    "Visión por computador",
    "Procesamiento de lenguaje natural",
    "Aprendizaje automático predictivo",
    "Sistemas expertos",
    "Visión por computador",
    "Procesamiento de lenguaje natural",
    "Robótica y sistemas autónomos",
    "Búsqueda y optimización",
    "Aprendizaje automático predictivo",
    "Procesamiento de lenguaje natural",
    "Visión por computador",
    "Sistemas expertos",
    "Robótica y sistemas autónomos",
    "Búsqueda y optimización",
]

# Funciones auxiliares
def normalize(text: str) -> str:
    text = text.strip().lower()
    text = unicodedata.normalize("NFD", text)
    text = "".join(ch for ch in text if unicodedata.category(ch) != "Mn")
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()

def normalize_header(text: str) -> str:
    return normalize(text).replace(" ", "")

def contains_keyword(text: str, keyword: str) -> bool:
    normalized_text = f" {normalize(text)} "
    normalized_keyword = normalize(keyword)
    return f" {normalized_keyword} " in normalized_text

def build_categories() -> list[Category]:
    result = []
    for category in CATEGORIES:
        extra = CUSTOM_RULES.get(category.name, ())
        result.append(Category(category.name, category.keywords + tuple(extra)))
    return result

def classify_problem(text: str) -> tuple[str, list[str], dict[str, int]]:
    scores = {}
    for category in build_categories():
        score = sum(contains_keyword(text, keyword) for keyword in category.keywords)
        scores[category.name] = score
    matches = [(score, index, category.name) for index, category in enumerate(build_categories()) if (score := scores[category.name]) > 0]
    matches.sort(key=lambda item: (-item[0], item[1]))
    detected = [name for _, _, name in matches]
    primary = detected[0] if detected else "Requiere análisis"
    return primary, detected or ["Requiere análisis"], scores

def read_cases() -> list[str]:
    if not CSV_FILE.exists():
        raise FileNotFoundError(f"No existe {CSV_FILE}. Crea data/casos_ia.csv antes de ejecutar la práctica.")
    with CSV_FILE.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        if not reader.fieldnames:
            raise ValueError("El CSV está vacío o no contiene encabezados.")
        original_headers = list(reader.fieldnames)
        reader.fieldnames = [normalize_header(name) for name in reader.fieldnames]
        if "descripcion" not in reader.fieldnames:
            raise ValueError(f"No se encontró la columna 'descripcion'. Encabezados encontrados: {original_headers}")
        cases = []
        for row in reader:
            description = (row.get("descripcion") or "").strip()
            if description:
                cases.append(description)
        if len(cases) < 20:
            raise ValueError(f"La práctica requiere al menos 20 casos y el archivo contiene {len(cases)}.")
        return cases

def write_report(results: list[dict]) -> None:
    REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)
    reference_count = min(len(results), len(MANUAL_REFERENCE))
    matches = sum(results[i]["primary"] == MANUAL_REFERENCE[i] for i in range(reference_count))
    accuracy = 100 * matches / reference_count if reference_count else 0.0
    lines = [
        "# Semana 03 - Taxonomía de Inteligencia Artificial",
        "",
        "## Resultado automático frente a clasificación manual de referencia",
        "",
        "| Caso | Categoría automática principal | Categorías detectadas | Manual | Estado |",
        "|---:|---|---|---|---|",
    ]
    for i, result in enumerate(results, start=1):
        manual = MANUAL_REFERENCE[i - 1] if i <= len(MANUAL_REFERENCE) else "Pendiente"
        status = "Coincide" if result["primary"] == manual else "Revisar"
        detected = ", ".join(result["detected"])
        lines.append(f"| {i} | {result['primary']} | {detected} | {manual} | {status} |")
    lines += [
        "",
        f"Coincidencia con la referencia: **{accuracy:.2f}%** ({matches}/{reference_count}).",
        "",
        "## Cinco reglas propias",
        "",
        "Reemplaza o amplía las cinco reglas de ejemplo de `CUSTOM_RULES` y explica aquí por qué son pertinentes para tu dominio.",
        "",
        "## Discrepancias y análisis",
        "",
        "Para cada discrepancia explica: (1) qué palabra o frase activó la regla, (2) por qué la clasificación manual difiere y (3) qué regla modificarías.",
        "",
        "## Nota técnica",
        "",
        "Un problema real puede pertenecer a varias áreas de IA. La columna 'principal' usa la categoría con mayor cantidad de coincidencias; las demás coincidencias se conservan como categorías secundarias.",
    ]
    REPORT_FILE.write_text("\n".join(lines), encoding="utf-8")

def main() -> None:
    cases = read_cases()
    results = []
    print("=" * 80)
    print("SEMANA 03 - TAXONOMÍA DE INTELIGENCIA ARTIFICIAL")
    print("=" * 80)
    for i, case in enumerate(cases, start=1):
        primary, detected, scores = classify_problem(case)
        results.append({"description": case,"primary": primary,"detected": detected,"scores": scores})
        print(f"{i:02d}. {case}")
        print(f" Principal: {primary}")
        print(f" Áreas detectadas: {', '.join(detected)}")
    write_report(results)
    print(f"\nCasos procesados: {len(results)}")
    print(f"Reporte generado: {REPORT_FILE}")

if __name__ == "__main__":
    main()
