from functools import wraps


class Aspect:
    def __init__(self, context=None):
        self.context = context

    def before(self, *args, **kwargs):
        pass

    def after(self, result):
        pass
