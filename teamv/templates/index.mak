<%inherit file="wrapper.mak" />

<%block name="includes">
    %if 'meeting' in request.POST and 'nickname' in request.POST:
        <script type="text/javascript" src="/static/javascript/chat.js"></script>
    %else:
        <script type="text/javascript" src="/static/javascript/login.js"></script>
    %endif
</%block>

%if not 'meeting' in request.POST or not 'nickname' in request.POST:
    <form name="enter_meeting" onsubmit="enter_meeting()">
        <p>Enter your nickname and meeting number</p>
        Nickname: <input type="text" id="nickname" placeholder="&quot;Jim Smith&quot;"><br/>
        Meeting number: <input type="text" id="meeting_number" placeholder="&quot;12345678&quot;"><br/>
        <button type="submit">Send</button>
    </form>
%else:
    
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
%endif
