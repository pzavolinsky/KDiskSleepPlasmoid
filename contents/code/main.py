# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyKDE4.plasma import Plasma
from PyKDE4 import plasmascript
from PyQt4 import QtCore
import commands
import os

class DiskSleep(plasmascript.Applet):
	
	def __init__(self,parent,args=None):
		plasmascript.Applet.__init__(self,parent)
	
	def init(self):
		self.setHasConfigurationInterface(False)
		self.setAspectRatioMode(Plasma.IgnoreAspectRatio)
		
		theme = Plasma.Theme.defaultTheme()
		self.theme = Plasma.Svg(self)
		self.theme.setImagePath("widgets/background")
		self.setBackgroundHints(Plasma.Applet.DefaultBackground)
		self.layout = QGraphicsLinearLayout(Qt.Vertical, self.applet)
		self.label = Plasma.Label(self.applet)
		
		self.layout.addItem(self.label);
		self.layout.addStretch();
		self.applet.setLayout(self.layout);
		
		self._updateStats();
		
		self.timer = QtCore.QTimer();
		self.timer.setInterval(2000);
		self.timer.start(2000);
		QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"), self._updateStats);

		
	def _updateStats(self):
		self.label.setText(commands.getoutput("ps -e -o state= -o pid= -o comm= | sed -ne 's/^D *//p'"));
	
def CreateApplet(parent):
	return DiskSleep(parent)
