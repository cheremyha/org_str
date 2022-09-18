from rest_framework import serializers
from .models import Positions, Employees


class PositionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Positions
        fields = ['id', 'position_name', ]


class EmployeesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employees
        fields = [
            'id',
            'position_id',
            'first_name',
            'last_name',
        ]

        