import {getTime} from "./timeProcessing.js";


function validateFields() {
    if ($("#user").val() == "") {
      $("#user").css("background-color", "red");
    }
    if ($("#password").val() == "") {
      $("#password").css("background-color", "red");;
    }
}


$("#button").click(function(){
    validateFields();
});


$(document).ready(function() {
    $(".navbar-text").text(getTime());
})
