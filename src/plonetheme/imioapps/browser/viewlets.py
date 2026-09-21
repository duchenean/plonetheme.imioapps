# -*- coding: utf-8 -*-
"""Viewlets the theme supplies to the iMio applications."""

from imio.helpers.workflow import get_state_infos
from plone.app.layout.viewlets import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class WorkflowState(ViewletBase):
    """Show the workflow state of the context as a badge.

    plonemeeting.core registers this viewlet for the meeting, the item and
    the advice. The badge takes its color from the skin, through the
    --imio-state-<state id> custom properties.
    """

    index = ViewPageTemplateFile("templates/viewlet_workflowstate.pt")

    def state_infos(self):
        return get_state_infos(self.context)
