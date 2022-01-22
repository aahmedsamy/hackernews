import graphene
from graphene_django import DjangoObjectType

from links.models import Link


class LinkType(DjangoObjectType):
    class Meta:
        model = Link


class LinkNode(DjangoObjectType):
    class Meta:
        model = Link
        # 3
        interfaces = (graphene.relay.Node,)
