function firstlastnameinput_error() {
  $('#firstlastnameinputgrp').addClass('has-error');
}
function friendlynameinput_error() {
  $('#friendlynameinputgrp').addClass('has-error');
}
function usernameinput_error() {
  $('#usernameinputgrp').addClass('has-error');
}
function emailinput_error() {
  $('#emailinputgrp').addClass('has-error');
}
function repeatemailinput_error() {
  $('#repeatemailinputgrp').addClass('has-error');
}
function password_error() {
  $('#passwordgrp').addClass('has-error');
}
function repeatedpassword_error() {
  $('#repeatedpasswordgrp').addClass('has-error');
}
function genderdropdown_error() {
  $('#genderDropdowngrp').addClass('has-error');
}
function create_success() {
  $('#feedback_error').html("<p class='help-block'><i class='fa fa-check' aria-hidden='true'></i> Welcome...</p>").hide().fadeIn( 1000 );
}

function account_already_taken() {
  $('#feedback_error').html("<p class='help-block'><i class='fa fa-exclamation-triangle' aria-hidden='true'></i> Sorry. That account has already been taken</p>").hide().fadeIn( 1000 );
  usernameinput_error();
}

$(document).keypress(function(event){

	var keycode = (event.keyCode ? event.keyCode : event.which);
	if(keycode == '13'){
		Sijax.request('create_account', [$('#firstnameinput').val(),
    $('#lastnameinput').val(),
    $('#friendlynameinput').val(),
    $('#usernameinput').val(),
    $('#emailinput').val(),
    $('#repeatemailinput').val(),
    $('#password').val(),
    $('#repeatedpassword').val(),
    $('#genderDropdown').val()]);
    $('#feedback_error').html("<p class='help-block'><i class='fa fa-circle-o-notch fa-spin fa-fw'></i> Checking...</p>");
	}
});
