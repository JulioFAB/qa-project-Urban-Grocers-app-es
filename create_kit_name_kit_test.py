import sender_stand_request
import data

def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

def positive_assert(kit_body):
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 201
    assert kit_response.json()['name'] == kit_body ['name']



def negative_assert(kit_body):
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 400

#Prueba1
def test_numero_de_caracteres_1():
    positive_assert(data.prueba_1)


#Prueba2
def test_numero_de_caracteres_2():
    positive_assert(data.prueba_2)

#Prueba3
def test_numero_de_caracteres_3():
    negative_assert(data.prueba_3)

#Prueba4
def test_numero_de_caracteres_4():
    negative_assert(data.prueba_4)
#Prueba5
def test_numero_de_caracteres_5():
    positive_assert(data.prueba_5)

#Prueba6
def test_numero_de_caracteres_6():
    positive_assert(data.prueba_6)

#Prueba7
def test_numero_de_caracteres_7():
    positive_assert(data.prueba_7)

#Prueba8
def test_numero_de_caracteres_8():
    negative_assert(data.prueba_8)

#Prueba9
def test_numero_de_caracteres_9():
    negative_assert(data.prueba_9)
