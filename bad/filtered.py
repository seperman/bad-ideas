def filtered(func, iterable):
    """
    filtered was originally a subclass of filter in the bad ideas package.
    However it made the iterator exhaust.
    I never imagined somebody would actually try to use it but they did.
    https://github.com/seperman/bad-ideas/issues/1
    So instead we are just returning a filter result converted to list.
    It is not as interesting/weird of solution as subclassing a built-in function
    but it does the job.
    """
    return list(filter(func, iterable))
