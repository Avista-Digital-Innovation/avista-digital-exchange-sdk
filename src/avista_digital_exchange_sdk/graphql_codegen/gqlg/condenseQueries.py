import os
import glob

gqlgQueriesDir = './output'
mutationsDir = f'{gqlgQueriesDir}/mutations'
queriesDir = f'{gqlgQueriesDir}/queries'
subscriptionsDir = f'{gqlgQueriesDir}/subscriptions'

queriesFilePath = './output/queries.graphql'

with open(queriesFilePath, 'w') as outputFile:
    for dirToCondense in [mutationsDir, queriesDir, subscriptionsDir]:
        for f in glob.glob(f'{dirToCondense}/*.gql'):
            with open(f, "r") as infile:
                outputFile.write(f'{infile.read()}\n\n')
