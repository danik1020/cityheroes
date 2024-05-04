import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QStackedWidget, QHBoxLayout, QSizePolicy
#from PyQt6.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt6.QtCore import Qt, QUrl

class EyeTrainingApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Eye Training App")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.stacked_widget = QStackedWidget(self.central_widget)

        self.main_page = MainPage()
       # self.exercises_page = ExercisePage()

        self.stacked_widget.addWidget(self.main_page)
        #self.stacked_widget.addWidget(self.exercises_page)

        self.layout.addWidget(self.stacked_widget)

        #self.main_page.button.clicked.connect(self.showExercisesPage)

    #def showExercisesPage(self):
        #self.stacked_widget.setCurrentWidget(self.exercises_page)

class MainPage(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.label = QLabel("Главное меню", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.label)

        self.button = QPushButton("Перейти к упражнениям", self)
        self.layout.addWidget(self.button)

class ExercisePage(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.label = QLabel("Упражнения для тренировки глаз", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.label)

        #self.video_player = QMediaPlayer()
        video_widget = QWidget(self)
        video_layout = QVBoxLayout(video_widget)
        video_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        video_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        video_layout.addWidget(QWidget())
        video_layout.addWidget(QWidget())
        video_layout.addWidget(QWidget())
        self.layout.addWidget(video_widget)

        self.next_button = QPushButton("Следующее упражнение", self)
        self.layout.addWidget(self.next_button)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    eye_training_app = EyeTrainingApp()
    eye_training_app.show()
    sys.exit(app.exec())