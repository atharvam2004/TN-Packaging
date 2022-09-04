
'''
import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.dirname(__file__))


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    #message = 'Dr._Aniket, It works!\n'
    #version = 'Python %s\n' % sys.version.split()[0]
    #response = '\n'.join([message, version])
    
    response = f'The Site is Ready To be Launched!\nYou will Soon see the Live Site\nTHANKS FOR VISITING\nTime: {datetime.now()}'
    
    return [response.encode()]
'''

import internship.wsgi as wsgi
application = wsgi.application