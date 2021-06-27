import requests

#define params
loc = input("Qual local deseja encontrar? ")
loctype = 'textquery'
fields = 'photos,formatted_address,name,rating,opening_hours,geometry,place_id'
#HOW TO GET A KEY: 'https://developers.google.com/maps/documentation/places/web-service/get-api-key?hl=pt-br'
key = '//SET YOUR OWN KEY FROM GOOGLE CLOUD//'

params_search = {'input': loc, 'inputtype': loctype, 'fields': fields, 'key': key}

#Place Search
url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json'
r = requests.get(url, params = params_search)
response = r.json()['candidates'][0]

print("Nome: {}\nEndereço: {}".format(response['name'], response['formatted_address']))

#Place Details
url = 'https://maps.googleapis.com/maps/api/place/details/json'
params_detail = {'place_id': response['place_id'], 'fields': 'formatted_phone_number,opening_hours/weekday_text,website', 'key': key}
r = requests.get(url, params = params_detail)
response = r.json()['result']

try:
    print("Contato: {}\nWebsite: {}".format(response['formatted_phone_number'], response['website']))
except:
    print("Sem informações de contato!")
try:
    op_h = response['opening_hours']
    print('Aberto em:')
    for each in op_h['weekday_text']:
        print('\t{}'.format(each))
except:
    print('Sem informações de horário de funcionamento')




