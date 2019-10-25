from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import action
from budgetappapi.models import DepartmentHour


class DepartmentHoursSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = DepartmentHour
        url = serializers.HyperlinkedIdentityField(
            view_name='departmenthours',
            lookup_field='id'
        )
        fields = ('id', 'url', 'created_at', 'hours_worked')


class DepartmentHours(ViewSet):

    def create(self, request):

        new_department_hours = DepartmentHour()
        new_department_hours.hours = request.data['hours']


        new_department_hours.save()

        serializer = DepartmentHours(new_department_hours, context={'request': request})

        return Response(serializer.data)

    def retrieve(self, request, pk=None):

        try:
            department_hours = DepartmentHour.objects.get(pk=pk)
            serializer = DepartmentHours(department_hours, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):

        department_hours = DepartmentHour.objects.get(pk=pk)
        new_department_hours.hours = request.data['hours']

        department_hours.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):

        try:
            department_hours = DepartmentHour.objects.get(pk=pk)
            department_hours.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except DepartmentHours.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def list(self, request):

        department_hours = DepartmentHour.objects.all()

        serializer = DepartmentHours(
            department_hours, many=True, context={'request': request})
        return Response(serializer.data)