function input_recorded() {
  $('#submit-button').addClass("btn-primary").removeClass("btn-warning");
  $('#chat-box').val("");
}

window.setInterval(function(){
  Sijax.request('get_latest_messages');
}, 5000);

$(document).keypress(function(event){

	var keycode = (event.keyCode ? event.keyCode : event.which);
	if(keycode == '13'){
		Sijax.request('take_input', [$('#chat-box').val()]);
    $('#submit-button').removeClass("btn-primary").addClass("btn-warning");
    $('#chat-box').val("");
	}
});
