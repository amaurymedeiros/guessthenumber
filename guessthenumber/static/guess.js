function guessNumber(encrypted) {
  var guess = $('#guess').val();
  $.post($SCRIPT_ROOT + '/guess_number',
    {'encrypted' : encrypted, 'guess' : guess},
    function(data) {
      console.log(data);
    });
}