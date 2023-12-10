from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class AnotherWindow(QWidget):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.wynik()

    def wynik(self):
        self.resize(300, 200)
        self.setWindowTitle("Wynik")
        label = QLabel("Przypisane zamówienia do pracowników:")
        data_label = QLabel(str(self.data))
        layout = QGridLayout(self)
        layout.addWidget(label, 0, 0)
        layout.addWidget(data_label, 1, 0)
        self.show()

class Sklep(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.second_window = None
        self.interfejs()

    def interfejs(self):
        widget = QWidget()
        layout = QGridLayout()

        layout.addWidget(QLabel('Liczba klientów:'), 0, 0)
        self.liczba1Edt = QLineEdit()
        self.liczba1Edt.setPlaceholderText("Wprowadź liczbę całkowitą")
        layout.addWidget(self.liczba1Edt, 0, 1)
        layout.addWidget(QLabel('Liczba pracowników:'), 1, 0)
        self.liczba2Edt = QLineEdit()
        self.liczba2Edt.setPlaceholderText("Wprowadź liczbę całkowitą")
        layout.addWidget(self.liczba2Edt, 1, 1)
        layout.addWidget(QLabel('Czas obsługi i-tego zamówienia:'), 2, 0)
        self.liczba3Edt = QLineEdit()
        self.liczba3Edt.setPlaceholderText("Wprowadź ciąg licz całkowitych, w postaci: 1,2,3,4 itd.")
        layout.addWidget(self.liczba3Edt, 2, 1)
        layout.addWidget(QLabel('Czas pracy każdego pracownika:'), 3, 0)
        self.liczba4Edt = QLineEdit()
        self.liczba4Edt.setPlaceholderText("Wprowadź liczbę całkowitą")
        layout.addWidget(self.liczba4Edt, 3, 1)

        self.button = QPushButton('Oblicz')
        layout.addWidget(self.button, 4, 1)
        self.button.clicked.connect(self.check)
        
        self.resize(600, 400)
        self.setWindowTitle("Przydzielanie pracowników")
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.show()

    def open_new_window(self):
            n = int(self.liczba1Edt.text())
            m = int(self.liczba2Edt.text())
            tekst = self.liczba3Edt.text()
            ti = [int(x) for x in tekst.split(',')]
            T = int(self.liczba4Edt.text())
                        
            zamowienia = list(range(1, n + 1))
            pracownicy = {i: [] for i in range(1, m + 1)}

            zamowienia.sort(key=lambda i: ti, reverse=True)
                        
            for i in zamowienia:
                for j in range(1, m + 1):
                    if sum(ti[z - 1] for z in pracownicy[j]) + ti[i - 1] <= T:
                        pracownicy[j].append(i)
                        break

        
            self.second_window = AnotherWindow(pracownicy)
            self.second_window.show()
            return pracownicy
    
    def check(self):
        try:
            n = int(self.liczba1Edt.text())
            m = int(self.liczba2Edt.text())
            tekst = self.liczba3Edt.text()
            ti = [int(x) for x in tekst.split(',')]
            T = int(self.liczba4Edt.text()) 
        except:
            QMessageBox.warning(self, "Błąd", "Błędne dane", QMessageBox.Ok)
        else:
            if  n<1 or n>100:
                QMessageBox.warning(self, "Błąd", "Błędne dane", QMessageBox.Ok)
            elif m<1 or m>10:
                QMessageBox.warning(self, "Błąd", "Błędne dane", QMessageBox.Ok)  
            elif any(x < 1 for x in ti) or any(x > 5 for x in ti):
                QMessageBox.warning(self, "Błąd", "Błędne dane", QMessageBox.Ok)  
            elif T<1 or T>8:
                QMessageBox.warning(self, "Błąd", "Błędne dane", QMessageBox.Ok) 
            elif len(ti)!= n:
                QMessageBox.warning(self, "Błąd", "Błędne dane", QMessageBox.Ok)
            else:
                self.open_new_window()

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = Sklep()
    sys.exit(app.exec_())