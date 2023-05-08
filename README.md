# Challenge-Mercantil-Andina

Para poder ejecutar el proyecto seguir las siguientes instrucciones 


1- Instalar python


 a) Abrir la URL: https://www.python.org/downloads/ 
 
 b) Descargar e instalar (Importante seleccionar la opcion PIP)
 
2- Validar que esten las siguientes librerias instaladas


  a) Abrir la terminal y ejecutar: pip list
  
  b) Validar existencias de librerias
  
    - selenium
    - pytest
    - webdriver-manager
    - requests
    - assertpy
    - pytest-html
    - pytest-xdist
    
  c) Si no estan las librerias, abrir la terminal y ejecutar:
  
    - pip list
    - pip install selenium
    - pip install pytest
    - pip install webdriver-manager
    - pip install requests
    - pip install assertpy
    - pip install pytest-html
    - pip install pytest-xdist
    
3- Abrir la terminal y ejecutar:

  a) pytest -m ALL -v --capture=sys     | Ejecuta todas las pruebas (API, FE Mercantil Andina, FE Provincia Seguros)
  
  b) pytest -m API -v --capture=sys     | Ejecuta las pruebas de API
  
  c) pytest -m FRONT -v --capture=sys   | Ejecuta las pruebas de FE
  
  d) pytest -m MA -v --capture=sys      | Ejecuta las pruebas de FE Mercantil Andina
  
  e) pytest -m PROV -v --capture=sys    | Ejecuta las pruebas de FE Provincia Seguros
  
 4- Para ver el reporte de las pruebas hay que abrir con un browser el ultimo archivo generado en la carpeta "report\carpeta(FECHA DE EJECUCION)\reporte(ULTIMA FECHA DE EJECUCION)
