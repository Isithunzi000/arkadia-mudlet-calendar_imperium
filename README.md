# Kalendarz Imperium — Mudlet

Pakiet do Mudleta: kalendarz domeny Imperium (Kalendarz Imperialny) dla Arkadii MUD. Komenda `/imperium` pokazuje przybliżony czas do najbliższych wydarzeń księżycowych, sezonowych i świąt — RL i IG.

Port pluginu [imperium_cal z klienta Dargoth](https://github.com/Isithunzi000/arkadia-dargoth-plugins) (v1.8.12).

---

## Jak zainstalować

1. Pobierz `.mpackage` albo `.xml` z [najnowszego wydania](https://github.com/Isithunzi000/arkadia-mudlet-calendar_imperium/releases/latest) (oba działają tak samo, wybierz który wolisz)
2. W Mudlecie: **Toolbox → Package Manager** (`Alt+O`) → **Install** i wskaż pobrany plik
3. Gotowe — wpisz `/imperium`

> Paczka powinna znajdować się powyżej skryptów ogólnodostępnych Arkadii — przesuń ją w górę listy w Package Manager.

Plik [`imperium_cal.xml`](imperium_cal.xml) w korzeniu repo to źródło pakietu — możesz podejrzeć cały kod bez pobierania.

---

## Komendy

| Komenda | Opis |
|---------|------|
| `/imperium` | pokazuje kalendarz Imperium |
| `/imperium help` | pomoc (działa też `/imperium pomoc`) |

## Co pokazuje

- najbliższy nów i pełnię Mannslieb (z godziną widoczności sierpa po zachodzie słońca)
- najbliższe wydarzenie sezonowe (wiosna, lato, jesień, zima)
- święta interkalarne: Hexentag, Mitterfruhl, Sonnstill, Mittherbst, Mondstille
- Hexennacht i Geheimnisnacht
- jeśli wydarzenie właśnie trwa — **TRWA TERAZ** z godziną zakończenia RL

## Jak to działa

- przy wywołaniu `/imperium` pakiet sam wysyła komendę `czas` i parsuje odpowiedź serwera (linia jest ukrywana z okna gry)
- odczytany czas zapisuje się jako **kotwica** (czas IG + timestamp RL); przy kolejnych wywołaniach czas jest ekstrapolowany z kotwicy, bez dodatkowych zapytań
- jeśli serwer nie odpowie na `czas` w ciągu 3,5 s i nie ma zapisanej kotwicy, zobaczysz komunikat o błędzie

---

## Problemy z instalacją

Objaw: `installPackage` zwraca `true`, ale pakiet nie pojawia się na liście i komenda `/imperium` nie działa.

Przyczyna: znany błąd Mudleta — jeśli wcześniejsza próba instalacji się nie powiodła (np. przerwane pobieranie, podwójna instalacja), w katalogu profilu zostaje martwy folder pakietu i każda kolejna instalacja po cichu się nie udaje. Ponawianie nie pomaga — folder trzeba usunąć ręcznie.

Naprawa:

1. W linii poleceń Mudleta wpisz `lua getMudletHomeDir()` i otwórz wyświetlony katalog
2. Skasuj folder `imperium_cal` oraz ewentualny folder nazwany jak pobrany plik bez rozszerzenia (np. `imperium_cal_1_8_12m`) — to martwe resztki
3. Zrestartuj profil
4. Zainstaluj pakiet przez **Toolbox → Package Manager** (`Alt+O`) → **Install**
5. Sprawdź `lua getPackages()` — pakiet powinien być na liście, a komenda działać

Jeśli nadal się nie instaluje, sprawdź konsolę główną pod kątem linii `[ ERROR ]` lub `[ WARN ]` tuż po instalacji.

---

## Uwagi

- przelicznik czasu: 2 sekundy RL = 1 minuta IG (1 godzina gry = 120 s RL)
- Kalendarz Imperialny: 400 dni (17 pozycji: 12 miesięcy + 5 świąt interkalarnych)
- źródłem czasu jest wyłącznie komenda `czas` — pakiet nie zależy od GMCP
- wersja `1.8.12m` bazuje na imperium_cal 1.8.12 (Dargoth)
