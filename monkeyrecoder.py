#Usage: monkeyrunner recorder.py
#recorder.py
#http://mirror.yongbok.net/linux/android/repository/platform/sdk/monkeyrunner/scripts/monkey_recorder.py
#com.android.monkeyrunner import MonkeyRunner as mr
#com.android.monkeyrunner.recorder import MonkeyRecorder as recorder


from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice
from com.android.monkeyrunner.recorder import MonkeyRecorder

device = MonkeyRunner.waitForConnection()
MonkeyRecorder.start(device)
#END recorder.py
