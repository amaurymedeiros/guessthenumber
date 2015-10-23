function guessNumber(encrypted) {
  var guess = $('#guess').val();
  $.post($SCRIPT_ROOT + '/guess_number',
    {'encrypted' : encrypted, 'guess' : guess},
    function(data) {
      checkResult(guess, data);
    });
}

function updateResult(guess, data) {
  var parsedData = data['white_pins'] + ' white pin(s). ' + data['black_pins']
                    + ' black pin(s).';
  $('#result').append('<p>' + guess + ': ' + parsedData + '</p>');
}

function checkResult(guess, data) {
  if (data['black_pins'] == 4) {
    endGame(guess);
    return;
  }
  updateResult(guess, data);
}

function endGame(guess) {
  // Fix numbers starting with 0
  if (guess.length == 3) {
    guess = '0' + guess;
  }
  $('#game').html('<p> Congratulations! You guessed the number: ' + guess 
                  + '</p>');
  $('#try_again').show();
}