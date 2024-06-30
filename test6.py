import inspect

def introspection_info(obj):
    info = {}
    info['type'] = type(obj).__name__
    info['attributes'] = [attr for attr in dir(obj) if not inspect.ismethod(getattr(obj, attr))]
    info['methods'] = [attr for attr in dir(obj) if inspect.ismethod(getattr(obj, attr))]
    info['module'] = inspect.getmodule(obj).__name__ if inspect.getmodule(obj) else 'built-in'
    return info


number_info = introspection_info(42)
print(number_info)