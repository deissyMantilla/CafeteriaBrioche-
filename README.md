Siga estos pasos para correr el proyecto:

1. Activar el entorno virtual:
* Desde la cmd ingrese a la ruta entVirBrioche2/Scripts
* Ejecute el archivo activate.bat para activar el entorno
* Devuélvase a la carpeta raíz del proyecto (CafeteriaBrioche-)
2. Luego con el entorno virtual activado ejecute los siguientes comandos:
* pip install flask
* pip install flask_mail
* set FLASK_APP=app
* set FLASK_ENV=development
* flask run (luego de ejecutar este comando estará corriendo el servidor en http://127.0.0.1:5000/)

Si por algún motivo presenta inconvenientes al activar el entorno virtual, cree uno nuevo en la carpeta raíz del proyecto con el siguiente comando:
* python -m venv <<nombreEntornoVirtual>>
Luego proceda con el paso 1 mostrado anteriormente.