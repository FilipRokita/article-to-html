from dotenv import load_dotenv
from openai import OpenAI
import os


# Define main function, on top for better readability
def main():
    # Configure program
    configure()

    # Load article from file
    article_text = load_article('Zadanie dla JJunior AI Developera - tresc artykulu.txt')

    # Generate HTML content from article text using OpenAI
    html_content = generate_html_content(article_text)

    # Save HTML content to file and print message
    save_html_content(html_content, 'artykul.html')
    print('HTML został wygenerowany i zapisany do pliku.')


# Define function to configure program
def configure():
    load_dotenv()

    global client
    client = OpenAI(
        api_key=os.getenv('OPENAI_API_KEY')
        )


# Define function to load article from file
def load_article(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


# Define function to generate HTML content from article text using OpenAI
def generate_html_content(article_text):
    # Define prompt for OpenAI
    prompt = f'''
    Jesteś ekspertem od tworzenia stron internetowych. Przygotuj HTML dla poniższego artykułu, stosując odpowiednie tagi HTML. 
    1. Struktura tekstu powinna obejmować nagłówki, paragrafy oraz miejsca na obrazy.
    2. Użyj tagów <img src="image_placeholder.jpg"> z atrybutem alt, gdzie to konieczne, wraz z podpisami pod grafikami.
    3. Tylko zawartość między <body> i </body>, bez tagów <html>, <head> i <body>.
    Oto artykuł:
    {article_text}
    '''

    # Generate HTML content using OpenAI
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    # Return generated HTML content
    return response.model_dump()['choices'][0]['message']['content']


# Define function to save HTML content to file
def save_html_content(html_content, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(html_content)


# Start the program if this script is run directly
if __name__ == '__main__':
    main()