from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel, QGridLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtWidgets import QMessageBox

class Sklep(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interfejs()

    def interfejs(self):

        # etykiety
        etykieta1 = QLabel("Liczba klientów:", self)
        etykieta2 = QLabel("Liczba pracowników:", self)
        etykieta3 = QLabel("Czas obsługi zamówienia kielna i:", self)
        etykieta4 = QLabel("Czas pracy każdego pracownika:", self)

        # przypisanie widgetów do układu tabelarycznego
        ukladT = QGridLayout()
        ukladT.addWidget(etykieta1, 0, 0)
        ukladT.addWidget(etykieta2, 0, 1)
        ukladT.addWidget(etykieta3, 0, 3)
        ukladT.addWidget(etykieta4, 0, 4)


        # 1-liniowe pola edycyjne
        self.liczba1Edt = QLineEdit()
        self.liczba2Edt = QLineEdit()
        self.liczba3Edt = QLineEdit()
        self.liczba4Edt = QLineEdit()
        self.wynikEdt = QLineEdit()

        self.wynikEdt.readonly = True
        self.wynikEdt.setToolTip('Wpisz <b>liczby</b> i wybierz działanie...')

        ukladT.addWidget(self.liczba1Edt, 1, 0)
        ukladT.addWidget(self.liczba2Edt, 1, 1)
        ukladT.addWidget(self.liczba3Edt, 1, 2)
        ukladT.addWidget(self.liczba4Edt, 1, 3)
        ukladT.addWidget(self.wynikEdt, 1, 2)

        # przyciski
        obliczBtn = QPushButton("&Oblicz", self)
        ukladH = QHBoxLayout()
        ukladH.addWidget(obliczBtn)
        ukladT.addLayout(ukladH, 2, 0, 1, 3)

        # przypisanie utworzonego układu do okna
        self.setLayout(ukladT)
        obliczBtn.clicked.connect(self.przydziel_pracownikow)

        self.resize(200, 400)
        self.setWindowTitle("Przydzielanie pracowników")
        self.show()

    def przydziel_pracownikow(self):

        nadawca = self.sender()    
        try:
            n = int(self.liczba1Edt.text())
            m = int(self.liczba2Edt.text())
            ti = int(self.liczba3Edt.text())
            T = int(self.liczba4Edt.text())
            zamowienia = list(range(1, n + 1))
            pracownicy = {i: [] for i in range(1, m + 1)}

            zamowienia.sort(key=lambda i: ti[i-1], reverse=True)
            if nadawca.text() == "&Oblicz":
                for i in zamowienia:
                    for j in range(1, m + 1):
                        if sum(ti[z - 1] for z in pracownicy[j]) + ti[i - 1] <= T:
                            pracownicy[j].append(i)
                            break

            else:
                pass
            self.wynikEdt.setText(str(pracownicy))
        except:
            QMessageBox.warning(self, "Błąd", "Błędne dane", QMessageBox.Ok)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = Sklep()
    sys.exit(app.exec_())




