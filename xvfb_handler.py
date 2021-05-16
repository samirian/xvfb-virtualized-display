import subprocess
import os


class XVFB_Handler:
    __reserved_servers = []

    @staticmethod
    def run_script(server_number: int, resolution: str, script_path: str, script_parameters={}, python_name='python3'):
        xvfb_command = f'xvfb-run --listen-tcp --server-num {server_number} --auth-file /tmp/xvfb.auth -s "-ac -screen 0 {resolution}x24"'
        python_command = f'{python_name} "{script_path}"'
        for option, value in script_parameters.items():
            if isinstance(value, bool):
                if value == True:
                    python_command += ' {}'.format(option)
                else:
                    pass
            elif isinstance(value, int):
                python_command += ' {} {}'.format(option, value)
            elif isinstance(value, str):
                python_command += ' {} "{}"'.format(option, value)
        export_command = f'& export DISPLAY=:{server_number}'
        cmd = f'{xvfb_command} {python_command} {export_command}'
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        XVFB_Handler.__reserved_servers.append(server_number)
        return process

    @staticmethod
    def get_free_server_number():
        index = 1
        while os.path.exists(f'/tmp/.X{index}-lock') or index in XVFB_Handler.__reserved_servers:
            index += 1
        return index

    @staticmethod
    def remove_server(server_number: int):
        XVFB_Handler.__reserved_servers.remove(server_number)