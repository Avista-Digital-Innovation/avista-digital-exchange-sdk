# Steps to generate GQL Client and Types from GraphQL Schema

Requires npm package gqlg (gql-generator?), and pip3 module ariadne-codegen to be installed.
Current working version is using:
gqlg version == gql-generator@1.0.19
ariadne-codegen version == 0.7.1

1. Place schema.graphql file in ./inputs/
   1. Delete lines with @aws_subscribe
   2. Remove all @aws_* tags
2. cd ./step_1_gqlg 
3. Run ./generate.sh
   1. This will use the gqlg util to generate query strings for all mutations, queries, and subscriptions. 
   2. Script will condense all generated query strings into a single file to be ingested in the next step.
4. cd ./step_2_ariadne
5. Run ./generate.sh
   1. This will use ariadne-codegen to create a GraphQL Client with functions for all queries, mutations, and subscriptions.
