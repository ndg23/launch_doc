import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QLineEdit
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DockerLaunch")
        self.setGeometry(100, 100, 600, 400)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f8f9fa;
            }
            QPushButton {
                background-color: #007bff;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
            QLabel, QLineEdit {
                font-size: 14px;
            }
            QLineEdit {
                padding: 5px;
                border: 1px solid #ced4da;
                border-radius: 4px;
            }
        """)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.dockerfile_label = QLabel("Dockerfile:")
        self.layout.addWidget(self.dockerfile_label)

        self.dockerfile_path = QLineEdit()
        self.layout.addWidget(self.dockerfile_path)

        self.select_dockerfile_button = QPushButton("Select Dockerfile")
        self.select_dockerfile_button.clicked.connect(self.select_dockerfile)
        self.layout.addWidget(self.select_dockerfile_button)

        self.build_button = QPushButton("Build Docker Image")
        self.build_button.clicked.connect(self.build_docker_image)
        self.layout.addWidget(self.build_button)

        self.deploy_button = QPushButton("Deploy Docker Image")
        self.deploy_button.clicked.connect(self.deploy_docker_image)
        self.layout.addWidget(self.deploy_button)

        self.layout.addStretch()

    def select_dockerfile(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Dockerfile", "", "Dockerfile (*)")
        if file_name:
            self.dockerfile_path.setText(file_name)

    def build_docker_image(self):
        # Ici, vous ajouterez la logique pour construire l'image Docker
        print("Building Docker image...")

    def deploy_docker_image(self):
        # Ici, vous ajouterez la logique pour déployer l'image Docker
        print("Deploying Docker image...")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())