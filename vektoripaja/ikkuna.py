import sys
from time import perf_counter

import pyvista as pv
from pyvistaqt import QtInteractor
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMainWindow

from vektoripaja.kierto import kiertokulma
from vektoripaja.teema import lataa_teema, TAUSTA, KOROSTUS


def kaynnista():
    app = QApplication.instance() or QApplication(sys.argv)
    lataa_teema(app)
    ikkuna = QMainWindow()
    ikkuna.setWindowTitle("Vektoripaja – pyörivän kuution testi")
    ikkuna.resize(900, 650)
    plotter = QtInteractor(ikkuna)
    ikkuna.setCentralWidget(plotter)
    plotter.set_background(TAUSTA)
    kuutio = plotter.add_mesh(pv.Cube(), color=KOROSTUS, show_edges=True)
    plotter.camera_position = "iso"
    alku = perf_counter()

    def paivita():
        kuutio.orientation = (0, kiertokulma(perf_counter() - alku, 0.5), 0)
        plotter.render()

    ajastin = QTimer(ikkuna)
    ajastin.setInterval(16)
    ajastin.timeout.connect(paivita)
    ajastin.start()
    app.aboutToQuit.connect(ajastin.stop)
    app.aboutToQuit.connect(plotter.close)
    ikkuna.show()
    return app.exec()
