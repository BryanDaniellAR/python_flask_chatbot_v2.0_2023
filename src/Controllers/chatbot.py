from utils.predict import predict_class
from utils.response import getResponse
from utils.tienda import tienda_data,new_reserva,new_reserva_nombre,new_reserva_numero,new_reserva_email,new_reserva_producto,new_reserva_cantidad
from keras.backend import *
from keras.models import load_model
import json
import pickle
import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

def chatbot(msg,contador):
    path_dictionary_text = "resource/training/dictionary/texts.pkl"
    path_dictionary_label = "resource/training/dictionary/labels.pkl"
    path_model = "resource/training/model/model.h5"
    path_data_json = "resource/training/data.json"
    path_data_tienda = "resource/tienda/tienda.xlsx"
    words = pickle.load(open(path_dictionary_text,'rb'))
    classes = pickle.load(open(path_dictionary_label,'rb'))
    intents = json.loads(open(path_data_json).read())
    model = load_model(path_model)

    if contador == 0:
        ints = predict_class(nltk,lemmatizer,classes,words,model,msg)
        res = getResponse(ints, intents)
        #data = interativo(msg)
        mensaje = res[1]
        if(res[0]=="tienda_ubicacion"):
            tienda_ubicacion = tienda_data(path_data_tienda,"Ubicacion")
            #list_id_ubicacion = tienda_ubicacion.id.to_list()
            list_descripcion_ubicacion = tienda_ubicacion.descripcion.to_list()
            for i, ubicacion in enumerate(list_descripcion_ubicacion):
                if i == len(list_descripcion_ubicacion) - 1:
                    mensaje += f"{ubicacion}"
                else:
                    mensaje += f"{ubicacion}; "
        elif (res[0]=="tienda_productos"):
            tienda_productos = tienda_data(path_data_tienda,"Productos")
            #list_id_ubicacion = tienda_ubicacion.id.to_list()
            list_name_producto = tienda_productos.producto.to_list()#msg
            list_descripcion_producto = tienda_productos.descripcion.to_list()
            list_costo_producto = tienda_productos.costo.to_list()
            for i, producto in enumerate(list_name_producto):
                if i == len(list_name_producto) - 1:
                    if(msg.__contains__(str("describeme")) or msg.__contains__(str("descripcion")) or msg.__contains__(str("describelas")) or msg.__contains__(str("descripciones"))):
                        mensaje += f"{producto}: {list_descripcion_producto[i]}"
                    elif(msg.__contains__(str("costo")) or msg.__contains__(str("precio")) or msg.__contains__(str("cuanto")) or msg.__contains__(str("costos"))):
                        mensaje += f"{producto}: {list_costo_producto[i]}"
                    else:
                        mensaje += f"{producto}"
                else:
                    if(msg.__contains__(str("describeme")) or msg.__contains__(str("descripcion")) or msg.__contains__(str("describelas")) or msg.__contains__(str("descripciones"))):
                        mensaje += f"{producto}: {list_descripcion_producto[i]}; "
                    elif(msg.__contains__(str("costo")) or msg.__contains__(str("precio")) or msg.__contains__(str("cuanto")) or msg.__contains__(str("costos"))):
                        mensaje += f"{producto}: {list_costo_producto[i]}; "
                    else:
                        mensaje += f"{producto}; "
        elif(res[0]=="tienda_horario"):
            tienda_horario = tienda_data(path_data_tienda,"Horario")
            #list_id_ubicacion = tienda_ubicacion.id.to_list()
            list_descripcion_horario = tienda_horario.horario.to_list()
            for i, horario in enumerate(list_descripcion_horario):
                if i == len(list_descripcion_horario) - 1:
                    mensaje += f"{horario}"
                else:
                    mensaje += f"{horario}; "
        elif(res[0]=="tienda_contacto"):
            tienda_contacto = tienda_data(path_data_tienda,"Contacto")
            #list_id_ubicacion = tienda_ubicacion.id.to_list()
            list_descripcion_contacto = tienda_contacto.contacto.to_list()
            for i, contacto in enumerate(list_descripcion_contacto):
                if i == len(list_descripcion_contacto) - 1:
                    mensaje += f"{contacto}"
                else:
                    mensaje += f"{contacto}; "
        elif(res[0]=="tienda_informacion"):
            tienda_informacion = tienda_data(path_data_tienda,"Informacion")
            #list_id_ubicacion = tienda_ubicacion.id.to_list()
            list_descripcion_informacion = tienda_informacion.descripcion.to_list()
            for i, informacion in enumerate(list_descripcion_informacion):
                if i == len(list_descripcion_informacion) - 1:
                    mensaje += f"{informacion}"
                else:
                    mensaje += f"{informacion}; "
        elif(res[0]=="tienda_reserva"):
            contador = 1
            new_reserva(path_data_tienda,"Reserva")
        return [mensaje,contador]
    elif contador == 1:
        new_reserva_nombre(path_data_tienda,"Reserva",msg)
        mensaje = "Perfecto, ahora prosiga con su numero de contacto."
        contador=2
        return [mensaje,contador]
    elif contador == 2:
        new_reserva_numero(path_data_tienda,"Reserva",msg)
        mensaje = "Perfecto, ahora prosiga con su email."
        contador=3
        return [mensaje,contador]
    elif contador == 3:
        tienda_productos = tienda_data(path_data_tienda,"Productos")
        list_name_producto = tienda_productos.producto.to_list()#msg
        new_reserva_email(path_data_tienda,"Reserva",msg)

        mensaje = "Perfecto, ahora prosiga con el nombre del producto, de los cuales tiene: "
        for i, producto in enumerate(list_name_producto):
            if i == len(list_name_producto) - 1:
                mensaje += f"{producto}"
            else:
                mensaje += f"{producto}; "
        contador=4
        return [mensaje,contador]
    elif contador == 4:
        new_reserva_producto(path_data_tienda,"Reserva",msg)
        mensaje = "Perfecto, ahora prosiga con la cantidad de productos querra."
        contador=5
        return [mensaje,contador]
    elif contador == 5:
        new_reserva_cantidad(path_data_tienda,"Reserva",msg)
        mensaje = "Perfecto, su registro ha finalizado, pagar al numero de cuenta BCP 191-1234566984321 antes de los siguientes 10 dias."
        contador=0
        return [mensaje,contador]
    else:
        return ["",contador]