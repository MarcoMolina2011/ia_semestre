import numpy as np

# 1) Representación numérica
sample = np.array([72.0, 0.85, 3.0])  # temperatura, carga, errores
reference = np.array([70.0, 0.80, 2.0])
distance = np.linalg.norm(sample - reference)
print("Distancia numérica:", round(float(distance), 3))

# 2) Representación simbólica
facts = {"temperatura_alta", "carga_alta", "errores_presentes"}
if {"temperatura_alta", "carga_alta"}.issubset(facts):
    print("Conclusión simbólica: riesgo_termico")

# 3) Autómata que reconoce secuencias que terminan en '01'
def accepts_01(text):
    state = "q0"
    transitions = {
        ("q0","0"):"q1", ("q0","1"):"q0",
        ("q1","0"):"q1", ("q1","1"):"q2",
        ("q2","0"):"q1", ("q2","1"):"q0",
    }
    for symbol in text:
        state = transitions[(state, symbol)]
    return state == "q2"

for seq in ("1101", "1110", "0001"):
    print(seq, "aceptada:", accepts_01(seq))
