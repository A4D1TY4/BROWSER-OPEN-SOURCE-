import sys
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *
from datetime import datetime





class MainWindow(QMainWindow):
                    def __init__(self):
                        super(MainWindow, self).__init__()
                        self.browser = QWebEngineView()
                        self.browser.setUrl(QUrl("https://google.com"))
                        self.setCentralWidget(self.browser)
                        self.showMaximized()

                        # navigation menus
                        nav = QToolBar()
                        self.addToolBar(nav)

                        back_button = QAction("◀", self)
                        back_button.triggered.connect(self.browser.back)
                        nav.addAction(back_button)

                        forward_button = QAction("▶", self)
                        forward_button.triggered.connect(self.browser.forward)
                        nav.addAction(forward_button)

                        reload_button = QAction("⟳", self)
                        reload_button.triggered.connect(self.browser.reload)
                        nav.addAction(reload_button)

                        home_button = QAction("🏠", self)
                        home_button.triggered.connect(self.navigate_home)
                        nav.addAction(home_button)

                        my_button = QAction("our website", self)
                        my_button.triggered.connect(self.navigate_ourwebsite)
                        nav.addAction(my_button)

                        
                        my_channel = QAction("our channel", self)
                        my_channel.triggered.connect(self.our_channel)
                        nav.addAction(my_channel)

                        youtube_button = QAction("youtube", self)
                        youtube_button.triggered.connect(self.navigate_youtube)
                        nav.addAction(youtube_button)

                        self.urlbar = QLineEdit()
                        self.urlbar.returnPressed.connect(self.go_url)
                        nav.addWidget(self.urlbar)

                        self.browser.urlChanged.connect(self.current_url)
                        
                        #search navbar


                    def navigate_youtube(self):
                        self.browser.setUrl(QUrl("https://youtube.com"))

                    def go_url(self):
                        url = self.urlbar.text()
                        self.browser.setUrl(QUrl(url))

                    def current_url(self, nowurl):
                        self.urlbar.setText(nowurl.toString())

                    def navigate_home(self):
                        self.browser.setUrl(QUrl("https://google.com"))

                    def our_channel(self):
                        self.browser.setUrl(QUrl("https://www.youtube.com/channel/UChD1_E-R1Oruz2FV2rSIqmQ"))


                    def navigate_ourwebsite(self):
                        self.browser.setUrl(QUrl("https://webfirstpy.000webhostapp.com"))


app = QApplication(sys.argv)
QApplication.setApplicationName("Web browser by ProLinuxToturials")
window = MainWindow()
app.exec_()
