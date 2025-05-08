from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import QTimer


class CountDownTimer:
    """
    A countdown timer that updates a QLabel every second.

    This class provides start, pause, resume, and stop functionality for a countdown timer,
    displaying the remaining time in HH:MM:SS format on a given QLabel.

    Args:
        label (QLabel): The QLabel widget to display the countdown.
    """

    def __init__(self, label: QLabel):
        self.label = label
        self.time_left = 0
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.__tick)
        self.running = False

    def start(self, seconds: int):
        """
        Start the countdown timer from the specified number of seconds.

        Args:
            seconds (int): The number of seconds to count down from.
        """
        self.time_left = seconds
        self.running = True
        self.label.setText(self.format_time(self.time_left))
        self.__tick()
        self.timer.start()


    def pause(self):
        """
        Pause the countdown timer if it is currently running.
        """
        if self.running:
            self.timer.stop()
            self.running = False

    def resume(self):
        """
        Resume the countdown timer if it is paused and time remains.
        """
        if not self.running and self.time_left > 0:
            self.timer.start()
            self.running = True

    def stop(self):
        """
        Stop the countdown timer and reset the display to 00:00:00.
        """
        if self.running and self.time_left > 0:
            self.timer.stop()
            self.label.setText(self.format_time(0))



    def __tick(self):
        """
        Internal method called every second to update the countdown.

        Decrements the remaining time, updates the label, and stops the timer when time is up.
        """
        self.time_left -= 1
        if self.time_left >= 0:
            self.label.setText(self.format_time(self.time_left))
        else:
            self.label.setText("Time's up!")
            self.timer.stop()


    def format_time(self, total_seconds: float):
        """
        Convert a number of seconds into a formatted time string (HH:MM:SS).

        Args:
            total_seconds (float): The total number of seconds to format.

        Returns:
            str: The time formatted as a string in HH:MM:SS format.
        """
        minutes, seconds = divmod(int(total_seconds), 60)
        hours, minutes = divmod(minutes, 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"