import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,  QTextEdit, QHBoxLayout, QFileDialog
# from PyQt5.QtGui import QIcon
import gtts
import pygame


class TextSpeech(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 100)
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle('Text to Speech')

        self.textEdit = QTextEdit(self)
        self.textEdit.setGeometry(30, 30, 550, 150)
        self.textEdit.setPlainText("hello")
        self.textEdit.textChanged.connect(self.onTextChanged)

        # Create a QHBoxLayout
        hbox = QHBoxLayout()
        

        # Create a button for text file upload
        self.upload_button = QPushButton("Upload Text File", self)
        self.upload_button.clicked.connect(self.upload_text_file)
        self.upload_button.setGeometry(10, 10, 20, 30)
        self.upload_button.setStyleSheet("padding:8px; font-size: 14px; margin-top:13px;")
        hbox.addWidget(self.upload_button)
        
        # Create a button for speech
        self.speech_button = QPushButton("speak", self)
        self.speech_button.clicked.connect(self.speak_text)  
        self.speech_button.setGeometry(10, 10, 10, 50)
        hbox.addWidget(self.speech_button)
        self.speech_button.setStyleSheet("background-color: green; color: white; padding: 8px; font-size: 14px; margin-top:13px;")

        # Add the hbox to the main layout
        self.setLayout(hbox)

        self.show()
        
    def onTextChanged(self):
        # This method will be called whenever the text inside the QTextEdit changes
        text = self.textEdit.toPlainText()

    def upload_text_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open file', '', 'Text files (*.txt)')

        if file_name:
            # Read the file content
            with open(file_name, 'r') as file:
                content = file.read()

            # Display the file content in the text edit area
            self.textEdit.setPlainText(content)
            
    def speak_text(self):
        text = self.textEdit.toPlainText()
        print(text)
        if os.path.exists("text.mp3"):
            # Attempt to delete the file
            os.remove("text.mp3")
        speech = gtts.gTTS(text)
        speech_file = "text.mp3"
        speech.save(speech_file)
        pygame.init()
        pygame.mixer.music.load(speech_file)
        pygame.mixer.music.play()
        

        # Keep the program running until the music finishes playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(1)
        pygame.mixer.music.unload()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TextSpeech()
    sys.exit(app.exec_())