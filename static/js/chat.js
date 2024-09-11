document.addEventListener('DOMContentLoaded', (event) => {
    const chatWindow = document.querySelector('.chat-window');
    const messageForm = document.querySelector('form');
    const messageInput = document.querySelector('input[name="message"]');

    function addMessageToChat(message) {
        const messageDiv = document.createElement('div');
        const messageDiv2 = document.createElement('div');
        messageDiv.classList.add('message');
        messageDiv2.classList.add(message.sender === 'admin' ? 'sent' : 'received');
        messageDiv.classList.add(message.sender === 'admin' ? 'right' : 'left');
        messageDiv2.classList.add('msg')
        messageDiv2.innerHTML = `
            <p>${message.content}</p>
            <small>${new Date(message.timestamp).toLocaleTimeString()}</small>
        `;
        messageDiv.appendChild(messageDiv2);
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
        console.log(message)
        if (message) {
            fetch('/api/chat/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message, sender: "guest" }),
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    addMessageToChat({...data.message, sender: 'guest'});
                    messageInput.value = '';
                }
            });
        }
    });

    loadMessages();
    // You might want to add a setInterval here to periodically fetch new messages
});