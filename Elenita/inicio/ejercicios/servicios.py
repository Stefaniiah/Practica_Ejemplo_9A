import requests

def solicitar():
    response = requests.get('https://reqres.in/api/users')
    if response.status_code == 200:
        respuesta = response.json()
        return respuesta.get('data')
    return ''


def obtener_mensaje():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        respuesta = response.json()
        return respuesta[:5] 
    return ''


