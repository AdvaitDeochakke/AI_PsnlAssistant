# Project Overview
Voice-Powered Personal Assistant with AI Capabilities
This project is the development of a voice-powered personal assistant with artificial intelligence (AI) capabilities. The assistant is designed to perform various tasks based on voice input from the user. Here's a high-level overview of the project components and functionality:

## 1. Speech Recognition
The project uses the speech_recognition library to convert spoken language into text. Users can interact with the assistant by speaking commands or queries.

## 2. Natural Language Processing with GPT-3.5
The core of this assistant's intelligence is powered by OpenAI's GPT-3.5 Turbo model. It takes the user's text input and generates responses, providing concise and informative answers to user queries.

## 3. Contextual Information Retrieval
The assistant leverages the Weaviate API to retrieve contextual information related to the user's input. It searches for articles or data in a database that may be relevant to the user's query and provides context.

## 4. Text-to-Speech (TTS)
The project incorporates text-to-speech capabilities using the pyttsx3 library. This enables the assistant to respond to the user with spoken words, enhancing the user experience.

## 5. Additional Features
Emotion Detection: The project may include an emotion detection component to make the assistant's responses more human-like and empathetic.
Conversation Memory: The assistant might have the ability to remember past interactions and refer back to them in the conversation.

## 6. Function Integration
The project introduces the concept of integrating functions into the assistant's capabilities. For example, it can retrieve real-time weather information using the get_current_weather function.

## 7. User-Friendly Response
The assistant's responses are designed to be user-friendly, concise, and under 100 words. It provides answers to user queries and can also perform specific tasks as requested.

## 8. Project Evolution
The project's development has evolved over time, with initial inspiration from AI Vtuber "Neuro-Sama." It aims to create a comprehensive and knowledgeable assistant capable of handling a wide range of user queries and tasks.

## 9. Future Plans
Future enhancements may include personalization, improved conversation memory, and further integration of AI capabilities to make the assistant even more versatile and helpful.

In summary, this project combines speech recognition, natural language processing, contextual information retrieval, and text-to-speech to create a voice-powered personal assistant with AI capabilities. It's designed to assist users with information retrieval and task execution in a user-friendly and efficient manner.

# Write stuff here
New Readme is AI Gen
I'll add it slowly
Basically Voice -> STT -> Keywords -> DB Query -> Context -> Reply Generation -> TTS

~~Need to add stuff like emotion detection, conversation memory, and more
Partially inspired by Nuero-Sama i guess~~

Change of plans, things evolved. Doing my own thing, trying to make a decent assisstant which knows things  
~~Checking out a different tts method, and changing API from davinci to chat completions~~  

Using pyttsx3 to access windows tts voices. Fast, enough quality. Obvioulously could try personalization but w/e  
Gonna work on functions with the gpt API, starting with weather retrieval  
(They have an example so it is easier to follow)
