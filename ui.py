import os
import threading
import pywhatkit
import sys
import wikipedia
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtGui import QMovie
from jarvis import jarvis


def main():
    # Create an instance of QApplication
    app = QApplication(sys.argv)

    def call_jarvis_thread():
        call_jarvis()

    def call_jarvis():
        j = jarvis()
        # voice = int(input("Enter 1 for male or 2 for female voice: "))
        j.getvoices()
        j.wishme()
        while True:
            query = j.takecommandCMD().lower().lower()
            if 'time' in query:
                j.time()
            # elif 'date' in query:
            #     j.date()
            elif 'email' in query:
                email_list = {
                    'haris': 'harismunib8@gmail.com',
                    'farooq': '35296@iqraisb.edu.pk',
                    'ahmed': 'ahmedarif01010101@gmail.com',
                    'anique': 'aniqueabbasi575@gmail.com',
                    '   '
                    'faizan': 'muhammadfaizanfazi869@gmail.com',
                    'umair': 'Rajaumair6013@gmail.com',
                    'ali': 'muhammadalikhan310@gmail.com',
                    'hassan':'hassanasifraja@gamail.com'

                }
                try:
                    j.speak("to whom I send the mail")
                    name = j.takecommandCMD().lower()
                    receiver = email_list[name]
                    j.speak("what is the subject of the mail")
                    subject = j.takecommandCMD().lower()
                    j.speak("what should I write")
                    content = j.takecommandCMD().lower()
                    j.sendEmail(content, receiver, subject)
                    j.speak("your email has been sent")
                except Exception as e:
                    print(e)
                    j.speak("unable to send email")
            elif 'wikipedia' in query:
                j.speak('what should i wikipedia ')
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                print(result)
                j.speak(result)
            elif 'search' in query:
                j.googlesearch()
            elif 'youtube' in query:
                j.speak("what should I play on youtube")
                topic = j.takecommandCMD().lower()
                pywhatkit.playonyt(topic)
            elif 'weather' in query:
                j.weather()
            elif 'news' in query:
                j.news()
            elif 'talk to me' in query:
                j.ai()
            elif 'open vs code' in query:
                vscode = 'C:\\Users\\Generation\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
                os.startfile(vscode)
            elif 'joke' in query:
                j.joke()
            elif 'shut down' in query:
                os.system("shutdown /s /t 0")  # This command schedules a system shutdown after 1 second
            elif 'screen shot' in query:
                j.screenshot()
            elif'cpu usage' in query:
                j.cpu_usage()
            elif 'offline' in query:
                quit()

    def exit_app():
        app.quit()

    # Create a QWidget (window)
    window = QWidget()
    window.setWindowTitle('PyQt5 Window')
    window.setGeometry(0, 0, 1360, 760)  # (x, y, width, height)

    # Create a label to display the GIF 1
    label = QLabel(window)
    label.setGeometry(0, 0, 1370, 750)  # (x, y, width, height)
    # Create QMovie object for the GIF
    movie = QMovie(r"E:\faro java\jarvis\images\ui2.gif")  # Use raw string literal or adjust path format
    label.setMovie(movie)
    movie.start()
    # Create two buttons
    # button 1
    button1 = QPushButton('Run', window)
    button1.setGeometry(1250, 640, 100, 50)  # (x, y, width, height)
    button1.setStyleSheet("background-color: rgb(58, 94, 58); font: 75 18pt;")
    button1.clicked.connect(lambda: threading.Thread(target=call_jarvis_thread).start())


    # button 2
    button2 = QPushButton('Exit', window)
    button2.setGeometry(1140, 640, 100, 50)  # (x, y, width, height)
    button2.setStyleSheet("background-color: rgb(27, 117, 113); font: 75 18pt;")
    button2.clicked.connect(exit_app)
    window.show()
    # Execute the application's event loop
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
