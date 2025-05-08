from PyQt6 import uic
from PyQt6 import QtWidgets
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QMainWindow, QApplication, QFrame
from timerApp import CountDownTimer
import sys # for command-line inputs




class GuiStuff(QMainWindow):
    

    def __init__(self):
        """
        Initializes the GUI components, loads the designer interface, sets up the 
        timer, and connects buttons to their respective actions.
        
        Sets default values for the LCD label, time setter spin box, and connects
        control buttons (e.g., close, set timer, reset, pause/resume, stop) to the 
        corresponding methods.
        """
        super().__init__()

        # load designer interface
        uic.loadUi('designs/test.ui', self)

        # display area
        self.counter = 0
        self.lcd_lbl.setText('00:00:00')
        self.time_setter_spbx.setValue(5)
        self.time_setter_spbx.setFocus()
        self.time_setter_spbx.setToolTip('Time value in seconds')

        # control buttons area
        # self.close_btn.clicked.connect(self.say_bye) # close button
        self.set_timer_btn.clicked.connect(self.set_timer) # set timer button
        self.reset_time_setter_btn.clicked.connect(self.reset_time_setter) # reset timer button
        self.pause_btn.clicked.connect(self.toggle_pause_resume) # pause resume button
        self.stop_btn.clicked.connect(self.stop_timer) # stop button

        # timer setting
        self.timer = CountDownTimer(self.lcd_lbl)
        self.time_setter_spbx.setValue(5)
        self.start_btn.clicked.connect(lambda: self.timer.start(self.time_setter_spbx.value()))



    def run_timer(self):
        self.timer.start(5)
        self.setter_frm.setEnabled(False)



    def toggle_pause_resume(self):
        if self.counter % 2 == 0:
            self.timer.pause()
            self.pause_btn.setText('Resume')
            self.blink_lcd(self.lcd_lbl)
        else:
            self.blink_lcd(self.lcd_lbl, start_blinking=False)
            self.timer.resume()
            self.pause_btn.setText('Pause')
        self.counter += 1



    def stop_timer(self):
        self.timer.stop()
        self.setter_frm.setEnabled(True)
        self.blink_lcd(self.lcd_lbl)



    def set_timer(self):
        total_sec = self.timer.format_time(total_seconds=float(self.time_setter_spbx.value()))
        self.lcd_lbl.setText(total_sec)


    def reset_time_setter(self):
        self.time_setter_spbx.setValue(0)
        self.lcd_lbl.setText('00:00:00')

    
    def update_counter(self):
        self.counter += 1
        self.counter_lcd.display(str(self.counter))



    def blink_lcd(self, label, start_blinking=True):
        if start_blinking:
            self.original_text = label.text()
            self._blink_state = True

            def toggle():
                label.setText('' if self._blink_state else self.original_text)
                self._blink_state = not self._blink_state

            self.blink_timer = QTimer(self)
            self.blink_timer.timeout.connect(toggle)
            self.blink_timer.start(500)
        else:
            if hasattr(self, 'blink_timer') and self.blink_timer.isActive():
                self.blink_timer.stop()
                label.setText(self.original_text)


  

app = QApplication(sys.argv)
gui = GuiStuff()
gui.show()
sys.exit(app.exec())
