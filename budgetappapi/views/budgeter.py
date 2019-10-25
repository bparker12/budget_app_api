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
        fields = ('id', 'url', 'company', 'user')
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

        # Support filtering Products by user id
        # user_id = self.request.query_params.get('budgeter', None)
        # if user_id is not None:
        #     budgeters = budgeters.filter(user__id=user_id)

        serializer = BudgeterSerializer(
            budgeters, many=True, context={'request': request})
        return Response(serializer.data)