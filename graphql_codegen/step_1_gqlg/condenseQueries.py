
import os
import glob
import sys
sys.path.append("..")


gqlgQueriesDir = './output'
mutationsDir = f'{gqlgQueriesDir}/mutations'
queriesDir = f'{gqlgQueriesDir}/queries'
subscriptionsDir = f'{gqlgQueriesDir}/subscriptions'

queriesFilePath = './output/queries.graphql'


def main():
    with open(queriesFilePath, 'w') as outputFile:
        from input import queriesToGenerate
        # Mutations
        for f in glob.glob(f'{mutationsDir}/*.gql'):
            queryName = os.path.splitext(os.path.basename(f))[0]
            if (queryName in queriesToGenerate.mutationsToGenerate):
                with open(f, "r") as infile:
                    content = infile.read()
                    outputFile.write(f'{content}\n\n')

        # Queries
        for f in glob.glob(f'{queriesDir}/*.gql'):
            queryName = os.path.splitext(os.path.basename(f))[0]
            if (queryName in queriesToGenerate.queriesToGenerate):
                with open(f, "r") as infile:
                    content = infile.read()
                    outputFile.write(f'{content}\n\n')

        # Subscriptions
        for f in glob.glob(f'{subscriptionsDir}/*.gql'):
            queryName = os.path.splitext(os.path.basename(f))[0]
            if (queryName in queriesToGenerate.subscriptionsToGenerate):
                with open(f, "r") as infile:
                    content = infile.read()
                    outputFile.write(f'{content}\n\n')


if __name__ == "__main__":
    main()
