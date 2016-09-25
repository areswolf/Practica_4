##Sitio Web
A continuación se detallan las características deseadas:  
**- En la página principal, deberán aparecer los últimos posts publicados por los usuarios.**    
**Hecho:**
----------

- Aparecen paginados de 9 en 9 (3 bloques de 3).
- Aprovechan CSS de la práctica anterior, con alguna corrección y mejora.
- Incluyen filtro por categorías 
- Incluye a la izquierda dos botones, uno para acceder a */blogs/* y otro para */newpost/*
- Incluye a la derecha el nombre de usuario logado (o nada, si no lo está) y accesos a login/registro o bien logout/Cambiar password.
- Toda la parte de gestión de usuario se ha hecho incorporando el módulo **"[Djando Registration Redux](https://django-registration-redux.readthedocs.io/en/latest/)"**      
- Para ello, se ha creado en *templates* una carpeta "registration" con todas las plantillas necesarias.
- Además, ha habido que modificar las URLs por defecto de "Registration" para adecuarse a las especificaciones del ejercicio"
- También ha habido que cambiar el formulario de registro, ya que el modelo *User* se ha extendido mediante el modelo *Profile* en relación 1 a 1 con campos adicionales.
- El proceso de registro se hace con confirmación por email, generando un enlace válido por 7 días para activar al usuario. Para ello, se ha creado una cuenta de gmail específicamente para el ejercicio.
- También por este motivo, y para facilitar el desarrollo, **no se ha hecho la validación de email**.
- Pese a haber botones de "Chats", "Posts" y "Likes", no se lleva ningún control al respecto, ni en backend ni en local. Sin embargo, el botón "Posts" lleva a los **posts del usuario concreto**.
- Tampoco se ha trabajado nada sobre los comentarios de lectores.          


**-En la URL /blogs/, se deberá mostrar un listado de los blogs de los usuarios que hay en la
plataforma.**   
El blog personal de cada usuario, se cargará en la URL /blogs/<nombre_de_usuario>/ donde
aparecerán todos los posts del usuario ordenados de más actual a más antiguo (los últimos
posts primero).
**Hecho:**
----------

- Aparecen paginados de 10 en 10.
- En esta vista, no se filtra por categorías.
- Los botones siguen las reglas de la vista anterior.   
 
**- En la URL /blogs/<nombre_de_usuario/<post_id> se deberá poder ver el detalle de un post.   
- Un post estará compuesto de: título, texto a modo de introducción, cuerpo del post, URL de
imagen o vídeo destacado (opcional), fecha y hora de publicación (para poder publicar un post
en el futuro), categorías en las que se publican (un post puede publicarse en una o varias
categorías). Las categorías deben poder ser gestionadas desde el administrador.      
- Tanto en la página principal como en el blog personal de cada usuario, se deberán listar los
posts con el mismo diseño/layout. Para cada post deberá aparecer el título, la imagen
destacada (si tiene) y el resumen.   
- En la URL /new-post deberá mostrarse un formulario para crear un nuevo post. Para acceder a
esta URL se deberá estar autenticado. En formulario para crear el post deberá identificar al
usuario autenticado para publicar el POST en el blog del usuario.   
- En la URL /login el usuario podrá hacer login en la plataforma   
- En la URL /logout el usuario podrá hacer logout de la plataforma   
- En la URL /signup el usuario podrá registrarse en la plataforma indicando su nombre, apellidos,
nombre de usuario, e-mail y contraseña.**   
**Hecho:**
----------
  - Aparecen paginados de 10 en 10 en las vistas donde hay paginación.
  - Para paginar, se ha incorporado código de terceros. También se ha usado el api **"[Crispy Forms](http://django-crispy-forms.readthedocs.io/en/latest/)"** para mejorar los formularios.
  - Un detalle: los campos **Visibility** y **Status** se han incorporado el último día, puesto que inicialmente no se contemplaron hasta desarrollar la parte REST. Por ello, no hay una buena adaptación al uso de los mismos en la web.
  - Otro detalle: por cuestiones de agenda, los TEMPLATES no están 100% optimizados, y los accesos a la DDBB tampoco, por lo que, aunque la aplicación se ajuste a lo pedido por el enunciado, requeriría de refactorización de bastantes apartados.
  - Sí se han aplicado **validadores**, **autorización** y **autenticación**, para ajustarse al p`lanteamiento del ejercicio de forma solvente.
  - Se han creado 3 *APPS*, una llamada **users**, donde se gestionan los *usuarios-blogs*, y otra llamada **blog** donde se gestionan los *posts*. La tercera es **files**, para gestión de uploads.  
  - Cada una tiene sus URL´s, templates, etc.

##API REST
Además del sitio web, se desea implementar un API REST que permita en un futuro desarrollar
una app móvil para que los usuarios puedan gestionar sus blogs desde la app móvil.
La app móvil deberá tener los siguientes **endpoints**:
###API de usuarios
- Endpoint que permita a cualquier usuario registrarse indicando su nombre, apellidos, nombre de
usuario, e-mail y contraseña. **¡HECHO!**  
- Endpoint que permita ver el detalle de un usuario. Sólo podrán ver el endpoint de detalle de un
usuario el propio usuario o un administrador.   **¡HECHO!**  
- Endpoint que permita actualizar los datos de un usuario. Sólo podrán usar el endpoint de un
usuario el propio usuario o un administrador.  **¡HECHO!**
- Endpoint que permita eliminar un usuario (para darse de baja). Sólo podrán usar el endpoint de
un usuario el propio usuario o un administrador.  **¡HECHO!**
###API de blogs
- Un endpoint que no requiera autenticación y devuelva el listado de blogs que hay en la
plataforma con la URL de cada uno. Este endpoint debe permitir buscar blogs por el nombre del
usuario y ordenarlos por nombre.  **¡HECHO!**
###API de posts
- Un endpoint para poder leer los artículos de un blog de manera que, si el usuario no está
autenticado, mostrará sólo los artículos publicados. Si el usuario está autenticado y es el
propietario del blog o un administrador, podrá ver todos los artículos (publicados o no). En este
endpoint se deberá mostrar únicamente el título del post, la imagen, el resumen y la fecha de
publicación. Este endpoint debe permitir buscar posts por título o contenido y ordenarlos por
título o fecha de publicación. Por defecto los posts deberán venir ordenados por fecha de
publicación descendente.   **¡HECHO!**
- Un endpoint para crear posts en el cual el usuario deberá estar autenticado. En este endpoint el
post quedará publicado automáticamente en el blog del usuario autenticado.  **¡HECHO!**
- Un endpoint de detalle de un post, en el cual se mostrará toda la información del POST. Si el
post no es público, sólo podrá acceder al mismo el dueño del post o un administrador.  **¡HECHO!**
- Un endpoint de actualización de un post. Sólo podrá acceder al mismo el dueño del post o un
administrador.  **¡HECHO!**
- Un endpoint de borrado de un post. Sólo podrá acceder al mismo el dueño del post o un
administrador.  **¡HECHO!**   
- NOTA: no se han implementado viewsets, y tampoco el "ordering" estándar de Rest Api. El filtering se ha implementado "a mano", es decir, recibiendo el parámetro en la url y creardo el queryset correspondiente. El objetivo de hacerlo así es poner algo más de dificultad en el ejercicio, más allá de habilitar los Filter y Search back ends que trae el Api Rest de forma estándar.
##Extras opcionales
###General
- Personalizar el administrador de Django para que la plataforma sea más fácil de administrar
pudiendo filtrar posts por categorías y mostrando los mismos datos que en el listado del API
como columnas en el listado de posts. Personalizar también la página de detalle del post.   **¡HECHO!**  
###Página web
- Integrar la página con el look and feel de la práctica de front-end avanzado  **¡HECHO!**
- Dotar de estilos CSS a la página  **¡HECHO!**
- Realizar filtrado por categorías en la página del blog de un usuario  **¡HECHO, + otras!**
- Paginar los posts en la página del blog de un usuario  **¡HECHO!**
###API Rest
- Crear un endpoint para la subida de archivos que pueda ser usado para subir imágenes a la
plataforma para luego utilizarlas como imágenes destacadas.  **¡HECHO!**
- Realizar filtrado por categorías en el endpoint de listado de posts  **¡HECHO!**
- En el API de blogs, mostrar el número de artículos que tiene cada blog  **¡HECHO!**, pero no me convence: lo devuelvo como un campo más en el json del get list, no he averiguado como añadirlo al json en un nivel superior.   
- Mostrar, en un campo ‘autor o author’, el nombre y apellidos del usuario en el endpoint de
listado y detalle de artículos de un blog.  **¡HECHO!**

