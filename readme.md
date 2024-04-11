Here's how you can update the README file to include instructions for running the Streamlit application from a zip file on a Mac:

1. **Download and Extract the Zip File**: 
   - Download the zip file containing the Streamlit application.
   - Extract the contents of the zip file to a directory on your Mac.

2. **Install Poetry**: 
   - If you haven't already, install Poetry by following the instructions on the official website: [https://python-poetry.org/docs/#installation](https://python-poetry.org/docs/#installation).

3. **Navigate to the Project Directory**: 
   - Open a terminal window.
   - Change your current directory to the project directory where you extracted the zip file.

     ```bash
     cd path/to/your/directory
     ```

4. **Install Dependencies**: 
   - Use Poetry to install the project dependencies specified in the `pyproject.toml` file.

     ```bash
     poetry install
     ```

5. **Activate the Virtual Environment**: 
   - Activate the Poetry-managed virtual environment to ensure that the installed dependencies are isolated.

     ```bash
     poetry shell
     ```

6. **Run the Streamlit Application**: 
   - Use the `streamlit run` command followed by the path to your Streamlit application Python file to start the application.

     ```bash
     streamlit run test_app.py
     ```

7. **Access the Application**: 
   - Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`) to view and interact with your Streamlit application.

8. **Make Changes**: 
   - If you need to make changes to your Streamlit application, simply edit the Python code files and save them. Streamlit will automatically update the application in your browser.

9. **Stop the Application**: 
   - To stop the Streamlit application, press `Ctrl + C` in the terminal where the application is running.