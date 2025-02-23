document.addEventListener("DOMContentLoaded", () => {
    const chatForm = document.getElementById("chat-form");
    const userInputField = document.getElementById("user-input");
    const chatMessages = document.getElementById("chat-messages");
    const voiceButton = document.getElementById("voice-button");

    // Function to add messages to chat window
    function addMessage(message, isUser) {
        const messageDiv = document.createElement("div");
        messageDiv.classList.add("message");
        messageDiv.classList.add(isUser ? "user-message" : "bot-message");
        messageDiv.textContent = message;
        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight; // Auto-scroll to latest message
    }

    // Handle form submission (User Input)
    chatForm.addEventListener("submit", async (event) => {
        event.preventDefault(); // Prevent form from reloading the page

        const userInput = userInputField.value.trim();
        if (!userInput) return;

        // Display user message
        addMessage(userInput, true);

        try {
            // Send request to Flask backend
            const response = await fetch("/chat", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message: userInput }),
            });

            const data = await response.json();

            // Display chatbot response
            addMessage(data.response, false);
        } catch (error) {
            console.error("Error:", error);
            addMessage("⚠️ Error communicating with the server!", false);
        }

        userInputField.value = ""; // Clear input field
    });

    // Handle voice input (Speech-to-Text)
    voiceButton.addEventListener("click", async () => {
        try {
            const response = await fetch("/speech-to-text", { method: "POST" });
            const data = await response.json();
            
            if (data.text) {
                userInputField.value = data.text; // Populate input field with recognized speech
            } else {
                addMessage("⚠️ Unable to process speech. Try again.", false);
            }
        } catch (error) {
            console.error("Speech API error:", error);
            addMessage("⚠️ Error with speech recognition.", false);
        }
    });
});