function input_recorded() {
  $('#submit-button').addClass("btn-primary").removeClass("btn-warning");
  $('#chat-box').val("");
}

//window.setInterval(function(){
//  $('#borderedbox').animate({"scrollTop": $('#borderedbox')[0].scrollHeight}, "slow");
//  Sijax.request('get_latest_messages');
//}, 5000);

window.setInterval(function(){
  Sijax.request('get_latest_update', [$('tr').last().attr('id')]);
}, 1000);

$(document).ready(function(){
  $('#borderedbox').animate({"scrollTop": $('#borderedbox')[0].scrollHeight}, "slow");
});

$(document).keypress(function(event){

	var keycode = (event.keyCode ? event.keyCode : event.which);
	if(keycode == '13'){
		Sijax.request('take_input', [$('#chat-box').val()]);
    $('#submit-button').removeClass("btn-primary").addClass("btn-warning");
    $('#chat-box').val("");
	}
});
