
# Key Insights Generator

The **Key Insights Generator** is a web application designed to extract meaningful insights from long stories or documents. It analyzes text to generate specific insights based on user queries, such as productivity tips, career guidance, or life hacks. The application supports multiple input methods, including file uploads (`TXT`, `PDF`, `DOCX`) and direct text input.

## Features
- **Multiple Input Options**:
  - Upload text files (`TXT`), PDF files (`PDF`), or Word documents (`DOCX`).
  - Type or paste text directly into the application.
- **Custom Insight Generation**:
  - Enter a specific topic (e.g., productivity, career advice) to generate relevant insights.
- **Efficient Text Processing**:
  - Handles large documents by chunking them into manageable parts for analysis.
- **Streamlit Interface**:
  - User-friendly interface with real-time interaction and insight display.
- **Support for ChatGPT Models**:
  - Uses OpenAI's `gpt-3.5-turbo` to provide intelligent and context-aware insights.

## How It Works
1. **Input the Story**:
   - Upload a file (`TXT`, `PDF`, `DOCX`) or paste the story directly.
2. **Specify the Insight Type**:
   - Enter the topic you want insights on (e.g., productivity).
3. **Generate Insights**:
   - Click the "Generate Insights" button to process the text and retrieve topic-specific insights.
4. **View Results**:
   - Display the insights in a clear, user-friendly format.

## Tools and Technologies Used
- **Frontend**:
  - [Streamlit](https://streamlit.io/) for creating an interactive web interface.
- **Backend**:
  - [LangChain](https://langchain.com/) for managing and processing language model interactions.
  - OpenAI's `gpt-3.5-turbo` for generating insights.
- **File Handling**:
  - `PyPDF2` for extracting text from PDF files.
  - `python-docx` for extracting text from Word documents.
- **Environment Management**:
  - `python-dotenv` for securely managing API keys.
- **Text Processing**:
  - LangChain's `CharacterTextSplitter` for splitting large texts into manageable chunks.

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/key-insights-generator.git
   cd key-insights-generator
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Add Your OpenAI API Key**:
   - Create a `.env` file in the project directory.
   - Add your OpenAI API key:
     ```plaintext
     OPENAI_API_KEY=your_openai_api_key
     ```

4. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

5. **Access the Web App**:
   - Open your browser and navigate to `http://localhost:8501`.

## Sample Use Cases
- Extracting productivity-related insights from a self-help book.
- Summarizing career advice from a long blog or article.
- Analyzing and retrieving key takeaways from meeting notes or documentation.

## Project Structure
```
.
├── app.py                 # Main application file
├── requirements.txt       # List of dependencies
├── .env                   # File to store API keys (not included in Git)
├── README.md              # Project documentation
```

## Future Enhancements
- Add support for more file formats (e.g., `EPUB`).
- Include advanced filtering options for insights.
- Extend support to `GPT-4` and other models for more nuanced insights.
- Implement user authentication for personalized experiences.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
