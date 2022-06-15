from functools import wraps


def batch_init(Aspects, context):
    res = []
    for Aspect in Aspects:
        a = Aspect(context)
        res.append(a)
    return res


def batch_before(aspects, *args, **kwargs):
    for aspect in aspects:
        aspect.before(*args, **kwargs)


def batch_after(aspects, callable_result, is_reversed):
    if is_reversed:
        aspects = aspects[::-1]

    for aspect in aspects:
        aspect.after(callable_result)


def batch_annotation(Aspects, is_stack=True):
    """
    涉及切面之间依赖的上下文，需要注意切面调用顺序
    """
    def deco(callable_object):
        @wraps(callable_object)
        def _deco(*args, **kwargs):
            context = {"CALLABLE_OBJECT_NAME": callable_object.__name__}
            aspects = batch_init(Aspects, context)
            batch_before(aspects, *args, **kwargs)
            result = callable_object(*args, **kwargs)
            batch_after(aspects, result, is_stack)
            return result
        return _deco
    return deco


def annotation(Aspect):
    def deco(callable_object):
        @wraps(callable_object)
        def _deco(*args, **kwargs):
            context = {"CALLABLE_OBJECT_NAME": callable_object.__name__}
            aspect = Aspect(context=context)
            aspect.before(*args, **kwargs)
            result = callable_object(*args, **kwargs)
            aspect.after(result)
            return result
        return _deco
    return deco


def log_error(logger):
    def _log_error(callable_object):
        @wraps(callable_object)
        def _wrapped_method(*args, **kwargs):
            try:
                return callable_object(*args, **kwargs)
            except Exception as error:
                ee = "logger_error:{}".format(error)
                logger.exception(ee)
                raise error
        return _wrapped_method
    return _log_error

