import pandas as pd
from collections import Counter
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# ---------- Funciones auxiliares ---------- #

def collatz_operations(n):
    """Devuelve la secuencia de operaciones Collatz (M para impar, D para par)"""
    ops = []
    while n != 1:
        if n % 2 == 0:
            ops.append('D')  # Divide entre 2
            n //= 2
        else:
            ops.append('M')  # Multiplica por 3 y suma 1
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

# ---------- Paso 1: Obtener los patrones más frecuentes ---------- #

pattern_counts = Counter()
for i in range(1, 1001):
    ops = collatz_operations(i)
    ngrams = extract_ngrams(ops, 4)
    pattern_counts.update(ngrams)

most_common_ngrams = pattern_counts.most_common(10)

# ---------- Paso 2: Calcular los early scores y pasos ---------- #

early_scores_40 = []
for i in range(1, 1001):
    score = early_pattern_score(i, n_steps=40, patterns=most_common_ngrams)
    full_steps = len(collatz_operations(i))
    early_scores_40.append((i, score, full_steps))

df = pd.DataFrame(early_scores_40, columns=['start', 'early_score_40', 'steps'])

# ---------- Paso 3: Clasificación (larga si pasa la mediana) ---------- #

median_steps = df['steps'].median()
df['long'] = (df['steps'] > median_steps).astype(int)

X = df[['early_score_40']]
y = df['long']

# ---------- Paso 4: Entrenamiento y evaluación ---------- #

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = LogisticRegression()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

report = classification_report(y_test, y_pred)

# ---------- Resultados ---------- #

print(f"Mediana de pasos: {median_steps}")
print("\nReporte de clasificación:\n")
print(report)
