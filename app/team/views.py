from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Team
from .serializers import TeamSerializer
from rest_framework import viewsets, status
from .permissions import IsTeamOwner


# Create your views here.


class TeamViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAuthenticated, IsTeamOwner]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action == 'leave_team':
            return None
        return super().get_serializer_class()

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def leave_team(self, request, pk=None):
        try:
            team = self.get_object()
            user = request.user

            if user == team.owner:
                return Response({'detail': 'The owner cannot leave the team.'}, status=status.HTTP_403_FORBIDDEN)

            if user in team.members.all():
                team.members.remove(user)
                return Response({'detail': 'Successfully left the team.'}, status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'detail': 'You are not a member of this team.'}, status=status.HTTP_400_BAD_REQUEST)

        except Team.DoesNotExist:
            return Response({'detail': 'Team not found.'}, status=status.HTTP_404_NOT_FOUND)



    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def my_own_teams(self, request):
        user_teams = self.queryset.filter(owner=request.user)
        serializer = self.get_serializer(user_teams, many=True)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        user_teams = self.queryset.filter(members=request.user)
        serializer = self.get_serializer(user_teams, many=True)
        return Response(serializer.data)