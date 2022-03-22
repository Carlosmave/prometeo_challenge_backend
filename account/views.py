import requests, json
from rest_framework.views import APIView
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime

class ProviderView(APIView):

    def get(self, request):
        headers = {"X-API-Key": settings.PROMETEO_API_KEY}
        key = request.query_params.get('key', None)
        if key:
            provider = request.query_params.get('provider', None)
            response = requests.get("{}provider/{}/?key={}".format(settings.PROMETEO_API_URL, provider, key), headers = headers)
            response_data = json.loads(response.content.decode("ascii"))
            try:
                response_data = response_data["provider"]
                response_data.pop("auth_fields", None)
                response_data.pop("endpoints_status", None)
                return Response(response_data)
            except KeyError:
                return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)
        else:
            response = requests.get("{}provider/".format(settings.PROMETEO_API_URL), headers = headers)
            response_data = json.loads(response.content.decode("ascii"))
            return Response(response_data["providers"])


class ClientView(APIView):

    def get(self, request):
        headers = {"X-API-Key": settings.PROMETEO_API_KEY}
        key = request.query_params.get('key', None)
        response = requests.get("{}client/?key={}".format(settings.PROMETEO_API_URL, key), headers = headers)
        response_data = json.loads(response.content.decode("ascii"))
        try:
            response_data = response_data["clients"]
            # response_data = {
            #     "0": "First Client",
            #     "1": "Second Client"
            #   }
            return Response(response_data)
        except KeyError:
            return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)


class AccountView(APIView):

    def get(self, request):
        headers = {"X-API-Key": settings.PROMETEO_API_KEY}
        key = request.query_params.get('key', None)
        response = requests.get("{}account/?key={}".format(settings.PROMETEO_API_URL, key), headers = headers)
        response_data = json.loads(response.content.decode("ascii"))
        try:
            response_data = response_data["accounts"]
            return Response(response_data)
        except KeyError:
            return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)


class CreditCardView(APIView):

    def get(self, request):
        headers = {"X-API-Key": settings.PROMETEO_API_KEY}
        key = request.query_params.get('key', None)
        response = requests.get("{}credit-card/?key={}".format(settings.PROMETEO_API_URL, key), headers = headers)
        response_data = json.loads(response.content.decode("ascii"))
        try:
            response_data = response_data["credit_cards"]
            return Response(response_data)
        except KeyError:
            return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)

class ProfileView(APIView):

    def get(self, request):
        headers = {"X-API-Key": settings.PROMETEO_API_KEY}
        key = request.query_params.get('key', None)
        response = requests.get("{}info/?key={}".format(settings.PROMETEO_API_URL, key), headers = headers)
        response_data = json.loads(response.content.decode("ascii"))
        try:
            response_data = response_data["info"]
            return Response(response_data)
        except KeyError:
            return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)

class MovementView(APIView):

    def get(self, request):
        headers = {"X-API-Key": settings.PROMETEO_API_KEY}
        key = request.query_params.get('key', None)
        currency = request.query_params.get('currency', None)
        date_start = datetime.strptime(request.query_params.get('date_start', None), "%Y-%m-%d").strftime("%d/%m/%Y")
        date_end = datetime.strptime(request.query_params.get('date_end', None), "%Y-%m-%d").strftime("%d/%m/%Y")
        account = request.query_params.get('account', None)
        if account:
            response = requests.get("{}account/{}/movement/?key={}&currency={}&date_start={}&date_end={}".format(settings.PROMETEO_API_URL, account, key, currency, date_start, date_end), headers = headers)
            response_data = json.loads(response.content.decode("ascii"))
        else:
            card_number = request.query_params.get('card_number', None)
            response = requests.get("{}credit-card/{}/movements?key={}&currency={}&date_start={}&date_end={}".format(settings.PROMETEO_API_URL, card_number, key, currency, date_start, date_end), headers = headers)
            response_data = json.loads(response.content.decode("ascii"))
        try:
            response_data = response_data["movements"]
            return Response(response_data)
        except KeyError:
            return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)


class TransferDestinationView(APIView):

    def get(self, request):
        headers = {"X-API-Key": settings.PROMETEO_API_KEY}
        key = request.query_params.get('key', None)
        response = requests.get("{}transfer/destinations?key={}".format(settings.PROMETEO_API_URL, key), headers = headers)
        response_data = json.loads(response.content.decode("ascii"))
        try:
            response_data = response_data["destinations"]
            return Response(response_data)
        except KeyError:
            return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)


class TransferenceView(APIView):

    def post(self, request):
        headers = {"X-API-Key": settings.PROMETEO_API_KEY}
        key = request.query_params.get('key', None)
        confirm = request.query_params.get('confirm', None)
        if confirm:
            data = {'request_id': request.data["request_id"], 'authorization_type': '',
            'authorization_data': '', 'authorization_device_number': ''}
            response = requests.post("{}transfer/confirm?key={}".format(settings.PROMETEO_API_URL, key), headers = headers, data = data)
            response_data = json.loads(response.content.decode("ascii"))
            try:
                response_data = response_data["transfer"]
                return Response(response_data)
            except KeyError:
                return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)
        else:
            data = {'origin_account': request.data["origin_account"]["number"], 'destination_institution': request.data["destination_institution"]["id"],
            'destination_account': request.data["destination_account"]["number"], 'currency': request.data["currency"]["code"], 'amount': request.data["amount"],
            'concept': request.data["concept"], 'destination_owner_name': request.data["destination_owner_name"], 'branch': ''}
            response = requests.post("{}transfer/preprocess?key={}".format(settings.PROMETEO_API_URL, key), headers = headers, data = data)
            response_data = json.loads(response.content.decode("ascii"))
            try:
                response_data = response_data["result"]
                return Response(response_data)
            except KeyError:
                return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)
