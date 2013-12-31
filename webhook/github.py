import requests

def url_for(request):
    return 'https://api.github.com/' + request

def hook_cidrs():
    r = requests.get(url_for('meta'))
    data = r.json()
    return data['hooks']
