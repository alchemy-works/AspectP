

def batch_init(Aspects):
    res = []
    context = {}
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


def annotation(Aspects, is_onion=True):
    def deco(callable_object):
        def _deco(*args, **kwargs):
            aspects = batch_init(Aspects)
            batch_before(aspects, *args, **kwargs)
            result = callable_object(*args, **kwargs)
            batch_after(aspects, result, is_onion)
            return result
        return _deco
    return deco

