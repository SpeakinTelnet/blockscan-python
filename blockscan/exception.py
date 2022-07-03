class ChainIDError(Exception):
    """
    The connection can't find the chain ID
    """

    pass


class SourceCodeNotVerified(Exception):
    """
    The source code returns as not verified
    """

    pass


class APITokenError(Exception):
    """
    This API Token is not recognized by the provider
    """

    pass


class EndpointError(Exception):
    """
    Raise when the requested endpoint does not exist for this chain
    """

    pass


class OperatorError(Exception):
    """ """


"""
TODO: Source code not verified,
      Incorrect API Token,
      No transaction found
      endpoint does not exist ("Error! Missing Or invalid Action name -- NOTOK")
      Invalid operator (logs)
"""
