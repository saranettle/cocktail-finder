$(document).ready(function() {

  $('#aboutButton').click(function() {
    $('#aboutPage').animate({
      opacity: 'toggle'
    });
    $('#mainApp').animate({
    	opacity: 'toggle'
    });
  });

  $('#backButton').click(function() {
    $('#aboutPage').animate({
      opacity: 'toggle'
    });
    $('#mainApp').animate({
    	opacity: 'toggle'
    });
  });


});
