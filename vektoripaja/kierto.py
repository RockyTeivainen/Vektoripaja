def kiertokulma(aika, nopeus):
    """Kulma asteina; nopeus kierroksina sekunnissa, kulma alkaa alusta."""
    return (aika * nopeus * 360) % 360
