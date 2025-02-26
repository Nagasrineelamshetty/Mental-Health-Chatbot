# Mental-Health-Chatbot






 
A web-based chatbot designed to provide a safe space for users to share their feelings and receive supportive responses. It uses **Natural Language Processing (NLP)** for emotion recognition to deliver empathetic interactions, ensuring user anonymity and privacy.  

## Features  
- Emotion recognition through NLP for personalized responses.  
- User-friendly interface with an anonymous chat environment.  
- Real-time text-based conversations.  
- Built with **Python**, **Flask**, **HTML**, **CSS**, and **JavaScript**.  

## Tech Stack  
- **Backend:** Flask (Python)  
- **Frontend:** HTML, CSS, JavaScript  
- **NLP:** Integrated emotion recognition  
- **Deployment:** Flask server  

## Installation  
1. **Clone the repository:**  
    ```bash
    git clone https://github.com/your-username/mental-health-chatbot.git
    cd mental-health-chatbot
    ```  
2. **Create a virtual environment and activate it:**  
    ```bash
    python -m venv venv  
    source venv/bin/activate  # On Windows: venv\Scripts\activate  
    ```  
3. **Install dependencies:**  
    ```bash
    pip install -r requirements.txt
    ```  
4. **Run the application:**  
    ```bash
    python app.py
    ```  
    The chatbot will be available at `http://localhost:5000`.  

## Usage  
- Visit `http://localhost:5000` in your browser.  
- Start a conversation by typing your thoughts.  
- The chatbot responds empathetically based on the detected emotion.  

## Project Structure  
```plaintext
mental-health-chatbot/  
├── app.py               # Flask application  
├── templates/           # HTML templates  
│   └── index.html       # Chatbot interface  
├── static/              # Static files (CSS, JS)  
│   ├── css/             # Stylesheets  
│   └── js/              # JavaScript files  
├── models/              # NLP models for emotion recognition  
└── requirements.txt     # Dependencies  
```

## Contributing  
Contributions are welcome!  
- Fork the repository.  
- Create a new branch (`git checkout -b feature-branch`).  
- Commit your changes (`git commit -m 'Add new feature'`).  
- Push to the branch (`git push origin feature-branch`).  
- Open a pull request.  

## License  
This project is licensed under the MIT License.  

## Acknowledgments  
- Inspired by the need for mental health support and emotional well-being.  
- Special thanks to open-source libraries and NLP frameworks used.  

---
