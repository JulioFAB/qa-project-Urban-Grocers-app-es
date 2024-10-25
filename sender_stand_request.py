import configuration
import requests
import data


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers
                         )


response = post_new_user(data.user_body).json()
authToken = response['authToken']



headers2= {
   "Content-Type": "application/json",
    "Authorization": f'Bearer{authToken}'
}




#def post_new_client_kit(kit_body):
   # return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
    #                     json = kit_body,
     #                    headers = headers2

    #)

def post_new_client_kit(kit_body):
    response = post_new_user(data.user_body).json()
    authToken = response['authToken']
    headers2= data.headers.copy()
    headers2["Authorization"] = f'Bearer {authToken}'

    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json = kit_body,
                         headers = headers2
    )