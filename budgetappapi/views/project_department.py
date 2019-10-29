from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import action
from budgetappapi.models import ProjectDepartment
from budgetappapi.models import Department
from budgetappapi.models import DepartmentHour
from budgetappapi.models import ProjectBudget


class ProjectDepartmentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ProjectDepartment
        url = serializers.HyperlinkedIdentityField(
            view_name='ProjectDepartment',
            lookup_field='id'
        )
        fields = ('id', 'url', 'department', 'department_hour_id')
        depth = 1


class ProjectDepartments(ViewSet):

    def create(self, request):

        new_project_deptarment = ProjectDepartment()
        department = Department.objects.get(pk=request.data["department_id"])
        project_budget = ProjectBudget.objects.get(pk=request.data["project_budget_id"])
        departmenthours = DepartmentHour.objects.get(pk=request.data['deparmenthours_id'])

        new_project_deptarment.department = department
        new_project_deptarment.project_budget = project_budget
        new_project_deptarment.departmenthours = departmenthours
        new_project_deptarment.save()

        serializer = ProjectDepartmentSerializer(new_project_deptarment, context={'request': request})

        return Response(serializer.data)

    def retrieve(self, request, pk=None):

        try:
            project_department = ProjectDepartment.objects.get(pk=pk)
            serializer = ProjectDepartmentSerializer(project_department, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):

        project_department = ProjectDepartment.objects.get(pk=pk)
        department = Department.objects.get(pk=request.data["department_id"])
        departmenthours = DepartmentHour.objects.get(pk=request.data['deparmenthours_id'])

        department_hours.deparment = department
        department_hours.departmenthours = departmenthours
        project_department.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):

        try:

            project_department = ProjectDepartment.objects.get(pk=pk)
            project_department.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except ProjectDepartment.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):

        project_department = ProjectDepartment.objects.all()

        department = self.request.query_params.get('department', None)
        department_hours = self.request.query_params.get('department_hours', None)


        # if product is not None:
        #     project_department = project_department.filter(product__id=product)
        # if order is not None:
        #     project_department = project_department.filter(order_payment=None)

        serializer = ProjectDepartmentSerializer(
            project_department, many=True, context={'request': request})
        return Response(serializer.data)
