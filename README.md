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
[https://collatz-explorer-mrw...streamlit.app](https://collatz-explorer-mrw...streamlit.app)

---


## ✍️ Autor

Creado por [@notcapi](https://github.com/notcapi) como experimento de visualización matemática e IA.  
