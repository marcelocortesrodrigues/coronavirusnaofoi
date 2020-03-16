import requests
def noticias():
    url = ('http://newsapi.org/v2/top-headlines?'
       'country=br&'
       'apiKey=710632deea85427c8d50b2a5b8e62ec3')
    req = requests.get(url, timeout=3000)
    vetor = req.json()
    # PERCORRENDO AS NOTÍCIAS
    desejado = ['coronavírus', 'coronavirus', 'Coronavirus', 'Coronavírus', 'Corona', 'Virus', 'virus', 'Abel']
    for c in range(len(vetor)):
        if desejado[c] in vetor:
            print('encontrado')
            print('Notícia ' + str(c + 1))
            print(vetor['articles'][c]['title'])
            print(vetor['articles'][c]['description'])
        else:
            print('não foi')
            print('Notícia ' + str(c + 1))
            print(vetor['articles'][c]['title'])
            print(vetor['articles'][c]['description'])
noticias()

'#br, us'