# Voice-Controlled Python Assistant

Welcome to the Voice-Controlled Python Assistant repository! This Python program serves as a versatile voice assistant, utilizing various modules to execute tasks based on user voice commands.

## Features:

- **Text-to-Speech:** The program utilizes the `pyttsx3` library for text-to-speech functionality, allowing the assistant to respond audibly.
- **Voice Recognition:** The `speech_recognition` module captures user voice input and converts it into text for processing.
- **Multifunctional Commands:** The assistant can perform the following tasks:

  1. **Wikipedia Search:**
     - Trigger: "Wikipedia"
     - Example: say : " Hello Wikipedia Python "

  2. **Music Playback:**
     - Triggers: "play music" or "play song"
     - Example: say : " Hello Play music "

  3. **Time Query:**
     - Trigger: "time"
     - Example: say : " Hello What's the time? "

  4. **Exit Program Command:**
     - Trigger: "exit"
     - Example: say : " Hello Exit "

  5. **Close An Opened Application:**
     - Trigger: "close"
     - Example: say : " Hello Close app Notepad "

  6. **Web Search or Play:**
     - Triggers: "search" or "play"
     - Example: say : " Hello Search OpenAI" or "Play jazz music "

  7. **System Shutdown:**
     - Trigger: "shutdown system"
     - Example: say : " Hello Shutdown system "

  8. **System Restart:**
     - Trigger: "restart system"
     - Example: say : " Hello Restart system "

  9. **System Hibernate or Sleep:**
     - Triggers: "hibernate system" or "sleep"
     - Example: say : " Hello Hibernate system" or "Sleep "

  10. **System Log Off:**
      - Triggers: "log off system" or "sign out"
      - Example: say : " Hello Log off system" or "Sign out "

  11. **Greeting:**
      - Trigger: "how are you"
      - Example: say : " Hello How are you? "

  12. **Application Opening:**
      - Trigger: "open + <appname> + app"
      - Example: say : " Hello Open Notepad App "

  13. **Website opening:**
      - Trigger: "Open  + <website name eg "google"> + .com"
      - Example: say : " Hello Open www.example.com "
  
  14. **Search Local Files:**
      - Trigger: "Open"
      - Example: say : " Hello <File Name> "

- **Continuous Interaction:** The program runs continuously, listening for user commands and responding dynamically.
  

## Prerequisites:

Before running the program, ensure that the following modules are installed:

- AppOpener
- pyttsx3
- speech_recognition
- wikipedia
- webbrowser

## Usage:

1. Clone the repository:

   ```bash
   gh repo clone FALLEN-01/Voice-Assistant
   ```

2. Install required modules:

   ```bash
   pip install AppOpener
   ```
   
   ```bash
   pip install pyttsx3
   ```
   ```bash
   pip install SpeechRecognition 
   ```
   ```bash
   pip install wikipedia
   ```
   ```bash
   pip install webbrowser
   ```
   

3. Run the program:

   ```bash
   python voice_assistant.py
   ```

## Customization:

Feel free to customize the assistant according to your preferences or extend its functionalities. The `hello` function in the code can be expanded to include new commands or actions.
information, examples, or usage scenarios based on your specific implementation.
If you feel hello isn't the word for you can change it in the code :

```bash
if 'hello' in query:
```
Replace the "Hello" with the word you like 
