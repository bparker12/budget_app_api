from django.http import HttpResponseServerError
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from budgetappapi.models import Budgeter


class BudgeterSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = Budgeter
        url = serializers.HyperlinkedIdentityField(
            view_name='budgeter',
            lookup_field='id'
        )
        fields = ('id', 'company', 'user_id')
        depth = 1

class Budgeters(ViewSet):

    def create(self, request):

        new_budgeter = Budgeter()
        new_budgeter.company = request.data["company"]


        new_budgeter.save()

        serializer = BudgeterSerializer(new_budgeter, context={'request': request})

        return Response(serializer.data)

    def retrieve(self, request, pk=None):

        try:
            budgeter = Budgeter.objects.get(pk=pk)
            serializer = BudgeterSerializer(budgeter, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):

        budgeters = Budgeter.objects.all()

        serializer = BudgeterSerializer(
            budgeters, many=True, context={'request': request})
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def currentBudgeter(self, request):

        try:
            budgeter = Budgeter.objects.get(user=request.auth.user)
        except budgeter.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        serializer = BudgeterSerializer(budgeter, context={'request': request})
        return Response(serializer.data)