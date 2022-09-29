class Unauthorized(Exception):
    def __init__(self, message="Unauthorized to perform the action"):
        self.message = message
        super().__init__(self.message)


class UnauthorizedException(Exception):
    def __init__(self, message="Unauthorized to perform the action. Possibly from an invalid or expired authentication token."):
        self.message = message
        super().__init__(self.message)


class QueryFailed(Exception):
    def __init__(self, message="The query failed.", error=""):
        self.message = f'{message}\nERROR - Query Result/Error: {error}'
        super().__init__(self.message)


class MutationFailed(Exception):
    def __init__(self, message="The mutation failed.", error=""):
        self.message = f'{message}\nERROR - Mutation Result/Error: {error}'
        super().__init__(self.message)


class SubscriptionFailed(Exception):
    def __init__(self, message="The subscription failed.", error=""):
        self.message = f'{message}\nERROR - subscription Result/Error: {error}'
        super().__init__(self.message)


class ParsingResultError(Exception):
    def __init__(self, message="Error encountered while processing the query result."):
        self.message = message
        super().__init__(self.message)


class MissingDataInResultException(Exception):
    def __init__(self, message="Missing expected data in result."):
        self.message = message
        super().__init__(self.message)


class ServiceTypeNotAvailable(Exception):
    def __init__(self, message="This service type is not yet supported in the SDK."):
        self.message = message
        super().__init__(self.message)


class MissingParameterException(Exception):
    def __init__(self, message="Missing required parameter."):
        self.message = message
        super().__init__(self.message)


class FileNotFoundException(Exception):
    def __init__(self, message="File not found in file system"):
        self.message = message
        super().__init__(self.message)


class FileUploadException(Exception):
    def __init__(self, message="File upload failed"):
        self.message = message
        super().__init__(self.message)


class InvalidParameterException(Exception):
    def __init__(self, message="You passed an invalid type to the function."):
        self.message = message
        super().__init__(self.message)


class InvalidTimestampParameter(Exception):
    def __init__(self, parameterName, timestamp):
        self.message = f'Received invalid timestamp for parameter "{parameterName}": "{timestamp}"'
        super().__init__(self.message)
