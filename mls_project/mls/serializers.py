from rest_framework import serializers
from .models import Player, Team


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    team = serializers.HyperlinkedRelatedField(
        view_name='player_detail',
        read_only=True
    )

    class Meta:
        model = Player
        fields = ('id', 'team', 'name', 'age', 'position', 'passes_attempted',
                  'passes_completed', 'tackles', 'goals', 'injured')


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    players = serializers.HyperlinkedRelatedField(
        view_name='team_detail',
        many=True,
        read_only=True)

    class Meta:
        model = Team
        fields = ('id', 'name', 'location', 'division',
                  'wins', 'losses', 'players')
