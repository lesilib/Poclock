import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QPixmap

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.image_label = None
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("'Din Clock")
        self.setGeometry(600, 350, 300, 100)

        self.image_label = QLabel(self)
        self.image_label.setPixmap(QPixmap("Din.png"))
        self.image_label.setScaledContents(True)
        self.image_label.lower()

        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet(
            "font-size:150px;"
            "color:hsl(111,100%,50%);"
            "background: transparent;"
        )

        vbox = QVBoxLayout(self)
        vbox.addWidget(self.time_label)

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()

    def resizeEvent(self, event):
        self.image_label.setGeometry(0, 0, self.width(), self.height())
        return super().resizeEvent(event)

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
