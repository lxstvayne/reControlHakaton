from rest_framework import serializers

from users.serializers import UserSerializer
from . import models


class FollowUpSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = models.FollowUp
        fields = ('id',
                  'user',
                  'date',
                  'text',
                  'created',
                  'modified')
        read_only_fields = ('id',
                            'user',
                            'created',
                            'modified')


class FollowUpSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = models.FollowUp
        fields = ('text', 'task')


class TaskSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = ('query',
                  'ticket',
                  'waiting_for',
                  'executor',
                  'status')


class TaskSerializer(serializers.ModelSerializer):
    follow_ups = FollowUpSerializer(many=True, read_only=True)
    executor = UserSerializer()

    class Meta:
        model = models.Task
        fields = ('id',
                  'query',
                  'waiting_for',
                  'executor',
                  'status',
                  'follow_ups')
        read_only_fields = ('id', 'follow_ups',)


class TicketSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = models.Ticket
        fields = ('id',
                  'title',
                  'owner',
                  'description',
                  'status',
                  'closed_date',
                  'created',
                  'updated',
                  'tasks')
        read_only_fields = ('id',
                            'owner',
                            'tasks',
                            'created',
                            'updated',
                            'closed_date')
