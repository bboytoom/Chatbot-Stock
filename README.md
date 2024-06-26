Ejemplo para implementar un proyecto en flask


## Instrucciones para probar

* Clonar el repositorio de Github
* Ejecuta el siguiente comando para instalar los paquetes
    - pip install -r requirements.txt
* Copia el siguiente archivo *“.env.example”* y lo renombras de la siguiente forma *“.env”*
    - Dentro del documento hay 2 keys que son las variables de entorno
        - ENV: Especifica el ambiente donde se va a trabajar
            - Ambientes de desarrollo soportados por el sistema
                - development
                - testing
                - production
        - DATABASE_URL: Es la URL de la base de datos
            - Formato necesario para la conexión a la base de datos
                - mysql+pymysql://{usuario}:{password}@{host}/{nombre_de_base_de_datos}
* Ejecuta las migraciones del sistema con el siguiente comando
    - flask db upgrade
* Ejecutar el sistema con el siguiente comando
    - python wsgi.py
* Para corroborar que el sistema esta ejecución existe un endpoint llamado *“Test url”* que se encuentra en la colección de postman
    - La colección de postman se encuentra en la carpeta de utilidades del proyecto



## Desarrollado con

* Python
* Mysql



#### Librerias principales

* Flask
* SQLAlchemy
* Marshmallow



## Estructura del proyecto

* logs: Contiene los registros diarios de errores, warnings e información que quisiéramos registrar.
* migrations: Contiene las migraciones para realizar cambios en la estructura de las tablas. Ademas, contiene scripts propios del paquete de migraciones que se utiliza.
* src: Contiene el código fuente del sistema, incluida la función principal donde se ejecuta toda la aplicación.
    - config: Contiene los archivos de configuración de la base de datos, registros de logs.
    - helpers: Contiene funcionalidades que se pueden reutilizar dentro de la aplicación, como el script de lectura del CSV.
    - models: Contiene los modelos de datos de la aplicación necesarios para acceder a la base de datos.
    - routes: Contiene la definición de las URL´s de la API.
    - schemas: Contiene la definición de los esquemas de datos que se utilizan para validación y serialización de la data.
    - views: Contiene clases y/o funciones necesarias para obtener y presentar datos al usuario.
        - decorators: Contiene decoradores utilizados para validar datos y parámetros de las URL.
* tests: Contiene las pruebas unitarias y de integración de la aplicación.
* utilities: Contiene las colecciones de los endpoints, imágenes o otro recurso que necesite el sistema.
