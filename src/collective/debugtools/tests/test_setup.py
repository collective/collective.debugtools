# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from collective.debugtools.testing import COLLECTIVE_DEBUGTOOLS_INTEGRATION_TESTING  # noqa: E501

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that collective.debugtools is properly installed."""

    layer = COLLECTIVE_DEBUGTOOLS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.debugtools is installed."""
        self.assertTrue(self.installer.is_product_installed(
            'collective.debugtools'))

    def test_browserlayer(self):
        """Test that ICollectiveDebugtoolsLayer is registered."""
        from collective.debugtools.interfaces import (
            ICollectiveDebugtoolsLayer)
        from plone.browserlayer import utils
        self.assertIn(
            ICollectiveDebugtoolsLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_DEBUGTOOLS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstall_product('collective.debugtools')
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if collective.debugtools is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed(
            'collective.debugtools'))

    def test_browserlayer_removed(self):
        """Test that ICollectiveDebugtoolsLayer is removed."""
        from collective.debugtools.interfaces import \
            ICollectiveDebugtoolsLayer
        from plone.browserlayer import utils
        self.assertNotIn(ICollectiveDebugtoolsLayer, utils.registered_layers())
