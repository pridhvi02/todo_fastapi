# FastAPI Todo Application

This is a simple Todo application built with FastAPI.

## Setup

1. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

2. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:

    ```bash
    uvicorn app.main:app --reload
    ```

4. Open your browser and go to `http://127.0.0.1:8000/docs` to see the API documentation.
