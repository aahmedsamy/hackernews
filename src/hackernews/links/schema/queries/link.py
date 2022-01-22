import django_filters
import graphene
from django.db.models import Q
from graphene_django.filter import DjangoFilterConnectionField

from links.models import Link
from links.schema.types import LinkType, LinkNode


# 1
class LinkFilter(django_filters.FilterSet):
    class Meta:
        model = Link
        fields = {
            'url': ['contains'],
            'description': ['contains']
        }


class LinkQuery(graphene.ObjectType):
    links = graphene.List(
        LinkType,
        search=graphene.String(),
        first=graphene.Int(),
        skip=graphene.Int(),
    )
    relay_link = graphene.relay.Node.Field(LinkNode)
    # 5
    relay_links = DjangoFilterConnectionField(LinkNode, filterset_class=LinkFilter)

    def resolve_links(self, info, search=None, first=None, skip=None, **kwargs):
        qs = Link.objects.all()
        if search:
            filter = (
                    Q(url__icontains=search) |
                    Q(description__icontains=search)
            )
            qs = qs.filter(filter)

        if skip:
            qs = qs[skip:]

        if first:
            qs = qs[:first]

        return qs
