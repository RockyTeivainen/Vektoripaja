# -*- mode: python ; coding: utf-8 -*-
# Vektoripaja – PyInstallerin määrittely. Tekee Windows-version kansioon dist/Vektoripaja
# (onedir: .exe ja sen vieressä kansio _internal). Valmis versio toimii ilman Pythonia.
#
# Aja:  python -m PyInstaller --noconfirm --clean vektoripaja.spec
# Tarkista sitten:  dist\Vektoripaja\Vektoripaja.exe --itsetesti
#
# Kun lisäät uuden datatiedoston tai kirjaston, lisää se tänne ja aja itsetesti.
from PyInstaller.utils.hooks import collect_data_files, collect_submodules

# Datatiedostot: (lähde, kohdekansio valmiissa versiossa)
datas = [
    ("vektoripaja/teema.qss", "vektoripaja"),
    ("esimerkit/esimerkki.svg", "esimerkit"),
]
datas += collect_data_files("pyvista")
datas += collect_data_files("trimesh")

# Piilotetut importit: moduulit, jotka kirjastot tuovat vasta ajon aikana,
# joten PyInstaller ei näe niitä koodista.
hiddenimports = []
# PyVista tuo osan moduuleistaan laiskasti. Selain- ja Jupyter-osia (trame, jupyter) ei tarvita.
hiddenimports += collect_submodules(
    "pyvista", filter=lambda nimi: not nimi.startswith(("pyvista.trame", "pyvista.jupyter"))
)
hiddenimports += collect_submodules("vtkmodules.util")  # VTK:n Python-osat (data_model, execution_model …)
hiddenimports += [
    "vtkmodules.qt.QVTKRenderWindowInteractor",         # pyvistaqt:n 3D-näkymä Qt-ikkunassa
    "vtkmodules.vtkRenderingOpenGL2",                   # VTK:n OpenGL-piirto
    "vtkmodules.vtkInteractionStyle",                   # hiirellä kierto ja zoom
    "vtkmodules.vtkRenderingFreeType",                  # tekstit 3D-näkymässä
    "PySide6.QtOpenGL",
    "PySide6.QtOpenGLWidgets",
]

# Qt:n platforms-liitännäiset (Windowsissa qwindows.dll) kerää PyInstallerin
# PySide6-hook automaattisesti. Itsetesti tarkistaa, että qwindows.dll on mukana.

a = Analysis(
    ["main.py"],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    runtime_hooks=[],
    excludes=["tkinter", "PyQt5", "PyQt6", "PySide2"],
    noarchive=False,
)
pyz = PYZ(a.pure)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="Vektoripaja",
    debug=False,
    strip=False,
    upx=False,
    console=False,  # työpöytäsovellus: ei terminaali-ikkunaa
)
coll = COLLECT(exe, a.binaries, a.datas, strip=False, upx=False, name="Vektoripaja")
