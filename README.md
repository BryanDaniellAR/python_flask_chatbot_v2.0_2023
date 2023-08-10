# chatbot_python_v3.9.7_v2.0_2023

ChatBot para una tienda de guitarras llamado "GuitarSound"

# Identificar el nombre del proyecto

* Lenguage programación: Python
* Versión Software: 3.9.7
* Nombre aplicación: chatbot
* Versión aplicación: 2.0
* Año de lanzamiento: 2023

# Ejecución

Paso 1: pip install -r requeriments.txt

Paso (Opcional): Si ha modificado el archivo "resource/training/data.json". Ejecutar el comando: py utils/training.py

> Esto permitira reescribir el modelo para que pueda interactuar con los mismos comandos, en preferencia no modificar los tags a menos modifique el codigo correspondiente.

Paso 2: Ejecutar py app.py

> Si requiere crear el modelo para el chat bot, ejecutar py training.py, utilizara datos del diccionario y lo creara en el archivo modelo

Paso 3: Reconocer modelo, lo que permite realizar "revisar el archivo resource/training/data.json"

- saludo
- ubicacion de la tienda
- productos de la tienda
- horario de atención
- formas de contacto
- informacion de la tienda
- solicitar opciones de lo que puede hacer
- reservar un pedido
- agradecimiento
- despedida
- Responder con "noanswer" al no entender correctamente el mensaje

# Chat Bot

![GuitarSound ChatBot](https://github.com/BryanDaniellAR/python_flask_chatbot_v2.0_2023/assets/97413969/8edb19bc-c764-49ef-ba97-6804d2b59943)
