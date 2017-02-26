# Practica_4
**Practica 4 Django y REST, only for students!**   
- URL de despliegue: http://ec2-52-87-195-215.compute-1.amazonaws.com/   
- DB: MySQL: only for students
- Se utiliza gunicorn como servidor de aplicación, y circus como gestor de procesos para que siempre esté en ejecución.    
- Se utiliza nginx como proxy inverso que se encargua de recibir las peticiones HTTP y derivárselas a gunicorn.    
- Los archivos estáticos de la aplicación (imágenes, css, etc.) son servidos por nginx con la cabecera **X-Served-From:areswolf**    
 
