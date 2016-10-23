from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from safedrawer.common import *

# Create your views here.
@api_view(['POST', 'GET'])
def alert(request):
	if request.method == 'POST':
		print("data", request.data)
		if test_sms():
			return Response("Test message sent.", status=status.HTTP_202_ACCEPTED)
		else:
			return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
	elif request.method == 'GET':
		return Response("Hello world", status=status.HTTP_202_ACCEPTED)

