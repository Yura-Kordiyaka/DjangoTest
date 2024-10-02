from rest_framework import serializers
from .models import Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id','name', 'members')
        read_only_fields = ('owner',)

    def create(self, validated_data):
        members_data = validated_data.pop('members', [])

        request = self.context.get('request')
        user = request.user if request and request.user.is_authenticated else None

        if user is None:
            raise serializers.ValidationError("User must be authenticated.")

        team = Team.objects.create(owner=user, **validated_data)

        team.members.set(members_data)

        return team

    def update(self, instance, validated_data):
        members_data = validated_data.pop('members', None)

        instance.name = validated_data.get('name', instance.name)
        instance.save()

        if members_data is not None:
            instance.members.set(members_data)

        return instance