import requests
from django.http import JsonResponse

CLIENT_ID = "x0OqkPVhmLlzSblJY7zSAjKGC0rIE2Ziu0dwuUUh"
CLIENT_SECRET = "DyDooaFuY5PTfeFzwh9kTalm2fsYan7jagC5cux7REIEkzGmTMmnc9LHNxzSo6RHNyIRndYMZOHXCkPpdfDiUqeduKtj7Kef8576E7ajsM1hHRHVKeG4A02r7hRRBOid"

def get_token_with_password(request):
    token_url = "http://localhost:8001/o/token/"

    data = {
        "grant_type": "password",
        "username": "admin",       
        "password": "admin",       
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    }

    response = requests.post(token_url, data=data)
    return JsonResponse(response.json())
