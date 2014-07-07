<%inherit file="wrapper.mak" />

<h1>Socket.io Chatterbox</h1>
<div id="status" class="border">Disconnected</div>
<form id="login">
    <label for="login-input">Login:</label>
    <input id="login-input">
</form>
<div>
    <div class="border left">
        <h3>Nicks</h3>
        <ul id="nicks">
        </ul>
    </div>
    <div class="border right">
        <form id="chat">
            <label for="chat-input">Chat:</label>
            <input id="chat-input">
        </form>
        <div id="chat-data">
        </div>
    </div>
</div>
