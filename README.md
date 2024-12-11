# Munich Sushi & Parking Assistant

An AI-powered assistant that helps users find sushi restaurants and parking spots in Munich. The assistant uses GPT-3.5-turbo to understand user queries and provide relevant information from a mock database.

## Setup

1. Clone the repository
2. Create a virtual environment and activate it:
```bash
python -m venv .venv       
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

3. Install requirements
```bash
pip install -r requirements.txt
```

4. Install the project in editable mode:
```bash
pip install -e .
```

5. Create a `.env` file in the root directory with your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Running the Project

There are three ways to interact with the assistant:

### 1. Jupyter Notebook
Explore the detailed implementation and test different scenarios:
```file
application.ipynb
```

### 2. Terminal Chat
Start an interactive chat session in the terminal:
```bash
python src/main_terminal.py
```

### 3. FastAPI Endpoint
Run a local API server:
```bash
python src/main_api.py
```
The API will be available at `http://localhost:8000`

- Swagger UI: `http://localhost:8000/docs`

## Features

- Dynamic function calling with instructor
- Checks users intend and selects response model
- Support for both sushi restaurant and parking queries (can switch in one session)
- Information about:
  - Restaurant locations, hours, and reviews
  - Parking spot availability and pricing
  - Distance from current location
  - Payment methods

## Project Structure

- `application.ipynb`: Detailed walkthrough of the assistant's functionality
- `src/main_terminal.py`: Terminal-based chat interface
- `src/main_api.py`: FastAPI server implementation
- `src/services/`: Core business logic and data handling
- `src/models/`: Pydantic models for type safety
- `src/data/`: Mock database JSON files
