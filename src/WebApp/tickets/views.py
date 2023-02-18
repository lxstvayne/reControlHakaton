from rest_framework import views, generics, permissions, viewsets

from . import serializers, models


class TicketListCreateView(generics.ListCreateAPIView):
    serializer_class = serializers.TicketSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.Ticket.objects.all()

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class TicketRetrieveView(generics.RetrieveAPIView):
    serializer_class = serializers.TicketSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.Ticket.objects.all()


class TicketStatusesListView(generics.ListAPIView):
    serializer_class = serializers.TicketStatusSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.TicketStatus.objects.all()


class TaskStatusesListView(generics.ListAPIView):
    serializer_class = serializers.TaskStatusSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.TaskStatus.objects.all()


class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = serializers.TaskSerializerPost
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.Task.objects.all()

    def list(self, request, *args, **kwargs):
        # Это плохое решение, потому что в сваггере будет отображаться неправильная схема
        self.serializer_class = serializers.TaskSerializer
        return super().list(request, *args, **kwargs)


class TaskUpdateDestroyView(generics.UpdateAPIView, generics.DestroyAPIView):
    serializer_class = serializers.TaskSerializerPost
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.Task.objects.all()


class FollowUpCreateView(generics.CreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    serializer_class = serializers.FollowUpSerializerPost
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.FollowUp.objects.all()

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
