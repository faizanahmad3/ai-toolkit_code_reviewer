# Project Title
AI Toolkit Code Reviewer

## Description
AI Toolkit Code Reviewer is an intelligent code review tool designed to automate the evaluation of programming assignments, projects, and assessments.

## Key Features
- Automated code review using GPT-4.
- Supports Python, Flutter, and Angular projects.
- Customizable criteria for evaluation.

## Installation
### Prerequisites
- Python 3.x
- OpenAI API Key
- Other dependencies (e.g., FASTAPI, zipfile)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/faizanahmad3/ai-toolkit_code_reviewer
   cd ai-toolkit_code_reviewer
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables for your OpenAI API key:
   ```bash
   export OPENAI_API_KEY='your-openai-api-key'
   ```
   
4. Set up environment variables for your FAST_API_KEY:
   ```bash
   export FAST_API_KEY='your-FAST_API_KEY'
   ```

5. Run the application:
   ```bash
   python main.py
   ```

## Usage
### API Endpoints
- **POST /upload_zip-file**: Upload a zip file to extract.
- **POST /analyze_code**: Review the code in the extracted folder.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request.

## License
This project is licensed under the MIT License.

## Contact
For any inquiries, contact [faizanahmad2468@gmail.com](mailto:your-email@example.com).
