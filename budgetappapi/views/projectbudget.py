from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import action
from budgetappapi.models import Budgeter
from budgetappapi.models import ProjectBudget
from budgetappapi.models import ProjectDepartment



class ProjectBudgetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectBudget
        url = serializers.HyperlinkedIdentityField(
            view_name='projectbudget',
            lookup_field='id'
        )
        # This fields method is to pull every attribute or piece of data from an instance of a created Model
        fields = ('id', 'url', 'budgeter_id', 'name', 'length', 'projectDepartment_id')
        depth = 1

class ProjectBudgets(ViewSet):
    def create(self, request):
        project_budget = ProjectBudget()
        project_budget.name = request.data['name']
        project_budget.length = request.data['length']
        budgeter = Budgeter.objects.get(user=request.auth.user)
        project_department = ProjectDepartment.objects.get(pk=request.data['project_department_id'])

        project_budget.project_department = project_department
        project_budget.budgeter = budgeter

        project_budget.save()

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
        project_department = ProjectDepartment.objects.get(pk=request.data['project_department_id'])

        project_budget.project_department = project_department
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

        # # Support filtering products by product categories
        # name = self.request.query_params.get('name', None)
        # if name is not None:
        #     product_types = product_types.filter(name__id=name)

        serializer = ProjectBudgetSerializer(
            project_budget, many=True, context={'request': request})
        return Response(serializer.data)
