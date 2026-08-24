# Kalendarz Imperium — Mudlet

Pakiet do Mudleta: kalendarz domeny Imperium (Kalendarz Imperialny) dla Arkadii MUD. Komenda `/imperium` pokazuje przybliżony czas do najbliższych wydarzeń księżycowych, sezonowych i świąt — RL i IG.

Port pluginu [imperium_cal z klienta Dargoth](https://github.com/Isithunzi000/arkadia-dargoth-plugins) .

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
| `/imperium reset` | czyści zapisaną datę (kotwicę) |
| `/imperium aktualizuj` | sprawdza i instaluje aktualizację z GitHub Releases |

## Co pokazuje

- najbliższy nów i pełnię Mannslieb (z godziną widoczności sierpa po zachodzie słońca)
- najbliższe wydarzenie sezonowe (wiosna, lato, jesień, zima)
- święta interkalarne: Hexentag, Mitterfruhl, Sonnstill, Mittherbst, Mondstille
- Hexennacht i Geheimnisnacht
- jeśli wydarzenie właśnie trwa — **TRWA TERAZ** z godziną zakończenia RL

## Jak to działa

- przy wywołaniu `/imperium` pakiet sam wysyła komendę `czas` i parsuje odpowiedź serwera (linia jest ukrywana z okna gry)
- udany odczyt zapisuje się jako **kotwica** (czas IG + timestamp RL) — to zapas na wypadek błędu odczytu, nie skrót: pakiet zawsze pyta serwer
- kotwica odnawia się też **pasywnie**: każda poprawna odpowiedź serwera na `czas` zapisuje datę, nawet gdy nikt nie wywołał `/imperium` (np. gdy o `czas` poprosił inny pakiet) — linia zostaje wtedy w oknie gry i nie ma raportu
- kotwica zapisuje się na dysku profilu (`imperium_cal_anchor_v2.lua`) i przeżywa restart klienta; uszkodzony, stary albo obcy plik jest po cichu ignorowany; `/imperium reset` usuwa kotwicę z dysku i pamięci
- gdy odczyt `czas` się nie powiedzie albo postać jest w innej domenie, pakiet liczy z zapisanej daty i **mówi o tym** — przed raportem pojawia się linia „Pokazuje Imperium wyliczone z zapisanej daty (ostatni odczyt: …)"
- gdy zapisanej daty nie ma, pakiet wyświetla komunikat zamiast zgadywać
- jeśli serwer nie odpowie na `czas` w ciągu 3,5 s i nie ma zapisanej daty, zobaczysz komunikat o błędzie
- gdy odpowiedź przyjdzie po upływie timeoutu (np. przez throttle'owanie timerów w mudlet-web), linia `czas` zostaje widoczna, a pakiet zapisuje tylko kotwicę — bez raportu i bez komunikatów (paritet z klientami przeglądarkowymi)

> W mudlet-web (Mudlet w przeglądarce) zapis działa przez IndexedDB — per origin i profil, best-effort (np. czyszczenie danych przeglądarki kasuje kotwicę).

---

## Aktualizacje

Pakiet sam sprawdza aktualizacje: przy starcie klienta (nie częściej niż co 8 godzin) pyta o najnowsze wydanie na GitHubie i — jeśli jest nowsza wersja — wyświetla powiadomienie. Sam nic nie instaluje: aktualizację uruchamiasz świadomie komendą `/imperium aktualizuj`, która pobiera paczkę, podmienia ją i prosi o restart Mudleta.

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
