# Practica_4
**Practica 4 Django y REST, only for students!**   
- URL de despliegue: http://practicadevops.areswolf.com  
- DB: MySQL: only for students
- Se utiliza gunicorn como servidor de aplicación, y circus como gestor de procesos para que siempre esté en ejecución.    
- Se utiliza nginx como proxy inverso que se encargua de recibir las peticiones HTTP y derivárselas a gunicorn.    
- Los archivos estáticos de la aplicación (imágenes, css, etc.) son servidos por nginx con la cabecera **X-Served-From:areswolf**     
- *NOTA: en practicadevops.areswolf.com/node-kc se pasa a la aplicación node, 100% rest*      


 
