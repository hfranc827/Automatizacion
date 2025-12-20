# Automatización

🧠 **Idea principal**

> “Cada vez que copio un archivo `.txt` a una carpeta llamada `entrada`,  
> quiero que Python lo detecte automáticamente y lo mueva a otra carpeta  
> llamada `procesados` sin que yo haga nada.”

🖊️💫

---

## ❌ Sin Watchdog

- Tendrías que revisar la carpeta manualmente  
- Ejecutar scripts una y otra vez  

---

## ✅ Con Watchdog

- Python **vigila** la carpeta 24/7  
- Reacciona automáticamente cuando aparece un archivo nuevo  

---

## 🧠 Conceptos que aprendes aquí

- Eventos del sistema de archivos  
- Programas que esperan eventos  
- Automatización en tiempo real  

---

## 📦 Instalación

```bash
pip install watchdog
```
---
| Problema                            | Solución             |
| ----------------------------------- | -------------------- |
| Detectar archivos nuevos            | Watchdog             |
| Evitar revisar carpetas manualmente | Observer             |
| Automatizar tareas repetitivas      | Eventos              |
| Programas que “esperan”             | `while` + `Observer` |

---
#🧪 LECCIÓN 2 — TYPER  
## Crear herramientas de consola profesionales con Python


En esta lección aprendes a transformar **scripts en Python** en **comandos reales de terminal**, como los que usan las herramientas profesionales.

Aquí pasas de ejecutar archivos manualmente a **usar Python como una CLI (Command Line Interface)**.

---

## 🔴 PROBLEMA (muy real)

> “Tengo scripts en Python, pero cada vez tengo que abrir el código y modificar valores a mano.  
> Quiero ejecutar acciones directamente desde la terminal.”

Ejemplos de lo que se quiere lograr:

```bash
python app.py Juan
Hola Juan, bienvenido a Python 🚀

python app.py entrada/datos.txt procesados/
✅ Archivo movido a procesados/
```
---
🧪 LECCIÓN 3 — RICH
Salida bonita, clara y profesional en la terminal

🔴 PROBLEMA (muy común)

“Mi programa funciona, pero la salida en la terminal es fea, desordenada y difícil de leer.”

❌ Con print():

-Texto plano

-Difícil distinguir errores

-No sabes el progreso real

✅ Con Rich:

-Colores

-Tablas

-Barras de progreso

-Errores legibles

🧠 CONCEPTOS QUE APRENDERÁS

-Salida visual en terminal

-Feedback para el usuario

-Programas más fáciles de usar

📦 INSTALACIÓN
pip install rich
---
🧪 EJERCICIO 1 — TEXTO CON COLORES
🎯 OBJETIVO

Mostrar mensajes informativos, éxito y error con colores.
🧠 EXPLICACIÓN

-Rich reemplaza print

-Usa etiquetas tipo HTML

-Hace la lectura inmediata

▶️ Ejecución
python app.py
---
🧪 EJERCICIO 2 — TABLA DE DATOS
🔴 PROBLEMA

“Tengo muchos datos y no quiero imprimirlos línea por línea.”

🧠 QUÉ APRENDISTE

-Organizar información

-Mostrar datos reales

-Hacer la terminal clara

▶️ Ejecución
python app2.py
---
🧪 EJERCICIO 3 — BARRA DE PROGRESO REAL
🔴 PROBLEMA

“Mi script tarda y el usuario no sabe si sigue vivo.”

🧠 EXPLICACIÓN

track() envuelve un loop

Rich muestra el progreso automáticamente.

▶️ Ejecución
python app3.py
---
🧪 EJERCICIO 4 — ERRORES LEGIBLES
🔴 PROBLEMA

“Los errores de Python son difíciles de leer.”

🧠 RESULTADO

-Muestra la línea exacta

-Variables involucradas

-Código resaltado

▶️ Ejecución
python app4.py


🧪 PROYECTO MINI — TYPER + RICH
🎯 OBJETIVO

>Un comando que muestre usuarios en una tabla bonita.

▶️ Ejecución
python app5.py

| Problema           | Solución           |
| ------------------ | ------------------ |
| Salida fea         | Rich               |
| Datos desordenados | Tablas             |
| Procesos largos    | Barras de progreso |
| Errores confusos   | Tracebacks claros  |

