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
    article_text = load_article('article_text.txt')

    # Generate HTML content from article text using OpenAI
    html_content = generate_html_content(article_text)

    # Save HTML content to file and print message
    save_html_content(html_content, 'article.html')
    print('HTML has been generated and saved to the file.')


# Define function to configure program
def configure():
    # Load environment variables from .env file
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
    I want you to generate structured HTML for the following article, adhering to these guidelines:
    1. Use appropriate HTML tags to structure the content, such as <h1>, <h2>, <h3> for headings and <p> for paragraphs. If needed, use lists and other standard HTML tags to present the information clearly.
    2. Where appropriate, include <img src="image_placeholder.jpg"> tags for images. Each <img> tag must have an alt attribute with an exact description of the image. The alt attribute should contain a precise prompt that can be used to generate the relevant image. Add a caption below each image using appropriate HTML tags to indicate its subject.
    3. The HTML code should not include CSS or JavaScript. The generated HTML should only contain code intended to go between the <body> and </body> tags. Do not include <html>, <head>, or <body> tags.
    4. Do not use Markdown characters (e.g., backticks) or other text formatting. The content should be pure HTML code.
    Here is the content of the article:
    {article_text}
    '''

    # Generate HTML content using OpenAI
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "You are an expert in web development and HTML code generation."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    # Return generated HTML content
    return response.choices[0].message.content


# Define function to save HTML content to file
def save_html_content(html_content, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(html_content)


# Start the program if this script is run directly
if __name__ == '__main__':
    main()