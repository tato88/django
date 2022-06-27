from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import ComputerModel
from .serializers import ComputerSerializer


class ComputersListCreateView(APIView):
    def get(self, *args, **kwargs):
        try:
            qs = ComputerModel.objects.all()
            serializer = ComputerSerializer(qs, many=True)
            return Response(serializer.data, status.HTTP_200_OK)
        except Exception as err:
            return Response(err)

    def post(self, *args, **kwargs):
        try:
            data = self.request.data
            # instance = ComputerModel.objects.create(**data)
            serializer = ComputerSerializer(data=data)
            if not serializer.is_valid():
                return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        except Exception as err:
            return Response(err)


class ComputerUpdateRetrieveDestroyView(APIView):
    def get(self, *args, **kwargs):
        try:
            computer_id = kwargs.get('pk')
            if not ComputerModel.objects.filter(pk=computer_id).exists():
                return Response('Computer with dat id NOT FOUND', status.HTTP_404_NOT_FOUND)
            computer = ComputerModel.objects.get(pk=computer_id)
            serializer = ComputerSerializer(computer)
            return Response(serializer.data, status.HTTP_200_OK)
        except Exception as err:
            return Response(err)

    def put(self, *args, **kwargs):
        try:
            data = self.request.data
            pk = kwargs.get('pk')
            if not ComputerModel.objects.filter(pk=pk).exists():
                return Response('Computer with dat id NOT FOUND', status.HTTP_404_NOT_FOUND)

            computer = ComputerModel.objects.get(pk=pk)
            serializer = ComputerSerializer(computer, data)

            # if not serializer.is_valid():
            #     return Response(serializer.errors)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        except Exception as err:
            return Response(err)

    def patch(self, *args, **kwargs):
        try:
            data = self.request.data
            pk = kwargs.get('pk')

            if not ComputerModel.objects.filter(pk=pk).exists():
                return Response('Computer with dat id NOT FOUND', status.HTTP_404_NOT_FOUND)

            computer = ComputerModel.objects.get(pk=pk)
            serializer = ComputerSerializer(computer, data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)

        except Exception as err:
            return Response(err)

    def delete(self, *args, **kwargs):
        try:
            pk = kwargs.get('pk')

            if not ComputerModel.objects.filter(pk=pk).exists():
                return Response('Computer with this id Not Found!', status.HTTP_404_NOT_FOUND)

            computer = ComputerModel.objects.get(pk=pk)
            computer.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as err:
            return Response(err)
