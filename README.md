# Konwerter Artykułów do HTML

Ten skrypt w Pythonie umożliwia konwersję artykułu tekstowego do uporządkowanego dokumentu HTML, wykorzystując model GPT-4o od OpenAI. Skrypt generuje kod HTML na podstawie dostarczonego tekstu artykułu i zapisuje go do pliku.

Interfejs użytkownika jest po polsku, co ułatwia obsługę, a reszta kodu jest w języku angielskim, co zapewnia lepszą kompatybilność z narzędziami i bibliotekami oraz ułatwia rozwój i wsparcie globalne.

## Funkcje

- Wczytywanie tekstu artykułu z pliku
- Generowanie strukturalnego kodu HTML
- Zapisywanie wygenerowanego kodu HTML do pliku
- Prosty interfejs wiersza poleceń

## Wymagania

- Python 3.x+
- Klucz API OpenAI (wymaga konta OpenAI)
- Plik `.env` zawierający klucz API OpenAI.
- Zainstalowane biblioteki `openai` i `python-dotenv`.

## Instalacja

1. Sklonuj lub pobierz repozytorium na swoją maszynę.

2. Zainstaluj wymagane biblioteki Python za pomocą pip:

   ```bash
   pip3 install -r requirements.txt
   ```

3. Stwórz plik `.env` w tym samym katalogu co skrypt, o następującej zawartości:

   ```
   OPENAI_API_KEY=twój_klucz_api_openai
   ```

   Zamień `twój_klucz_api_openai` na swój rzeczywisty klucz API OpenAI.

## Użycie

1. Umieść artykuł, który chcesz skonwertować do HTML, w pliku tekstowym `artykul_tekst.txt`
2. Uruchom skrypt:

   ```bash
   python3 main.py
   ```

3. Skrypt wykona następujące czynności:
   - Wczyta artykuł z podanego pliku.
   - Wygeneruje kod HTML przy pomocy OpenAI.
   - Zapisze wygenerowany kod HTML do pliku `artykul.html`.
   - Wyświetli komunikat o pomyślnym wygenerowaniu i zapisaniu HTML.

## Przegląd kodu

`main()`  
Główna funkcja, która konfiguruje program, ładuje artykuł, generuje HTML i zapisuje go do pliku.

`configure()`  
Konfiguruje klienta OpenAI, ładując klucz API z pliku .env za pomocą biblioteki `python-dotenv`.

`load_article(filename)`  
Ładuje artykuł z podanego pliku.

`generate_html_content(article_text)`  
Generuje HTML z artykułu, korzystając z modelu GPT-4o. HTML jest strukturalnie organizowany według wytycznych.

`save_html_content(html_content, filename)`  
Zapisuje wygenerowany kod HTML do wskazanego pliku.

## Autor
Filip Rokita  
[www.filiprokita.com](https://www.filiprokita.com/)