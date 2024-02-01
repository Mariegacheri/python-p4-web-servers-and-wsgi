#!/usr/bin/env python3
from werkzeug.wrappers import Request,Response

@Request.application
def hello_world(request):
    print (f"This web server is running at {request.remote_addr}")
    return  Response("A WSGI generated response!")

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple("localhost", 8080, application= application)