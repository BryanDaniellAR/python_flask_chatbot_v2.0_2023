from flask import render_template, request
from utils.training import trainingController
from utils.tienda import tienda_data
from src.Controllers.chatbot import chatbot

def botRoute(app):
    global contador
    contador=0
    @app.route('/get', methods = ['GET'])
    def bot():
        try:
            global contador
            userText = request.args.get('msg')
            data = chatbot(userText,contador)
            contador = data[1]
            return data[0]
        except:
            return render_template("errorBot.html")