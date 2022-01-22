import graphene

from links.models import Vote
from links.schema.types import VoteType


class VoteQuery(graphene.ObjectType):
    votes = graphene.List(VoteType)

    def resolve_votes(self, info, **kwargs):
        return Vote.objects.all()
