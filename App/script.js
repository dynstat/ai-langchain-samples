const chat = document.getElementById('chat');
const messageInput = document.getElementById('message');
const sendBtn = document.getElementById('send');

function appendMessage(text, sender) {
    const div = document.createElement('div');
    div.className = 'msg ' + sender;
    div.innerHTML = `<b>${sender === 'user' ? 'You' : 'AI'}: </b>  ${text}`;
    chat.appendChild(div);
    chat.scrollTop = chat.scrollHeight;
}

sendBtn.onclick = async function() {
    const text = messageInput.value.trim();
    if (!text) return;
    appendMessage(text, 'user');
    messageInput.value = '';
    sendBtn.disabled = true;
    const response = await window.pywebview.api.send_message(text);
    appendMessage(response, 'bot');
    sendBtn.disabled = false;
    messageInput.focus();
};

messageInput.addEventListener('keydown', function(e) {
    if (e.key === 'Enter') sendBtn.click();
});