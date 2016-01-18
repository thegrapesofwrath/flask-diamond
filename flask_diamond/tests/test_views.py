# -*- coding: utf-8 -*-
# Flask-Diamond (c) Ian Dennis Miller

from nose.plugins.attrib import attr
from flask_diamond.utils.testhelpers import GeneralTestCase


class ViewTestCase(GeneralTestCase):
    def test_login(self):
        rv = self.client.get('/login')
        assert 'Flask-Diamond' in rv.data

    def test_index(self):
        rv = self.client.get('/', follow_redirects=True)
        assert 'Flask-Diamond' in rv.data
