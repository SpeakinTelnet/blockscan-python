import types


class Module:
    @classmethod
    def _add_decorator(cls, decorator):
        for func in dir(cls):
            if not func.startswith("_"):
                obj = getattr(cls, func)
                if isinstance(obj, types.FunctionType):
                    if hasattr(obj, "__wrapped__"):
                        setattr(cls, func, decorator(obj.__wrapped__))
                    else:
                        setattr(cls, func, decorator(obj))
