import requests, json
from rest_framework.views import APIView
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status

class ProviderView(APIView):

    def get(self, request):
        headers = {"X-API-Key": settings.PROMETEO_API_KEY}
        response = requests.get("{}provider/".format(settings.PROMETEO_API_URL), headers = headers)
        response_data = json.loads(response.content.decode("ascii"))
        return Response(response_data["providers"])


class LoginView(APIView):

    def post(self, request):
        headers = {"X-API-Key": settings.PROMETEO_API_KEY, 'Content-Type': 'application/x-www-form-urlencoded'}
        data = {'username': request.data["username"], 'password': request.data["password"], 'provider': request.data["provider"]["code"],
        'type': request.data["type"]}
        response = requests.post("{}login/".format(settings.PROMETEO_API_URL), headers = headers, data = data)
        response_data = json.loads(response.content.decode("ascii"))
        if response.status_code == 200:
            return Response(response_data, status=status.HTTP_200_OK)
        elif response.status_code == 401:
            return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)
        elif response.status_code == 403:
            return Response(response_data, status=status.HTTP_403_FORBIDDEN)

class LogoutView(APIView):

    def post(self, request):
        headers = {"X-API-Key": settings.PROMETEO_API_KEY}
        response = requests.get("{}logout/?key={}".format(settings.PROMETEO_API_URL, request.data["key"]), headers = headers)
        response_data = json.loads(response.content.decode("ascii"))
        return Response(response_data, status=status.HTTP_200_OK)
