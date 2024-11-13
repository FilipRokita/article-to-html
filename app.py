import openai

# Set API key
openai.api = "TEST123123"

# Define main function, on top for readability
def main():
    article_text = "Lorem Ipsum" # TODO: Load article from file
    html_content = "Lorem Ipsum" # TODO: Generate HTML content from article

# Define function to load article from file
def load_article(filename):
    with open(filename, 'r') as file:
        return file.read()

# Start the program if this script is run directly
if __name__ == "__main__":
    main()