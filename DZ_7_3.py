documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "polis", "number": "5901"}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

def see_names(documents):
     for doc in documents:
        try:
         print(doc["name"])
        except KeyError:
         print('Владелец документа неизвестен')

see_names(documents)


