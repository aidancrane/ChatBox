function login_error() {

  $('#email_box_element').addClass('has-error');
  $('#password_box_element').addClass('has-error');
  $('#feedback_error').html("<div class='col-sm-offset-2 col-sm-10'> <p class='help-block'><i class='fa fa-exclamation-triangle' aria-hidden='true'></i> Sorry. That combination doesn't work...</p> </div>").hide().fadeIn( 1000 );
}
function login_success() {

  $('#email_box_element').addClass('has-success');
  $('#password_box_element').addClass('has-success');
  $('#feedback_error').html("<div class='col-sm-offset-2 col-sm-10'> <p class='help-block'><i class='fa fa-check' aria-hidden='true'></i> Welcome...</p> </div>").hide().fadeIn( 1000 );
  $(location).attr('href', './dashboard')
}

$(document).keypress(function(event){

	var keycode = (event.keyCode ? event.keyCode : event.which);
	if(keycode == '13'){
		Sijax.request('check_loginbox', [$('#inputEmail3').val(), $('#inputPassword3').val()]);
    $('#feedback_error').html("<div class='col-sm-offset-2 col-sm-10'> <p class='help-block'><i class='fa fa-circle-o-notch fa-spin fa-fw'></i> Checking...</p> </div>");
	}
});
