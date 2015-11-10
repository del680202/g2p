#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    g2p.py
    ~~~~~~~~
    
    HTTP Proxy Server in Python.
    
    :copyright: (c) 2015 by Terrence Chin.
    :license: BSD, see LICENSE for more details.
"""

import sys
import datetime
import argparse
import requests
import logging
import yaml

from actions.action import *
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from urlparse import urlparse, parse_qs

logger = logging.getLogger(__name__)


class Proxy(object):
    """
    This proxy make GET request be converted to POST request
    """

    def __init__(self, url, actions):
        self.url = url
        self.actions = actions

    def handle(self):
        request = {'url':self.url}
        for action in self.actions:
            request = action.handle(request)
        return requests.post(**request)


class RequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        
        request_path = self.path
        parser = urlparse(request_path)
        params = parse_qs(parser.query)
        url = params.get('url', None)
        if url is not None:
            url = url[0] #['url'] -> 'url'
            logger.info("Forword request:%s" % url)
            proxy = Proxy(url, RequestHandler.actions)
            result = proxy.handle()
            self.send_response(result.status_code)
            if result.headers.get('content-type', False):
                self.send_header('content-type', result.headers.get('content-type'))
            self.end_headers()
            self.wfile.write(result.content)
        else:
            self.send_response(200)
            self.end_headers()
        
    do_POST = do_GET    
    do_PUT = do_GET
    do_DELETE = do_GET


def main():
    parser = argparse.ArgumentParser(
        description='g2p.py --config xxx --port xxx',
        epilog=''
    )
    
    parser.add_argument('--port', default='8899', help='Default: 8899')
    parser.add_argument('--config', default='conf/action.yaml', help='ConfigPath: conf/action.yaml')
    parser.add_argument('--log-level', default='INFO', help='DEBUG, INFO, WARNING, ERROR, CRITICAL')
    args = parser.parse_args()
    
    logging.basicConfig(level=getattr(logging, args.log_level), format='%(asctime)s - %(levelname)s - pid:%(process)d - %(message)s')
    
    port = int(args.port)
    RequestHandler.actions = ActionFactory(args.config).build()
    
    try:
        logger.info("Start server on port=%s" % port)
        server = HTTPServer(('', port), RequestHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
