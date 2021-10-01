# (c) 2017, Ansible Project
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#
from __future__ import absolute_import, division, print_function

__metaclass__ = type

import traceback
from time import sleep

from ansible.module_utils._text import to_bytes, to_text
from ansible.module_utils.six import text_type
from ansible.plugins.action import ActionBase
from ansible.utils.display import Display

import re
import paramiko
from paramiko_expect import SSHClientInteraction
display = Display()

def check_if_config(output):
    config_regex = r"System configuration has been modified"
    if re.search(config_regex, output, re.MULTILINE):
        return True
    else:
        return False
def check_if_reload(output):
    config_regex = r"Image added"
    if re.search(config_regex, output, re.MULTILINE):
        return True
    else:
        return False

class ActionModule(ActionBase):
    TRANSFERS_FILES = False

    def run(self, tmp=None, task_vars=None):
        result = super(ActionModule, self).run(tmp, task_vars)
        display.vvvvv(task_vars)
        host = to_text(
            self._task.args.get("host", self._play_context.remote_addr)
        )
        user = to_text(
            self._task.args.get("user", self._play_context.remote_user)
        )
        password = to_text(
            self._task.args.get("password", self._play_context.password)
        )
        module_args = self._task.args.copy()
        command=module_args["command"]

        PROMPT = '(.*)#$'

        try:
            client = paramiko.SSHClient()

            # Set SSH key parameters to auto accept unknown hosts
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            # Connect to the host
            client.connect(hostname=host, username=user, password=password)

            # Create a client interaction class which will interact with the host
            with SSHClientInteraction(client, timeout=10, display=True) as interact:
                interact.expect(PROMPT)

                # Run the first command and capture the cleaned output, if you want
                # the output without cleaning, simply grab current_output instead.
                interact.send(command)
                save_config_prompt = 'Press Quit\(q\) to exit, you may save configuration and re-enter the command. \[y/n/q\]'
                reload_config_prompt = 'This operation may require a reload of the system. Do you want to proceed? \[y/n\]'
                # interact.
                # we need to expect either for the prompt or for configuration quit or for reload
                interact.expect([PROMPT, save_config_prompt, reload_config_prompt],timeout=300)
                cmd_output = interact.current_output_clean

                # the cmd_output will not consist of actual prompt. We need to check the previous outputs
                # and verify if it is indeed the prompt we are expecting

                if check_if_config(cmd_output):
                    interact.send('y')
                    interact.expect([PROMPT, reload_config_prompt],timeout=300)
                    if check_if_reload(cmd_output):
                        interact.send('y')
                        # after this device will be unreachable as device will restart
                elif check_if_reload(cmd_output):
                    interact.send('y')
                    # after this device will be unreachable as device will restart
                else:
                    print("Command completed. Returned to prompt")
                final_op=interact.current_output_clean
                result["std_out"] = final_op

        except Exception as e:
            #module.fail_json(msg="Error while searching:\n{}".format(traceback.format_exc()))
         traceback.print_exc()
        finally:
            try:
                client.close()
            except Exception:
                pass

        return result

