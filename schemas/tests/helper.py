#!/usr/bin/env python
# encoding: utf-8
"""
helper.py

Created by Keith Fahlgren on Tue Jan 12 10:09:59 PST 2010
Copyright (c) 2010 Keith Fahlgren. All rights reserved.
"""

import subprocess 

class DocumentInvalid(Exception):
    """Exception raised by a failing validation pass by the RelamesValidator."""
    pass

class RelamesValidator(object):
    """Attempt embedded-schematron validation of Relax NG files"""
    def __init__(self, schema_fn):
        self.schema_fn = schema_fn

    def assertValid(self, xml_fn):    
        cmd = ['msv', self.schema_fn, xml_fn]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, errors = p.communicate()
        if 'NOT valid' in output:
            self.error_log = errors
            raise DocumentInvalid()

