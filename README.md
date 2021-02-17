# renamecomputer
App para cambiar los nombres de equipos en una red
Se consume el recurso nativo de Windows renamecomputer por lo que se requieren permisos de administración a nivel local en los equipos a los cuales se requiere hacer el cambio de nombre

Generación de ejecutable (.exe)
Instalar pyinstaller
Una vez parados en el directorio donde estan los archivos del proyecto ejecutar 'pyinstaller --onefile --windowed index.py'
  --onefile generara un solo archivo exe con todos los recursos necesarios para ser ejecutado
  --windowed suprimira la ventana de comandos que se habre para ejecutar un archivo py
