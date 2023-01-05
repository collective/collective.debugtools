# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PLONE_FIXTURE
    PloneSandboxLayer,
)
from plone.testing import z2

import collective.debugtools


class CollectiveDebugtoolsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=collective.debugtools)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.debugtools:default')


COLLECTIVE_DEBUGTOOLS_FIXTURE = CollectiveDebugtoolsLayer()


COLLECTIVE_DEBUGTOOLS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_DEBUGTOOLS_FIXTURE,),
    name='CollectiveDebugtoolsLayer:IntegrationTesting',
)


COLLECTIVE_DEBUGTOOLS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_DEBUGTOOLS_FIXTURE,),
    name='CollectiveDebugtoolsLayer:FunctionalTesting',
)


COLLECTIVE_DEBUGTOOLS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_DEBUGTOOLS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='CollectiveDebugtoolsLayer:AcceptanceTesting',
)
