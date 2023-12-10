from gtts import gTTS
import speech_recognition as sr
from playsound import playsound


def speak(text, lang='tl'):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save("output.mp3")
    playsound("output.mp3")


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio, language='tl-PH')
        print(f"User said: {text}")
        return text.lower()
    except sr.UnknownValueError:
        print("Sorry, I did not understand. Please try again.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""


def main():
    speak("Magandang araw! Paano kita matutulungan ngayon?", lang='tl')

    while True:
        command = listen()

        if "paalam" in command:
            speak("Paalam! Ingat ka palagi.")
            break
        elif command:
            # Add your custom commands and responses here
            if "kamusta ka" in command:
                speak("Mabuti naman! Salamat sa pagtanong.")
            else:
                speak("Pasensya na, hindi ko maintindihan ang iyong utos.")


if __name__ == "__main__":
    main()
