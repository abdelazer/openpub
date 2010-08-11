#!/usr/bin/env python
# encoding: utf-8
"""
test_opds_catalog_entry_schema.py

Created by Keith Fahlgren on Tue Jan 12 09:09:01 PST 2010
Copyright (c) 2010 Keith Fahlgre. All rights reserved.
"""

import glob
import logging
import os.path

from nose.tools import *

import helper

log = logging.getLogger(__name__)

class TestOPDSCatalogEntrySchema(object):
    def setup(self):
        self.testfiles_dir = os.path.join(os.path.dirname(__file__), 'files')
        self.schemas_dir = os.path.join(os.path.dirname(__file__), '..')
        self.schema_fn = os.path.join(self.schemas_dir, 'opds_catalog.rng')
        self.validator = helper.RelamesValidator(self.schema_fn)

    def test_xml_entry_files_pass_smoke(self):
        """All valid OPDS Catalog Entry Documents collected for smoketesting should pass Relax NG validation."""
        for xml_fn in glob.glob(self.testfiles_dir + '/entry*.pass.xml'):
            log.debug('Attempting validation of %s' % xml_fn)
            try:
                self.validator.assertValid(xml_fn)
            except helper.DocumentInvalid:
                error_log = self.validator.error_log
                log.warn('Validation errors:\n%s' % error_log)
                raise AssertionError

    def test_xml_entry_files_fail_smoke(self):
        """All invalid OPDS Catalog Entry Documents collected for smoketesting should not pass Relax NG validation."""
        for xml_fn in glob.glob(self.testfiles_dir + '/entry*.fail.xml'):
            log.debug('Attempting to confirm invalidity of of %s' % xml_fn)
            assert_raises(helper.DocumentInvalid, self.validator.assertValid, xml_fn)

