import tkinter as tk
from tkinter import scrolledtext
import speech_recognition as sr
import google.generativeai as genai

# Set up Gemini API (Replace with your API key)
genai.configure(api_key="API_KEY")

def chat_with_gemini(prompt):
    """Get response from Gemini AI """
    try:
        system_prompt = (
            "You are a compassionate and supportive mental health assistant."
            " When I share my thoughts, feelings, or incidents, listen empathetically and provide thoughtful guidance."
            "Offer validation, coping strategies, and practical tips for emotional well-being. "
            "Suggest mindfulness techniques, self-care routines, and ways to manage stress, anxiety, or difficult emotions."
            " If needed, encourage seeking professional help in a gentle and supportive way."
            " Keep your tone warm, understanding, and non-judgmental, making me feel heard and supported."
            "If a user asks something unrelated to education, politely tell them "
            "that you only teach educational subjects."
        )

        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(system_prompt + " " + prompt)
        return response.text
    except Exception as e:
        return "Sorry, I couldn't connect to the chatbot service."

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("Adjusting for ambient noise... Please wait.")
            recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)

            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Could not understand the audio. Please speak clearly."
        except sr.RequestError:
            return "Could not request results, check your internet connection."
        except sr.WaitTimeoutError:
            return "Listening timed out. Please try again."

# Initialize main window
root = tk.Tk()
root.title("Mental Health Assisstant")
root.geometry("800x600")
root.configure(bg="#A9D1E6")  # Light blue pastel background

# Header
header_frame = tk.Frame(root, bg="#444444", pady=10)
header_frame.pack(fill=tk.X)
header_label = tk.Label(
    header_frame, text="Soul Bot", font=("Arial", 18, "bold"), fg="#ffffff", bg="#444444"
)
header_label.pack()

# Chat display area
chat_frame = tk.Frame(root, bg="#A9D1E6")  # Light blue pastel background
chat_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
canvas = tk.Canvas(chat_frame, bg="#A9D1E6", highlightthickness=0)
scrollbar = tk.Scrollbar(chat_frame, orient=tk.VERTICAL, command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="#A9D1E6")

scrollable_frame.bind(
    "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.bind_all("<MouseWheel>",lambda event:canvas.yview_scroll(-1*(event.delta//120),"units"))
# Display static welcome message
def display_static_message():
    display_message("Hey!! I'm your good friend. Share your thoughts with me!", sender="bot")

# Input area
input_frame = tk.Frame(root, bg="#A9D1E6")  # Light blue pastel background
input_frame.pack(fill=tk.X, padx=10, pady=10)

input_box = tk.Entry(
    input_frame, font=("Arial", 14), bg="#ffffff", fg="#000000", bd=2, relief=tk.GROOVE  # White input text
)
input_box.insert(0, "Share anything with me...")  # Placeholder text
input_box.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))

send_button = tk.Button(
    input_frame, text="Send", font=("Arial", 12), bg="#FFD662", fg="#ffffff", relief=tk.FLAT, padx=10, pady=5
)
send_button.pack(side=tk.RIGHT)

# Voice Input button with a lighter shade of green
# Voice Input button with brown color
voice_button = tk.Button(
    input_frame, text="Voice Input", font=("Arial", 12), bg="#00539C", fg="#ffffff", relief=tk.FLAT, padx=10, pady=5
)



voice_button.pack(side=tk.RIGHT, padx=(10, 0))

def display_message(message, sender="user"):
    """Display a message in the chat area, aligning based on sender."""
    frame = tk.Frame(scrollable_frame, bg="#A9D1E6", pady=5)  # Light blue pastel background
    message_label = tk.Label(
        frame,
        text=message,
        bg="#D3D3D3",  # Light grey background
        fg="#000000",  # Black text
        font=("Arial", 12),
        wraplength=600,
        justify="left",
        anchor="w" if sender == "bot" else "e",
        padx=10,
        pady=5,
    )
    message_label.pack(anchor="w" if sender == "bot" else "e", fill=tk.NONE, padx=10, pady=2)
    frame.pack(fill=tk.BOTH, expand=True)
    canvas.update_idletasks()
    canvas.yview_moveto(1)

def send_message():
    """Handle user input and AI response in text mode."""
    user_message = input_box.get()
    if user_message.strip():
        display_message(user_message, sender="user")
        input_box.delete(0, tk.END)
        
        # Get AI response
        bot_response = chat_with_gemini(user_message)
        display_message(bot_response, sender="bot")

def speech_to_text():
    """Handle user input via speech and AI response."""
    display_message("Listening for your voice...", sender="bot")
    user_message = recognize_speech()
    if user_message:
        display_message(user_message, sender="user")
        bot_response = chat_with_gemini(user_message)
        display_message(bot_response, sender="bot")

# Bind buttons to actions
send_button.config(command=send_message)
voice_button.config(command=speech_to_text)

# Footer
footer_frame = tk.Frame(root, bg="#A9D1E6", pady=10)  # Light blue pastel background
footer_frame.pack(fill=tk.X)
footer_label = tk.Label(
    footer_frame, text="Your personal AI assistant", font=("Arial", 10), fg="#888888", bg="#A9D1E6"
)
footer_label.pack()

# Display the static message when the application starts
display_static_message()

# Run the main event loop
root.mainloop()
