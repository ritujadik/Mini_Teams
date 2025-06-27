let socket;
let username = "";
let connected = false; // 👈 Prevents double join

function joinTeam() {
  if (connected) return; // ✅ Already connected? Skip.
  connected = true;

  username = document.getElementById("username").value;
  const team = document.getElementById("team").value;

  if (!username || !team) {
    alert("Enter a username and select a team!");
    connected = false;
    return;
  }

  const protocol = window.location.protocol === "https:" ? "wss" : "ws";
  const host = window.location.host;

  socket = new WebSocket(`${protocol}://${host}/ws/${team}`);

  socket.onopen = () => {
    console.log("✅ Connected to WebSocket");
    document.getElementById("chat").style.display = "block";
  };

  socket.onmessage = function (event) {
    const li = document.createElement("li");
    li.textContent = event.data;
    document.getElementById("messages").appendChild(li);
  };

  window.sendMessage = function () {
    const input = document.getElementById("message");
    if (input.value.trim() !== "") {
      socket.send(`${username}: ${input.value}`);
      input.value = '';
    }
  };
}
