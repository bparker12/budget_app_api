from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import action
from budgetappapi.models import DepartmentHours


class DepartmentHoursSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = DepartmentHours
        url = serializers.HyperlinkedIdentityField(
            view_name='departmenthours',
            lookup_field='id'
        )
        fields = ('id', 'url', 'created_at', 'hours_worked')


class DepartmentHoursClass(ViewSet):

    def create(self, request):

        new_department_hours = DepartmentHours()
        new_department_hours.hours = request.data['hours']


        new_department_hours.save()

        serializer = DepartmentHoursSerializer(new_department_hours, context={'request': request})

        return Response(serializer.data)

    def retrieve(self, request, pk=None):

        try:
            department_hours = DepartmentHours.objects.get(pk=pk)
            serializer = DepartmentHoursSerializer(department_hours, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):

        department_hours = DepartmentHours.objects.get(pk=pk)
        new_department_hours.hours = request.data['hours']

        department_hours.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):

        try:
            department_hours = DepartmentHours.objects.get(pk=pk)
            department_hours.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except DepartmentHours.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def list(self, request):

        department_hours = DepartmentHours.objects.all()

        serializer = DepartmentHoursSerializer(
            department_hours, many=True, context={'request': request})
        return Response(serializer.data)