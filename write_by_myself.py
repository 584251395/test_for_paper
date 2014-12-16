from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice
device=MonkeyRunner.waitForConnection()
if not device:
    print "Please connect a device to start!"
else:
    print "Start"
device.wake()
MonkeyRunner.sleep(2)
device.drag((240,700),(480,700),0.5,5)

MonkeyRunner.sleep(1)

device.startActivity(component="api.demos/com.example.android.apis.ApiDemos")
#MonkeyRunner.sleep(5)

#TextView:App[0,76] [480,172]
device.touch(240,124,'DOWN_AND_UP')
print "App"
MonkeyRunner.sleep(0.5)
device.press('KEYCODE_BACK','DOWN_AND_UP') 
MonkeyRunner.sleep(0.5) 
device.touch(240,221,'DOWN_AND_UP') 
print "Content" 
MonkeyRunner.sleep(0.5) 
device.press('KEYCODE_BACK','DOWN_AND_UP') 
MonkeyRunner.sleep(0.5)
device.touch(240,318,'DOWN_AND_UP')
print "Graphics"
MonkeyRunner.sleep(0.5)
device.press('KEYCODE_BACK','DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(240,418,'DOWN_AND_UP')
print "Media"
MonkeyRunner.sleep(0.5)
device.press('KEYCODE_BACK','DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(240,512,'DOWN_AND_UP')
print "OS"
MonkeyRunner.sleep(0.5)
device.press('KEYCODE_BACK','DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(240,619,'DOWN_AND_UP')
print "Text"
MonkeyRunner.sleep(0.5)
device.press('KEYCODE_BACK','DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(240,715,'DOWN_AND_UP')
print "View"
MonkeyRunner.sleep(0.5)
device.press('KEYCODE_BACK','DOWN_AND_UP')
MonkeyRunner.sleep(0.5)

#here have finished the firsr page
device.touch(240,124,'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
print "=====================come into app====================="

device.touch(240,124,'DOWN_AND_UP')
print "Activity"
MonkeyRunner.sleep(0.5)
device.press('KEYCODE_BACK','DOWN_AND_UP') 
MonkeyRunner.sleep(0.5) 
device.touch(240,221,'DOWN_AND_UP') 
print "Alarm" 
MonkeyRunner.sleep(0.5) 
device.press('KEYCODE_BACK','DOWN_AND_UP') 
MonkeyRunner.sleep(0.5)
device.touch(240,318,'DOWN_AND_UP')
print "Dialog"
MonkeyRunner.sleep(0.5)
device.press('KEYCODE_BACK','DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(240,418,'DOWN_AND_UP')
print "Intents"
MonkeyRunner.sleep(0.5)
device.press('KEYCODE_BACK','DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(240,512,'DOWN_AND_UP')
print "Launcher Shortcuts"
MonkeyRunner.sleep(0.5)
device.press('KEYCODE_BACK','DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(240,619,'DOWN_AND_UP')
print "Menus"
MonkeyRunner.sleep(0.5)
device.press('KEYCODE_BACK','DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(240,715,'DOWN_AND_UP')
print "Notification"
MonkeyRunner.sleep(0.5)
device.press('KEYCODE_BACK','DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(240,811,'DOWN_AND_UP')
print "Preferences"
MonkeyRunner.sleep(0.5)
device.press('KEYCODE_BACK','DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
print "=========================here we need drag ================="
device.drag((240,600),(240,200),0.1,20)
print "=====from top to end====="
device.drag((240,200),(240,600),0.1,20)
print "=====from end to top====="
device.drag((240,600),(240,200),0.1,20)
print "=====from top to end====="
print "=========================finished drag out ================="
MonkeyRunner.sleep(0.5)
device.touch(240,619,'DOWN_AND_UP')
print "Search"
MonkeyRunner.sleep(0.5)
device.press('KEYCODE_BACK','DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(240,715,'DOWN_AND_UP')
print "Service"
MonkeyRunner.sleep(0.5)
device.press('KEYCODE_BACK','DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(240,811,'DOWN_AND_UP')
print "Voice Recognition"
MonkeyRunner.sleep(0.5)
device.press('KEYCODE_BACK','DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
print "=========================here we need drag ================="
device.drag((240,200),(240,600),0.1,20)
print "=====from top to end====="
device.drag((240,600),(240,200),0.1,20)
print "=====from end to top====="
device.drag((240,200),(240,600),0.1,20)
print "=====from top to end====="
print "=========================finished drag out ================="
MonkeyRunner.sleep(0.5)
#here have finished the second page
device.touch(240,124,'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
print "=================come into app come into Activity================"
device.touch(240,124,'DOWN_AND_UP')
print "Custom Dialog"
MonkeyRunner.sleep(0.5)
device.press('KEYCODE_BACK','DOWN_AND_UP') 
MonkeyRunner.sleep(0.5) 
device.touch(240,221,'DOWN_AND_UP') 
print "Custom Title" 
MonkeyRunner.sleep(0.5) 
device.press('KEYCODE_BACK','DOWN_AND_UP') 
MonkeyRunner.sleep(0.5)
device.press('KEYCODE_BACK','DOWN_AND_UP') 
MonkeyRunner.sleep(0.5)
device.touch(240,318,'DOWN_AND_UP')
print "Dialog"
MonkeyRunner.sleep(0.5)
device.press('KEYCODE_BACK','DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(240,418,'DOWN_AND_UP')
print "Forwarding"
MonkeyRunner.sleep(0.5)
device.press('KEYCODE_BACK','DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(240,512,'DOWN_AND_UP')
print "Hello World"
MonkeyRunner.sleep(0.5)
device.press('KEYCODE_BACK','DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(240,619,'DOWN_AND_UP')
print "Persistent State"
MonkeyRunner.sleep(0.5)
device.press('KEYCODE_BACK','DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.press('KEYCODE_BACK','DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(240,715,'DOWN_AND_UP')
print "Receive Result"
MonkeyRunner.sleep(0.5)
device.press('KEYCODE_BACK','DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(240,811,'DOWN_AND_UP')
print "Redirection"
MonkeyRunner.sleep(0.5)
device.press('KEYCODE_BACK','DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
print "=========================here we need drag ================="
device.drag((240,600),(240,200),0.1,20)
print "=====from top to end====="
device.drag((240,200),(240,600),0.1,20)
print "=====from end to top====="
device.drag((240,600),(240,200),0.1,20)
print "=====from top to end====="
print "=========================finished drag out ================="
MonkeyRunner.sleep(0.5)
device.touch(240,523,'DOWN_AND_UP')
print "Reorder Activities"
MonkeyRunner.sleep(0.5)
device.press('KEYCODE_BACK','DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(240,619,'DOWN_AND_UP')
print "Save & Restore State"
MonkeyRunner.sleep(0.5)
device.press('KEYCODE_BACK','DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.press('KEYCODE_BACK','DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(240,715,'DOWN_AND_UP')
print "Translucent"
MonkeyRunner.sleep(0.5)
device.press('KEYCODE_BACK','DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(240,811,'DOWN_AND_UP')
print "Translucent Blur"
MonkeyRunner.sleep(0.5)
device.press('KEYCODE_BACK','DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
print "=========================here we need drag ================="
device.drag((240,200),(240,600),0.1,20)
print "=====from top to end====="
device.drag((240,600),(240,200),0.1,20)
print "=====from end to top====="
device.drag((240,200),(240,600),0.1,20)
print "=====from top to end====="
print "=========================finished drag out ================="
MonkeyRunner.sleep(0.5)

