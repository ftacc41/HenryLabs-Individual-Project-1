# **PI-01_FRANCO TACCHELLA**


_ PROYECTO INDIVIDUAL Nº1 para Henry_ Diciembre 2022

Data Engineering

## **Introducción**

Mi nombre es Franco Tacchella y el siguiente proyecto fue realizado como parte de la cursada del bootcamp de Data Science propuesto por SoyHenry. 

Puedes ver el programa en https://www.soyhenry.com/carrera-data-science

## **Objetivo de trabajo**

El proyecto consiste en realizar una ingesta de datos desde diversas fuentes, posteriormente aplicar las transformaciones que consideren pertinentes, y luego disponibilizar los datos limpios para su consulta a través de una API. Esta API deberán construirla en un entorno virtual dockerizado.

Los datos serán provistos en archivos de diferentes extensiones, como *csv* o *json*. Se espera que realicen un EDA para cada dataset y corrijan los tipos de datos, valores nulos y duplicados, entre otras tareas. Posteriormente, tendrán que relacionar los datasets así pueden acceder a su información por medio de consultas a la API.

Las consultas a realizar son:

+ Máxima duración según tipo de film (película/serie), por plataforma y por año:

    El request debe ser: get_max_duration(año, plataforma, [min o season])

+ Cantidad de películas y series (separado) por plataforma

    El request debe ser: get_count_plataform(plataforma)  
  
+ Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo.

    El request debe ser: get_listedin('genero')  

    Como ejemplo de género pueden usar 'comedy', el cuál deberia devolverles un cunt de 2099 para la plataforma de amazon.

+ Actor que más se repite según plataforma y año.

  El request debe ser: get_actor(plataforma, año)


## *Trabajo realizado y Criterio**

El primer paso de este proyecto fue realizar el EDA según las consignas propuestas. A partir de esto llego a las conclusiones necesarias para diferenciar la información que es neceseria para el proyecto y la que no.

El segundo paso de este proyecto es realizar la ETL. En este caso utlicé la librerias de Pandas para leer los archivos, dropear columnas innecesarias, agregar algunas que nos faltan, llenar valores nulos y normalizar las tablas. Finalmente las uní en una única tabla con la cual puedo correr las querys.

Es importante aclarar que la limpieza de datos realizada está optimizada para las consultas puntuales que solicita el proyecto y no contempla nada que se salga de esto. 


## **Estructura de Carpetas**

- Datasets
        - archivos raw
- ETL
        - archivo jupyter Notebook 

- csv_limpios
        - content_global.csv 


 Archivos globales: 

-	querys.py 
-	main.py (estructura de API)
-	dockerfile
-	requierments.txt 

## **Herramientas utilizadas:**

        - Python
        - Pandas
        - Docker
        - FastAPI

## **Links de consultas:**
        -https://www.youtube.com/watch?v=BvvH3ohis6E&t=554s
        -
        -
        
