from uiautomator import Device
from time import sleep
import os
import subprocess

def run_cmd_return_output(cmd):
    '''takes command as a string and splits on the spaces - enters the
    resulting list as the first argument in subprocess.popen'''
    p = subprocess.Popen(cmd.split(" "), stdout=subprocess.PIPE)
    return p.stdout.read()

class Android_Device:

    def __init__(self, ip_address):
        '''connects to android device using ip or serial returns exception on failure'''
        self.ip_address = ip_address
        self.device = None
        os.system("adb kill-server > /dev/null 2>&1")
        os.system("adb start-server > /dev/null 2>&1")
        os.system("adb root > /dev/null 2>&1")
        connection_status = run_cmd_return_output("adb connect " + self.ip_address)
        if  "connected" in run_cmd_return_output("adb connect " + self.ip_address):
            self.device = Device(ip_address)
        else:
            raise Exception(connection_status)

    def take_screenshot(self, png_file):
        '''takes screenshot - saves to filename
        can enter path to file like - /images/sample.png
        example take_screenshot(bsq, "/images/sample.png")
        uses adb shell cmd instead of uiautomator screenshot
        because it is more reliable - ****warning*** will overwrite files of the same name
        '''
        ip = self.ip_address
        os.system("adb -s " + ip + " shell screencap -p | perl -pe 's/\\x0D\\x0A/\\x0A/g' > " + png_file )

    def save_logcat_to_file(self, file_name):
        ip = self.ip_address
        p = subprocess.Popen('adb -s ' + ip +  ' logcat >> ' + file_name, stdout=subprocess.PIPE, shell=True)
        sleep(8)
        p.kill()

    def click_view_with_text(self, view_text, wait_time):
        #wait time is in seconds
       for i in range(1,wait_time + 1):
           if self.device(text=view_text).exists:
               self.device(text=view_text).click()
               return
           else:
               sleep(1)
       self.take_screenshot("view_not_found.png")
       raise Exception("view with text " + view_text + " not found")







