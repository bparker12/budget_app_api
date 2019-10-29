from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import action
from budgetappapi.models import Budgeter
from budgetappapi.models import ProjectBudget
from budgetappapi.models import ProjectDepartment
from budgetappapi.models import Department



class ProjectBudgetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectBudget
        url = serializers.HyperlinkedIdentityField(
            view_name='projectbudget',
            lookup_field='id'
        )
        # This fields method is to pull every attribute or piece of data from an instance of a created Model
        fields = ('id', 'url', 'budgeter_id', 'name', 'length')
        depth = 1

class ProjectBudgets(ViewSet):
    def create(self, request):

        project_department = ProjectDepartment()

        project_budget = ProjectBudget()
        project_budget.name = request.data['name']
        project_budget.length = request.data['length']
        budgeter = Budgeter.objects.get(user=request.auth.user)

        project_budget.budgeter = budgeter

        project_budget.save()
        for dept in request.data['dept']:
            project_department.department = Department.objects.get(pk=request.data['id'])
            project_department.project_budget = project_budget

            project_department.save()


            serializer = ProjectBudgetSerializer(project_budget, context={'request': request})

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            project_budget = ProjectBudget.objects.get(pk=pk)
            serializer = ProjectBudgetSerializer(project_budget, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):

        project_budget = ProjectBudget.objects.get(pk=pk)
        project_budget.name = request.data['name']
        project_budget.length = request.data['length']
        budgeter = Budgeter.objects.get(user=request.auth.user)

        project_budget.budgeter = budgeter

        project_budget.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):

        try:
            project_budget = ProjectBudget.objects.get(pk=pk)
            project_budget.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except ProjectBudget.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):

        project_budget = ProjectBudget.objects.all()

        try:
            budgeter = Budgeter.objects.get(user=request.auth.user)
            projects_for_budgeter = ProjectBudget.objects.filter(budgeter_id=budgeter)
        except ProjectBudget.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProjectBudgetSerializer(
            projects_for_budgeter, many=True, context={'request': request})
        return Response(serializer.data)
