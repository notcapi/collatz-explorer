import streamlit as st
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# --- Lógica de Collatz --- #

def collatz_operations(n):
    ops = []
    while n != 1:
        if n % 2 == 0:
            ops.append('D')
            n //= 2
        else:
            ops.append('M')
            n = 3 * n + 1
    return ops

def extract_ngrams(sequence, n=4):
    return [''.join(sequence[i:i+n]) for i in range(len(sequence)-n+1)]

def count_common_patterns(ops, patterns):
    ngram_list = extract_ngrams(ops, 4)
    return sum(ngram_list.count(p) for p, _ in patterns)

def early_pattern_score(n, n_steps=40, patterns=None):
    ops = collatz_operations(n)[:n_steps]
    return count_common_patterns(ops, patterns)

# --- Carga de patrones y modelo --- #

@st.cache_data
def train_classifier():
    pattern_counts = Counter()
    for i in range(1, 1001):
        ops = collatz_operations(i)
        ngrams = extract_ngrams(ops, 4)
        pattern_counts.update(ngrams)

    most_common_ngrams = pattern_counts.most_common(10)

    data = []
    for i in range(1, 1001):
        score = early_pattern_score(i, n_steps=40, patterns=most_common_ngrams)
        steps = len(collatz_operations(i))
        data.append((i, score, steps))

    df = pd.DataFrame(data, columns=['start', 'early_score_40', 'steps'])
    median_steps = df['steps'].median()
    df['long'] = (df['steps'] > median_steps).astype(int)

    X = df[['early_score_40']]
    y = df['long']
    clf = LogisticRegression()
    clf.fit(X, y)

    return clf, most_common_ngrams, median_steps

# --- Interfaz Streamlit --- #

st.title("🔢 Collatz Explorer")
st.markdown("""
La **conjetura de Collatz** es una famosa hipótesis matemática que dice que, si tomas cualquier número natural y aplicas estas reglas:
- Si el número es par, lo divides entre 2.
- Si es impar, lo multiplicas por 3 y le sumas 1.

...eventualmente siempre llegarás al número 1, sin importar con qué número empieces.

---

### 🔎 ¿Qué hace esta app?

Esta app:
- Calcula la secuencia de Collatz para el número que introduzcas.
- Analiza si la secuencia es *corta* o *larga*, según cuánto tarda en llegar a 1.
- Muestra gráficamente cómo evoluciona la secuencia.
- Usa inteligencia artificial para hacer predicciones basadas en los primeros pasos de la secuencia.

""")

st.write("Introduce un número natural y predice si su secuencia será larga o corta.")

n = st.number_input("Número inicial", min_value=1, value=27)

if st.button("Analizar"):
    clf, patterns, mediana = train_classifier()

    ops = collatz_operations(n)
    score = early_pattern_score(n, 40, patterns)
    prediction = clf.predict([[score]])[0]

    st.write(f"🔁 Longitud de la secuencia: {len(ops)} pasos")
    st.write(f"🧠 Early Score (40 pasos): {score}")
    st.write(f"📊 Clasificación: {'LARGA' if prediction == 1 else 'CORTA'} (mediana = {mediana})")

    st.subheader("📈 Evolución de la secuencia")
    val = n
    sequence = [val]
    while val != 1:
        val = val // 2 if val % 2 == 0 else 3 * val + 1
        sequence.append(val)

    st.line_chart(sequence)
