#View using HTTP request

from django.views import View
class Booklist(View):
    def post(self,request):
        pdb.set_trace()

#View using REST ENDPOINT
from rest_framework.views import APIView
class Booklist(APIView):
    def post(self, request):
        pdb.set_trance()



