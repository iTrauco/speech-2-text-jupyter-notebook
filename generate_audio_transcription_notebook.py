#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#!/usr/bin/env python

def create_notebook():
    notebook_content = """
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Audio Transcription Guide\\n",
    "\\n",
    "This notebook provides instructions for recording audio on Linux and transcribing it using the Google Cloud Speech-to-Text API.\\n",
    "\\n",
    "## Recording Audio on Linux\\n",
    "\\n",
    "### Using arecord (ALSA Project)\\n",
    "\\n",
    "#### 1. Install `alsa-utils`\\n",
    "If you haven't already installed `alsa-utils`, you can do so using your package manager. For example, on Debian/Ubuntu-based systems:\\n",
    "\\n",
    "```bash\\n",
    "sudo apt-get install alsa-utils\\n",
    "```\\n",
    "\\n",
    "#### 2. Record Audio\\n",
    "Use the `arecord` command to capture audio. For example, to record audio for 10 seconds and save it to a WAV file:\\n",
    "\\n",
    "```bash\\n",
    "arecord -f cd -t wav -d 10 -r 44100 -D hw:0,0 audio.wav\\n",
    "```\\n",
    "\\n",
    "### Using sox (Sound eXchange)\\n",
    "\\n",
    "#### 1. Install `sox`\\n",
    "If you haven't already installed `sox`, you can do so using your package manager. For example, on Debian/Ubuntu-based systems:\\n",
    "\\n",
    "```bash\\n",
    "sudo apt-get install sox\\n",
    "```\\n",
    "\\n",
    "#### 2. Record Audio\\n",
    "Use the `rec` command from `sox` to capture audio. For example, to record audio for 10 seconds and save it to a WAV file:\\n",
    "\\n",
    "```bash\\n",
    "rec -r 44100 -c 2 audio.wav trim 0 10\\n",
    "```\\n",
    "\\n",
    "## Transcribing Audio Using Google Cloud Speech-to-Text API\\n",
    "\\n",
    "### 1. Set Up Google Cloud Speech-to-Text API\\n",
    "Follow the instructions provided earlier to enable the Speech-to-Text API for your Google Cloud project and create a service account key.\\n",
    "\\n",
    "### 2. Install Required Python Packages\\n",
    "Install the `google-cloud-speech` Python package using pip:\\n",
    "\\n",
    "```bash\\n",
    "pip install google-cloud-speech\\n",
    "```\\n",
    "\\n",
    "### 3. Write Python Script\\n",
    "Create a Python script that reads the recorded audio files, transcribes them using the Speech-to-Text API, and prints the transcribed text. You can use the script provided earlier as a starting point.\\n",
    "\\n",
    "### 4. Run the Script\\n",
    "Run the Python script from the command line, passing the path to the recorded audio file as an argument:\\n",
    "\\n",
    "```bash\\n",
    "python transcribe_audio.py audio.wav\\n",
    "```\\n",
    "\\n",
    "Replace `audio.wav` with the path to your recorded audio file.\\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
"""
    with open("audio_transcription_guide.ipynb", "w") as f:
        f.write(notebook_content)

if __name__ == "__main__":
    create_notebook()

