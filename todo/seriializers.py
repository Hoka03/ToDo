from rest_framework import serializers

from todo.models import ToDO


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDO
        fields = '__all__'
