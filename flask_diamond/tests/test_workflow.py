# -*- coding: utf-8 -*-
# Flask-Diamond (c) Ian Dennis Miller

from nose.plugins.attrib import attr
from ..utils.testhelpers import GeneralTestCase
from ..models.user import User


class WorkflowTestCase(GeneralTestCase):
    def setUp(self):
        super(ModelTestCase, self).setUp()
        typical_workflow()

    @attr("single")
    def test_user(self):
        "user created in workflow"
        User.add_system_users()

        u = User.find(email='guest')
        assert u
        assert u.email == 'guest'
