import graphene

from links.models import Link
from users.schema.types import UserType


class CreateLink(graphene.Mutation):
    id = graphene.Int()
    url = graphene.String()
    description = graphene.String()
    posted_by = graphene.Field(UserType)


    # 2
    class Arguments:
        url = graphene.String()
        description = graphene.String()

    # 3
    def mutate(self, info, url, description):
        link = Link(url=url, description=description)
        link.save()

        return CreateLink(
            id=link.id,
            url=link.url,
            description=link.description,
        )


# 4
class LinkMutation(graphene.ObjectType):
    create_link = CreateLink.Field()
