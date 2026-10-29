import sys
from xml.etree.ElementTree import ParseError

import pyvista as pv
from pyvistaqt import QtInteractor
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from svgelements import Close

from vektoripaja.teema import lataa_teema, TAUSTA
from vektoripaja.tuonti import tuo_svg


def kaynnista():
    app = QApplication.instance() or QApplication(sys.argv)
    lataa_teema(app)
    ikkuna = QMainWindow()
    ikkuna.setWindowTitle("Vektoripaja")
    ikkuna.resize(900, 650)

    sisalto = QWidget(ikkuna)
    asettelu = QVBoxLayout(sisalto)
    avaa_painike = QPushButton("Avaa", sisalto)
    plotter = QtInteractor(sisalto)
    asettelu.addWidget(avaa_painike)
    asettelu.addWidget(plotter)
    ikkuna.setCentralWidget(sisalto)
    plotter.set_background(TAUSTA)

    def avaa_svg():
        tiedostopolku, _ = QFileDialog.getOpenFileName(
            ikkuna,
            "Avaa SVG-tiedosto",
            "",
            "SVG-tiedostot (*.svg)",
        )
        if not tiedostopolku:
            return

        try:
            polut = tuo_svg(tiedostopolku)
            for polku in polut:
                pituus = polku.length()
                if pituus <= 0:
                    continue
                pisteiden_maara = max(12, min(512, int(pituus / 2)))
                pisteet = [
                    (p.x, p.y, 0)
                    for p in (
                        polku.point(i / pisteiden_maara)
                        for i in range(pisteiden_maara + 1)
                    )
                ]
                suljettu = isinstance(polku[-1], Close)

                if suljettu and len(pisteet) > 3:
                    polygon = pv.PolyData(
                        pisteet,
                        faces=[len(pisteet) - 1, *range(len(pisteet) - 1)],
                    ).triangulate()
                    plotter.add_mesh(
                        polygon,
                        color="#000055",
                        show_edges=False,
                    )

                if len(pisteet) > 1:
                    plotter.add_lines(
                        pisteet,
                        color="#00c8df",
                        width=2,
                    )

            plotter.view_xy()
            plotter.reset_camera()
            plotter.render()
        except (OSError, ValueError, ParseError, RuntimeError) as virhe:
            QMessageBox.critical(
                ikkuna,
                "SVG:n avaaminen epäonnistui",
                str(virhe),
            )

    avaa_painike.clicked.connect(lambda _checked=False: avaa_svg())
    app.aboutToQuit.connect(plotter.close)
    ikkuna.show()
    return app.exec()
