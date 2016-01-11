



fontsize = function () {
    var x = $(window).width() * 0.10; // 10% of container width
    var y = $(window).height() * 0.10; // 10% of container height
    var fontSize = Math.min(x,y);
    $("body").css('font-size', fontSize);
};
$(window).resize(fontsize);
$(document).ready(fontsize);

var $letters = ['a','b','c','d','e','f']


makeLetterBox = function (){
   

    for( var i=0; i < 6; i++ ) {
         document.getElementById("letter"+i).innerHTML = $letters[i];
    }
};

//$(document).ready(makeLetterBox);



keyPressLetter = function () {
   $('#contract-input').keyup(function() {
      
      
   var $txtVal = this.value.toLowerCase();
   var $unusedLetters = [];
   for (var i=0; i < 6; i++) {
      $unusedLetters[i] = document.getElementById("letter"+i).innerHTML;
   }
   var $len = $txtVal.length;
   $unusedLetters[7] = true;
   
   var $xx = '';

   for (var i=0; i < $len; i++) {
      var $theletter = $txtVal.charAt(i);
      var $indextheLetter = $unusedLetters.indexOf($theletter);
      
      if ($indextheLetter >= 0) {
         $unusedLetters[$indextheLetter] = false;
         $xx += $theletter;
      } else {
         $unusedLetters[7] = false;
      }
         
   }
   
   for (var j=0; j < 6; j++) {
      
      if ($unusedLetters[j] == false) {
         $("#letter"+j).css('background-color', 'rgb(242,76,67)')
      } else {
         $("#letter"+j).css('background-color', 'rgb(132,188,232)')
   }
   }
   
   $('input[name=word]').val($xx);
   

   
   })
      
};
   
$(document).ready(keyPressLetter);

