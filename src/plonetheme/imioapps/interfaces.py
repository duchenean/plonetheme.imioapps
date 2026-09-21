# -*- coding: utf-8 -*-
"""Browser layers for the theme.

The base layer is active on every iMio application. Each application also
has its own layer. Register a viewlet or a template on an application
layer to change one application only.
"""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IImioAppsLayer(IDefaultBrowserLayer):
    """Base layer. The default profile installs it."""


class IIaDelibLayer(IImioAppsLayer):
    """Layer for iA.Delib."""


class IGedLayer(IImioAppsLayer):
    """Layer for GED."""
