




import pyttsx3

# Initialize the engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 150)  # Speed of speech (words per minute)
engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)

# Say something
engine.say("Hello Sir. I am speaking, Jarvis")

# Run and wait for the speech to finish
engine.runAndWait()