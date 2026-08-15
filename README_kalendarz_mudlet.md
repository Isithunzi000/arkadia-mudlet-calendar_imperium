# Kalendarz Imperium & Ishtar — pakiety Mudlet

Porty pluginów kalendarza z klienta Dargoth (Arkadia web client) do klienta Mudlet. Źródłem czasu jest wyłącznie komenda `czas` — bez zależności od GMCP.

## Instalacja

1. Otwórz Mudlet i połącz się z Arkadią.
2. Idź do **Toolbox** → **Package Manager** (lub `Alt+O`).
3. Kliknij **Install** i wybierz plik `.mpackage`. Powtórz dla drugiego pakietu.

Alternatywnie, w linii poleceń Mudlet:
```
lua installPackage("/sciezka/do/imperium_cal.mpackage")
lua installPackage("/sciezka/do/ishtar_cal.mpackage")
```

> Paczka powinna się znajdować powyżej skryptów ogólnodostępnych Arkadii. Ustaw to w Package Manager przesuwając paczkę w górę listy.

## Problemy z instalacją

Objaw: `installPackage` zwraca `true`, ale pakiet nie pojawia się na liście w Package Manager i komenda (`/imperium` lub `/ishtar`) nie działa.

Przyczyna: znany błąd Mudleta — jeśli wcześniejsza próba instalacji się nie powiodła (np. przerwane pobieranie pliku, podwójna instalacja), w katalogu profilu zostaje martwy folder pakietu i każda kolejna instalacja po cichu się nie udaje. Ponawianie instalacji nie pomaga — folder trzeba usunąć ręcznie.

Naprawa:

1. W linii poleceń Mudlet wpisz `lua getMudletHomeDir()` i otwórz wyświetlony katalog.
2. Skasuj folder pakietu, którego dotyczy problem — `imperium_cal` lub `ishtar_cal` — oraz ewentualny folder nazwany jak pobrany plik bez rozszerzenia (np. `ishtar_cal_1_8_11m`). To martwe resztki; poprawnie zainstalowany pakiet byłby widoczny na liście.
3. Zrestartuj profil.
4. Zainstaluj pakiet przez **Toolbox** → **Package Manager** (`Alt+O`) → **Install**.
5. Sprawdź `lua getPackages()` — pakiet powinien być na liście, a komenda działać.

Jeśli pakiet nadal się nie instaluje, sprawdź konsolę główną pod kątem linii `[ ERROR ]` lub `[ WARN ]` tuż po instalacji i zgłoś problem na Discordzie.

## Użycie

| Komenda | Opis |
|---------|------|
| `/imperium` | Kalendarz Imperium |
| `/imperium help` | Pomoc do kalendarza Imperium |
| `/ishtar` | Kalendarz Ishtar |
| `/ishtar help` | Pomoc do kalendarza Ishtar |

Zamiast `help` można użyć `pomoc`.

## Co wyświetla

### /imperium

- Najbliższy nów i pełnia Mannslieb
- Nów widoczny po zachodzie słońca
- Najbliższe wydarzenie sezonowe
- Hexentag, Hexennacht, Geheimnisnacht
- Pozostałe święta interkalarne
- Jeśli event aktualnie trwa — `TRWA TERAZ` z godziną zakończenia RL

### /ishtar

- Belleteyn i Saovine (główne święta magiczne)
- Święta astronomiczne i magiczne (Midinvaerne, Birke, Midaete, Velen, Imbaelk, Lammas)
- Pełnia księżyca
- Festyn w Eysenlaan — dwa najbliższe wystąpienia (od–do)
- Jeśli event aktualnie trwa — `TRWA TERAZ` z godziną zakończenia RL

## Jak to działa

Po wpisaniu `/imperium` lub `/ishtar` plugin automatycznie wysyła komendę `czas` i parsuje odpowiedź serwera. Linia `czas` jest usuwana z okna gry.

Odczytany czas IG jest zapisywany jako **kotwica** (czas IG + timestamp RL). Przy każdym kolejnym uruchomieniu plugin ekstrapoluje aktualny czas IG z kotwicy według przelicznika:

- 1 minuta gry = 2 sekundy czasu rzeczywistego
- 1 godzina gry = 120 sekund czasu rzeczywistego

Jeśli komenda `czas` nie zwróci odpowiedzi w ciągu 3,5 sekundy i nie ma zapisanej kotwicy, plugin wyświetli komunikat o błędzie.

## Wersja

| Pakiet | Wersja | Data | Bazuje na |
|--------|--------|------|-----------|
| `imperium_cal` | 1.8.12m | 15-08-2026 | imperium_cal 1.8.12 (Dargoth) |
| `ishtar_cal` | 1.8.11m | 24-06-2026 | ishtar_cal 1.8.11 (Dargoth) |
