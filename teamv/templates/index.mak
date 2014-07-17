<%inherit file="wrapper.mak" />

<%block name="includes">
    % if meeting is not None and nickname is not None:
        <script type="text/javascript" src="/static/javascript/chat.js"></script>
    % endif
</%block>

% if meeting is None or nickname is None:
    <form name="enter_meeting" method="GET" action="/">
        <p>Enter your nickname and meeting number</p>
        Nickname: <input type="text" name="nickname" placeholder="&quot;Jim Smith&quot;"><br/>
        Meeting number: <input type="text" name="meeting" placeholder="&quot;12345678&quot;"><br/>
        <input type="submit" value="Submit">
    </form>
% else:
    <h1>Chat Log</h1>
    <textarea id="chatlog" readonly="readonly"></textarea>
    <br />
    <form name = "chat_form"  id="chat_form">
        <input type="text" id="chatbox">
        <button type="submit" id="submit" >Send</button>
        <input type="button" id="start_listening" value="Start Listening" onclick="recognition.start()">
        <input type="button" id="stop_listening" value="Stop Listening" onclick="recognition.stop()"> 
    </form>
    
    <span id="ws-unsupported" class="hidden">API not supported</span>
% endif
