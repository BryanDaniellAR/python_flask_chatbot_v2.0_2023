import random
def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    result = None
    value = None
    for i in list_of_intents:
        if(i['tag']== tag):
            value=i['tag']
            result = random.choice(i['responses'])
            break
     # Si no se encontró una respuesta en la intención específica, usar la intención "noanswer"
    if result is None:
        for i in list_of_intents:
            if i['tag'] == 'noanswer':
                value=i['tag']
                result = random.choice(i['responses'])
                break
    return [value,result]