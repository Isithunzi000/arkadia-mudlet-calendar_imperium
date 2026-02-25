# Kalendarz Imperium & Ishtar - pakiety Mudlet

Porty pluginow kalendarza z klienta Dargoth (Arkadia web client) do klienta Mudlet.

## Instalacja

1. Otworz Mudlet i polacz sie z Arkadia
2. Idz do **Toolbox** -> **Package Manager** (lub `Alt+O`)
3. Kliknij **Install** i wybierz plik `.mpackage`
4. Powtorz dla drugiego pakietu

> **Wazne:** Paczka kalendarzy powinna sie znajdowac powyzej skryptow ogolnodostepnych Arkadii. Mozesz to ustawic w Package Manager przesuwajac paczke w gore listy.

Alternatywnie, w linii polecen Mudlet:
```
lua installPackage("/sciezka/do/imperium_cal.mpackage")
lua installPackage("/sciezka/do/ishtar_cal.mpackage")
```

## Uzycie

- **`/imperium`** - wyswietla kalendarz Imperium (najblizsze nowia, pelnie, swieta sezonowe i interkalarne)
- **`/ishtar`** - wyswietla kalendarz Ishtar (najblizsze swieta astronomiczne, magiczne, pelnie i festyn w Eysenlaan)

## Jak to dziala

Pluginy pobieraja aktualny czas gry na dwa sposoby:
1. **GMCP** (jesli serwer Arkadii wysyla zdarzenia zegara przez GMCP) - natychmiastowy odczyt
2. **Komenda `czas`** - plugin automatycznie wysyla komende i parsuje odpowiedz serwera

Nastepnie wylicza czas rzeczywisty do najblizszych wydarzen na podstawie przelicznika:
- 1 minuta gry = 2 sekundy czasu rzeczywistego
- 1 godzina gry = 120 sekund czasu rzeczywistego

## Wersja

- Wersja: 1.8.0m (Mudlet port)
- Bazuje na: imperium_cal/ishtar_cal v1.8.0 dla klienta Dargoth
- Data portu: 14-02-2026
