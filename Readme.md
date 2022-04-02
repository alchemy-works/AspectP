## AspectP

- Python AOP

```python
from src import aspect, annotation


class Aspect1(aspect.Aspect):
    def __init__(self, context):
        super().__init__(context)

    def before(self, *args, **kwargs):
        print(f"{self.__class__}, before")

    def after(self, result):
        print(f"{self.__class__}, after")


class Aspect2(aspect.Aspect):
    def __init__(self, context):
        super().__init__(context)

    def before(self, *args, **kwargs):
        print(f"{self.__class__}, before")

    def after(self, result):
        print(f"{self.__class__}, after")


@annotation.annotation(Aspects=[Aspect1, Aspect2])
def foo(name):
    print(f"foo {name}")


foo("are you ok")

```
```console
<class '__main__.Aspect1'>, before
<class '__main__.Aspect2'>, before
foo are you ok
<class '__main__.Aspect2'>, after
<class '__main__.Aspect1'>, after

Process finished with exit code 0
```