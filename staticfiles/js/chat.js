document.addEventListener('DOMContentLoaded', (event) => {
    const chatWindow = document.querySelector('.chat-window');
    const messageForm = document.querySelector('form');
    const messageInput = document.querySelector('input[name="message"]');

    function addMessageToChat(message) {
        const messageDiv = document.createElement('div');
        const m2Div = document.createElement('div')
        messageDiv.classList.add('message');
        m2Div.classList.add(message.sender === 'user' ? 'sent' : 'received');
        m2Div.innerHTML = `
            <p>${message.content}</p>
            <small>${new Date(message.timestamp).toLocaleTimeString()}</small>
        `;
        messageDiv.appendChild(m2Div);
        chatWindow.appendChild(messageDiv);
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }

    function loadMessages() {
        fetch('/api/chat/')
            .then(response => response.json())
            .then(data => {
                chatWindow.innerHTML = '';
                data.messages.forEach(message => addMessageToChat(message));
            });
    }

    messageForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const message = messageInput.value.trim();
        if (message) {
            fetch('/api/chat/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message }),
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    addMessageToChat({...data.message, sender: 'user'});
                    messageInput.value = '';
                }
            });
        }
    });

    loadMessages();
    // You might want to add a setInterval here to periodically fetch new messages
});