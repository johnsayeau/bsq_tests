from uiautomator import Device
from time import sleep
import os
import subprocess

def run_cmd_return_output(cmd):
    '''takes command as a string and splits on the spaces - enters the
    resulting list as the first argument in subprocess.popen'''
    p = subprocess.Popen(cmd.split(" "), stdout=subprocess.PIPE)
    return p.stdout.read()

class Android_Device(Device):
    '''extended the uiautomator Device class to add a working screenshot method and a save logcat method.
    als changed the constructor to do all the work of connecting the device to adb
    to see all the available methods etc of the parent class go here - https://github.com/xiaocong/uiautomator'''

    def __init__(self, ip_address):
        '''connects to android device using ip or serial returns exception on failure
        you should also be able to connect using the serial number instead of the IP address
        '''

        self.ip_address = ip_address
        self.device = None
        os.system("adb kill-server > /dev/null 2>&1")
        os.system("adb start-server > /dev/null 2>&1")
        os.system("adb root > /dev/null 2>&1")
        connection_status = run_cmd_return_output("adb connect " + self.ip_address)
        if  "connected" in run_cmd_return_output("adb connect " + self.ip_address):
            super(Android_Device, self).__init__()
        else:
            raise Exception(connection_status)

    def take_screenshot(self, png_file):
        '''takes screenshot - saves to filename
        can enter path to file like - /images/sample.png
        example take_screenshot(bsq, "/images/sample.png")
        uses adb shell cmd instead of uiautomator screenshot
        because it is more reliable - ****warning*** will overwrite files of the same name
        !!!may only run from a mac or some other os where perl exists!!! '''
        ip = self.ip_address
        os.system("adb -s " + ip + " shell screencap -p | perl -pe 's/\\x0D\\x0A/\\x0A/g' > " + png_file )

    def save_logcat_to_file(self, file_name, logcat_time=8):
        '''sends the output of logcat to a file '''
        ip = self.ip_address
        p = subprocess.Popen('adb -s ' + ip +  ' logcat >> ' + file_name, stdout=subprocess.PIPE, shell=True)
        sleep(logcat_time)
        p.kill()













