function firstlastnameinput_error() {
  $('#firstlastnameinputgrp').addClass('has-error');
  this_is_all_wrong()

  setTimeout(function() {
    $('#firstlastnameinputgrp').removeClass("has-error");
}, 4800);
}
function friendlynameinput_error() {
  $('#friendlynameinputgrp').addClass('has-error');
  this_is_all_wrong()

  setTimeout(function() {
    $('#friendlynameinputgrp').removeClass("has-error");
}, 5800);
}
function usernameinput_error() {
  $('#usernameinputgrp').addClass('has-error');
  this_is_all_wrong()

  setTimeout(function() {
    $('#usernameinputgrp').removeClass("has-error");
}, 6800);
}
function emailinput_error() {
  $('#emailinputgrp').addClass('has-error');
  this_is_all_wrong()

  setTimeout(function() {
    $('#emailinputgrp').removeClass("has-error");
}, 7800);
}
function repeatemailinput_error() {
  $('#repeatemailinputgrp').addClass('has-error');
  this_is_all_wrong()

  setTimeout(function() {
    $('#repeatemailinputgrp').removeClass("has-error");
}, 8800);
}
function password_error() {
  $('#passwordgrp').addClass('has-error');
  this_is_all_wrong()

  setTimeout(function() {
    $('#passwordgrp').removeClass("has-error");
}, 9800);
}
function repeatedpassword_error() {
  $('#repeatedpasswordgrp').addClass('has-error');

  setTimeout(function() {
    $('#repeatedpasswordgrp').removeClass("has-error");
}, 10800);
}
function genderdropdown_error() {
  $('#genderDropdowngrp').addClass('has-error');
  this_is_all_wrong()

  setTimeout(function() {
    $('#genderDropdowngrp').removeClass("has-error");
}, 11800);
}

function email_match() {
  $('#emailinputgrp').addClass('has-success');
  $('#repeatemailinputgrp').addClass('has-success');
}


function create_success() {
  $('#feedback_error').html("<div class='col-sm-offset-2 col-sm-10'> <p class='help-block'><i class='fa fa-check' aria-hidden='true'></i> Welcome...</p> </div>").hide().fadeIn( 1000 );
  $(location).attr('href', './signup/complete');
}

function emails_dont_match() {
  $('#feedback_error').html("<p class='help-block'><i class='fa fa-exclamation-triangle' aria-hidden='true'></i> The Email addresses do not match...</p>").hide().fadeIn( 1000 );

  setTimeout(function() {
    $('#feedback_error').fadeOut();
}, 5800);
}

function username_bad() {
  $('#feedback_error').html("<p class='help-block'><i class='fa fa-exclamation-triangle' aria-hidden='true'></i> That username is not allowed. (Please only use (A-Z)(a-z) and 0 to 9 in your Username...)</p>").hide().fadeIn( 1000 );

  setTimeout(function() {
    $('#feedback_error').fadeOut();
}, 5800);
}

function password_too_short() {
  $('#feedback_error').html("<p class='help-block'><i class='fa fa-exclamation-triangle' aria-hidden='true'></i> That password is too short...</p>").hide().fadeIn( 1000 );

  setTimeout(function() {
    $('#feedback_error').fadeOut();
}, 5800);
}

function password_too_silly() {
  $('#feedback_error').html("<p class='help-block'><i class='fa fa-exclamation-triangle' aria-hidden='true'></i> Sorry, that password is too simple...</p>").hide().fadeIn( 1000 );

  setTimeout(function() {
    $('#feedback_error').fadeOut();
}, 5800);
}

function too_long_error() {
  $('#feedback_error').html("<p class='help-block'><i class='fa fa-exclamation-triangle' aria-hidden='true'></i> Sorry, Names must be no longer than 30 characters and usernames must be no longer than 16 characters...</p>").hide().fadeIn( 1000 );

  setTimeout(function() {
    $('#feedback_error').fadeOut();
}, 5800);
}

function name_firendlyname_bad() {
  $('#feedback_error').html("<p class='help-block'><i class='fa fa-exclamation-triangle' aria-hidden='true'></i> You cannot use that as your name.  Your nickname can contain spaces. (Please only use (A-Z)(a-z) and 0 to 9...)</p>").hide().fadeIn( 1000 );

  setTimeout(function() {
    $('#feedback_error').fadeOut();
}, 5800);
}

function emails_dont_contain_at() {
  $('#feedback_error').html("<p class='help-block'><i class='fa fa-exclamation-triangle' aria-hidden='true'></i> That email address is not allowed...</p>").hide().fadeIn( 1000 );

  setTimeout(function() {
    $('#feedback_error').fadeOut();
}, 5800);
}

function account_already_taken() {
  $('#feedback_error').html("<p class='help-block'><i class='fa fa-exclamation-triangle' aria-hidden='true'></i> Sorry. That account has already been taken. Try a different Username</p>").hide().fadeIn( 1000 );

  setTimeout(function() {
    $('#feedback_error').fadeOut();
}, 5800);
}

function email_already_taken() {
  $('#feedback_error').html("<p class='help-block'><i class='fa fa-exclamation-triangle' aria-hidden='true'></i> Sorry. That email address has already been used. </p>").hide().fadeIn( 1000 );

  setTimeout(function() {
    $('#feedback_error').fadeOut();
}, 5800);
}

function this_is_all_wrong() {
  $('#feedback_error').html("<p class='help-block'><i class='fa fa-exclamation-triangle' aria-hidden='true'></i> Sorry. You've missed something out...</p>").hide().fadeIn( 1000 );

  setTimeout(function() {
    $('#feedback_error').fadeOut();
}, 5800);
}
function does_not_match() {
  $('#feedback_error').html("<p class='help-block'><i class='fa fa-exclamation-triangle' aria-hidden='true'></i> The passwords do not match...</p>").hide().fadeIn( 1000 );

  setTimeout(function() {
    $('#feedback_error').fadeOut();
}, 5800);
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
