from ..base_dir.base import log


class APIError(Exception):
    pass


class NotKnownQuery(APIError):
    def __init__(self):
        super().__init__("The name of the query is not known, sorry")
        log.error("The name of the query is not known, sorry")


class InvalidKey(APIError):
    def __init__(self):
        super().__init__("They key for API is not valid")
        log.error("They key for API is not valid")


class InvalidRecipeApiKey(InvalidKey):
    def __init__(self):
        super().__init__()
        log.error("Specifically, the recipe API key is not valid")


class LimitExceeding(APIError):
    def __init__(self):
        super().__init__()
        log.error("You have exceeded your limit")