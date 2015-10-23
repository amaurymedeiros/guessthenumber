function guessNumber(encrypted) {
  var guess = $('#guess').val();
  $.post($SCRIPT_ROOT + '/guess_number',
    {'encrypted' : encrypted, 'guess' : guess},
    function(data) {
      updateResult(guess, data);
    });
}

function updateResult(guess, data) {
  var parsedData = data['white_pins'] + ' white pin(s). ' + data['black_pins']
                    + ' black pin(s).';
  $('#result').append('<p>' + guess + ': ' + parsedData + '</p>');
}