#!/usr/bin/env python
# -*- coding: utf-8 -*-


import logging
import os
import re
import yaml

logger = logging.getLogger(__name__)


class BasicActionHandler(object):

    def do_handle(self, request):
        raise Exception("not yet implemented")

    def handle(self, request):
        if self.match and re.search(self.match, request['url']):
            return self.do_handle(request)
        return request


class BasicAuthenticationAction(BasicActionHandler):

    def __init__(self, config):
        self.user = config['user']
        self.password = config['password']

    def do_handle(self, request):
        request['auth'] = (self.user, self.password)
        return request


class ActionFactory(object):

    def __init__(self, config_path):
        self.config = None
        try:
            with open(config_path, 'r') as f:
                self.config = yaml.load(f.read())
                logger.info("Read action config from %s" % config_path)
        except Exception as e:
            print e.message

    def build(self):
        if self.config is None: return []
        result = []
        for action_name in self.config:
            action_config = self.config[action_name]
            action_type= action_config['type']
            action = eval("%s(action_config)" % (action_type))
            action.match = action_config['match']
            result.append(action)
        return result
