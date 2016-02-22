# -*- coding: utf-8 -*-

import os

from django import dispatch

remove_proposal_file = dispatch.Signal(providing_args=["instance"])
remove_proposal_folder = dispatch.Signal(providing_args=["instance", "ente"])
