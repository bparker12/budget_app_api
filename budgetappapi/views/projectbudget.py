from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import action
from budgetappapi.models import Budgeter
from budgetappapi.models import ProjectBudget



class ProjectBudgetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectBudget
        url = serializers.HyperlinkedIdentityField(
            view_name='projectbudget',
            lookup_field='id'
        )
        # This fields method is to pull every attribute or piece of data from an instance of a created Model
        fields = ('id', 'url', 'budgeter', 'name', 'length', 'projectdepartment')
        depth = 1

    def create(self, request):
        new_product = ProjectBudget()
        new_product.name = request.data['name']
        new_product.length = request.data['length']
        budgeter = Budgeter.objects.get(user=request.auth.user)
        project_department = ProjectBudget.objects.get(pk=request.data['project_department_id'])
        
        new_product.project_department = project_department
        new_product.budgeter = budgeter

        new_product.save()

        serializer = ProjectBudgetSerializer(new_product, context={'request': request})

        return Response(serializer.data)