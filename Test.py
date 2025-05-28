from deep_translator import GoogleTranslator
import pyttsx3

# Originele tekst in het Nederlands
tekst = "Hallo, ik wil dit gaan vertalen."

# Vertaal naar Engels
vertaling = GoogleTranslator(source='nl', target='en').translate(tekst)
print(f"🔁 Vertaald: {vertaling}")

# Voorlezen
engine = pyttsx3.init()
engine.say(vertaling)
engine.runAndWait()
