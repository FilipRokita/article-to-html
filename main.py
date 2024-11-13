import openai

# Set API key
openai.api = "TEST123123"


# Define main function, on top for readability
def main():
    article_text = load_article("Zadanie dla JJunior AI Developera - tresc artykulu.txt")
    html_content = "Lorem Ipsum" # TODO: Generate HTML content from article


# Define function to load article from file
def load_article(filename):
    with open(filename, 'r') as file:
        return file.read()


# Define function to generate HTML content from article text using OpenAI
def generate_html_content(article_text):
    # Define prompt for OpenAI
    prompt = f"""
    Jesteś ekspertem od tworzenia stron internetowych. Przygotuj HTML dla poniższego artykułu, stosując odpowiednie tagi HTML. 
    1. Struktura tekstu powinna obejmować nagłówki, paragrafy oraz miejsca na obrazy.
    2. Użyj tagów <img src="image_placeholder.jpg"> z atrybutem alt, gdzie to konieczne, wraz z podpisami pod grafikami.
    3. Tylko zawartość między <body> i </body>, bez tagów <html>, <head> i <body>.
    Oto artykuł:
    {article_text}
    """

    # Generate HTML content using OpenAI
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2000,
        temperature=0.7
    )

    # Return generated HTML content
    return response.choices[0].text.strip()


# Start the program if this script is run directly
if __name__ == "__main__":
    main()