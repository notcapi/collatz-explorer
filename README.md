# 🔢 Collatz Explorer

Esta aplicación explora de forma visual y con ayuda de la inteligencia artificial la famosa **Conjetura de Collatz**.

## 📚 ¿Qué es la conjetura de Collatz?

Es una hipótesis matemática que dice que, si tomas cualquier número natural y aplicas estas reglas:

- Si el número es **par**, lo divides entre 2.
- Si es **impar**, lo multiplicas por 3 y le sumas 1.

Y repites el proceso con el nuevo número...

➡️ **Siempre acabarás llegando al número 1**, sin importar con qué número empieces.

Ejemplo con el 6:

6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1

---

## 💡 ¿Qué hace esta app?

Esta aplicación te permite:

✅ Introducir un número natural y generar su **secuencia de Collatz**.  
✅ Ver cuántos pasos tarda en llegar a 1.  
✅ Saber cuántas veces se ha dividido entre 2 y cuántas veces se ha hecho `3n + 1`.  
✅ Clasificar si la secuencia es **larga o corta** usando inteligencia artificial.  
✅ Mostrar la evolución de la secuencia en un gráfico.  

---

## 🤖 ¿Cómo se usa la IA?

- Se analizan los **primeros 40 pasos** de cada secuencia.
- Se detectan patrones frecuentes (n-gramas de operaciones D y M).
- Se entrena un modelo de regresión logística para predecir si una secuencia será larga o corta **sin tener que calcularla entera**.

---

## 📊 ¿Qué tecnologías usa?

- `Python`
- `Streamlit`
- `scikit-learn`
- `pandas`, `matplotlib`

---

## 🚀 Pruébalo tú mismo

👉 Puedes probar la app en Streamlit aquí:  
[https://collatz-explorer-mrwnv5yscyoscq4hyxvikd.streamlit.app/](https://collatz-explorer-mrwnv5yscyoscq4hyxvikd.streamlit.app/)

---

## ❓ ¿Por qué esta app es relevante?

Aunque la conjetura de Collatz ha sido verificada computacionalmente para billones de números, **nadie ha conseguido demostrar que funcione para todos los casos posibles**.

La comunidad matemática aún no tiene una **demostración general** que garantice que cualquier número natural, sin importar su tamaño, acabará alcanzando el 1.

Esta app no resuelve la conjetura, pero sí:

- Detecta patrones ocultos en las secuencias.
- Clasifica si un número tendrá una secuencia larga o corta **usando IA**.
- Muestra gráficamente la evolución de cada número.
- Analiza cuántas veces se divide o se multiplica por 3 y suma 1.

📌 Todo esto aporta una mirada computacional e intuitiva a un problema todavía abierto.  
Y quién sabe… quizás aquí haya una pista para el futuro.

---

## ✍️ Autor

Creado por [@notcapi](https://github.com/notcapi) como experimento de visualización matemática e IA.  

---

# 🇬🇧 Collatz Explorer (English)

A web app that visualizes and predicts the behavior of the famous **Collatz conjecture** using AI.

---

## 📚 What is the Collatz Conjecture?

It states that for any natural number:

- If it’s even, divide it by 2.
- If it’s odd, multiply by 3 and add 1.

Repeating this will **always reach 1**, no matter the starting number.  
Although tested for trillions of numbers, a general proof **still does not exist**.

---

## 💡 What does this app do?

- Enter any number and generate its Collatz sequence
- Predict whether the sequence is *long* or *short*
- Graph its evolution
- Show how many times it was divided or multiplied
- Let you switch between English and Spanish

---

## ❓ Why is this relevant?

This app brings a new perspective to Collatz using machine learning to **spot patterns early** in the sequence and provide insight into its complexity.

---

## 🎯 Try it now:

👉 [https://collatz-explorer-xxxx.streamlit.app](https://collatz-explorer-xxxx.streamlit.app)

---

## 👤 Author

Developed by [@notcapi](https://github.com/notcapi)
