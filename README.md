
# Article Converter to HTML

This Python script allows converting a text article into a structured HTML document using the GPT-4o model from OpenAI. The script generates HTML code based on the provided article text and saves it to a file.

## Features

- Load article text from a file
- Generate structured HTML code
- Save the generated HTML code to a file
- Simple command-line interface

## Requirements

- Python 3.x+
- OpenAI API Key (requires an OpenAI account)
- A `.env` file containing the OpenAI API key
- Installed `openai` and `python-dotenv` libraries

## Installation

1. Clone or download the repository to your machine.

2. Install the required Python libraries using pip:

   ```bash
   pip3 install -r requirements.txt
   ```

3. Create a `.env` file in the same directory as the script, with the following content:

   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

   Replace `your_openai_api_key` with your actual OpenAI API key.

## Usage

1. Place the article you want to convert to HTML in a text file named `article_text.txt`.
2. Run the script:

   ```bash
   python3 main.py
   ```

3. The script will perform the following steps:
   - Load the article from the specified file.
   - Generate HTML code using OpenAI.
   - Save the generated HTML code to a file named `article.html`.
   - Display a message indicating successful generation and saving of the HTML.

## Code Overview

`main()`  
The main function that sets up the program, loads the article, generates HTML, and saves it to a file.

`configure()`  
Configures the OpenAI client by loading the API key from the `.env` file using the `python-dotenv` library.

`load_article(filename)`  
Loads the article from the specified file.

`generate_html_content(article_text)`  
Generates HTML from the article using the GPT-4o model. The HTML is structurally organized according to guidelines.

`save_html_content(html_content, filename)`  
Saves the generated HTML code to the specified file.

## Author

Filip Rokita  
[www.filiprokita.com](https://www.filiprokita.com/)
