"""Vektoripajan käynnistys.

Kehityksessä:  python main.py
Valmiina:      Vektoripaja.exe
Itsetesti:     python main.py --itsetesti  tai  Vektoripaja.exe --itsetesti
"""
import sys


def main() -> int:
    if "--itsetesti" in sys.argv:
        from vektoripaja.itsetesti import aja

        return aja()

    
    from vektoripaja.ikkuna import kaynnista

    return kaynnista()


if __name__ == "__main__":
    sys.exit(main())
