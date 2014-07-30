function toggle(el){
    if(el.className=="unmute")
    {
        el.src='/static/images/mute.png';
        el.className="mute";
		el.title='Unmute';
    }
    else if(el.className=="mute")
    {
        el.src='/static/images/unmute.png';
        el.className="unmute";
		el.title='Mute';
    }
	
	else if(el.className=="recording_off")
    {
        el.src='/static/images/recording_on.png';
        el.className="recording_on";
		el.title='Recording';
    }
    else if(el.className=="recording_on")
    {
        el.src='/static/images/recording_off.png';
        el.className="recording_off";
		el.title='Idle';
    }

    return false;
} 
/*
var meeting = getParameterByName('meeting');

 // For End Meeting button
    var end_form = document.getElementById("end_meeting");
    var m_num = document.createElement('input');
    m_num.type = 'hidden';
    m_num.name = 'meeting';
    m_num.value = meeting;
    end_form.append(m_num);

 */
