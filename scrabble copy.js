



fontsize = function () {
    var x = $(window).width() * 0.10; // 10% of container width
    var y = $(window).height() * 0.10; // 10% of container height
    var fontSize = Math.min(x,y);
    $("body").css('font-size', fontSize);
};
$(window).resize(fontsize);
$(document).ready(fontsize);

var $letters = [];
var $lettersUsed = [];


makeLetterBox = function (){
    var vpossible = "aeiou";
    var cpossible = "bcdfghjklmnpqrstvwxy";

    for( var i=0; i < 2; i++ ) {
         $choose = Math.floor(Math.random() * vpossible.length);
         $letters[i] = vpossible.charAt($choose);
         document.getElementById("letter"+i).innerHTML = $letters[i];
         $lettersUsed[i]=false;
         vpossible = vpossible.slice(0, $choose) + vpossible.slice($choose+1, vpossible.length)
    }
    
    for( var i=2; i < 6; i++ ) {
         $choose = Math.floor(Math.random() * cpossible.length);
         $letters[i] = cpossible.charAt($choose);
         document.getElementById("letter"+i).innerHTML = $letters[i];
         $lettersUsed[i]=false;
         cpossible = cpossible.slice(0, $choose) + cpossible.slice($choose+1, cpossible.length)
    }
    
    return $letters

}

$(document).ready(makeLetterBox);


keyPressLetter = function () {
   $('#contract-input').keyup(function() {
    var txtVal = this.value.toLowerCase();
    var lastLetter = txtVal.charAt(txtVal.length-1);
    
    if ($lettersUsed[jQuery.inArray( lastLetter, $letters )]) {
      $('#error').fadeIn(100, function(){
         $('#error').fadeOut(100)
         $('input[name=word]').val(txtVal.substring(0, txtVal.length - 1));
      }) ;
    } else {    
    for(var i=0; i < 6; i++ ) {
         $lettersUsed[i]=false;
         for (var j=0; j < txtVal.length; j++) {
            if ($letters[i] == txtVal.charAt(j) ) {
               $lettersUsed[i] = true;
            }
        }
        if ($lettersUsed[i]) {
            $("#letter"+i).css('background-color', 'rgb(242,76,67)')
        } else {
         $("#letter"+i).css('background', 'none')
        }
    }
    }
    if (txtVal.length != 0) {
      if (jQuery.inArray( lastLetter, $letters ) == -1) { 
      $('#error').fadeIn(100, function(){
         $('#error').fadeOut(100)
         $('input[name=word]').val(txtVal.substring(0, txtVal.length - 1));
      }) ;
    }
    }
   })
      
};
   
$(document).ready(keyPressLetter);

