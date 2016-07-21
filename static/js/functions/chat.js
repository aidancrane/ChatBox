function input_recorded() {
  $('#submit-button').addClass("btn-primary").removeClass("btn-warning");
}

$(document).keypress(function(event){

	var keycode = (event.keyCode ? event.keyCode : event.which);
	if(keycode == '13'){
		Sijax.request('take_input', [$('#chat-box').val()]);
    $('#submit-button').removeClass("btn-primary").addClass("btn-warning");
	}
});
