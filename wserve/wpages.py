wmap = {}

def wpage(path: str, pretty=False):
    def decorator(func):
        outp = str(func())
        
        if pretty:
            with open('wserve/templates/base.html', 'r') as f:
                base_html = f.read()

            html = base_html.replace('{{ content | safe }}', outp)
        else:
            html = outp

        wmap[path] = html
    return decorator
