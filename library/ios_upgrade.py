#!/usr/bin/python
# Copyright: Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = """
module:ios_upgrade
author: Kolluru Som Shekhar Sharma
short_description: Running upgrade commands on IOS devices

"""

EXAMPLES = """
- name: Run the upgrade command
  ios_upgrade:
   command: "install add file bootflash:cat9k_iosxe.17.03.03.SPA.bin activate commit"



"""

RETURN = """
"""
