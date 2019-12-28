import wmi
import pythoncom
import sys, win32gui, win32con
from os import getpid, system
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/brightness/<b_value>')
def brightness(b_value):
	brightness = int(b_value) # percentage [0-100]
	if brightness > 100:
		brightness = 100
	if brightness < 0:
		brightness = 0

	if brightness == 0:
		win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SYSCOMMAND, win32con.SC_MONITORPOWER, 2)
	else:
		pythoncom.CoInitialize()
		win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SYSCOMMAND, win32con.SC_MONITORPOWER, -1)
		c = wmi.WMI(namespace='wmi')
		methods = c.WmiMonitorBrightnessMethods()[0]
		methods.WmiSetBrightness(brightness, 0)
	return b_value


if __name__ == '__main__':
    app.run(host='0.0.0.0')