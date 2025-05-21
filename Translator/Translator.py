import pyttsx3  # Zorg dat je pyttsx3 hebt geïnstalleerd: pip install pyttsx3

# Woordenboek Engels -> Nederlands
dictionary = {
    "hello": "hallo",
    "world": "wereld",
    "cat": "kat",
    "dog": "hond",
    "good": "goed",
    "morning": "ochtend",
    "evening": "avond",
    "how": "hoe",
    "are": "zijn",
    "you": "jij",
}

def speak(text):
    """Spreek de tekst uit."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def translate_word_nl_en(word):
    """Vertaal een enkel woord van Nederlands naar Engels."""
    reverse_dictionary = {v: k for k, v in dictionary.items()}
    return reverse_dictionary.get(word.lower(), f"[{word}]")

def translate_sentence_nl_en(sentence):
    """Vertaal een hele zin woord voor woord van NL naar EN."""
    words = sentence.split()
    translated = [translate_word_nl_en(word) for word in words]
    return " ".join(translated)

if __name__ == "__main__":
    zin = input("Voer een Nederlandse zin in: ")
    vertaling = translate_sentence_nl_en(zin)
    print("Engelse vertaling:", vertaling)
    speak(vertaling)