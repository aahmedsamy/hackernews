import graphene
from graphene_django import DjangoObjectType

from links.models import Vote


class VoteType(DjangoObjectType):
    class Meta:
        model = Vote

class VoteNode(DjangoObjectType):
    class Meta:
        model = Vote
        interfaces = (graphene.relay.Node,)