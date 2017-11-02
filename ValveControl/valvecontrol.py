# -*- coding: utf-8 -*-

import sys
import valve
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets
import datetime as dt
import time
class ValveApp(QtWidgets.QMainWindow, valve.Ui_MainWindow):
    def __init__(self):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        
        self.numCycles = 0
        self.skipGas = [False]*8
        self.status = [False]*9
        self.progress = [0.0]*8
        self.timeRemaining = [0]*8
#        self.flowTime = dt.time()
#        self.dwellTime = dt.time()
        self.flowTime = dt.timedelta()
        self.dwellTime = dt.timedelta()
        self.startTime = dt.datetime.utcnow()
        self.endTime = dt.datetime.utcnow()
        self.closeTime = dt.time()
        self.override = False
        self.valveRunTime = 0
        self.setupUi(self)  # This is defined in design.py file automatically
                            # It sets up layout and widgets that are defined
        self.startButton.clicked.connect(self._start)
        
        self._set_progress()
        self._set_timeremaining()
        
        self._valveIndex = -1
#        self.timer = QtCore.QTimer(self)
#        self.timer.timeout.connect(self._timerEvent)
#        self.timer.start(1000)        
        
        
    def _start(self):
        print("Start")
        
        ## Determine if we are skipping any valves
        self.skipGas = [self.skip1.isChecked(),self.skip2.isChecked(),
                        self.skip3.isChecked(),self.skip4.isChecked(),
                        self.skip5.isChecked(),self.skip6.isChecked(),
                        self.skip7.isChecked(),self.skip8.isChecked()]
        
        ## Save all of the current input settings
        self.numCycles = self.CycleBox.value()
        self.override = self.checkBox.checkState()
        self.startTime = dt.datetime.utcnow()
        self.startTime = self.startTime.replace(microsecond=0)

#        temp = self.flowTime.replace(hour = self.flowTimeBox.time().hour(),
#                                     minute = self.flowTimeBox.time().minute(),
#                                     second = self.flowTimeBox.time().second())
#        self.flowTime = temp
#        
#        temp = self.dwellTime.replace(hour = self.dwellTimeBox.time().hour(),
#                                      minute = self.dwellTimeBox.time().minute(),
#                                      second = self.dwellTimeBox.time().second())
#        self.dwellTime = temp
       
        self.flowTime = dt.timedelta(hours = self.flowTimeBox.time().hour(),
                                     minutes = self.flowTimeBox.time().minute(),
                                     seconds = self.flowTimeBox.time().second())
        self.dwellTime = dt.timedelta(hours = self.dwellTimeBox.time().hour(),
                                      minutes = self.dwellTimeBox.time().minute(),
                                      seconds = self.dwellTimeBox.time().second())
        
#        print(self.flowTime)
#        print(self.dwellTime)
        
        self.valveRunTime = self.flowTime + self.dwellTime
        print(self.valveRunTime)
#        timeList = [self.flowTime,self.dwellTime]
#        self.valveRunTime = dt.timedelta()
#        for i in timeList:
#            d = dt.timedelta(hours=int(i.hour), minutes=int(i.minute), seconds=int(i.second))
#            self.valveRunTime += d
            
        self.valveRunTime *= self.numCycles
        print(self.valveRunTime)
        self.timeRemaining = [self.valveRunTime.total_seconds()]*8
        self._set_timeremaining()
#        self.valveRunTime *= self.
        
        self.endTime = (self.startTime + self.valveRunTime) 
        
        self.startTimeBox.setText(str(self.startTime))
        self.endTimeBox.setText(str(self.endTime))
        print(self.endTime)
        

        
        self._run()
        
    def _set_start_condition(self):
        pass
        
    def _run(self):
        print("run")
        
        for i in range(8):
            
            self._valveIndex = i
            
            dwellTime = self.valveRunTime - self.flowTime
            
            for i in range(10):
                time.sleep(1)
            ## Set Valve i Open
            # OpenValve(i)
#            while(self.timeRemaining[i]>(dwellTime)):
#                pass
            
            ## Set Valve i Closed
            # CloseValve(i)
#            while(self.timeRemaining[i] >0 ):
#                pass
    def _set_progress(self):
        self.progress1.setValue(self.progress[0])
        self.progress2.setValue(self.progress[1])
        self.progress3.setValue(self.progress[2])
        self.progress4.setValue(self.progress[3])
        self.progress5.setValue(self.progress[4])
        self.progress6.setValue(self.progress[5])
        self.progress7.setValue(self.progress[6])
        self.progress8.setValue(self.progress[7])
        
    def _set_timeremaining(self):
        self.lcd1.display(self.timeRemaining[0])
        self.lcd2.display(self.timeRemaining[1])
        self.lcd3.display(self.timeRemaining[2])
        self.lcd4.display(self.timeRemaining[3])
        self.lcd5.display(self.timeRemaining[4])
        self.lcd6.display(self.timeRemaining[5])
        self.lcd7.display(self.timeRemaining[6])
        self.lcd8.display(self.timeRemaining[7])
        
    def _timerEvent(self):
        if(self._valveIndex >= 0):
            self.timeRemaining[self._valveIndex] -= 1
def main():
    app = QtWidgets.QApplication(sys.argv)  # A new instance of QApplication
    form = ValveApp()                 # We set the form to be our ExampleApp (design)
    form.show()                         # Show the form
    app.exec_()                         # and execute the app


if __name__ == '__main__':              # if we're running file directly and not importing it
    main()                              # run the main function
