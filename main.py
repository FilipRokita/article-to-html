# Filip Rokita
# www.filiprokita.com


# Import necessary modules
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
    # Load API key from .env file
    load_dotenv()

    # Create global OpenAI client variable and load API key
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
    Jesteś ekspertem w tworzeniu stron internetowych i generowaniu kodu HTML. Chcę, abyś wygenerował strukturalny HTML dla poniższego artykułu, stosując się do następujących wytycznych:
    1. Użyj odpowiednich tagów HTML do strukturyzacji treści, takich jak <h1>, <h2>, <h3> dla nagłówków oraz <p> dla paragrafów. W razie potrzeby możesz użyć list i innych standardowych tagów HTML, aby czytelnie przedstawić informacje.
    2. W miejscach, gdzie warto wstawić grafikę, dodaj tag <img src="image_placeholder.jpg">. Każdy tag <img> musi mieć atrybut alt z dokładnym opisem grafiki. Atrybut alt powinien zawierać precyzyjny prompt, który można użyć do wygenerowania odpowiedniej grafiki. Pod każdą grafiką umieść podpis, stosując odpowiedni tag HTML, aby wskazać jej temat.
    3. Kod HTML nie powinien zawierać CSS ani JavaScript. Wygenerowany HTML powinien zawierać wyłącznie kod przeznaczony do wstawienia pomiędzy tagi <body> i </body>. Nie dodawaj tagów <html>, <head>, ani <body>.
    4. Nie używaj żadnych znaków Markdown (np. backticków) ani innych formatów tekstowych. Treść ma być czystym kodem HTML.
    Oto treść artykułu:
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
    # return response.model_dump()['choices'][0]['message']['content']
    return response.choices[0].message.content


# Define function to save HTML content to file
def save_html_content(html_content, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(html_content)


# Start the program if this script is run directly
if __name__ == '__main__':
    main()