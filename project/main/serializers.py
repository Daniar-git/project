from rest_framework import serializers
from .models import Todo
from .constants import StatusType


class TodoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    todo_constant = serializers.SerializerMethodField(read_only=True)


    def get_todo_constant(self, obj):
        return StatusType(obj.todo_status).label


    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        validated_data['todo_status'] = StatusType.NOT_FINISHED
        return super().create(validated_data)



    class Meta:
        model = Todo
        fields = ['id', 'title', 'todo_status', 'created', 'todo_constant']