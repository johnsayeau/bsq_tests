from android_device import Android_Device

bsq = Android_Device("10.1.108.93")
bsq.take_screenshot("test.png")
bsq.save_logcat_to_file("loggy.txt", 5)
bsq(text="About board").click()
bsq.press("back")
print bsq(text="Sound").info
