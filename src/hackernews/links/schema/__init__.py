import graphene

from .queries import LinkQuery, VoteQuery
from .mutations import LinkMutation, VoteMutation


class LinksQuery(
    LinkQuery,
    VoteQuery,
    graphene.ObjectType):
    pass


class LinksMutation(
    LinkMutation,
    VoteMutation,
    graphene.ObjectType):
    pass
