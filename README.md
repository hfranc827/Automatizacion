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

---
| Problema                            | Solución             |
| ----------------------------------- | -------------------- |
| Detectar archivos nuevos            | Watchdog             |
| Evitar revisar carpetas manualmente | Observer             |
| Automatizar tareas repetitivas      | Eventos              |
| Programas que “esperan”             | `while` + `Observer` |

---
# 🧪 LECCIÓN 2 — TYPER  
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
>>
✅ Archivo movido a procesados/


