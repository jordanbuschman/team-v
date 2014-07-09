<%inherit file="wrapper.mak" />

<%block name="includes">
    <script type="text/javascript" src="/static/javascript/chat.js"></script>
</%block>

<h1>Chat Log</h1>
<div id="chatlog"></div>
<br />
<form id="chat_form">
    <input type="text" id="chatbox"></input>
    <button type="submit" id="submit">Send</button>
</form>
