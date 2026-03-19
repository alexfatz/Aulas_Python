const form = document.getElementById("message-form");
const input = document.getElementById("message-input");
const messages = document.getElementById("messages");
const protocol = window.location.protocol === "https:" ? "wss" : "ws";
const socket = new WebSocket(`${protocol}://${window.location.host}/ws`);


socket.onopen = () => {
    console.log("Conectado ao servidor");
};


socket.onmessage = (event) => {
    const data = JSON.parse(event.data);
    const li = document.createElement("li");
    li.textContent = data.message;
    messages.appendChild(li);
};


socket.onclose = () => {
    console.log("Desconectado do servidor");
};


form.addEventListener("submit", (event) => {
    event.preventDefault(); // evita que a página recarregue ao enviar e perca a conexão com websocket

    const message = input.value.trim();

    if (!message) { return };
    
    socket.send(JSON.stringify({ message: message }));
    
    //resetar após envio
    input.value = "";
    input.focus(); // enviar cursor no input para uma nova mensagem
});
