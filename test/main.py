from src import aspect, annotation


class Aspect1(aspect.Aspect):
    def __init__(self, context):
        super().__init__(context)

    def before(self, *args, **kwargs):
        print(f"{self.__class__}, before")
        name = args[0]

        self.context[self.__class__] = name

    def after(self, result):
        print(f"{self.__class__}, after")


class Aspect2(aspect.Aspect):
    def __init__(self, context):
        super().__init__(context)

    def before(self, *args, **kwargs):
        print(f"{self.__class__}, before")

    def after(self, result):
        print(f"{self.__class__}, self.context:{self.context} after")


@annotation.batch_annotation(Aspects=[Aspect1, Aspect2],)
def foo(name):
    print(f"foo {name}")


foo("are you ok")
