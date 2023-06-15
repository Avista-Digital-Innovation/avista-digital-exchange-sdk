# Create queries.graphql
# Need to comment out @aws_subscribe lines in schema.graphql
gqlg --schemaFilePath ../input/schema.graphql --destDirPath ./output/ --depthLimit 200;
python3 condenseQueries.py;

# Regex to match all non @aws_lambda types, inputs, and enums
# (type ((?!aws_lambda|Mutation|Query|Schema|S3Object|Subscription).)*{(.|\n)*?}){1}|(enum ((?!aws_lambda).)*{(.|\n)*?}){1}|(input ((?!aws_lambda).)*{(.|\n)*?}){1}