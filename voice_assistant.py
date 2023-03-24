#!/usr/bin/env python
# coding: utf-8

# # Voice Assistant Using ChatGPT and Whisper APIs

# Import necessary libraries

# In[2]:


import gradio as gr
import openai, config, subprocess
from pydub import AudioSegment


# Set OpenAI API key and Define initial system message

# In[4]:


openai.api_key = config.OPENAI_API_KEY
messages = [{"role": "system", "content": 'You are a Helpful assistant, respond in 30 words or less'}]


# Define the transcribe function that transcribes audio using OpenAI

# In[5]:


def transcribe(audio):
    global messages

    audio_file_wav = open(audio, "rb")
    audio_file_mp3 = AudioSegment.from_wav(audio_file_wav).export("audio.mp3", format="mp3")
    transcript = openai.Audio.transcribe("whisper-1", audio_file_mp3)

    messages.append({"role": "user", "content": transcript["text"]})

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    system_message = response["choices"][0]["message"]
    messages.append(system_message)

    subprocess.call(["say", system_message['content']])

    chat_transcript = ""
    for message in messages:
        if message['role'] != 'system':
            chat_transcript += message['role'] + ": " + message['content'] + "\n\n"

    return chat_transcript


# Create a Gradio interface for the transcribe function

# In[7]:


ui = gr.Interface(fn=transcribe, inputs=gr.Audio(source="microphone", type="filepath"), outputs="text")
ui.launch()


# In[ ]:




