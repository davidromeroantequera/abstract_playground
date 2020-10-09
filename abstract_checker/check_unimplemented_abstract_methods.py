import inspect


def check_unimplemented_abstract_methods(module_name: str, property_name: str):
    offending_classes = []
    module = __import__(module_name)
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj):
            prop = getattr(obj, property_name, None)
            if callable(prop) and hasattr(prop, "__isabstractmethod__"):
                offending_classes.append(name)
    return offending_classes
