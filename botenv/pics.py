import requests
res = requests.get('https://api.thecatapi.com/v1/images/search?limit=50&api_key=live_hsdgsb1mW4QfRrGZt6I0IXfmAecBn5hAqhdcaTJoTr260mR4DwiJ14rdyp62gLI4')
if(res.status_code == 200):
    cats = res.json()
    for cat in cats:
        print(cat["url"])
