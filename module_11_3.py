import inspect


def introspection_info(obj):
    obj_type = type(obj).__name__

    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]

    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]

    obj_module = obj.__mod__

    additional_info = {}
    if inspect.isclass(obj):
        additional_info['parent_class'] = obj.__bases__

    return {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module,
        'additional_info': additional_info if additional_info else None
    }

number_info = introspection_info(42)
print(number_info)

string_info = introspection_info("Hello, world!")
print(string_info)

class_info = introspection_info(str)
print(class_info)