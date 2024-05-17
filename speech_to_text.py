import nbformat as nbf

def generate_notebook():
    # Create a new notebook
    nb = nbf.v4.new_notebook()

    # Markdown content for the notebook cells
    markdown_cells = [
        "# Transcribing Audio with Google Cloud Speech-to-Text API",
        "",
        "This notebook demonstrates how to transcribe an audio file using the Google Cloud Speech-to-Text API.",
        "",
        "## Step 1: Prerequisites",
        "",
        "- Google Cloud Platform (GCP) account.",
        "- Project set up on GCP.",
        "- Google Cloud SDK installed.",
        "- Python installed.",
        "- Audio file to transcribe.",
        "",
        "## Step 2: Set Up Google Cloud Speech-to-Text API",
        "",
        "1. Go to the [Google Cloud Console](https://console.cloud.google.com/).",
        "2. Enable the Cloud Speech-to-Text API for your project.",
        "3. Create a service account key and download the JSON file containing your credentials.",
        "",
        "## Step 3: Install Required Python Packages",
        "",
        "```bash",
        "!pip install google-cloud-speech",
        "```",
        "",
        "## Step 4: Write Python Script",
        "",
        "Create a Python script with the following code:",
        "",
        "```python",
        "import io",
        "from google.cloud import speech_v1p1beta1 as speech",
        "",
        "# Insert the code snippet for transcribing audio here",
        "```",
        "",
        "Replace `'path/to/your/credentials.json'` with the path to your Google Cloud service account credentials JSON file, and `'path/to/your/audio/file.wav'` with the path to your audio file.",
        "",
        "## Step 5: Run the Script",
        "",
        "Run the script in your Jupyter Notebook or from the command line.",
        "",
        "## Step 6: Verify Results",
        "",
        "Check the output to verify that the transcribed text matches the content of your audio file."
    ]

    # Add markdown cells to the notebook
    for cell_content in markdown_cells:
        nb['cells'].append(nbf.v4.new_markdown_cell(cell_content))

    # Write the notebook to a file
    nbf.write(nb, 'transcribe_audio_with_gcp_api.ipynb')

if __name__ == "__main__":
    generate_notebook()

