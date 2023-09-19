function displayError(elementId, errorMessage) {
  var errorElement = $('#' + elementId);
  if (errorMessage !== '') {
    errorElement.html(errorMessage);
    errorElement.show();
  } else {
    errorElement.html('');
    errorElement.hide();
  }
}

function validate() {
  var nameInput = $('#name');
  var emailInput = $('#email');
  var phoneInput = $('#phone');
  var commentsInput = $('#comments');

  // Validate name
  if (nameInput.val().trim() === '') {
    displayError('name-error', 'Please enter your name.');
    return false;
  } else {
    displayError('name-error', '');
  }

  // Validate email
  var emailPattern = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
  if (!emailPattern.test(emailInput.val())) {
    displayError('email-error', 'Please enter a valid email address.');
    return false;
  } else {
    displayError('email-error', '');
  }

  // Validate phone number
  var phonePattern = /^\d{10}$/;
  if (!phonePattern.test(phoneInput.val())) {
    displayError('phone-error', 'Please enter a valid 10-digit phone number.');
    return false;
  } else {
    displayError('phone-error', '');
  }

  // Validate comments
  if (commentsInput.val().trim() === '') {
    displayError('comments-error', 'Please enter the query.');
    return false;
  } else {
    displayError('comments-error', '');
  }
  displaySuccessMessage('Success! Form submitted.');
  document.getElementById('submit').disabled = true;
  document.getElementById('reset').disabled = true;
  document.getElementById('reset-link').style.display = 'inline';
  

 

  $.ajax({
    url: '/submit_form_view/',
    type: 'POST',
    data: JSON.stringify(formData),
    contentType: 'application/json',
    success: function(response) {
      // Handle the success response
      displaySuccessMessage('Success! Form submitted.');
      $('#submit').prop('disabled', true);
      $('#reset').prop('disabled', true);
      $('#reset-link').show();
    },
    error: function(error) {
      // Handle the error response
      displayError('form-error', 'An error occurred. Please try again later.');
    }
  });

  return true;
}

function reset() {
  $('#name').val('');
  $('#email').val('');
  $('#phone').val('');
  $('#comments').val('');
  displayError('name-error', '');
  displayError('email-error', '');
  displayError('phone-error', '');
  displayError('comments-error', '');
  displayError('form-error', '');
  displaySuccessMessage('');
  $('#submit').prop('disabled', false);
  $('#reset').prop('disabled', false);
  $('#reset-link').hide();
}

function displaySuccessMessage(message) {
  $('#success-message').html(message);
  $('#success-message').show();
  $('#reset-link').show(); // Show the "Fill Form Again" link
}


