import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self) :
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://google.com"))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction("Back", self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)
        forward_btn = QAction("Forward", self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)
        refresh_btn = QAction("Refresh", self)
        refresh_btn.triggered.connect(self.browser.reload)
        navbar.addAction(refresh_btn)
        Home_btn = QAction("Home", self)
        Home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(Home_btn)

        self.url_bar =QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_url)
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)


    def update_url(self, url):
        self.url_bar.setText(url.toString())


    def navigate_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))


    def navigate_home(self):
        self.browser.setUrl((QUrl('http://google.com')))

app = QApplication(sys.argv)
QApplication.setApplicationName("Internet Surfer V 1.0")
window = MainWindow()
app.exec_()
window.update()
