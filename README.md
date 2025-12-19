# Automatizacion

🧠 “Cada vez que copio un archivo .txt a una carpeta llamada entrada, 
quiero que Python lo detecte automáticamente y lo mueva a otra carpeta
llamada procesados sin que yo haga nada.”🖊️💫
❌ Sin Watchdog:
Tendrías que revisar la carpeta manualmente
Ejecutar scripts una y otra vez
✅ Con Watchdog:
Python “vigila” la carpeta 24/7
Reacciona solo cuando aparece un archivo nuevo
🧠 CONCEPTOS QUE APRENDES AQUÍ
Eventos del sistema de archivos
Programas que esperan eventos
Automatización en tiempo real
📦 INSTALACIÓN
pip install watchdog
## Problema	                          Solución
Detectar archivos nuevos	           Watchdog
Evitar revisar carpetas manualmente	 Observer
Automatizar tareas repetitivas	     Eventos
Programas que “esperan”        	  while + observer
