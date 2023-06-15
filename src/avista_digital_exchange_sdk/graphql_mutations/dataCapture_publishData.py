from ..gql2.schema_types import DataCapture_publishDataParams, DataCapture_publishDataMutationResult, Mutation

mut = Mutation["dataCapture_publishData"]

query = QueryType()


@query.field('me')
def resolve_me(obj, info: GraphQLResolveInfo) -> MeQueryResult:
    #  implementation to obtain current user
    return mocked_user
