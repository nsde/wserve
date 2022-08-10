import http.server

from pprint import pprint

def whandle(wmap):
    class WHandler(http.server.BaseHTTPRequestHandler):

        def _serve(self, html: str, code: int=200):
            self.send_response(code)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(html, 'utf-8'))                    

        def do_GET(self):
            pprint(self.__dict__)
            for path, html in wmap.items():
                if self.path == path:
                    self._serve(html)
                    return
            self._serve('<h1>Error 404 - Not found.</h1><hr>wServe', 404)

    return WHandler
