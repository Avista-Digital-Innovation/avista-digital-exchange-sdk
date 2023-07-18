FILE=../step_1_gqlg/output/queries.graphql
if [ -f "$FILE" ]; then
    echo "$FILE exists. Running ariadne-codegen command.";
    # ariadne-codegen;
else 
    echo "$FILE does not exist. You must first run step_1_gqlg/generate.sh. This should generate files in directory ../step1_gqlg/output/";
    exit 1
fi
