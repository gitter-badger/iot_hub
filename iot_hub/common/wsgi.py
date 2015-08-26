from eventlet import wsgi
import eventlet

def _get_bind_addr(default_port=None):
    # TODO: Replace the host and port values to dynamic value.
    return ("0.0.0.0", 8080 or default_port)

def get_socket(default_port=None):
    bind_addr = _get_bind_addr(default_port)
    return eventlet.listen(bind_addr)

def parse_request(environ):
    response = {'response': {}}
    method = environ.get('REQUEST_METHOD')
    if method == 'GET':
        response["data"] = "GET\n"
    elif method == 'POST':
        response["data"] = "POST\n"

    return response

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/json')])
    
    return parse_request(environ)

if __name__ == '__main__':

    server_socket = get_socket()

    wsgi.server(server_socket, application)
