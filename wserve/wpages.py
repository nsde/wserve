wmap = {}

def wpage(path: str):
    def decorator(func):
        wmap[path] = func()
    return decorator
