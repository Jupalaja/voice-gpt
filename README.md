# Voice-assistant using chatgpt and whisper APIs

This repository contains a Python script that transcribes audio using the OpenAI's Whisper API and initiates a chat using OpenAI's GPT-3.5-Turbo model.

## Prerequisites
- [ffmpeg](https://ffmpeg.org/) needs to be installed on your system for audio - processing.
- [Python](https://www.python.org/downloads/release/python-3100/) (version 3.10 recommended) needs to be installed.

## Clone the Repository
------------
To clone this repository, run the following command in your terminal:

```
git clone https://github.com/Jupalaja/voice-gpt.git
```

## Create a Virtual Environment
------------
It is recommended to create a virtual environment to avoid conflicts with other installed Python libraries. To create a virtual environment called `venv`, run the following command in your terminal:

```
python3.10 -m venv venv
```
This will create a virtual environment named env in your current directory. 

## Activate the virtual Environment
------------
To activate the virtual environment, run the following command in your terminal:
```
source env/bin/activate
```
## Install Required Libraries
------------
To install the required libraries, run the following command in your terminal:
```
pip install -r requirements.txt
```

## Setting up the Virtual Environment in Jupyter Notebook
------------
I find Jupyter Notebooks to be helpful for faster project understanding and setup. The notebook can later be converted to `.py` files. Let's make use of the `ipykernel` library to create a kernel for the virtual environment. This will allow us to use the virtual environment in Jupyter Notebook.

```
python -m ipykernel install --user --name=voicegpt
```

Now let's convert the Jupyter notebook to Python scripts using nbconvert, which is useful for running the code locally.
```
jupyter nbconvert --to script voice_assistant.ipynb
```

## Contributing
------------

If you would like to contribute to this project, please open an issue or submit a pull request.


## License
------------

The source code for the site is licensed under the MIT license, which you can find in the LICENSE.md file.

