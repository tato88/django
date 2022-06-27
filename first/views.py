from rest_framework.views import APIView
from rest_framework.response import Response


class FirstView(APIView):
    def get(self, request):
        return Response('Method Get')

    def post(self, request):
        return Response('Method POST')

    def put(self, request):
        return Response('Method PUT')
    def patch(self, request):
        return Response('Method PATCH')

    def delete(self, request):
        return Response('Method DELETE')


class SecondView(APIView):
    def get(self, *args, **kwargs):
        query_params = self.request.query_params.dict()
        print(query_params)
        return Response(query_params)

    def post(self, *args, **kwargs):
        data = self.request.data
        print(data)
        return Response(data)


class ThirdView(APIView):
    def get(self, *args, **kwargs):
        print(kwargs)
        return Response(kwargs)
