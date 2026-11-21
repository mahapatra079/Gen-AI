# Gen-AI

Python tutorials and examples.

## Repository structure

```text
Gen-AI/
├── python_tutorials/
├── .gitignore
├── requirements.txt
├── send_request.py
├── README.md
└── venv/ (local only; excluded from Git)
```

## Set up the environment

Create and activate a virtual environment, then install the project dependencies:

```powershell
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install Streamlit
pip install streamlit

# Install NumPy
pip install numpy
```

## Run the Streamlit app

From the repository root, change to the Streamlit folder and run:

```powershell
cd python_tutorials\Streamlit
python -m streamlit run app.py
```

Keep the terminal open while the app is running. Streamlit prints a local URL,
usually `http://localhost:8501`. If the browser does not open automatically,
open that URL manually.

The `venv/` folder is local to your machine and is not included in Git. Each
developer should create their own environment using the commands above.