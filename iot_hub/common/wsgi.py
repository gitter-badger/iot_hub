from eventlet import wsgi
import eventlet

def get_bind_addr(default_port=None):
    """Return the name or ip address of host and port to bind to."""
    # TODO Replace the host and port values to dynamic value.
    return ("0.0.0.0", "8080" or default_port)

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
    bind_addr = '0.0.0.0'
    port = 8080
    server_socket = eventlet.listen((bind_addr, port))

    wsgi.server(server_socket, application)
