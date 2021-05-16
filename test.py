from xvfb_handler import XVFB_Handler
import os


server_number = XVFB_Handler.get_free_server_number()
resolution = '1366x768'
script_path = os.path.join(os.path.dirname(__file__), 'browser.py')
script_parameters = {
    '--server_number': server_number,
    '--resolution': resolution
}
process = XVFB_Handler.run_script(server_number, resolution, script_path, script_parameters, 'python3')
(output, err) = process.communicate()
output = output.decode('utf-8')
err = err.decode('utf-8')
print(output)
print(err)
process.kill()
XVFB_Handler.remove_server(server_number)
