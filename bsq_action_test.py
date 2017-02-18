from android_device import Android_Device

bsq = Android_Device("10.1.108.93")
bsq.take_screenshot("test.png")
bsq.save_logcat_to_file("loggy.txt")
bsq.wait_for_view_and_click("About board", 5)