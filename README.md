The Prancing Pony 
Coderhouse - Proyecto Final

The Prancing Pony es un blog hecho por y para fans de los mundos de fantasía.
Dentro de la taberna, los usuarios podrán crear posteos, editar los mismos, borrarlos, editar la informacion de su perfil, charlar con el resto de usuarios y más!

Autores:
Plana, Mateo
Robledal, Pablo

En terminos generales, Plana se encargó de la AppUsers y la mensajería y Robledal de la AppBlog y la implementacion de CSS. En realidad ambos colaboramos en todos los aspectos del blog pero lo mencionado anteriormente hace referencia al enfoque principal de cada uno.

Enlace al video de muestra:
https://youtu.be/slIFS8aRiWs

Para la realizacion del proyecto implementamos:
Python
Django
Jinja
HTML
CSS
JS

El proyecto está dividido en dos apliaciones:
AppUsers:
    Se encarga de todo lo relacionado con los usuarios en sí, ya sea su registro, inicio de sesion, edicion, etc.
    Las urls dentro de AppUsers son:
        'registro'  #Se encarga del resgitro de los usuarios
        'login' #Se encarga de logear a los usuarios
        'logout' #Se encarga de cerrar sesion de los usuarios
        'editar_perfil/ #Se encarga de editar el perfil de los usuarios
        'borrar_usuario/' #Se encarga de eliminar un usuario junto con su perfil
        'perfil/' #Se encarga de visitar el perfil del usuario
        'editar_contraseña/' #Se encarga de editar la contraseña del usuario
        'usuarios' #Se encarga de listar los usuarios del blog

AppBlog: 
    Se encarga de todo lo relacionado con el funcionamiento del blog. Acá podremos crear y editar posteos, buscar, visitar posteos, leer información acerca de los universos tratados y mucho más.
    Las urls dentro de AppUsers son:
        '' Se encarga de llevarnos al inicio de la pagina
        'nosotros/' Se encarga de mostranos informacion acerca de los autores del blog
        'reglas/' Se encarga de mostrarnos las reglas de la taberna
        'lotr' Se encarga de mostrarnos informacion acerca del universo del Señor de los Anillos
        'mistborn/' Se encarga de mostrarnos informacion acerca del universo de Mistborn
        'narnia/' Se encarga de mostrarnos informacion acerca del universo de Narnia
        'got' Se encarga de mostrarnos informacion acerca del universo de Game of Thrones
        'crear_posteo' Nos permite crear un posteo nuevo
        'editar_posteo/ Nos permite editar un posteo de propia autoria
        'borrar_posteo/ Nos permite borrar un posteo de propia autoria
        'visitar_perfil/ Nos permite visitar el perfil de otro usuario
        'visitar_posteo/ Nos permite visualizar los posteos del blog
        'resultado_busqueda' Se encarga de mostrarnos el resultado de la busqueda ingresada



