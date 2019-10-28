from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import action
from budgetappapi.models import Department


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for park areas

    Arguments:
        serializers
    """
    class Meta:
        model = Department
        url = serializers.HyperlinkedIdentityField(
            view_name='department',
            lookup_field='id'
        )
        fields = ('id', 'url', 'name', 'quantity', 'rate')

class Departments(ViewSet):

    def create(self, request):

        for info in request.data:

            new_department = Department()
            new_department.name = info["name"]
            new_department.rate = info["rate"]
            new_department.quantity = info["quantity"]

            new_department.save()

            serializer = DepartmentSerializer(new_department, context={'request': request})

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            department = Department.objects.get(pk=pk)
            serializer = DepartmentSerializer(department, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):

        department = Department.objects.get(pk=pk)
        department.name = request.data["name"]
        department.rate = request.data["rate"]
        department.quantity = request.data["quantity"]
        department.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        try:
            department = Department.objects.get(pk=pk)
            department.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except department.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):

        department = Department.objects.all()

        serializer = DepartmentSerializer(
            department, many=True, context={'request': request})
        return Response(serializer.data)