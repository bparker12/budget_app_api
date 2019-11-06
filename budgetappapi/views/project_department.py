from django.http import HttpResponseServerError
from django.db.models import OuterRef
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import action
from budgetappapi.models import ProjectDepartment
from budgetappapi.models import Department
from budgetappapi.models import DepartmentHour
from budgetappapi.models import ProjectBudget
from budgetappapi.models import Budgeter
from .department import DepartmentSerializer
from .projectbudget import ProjectBudgetSerializer
from .derpartmenthours import DepartmentHoursSerializer


class ProjectDepartmentSerializer(serializers.HyperlinkedModelSerializer):

    department = DepartmentSerializer(many=False)
    project_budget = ProjectBudgetSerializer(many=False)
    department_hour = DepartmentHoursSerializer(many=False)

    class Meta:
        model = ProjectDepartment
        url = serializers.HyperlinkedIdentityField(
            view_name='ProjectDepartment',
            lookup_field='id'
        )
        fields = ('id', 'url', 'department', 'department_hour', 'project_budget', 'weekly_cost', 'monthly_cost', 'total_cost', 'budgeted_monthly_hours', 'project_length_remaining', 'actual_monthly_cost', 'monthly_dif', 'actual_project_cost', 'project_diff')
        depth = 1


class ProjectDepartments(ViewSet):

    def create(self, request):

        new_project_deptarment = ProjectDepartment()
        department = Department.objects.get(pk=request.data["department.id"])
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
            budget_id = project_department.project_budget
            dept_hour = project_department.department_hour


            project_department.delete()

            checked_department = ProjectDepartment.objects.filter(project_budget_id = budget_id)


            if dept_hour:
                department_hours = DepartmentHour.objects.get(pk=dept_hour.id)
                department_hours.delete()
                if checked_department:
                    return Response({}, status=status.HTTP_204_NO_CONTENT)
                else:
                    project_budget = ProjectBudget.objects.get(pk=budget_id.id)

                    project_budget.delete()
                    return Response({}, status=status.HTTP_204_NO_CONTENT)
            else:
                if checked_department:
                    return Response({}, status=status.HTTP_204_NO_CONTENT)
                else:
                    project_budget = ProjectBudget.objects.get(pk=budget_id.id)

                    project_budget.delete()
                    return Response({}, status=status.HTTP_204_NO_CONTENT)



        except ProjectDepartment.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
                return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):

        budgeter = Budgeter.objects.get(user=request.auth.user)
        project_department = ProjectDepartment.objects.all()

        projectId = self.request.query_params.get('project_budget', None)
        project_dept_id = self.request.query_params.get('project_department', None)

        if projectId is not None:
            project_department = project_department.filter(project_budget_id=projectId)

        if project_dept_id is not None:
            project_department = project_department.filter(id=project_dept_id)


        serializer = ProjectDepartmentSerializer(
            project_department, many=True, context={'request': request})
        return Response(serializer.data)
