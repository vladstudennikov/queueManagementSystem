import {getCustomers} from "./getCustomers.js";
import {getWorkplaces} from "./getWorkplaces.js";
import {getStates} from "./getOperatorsStates.js";
import {getTime} from "./timeProcessing.js";


$(document).ready(function() {
    $(".navbar-text").text(getTime());
})


$("#add_cust").click(function() {
    $.ajax({
        type: "POST",
        url: "/addCustomer",
        data: {"add" : 1},
        success: function(response) {
            getWorkplaces();
            getStates();
            getCustomers();
        }
    });
})


setInterval(() => {
    getWorkplaces();
    getCustomers();
    getStates();
}, 5 * Math.pow(10, 3));


setInterval(() => {
    $(".navbar-text").text(getTime());
}, 10 * Math.pow(10, 3));
