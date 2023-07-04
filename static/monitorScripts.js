import {getTime} from "./timeProcessing.js";
import {getCustomers} from "./getCustomers.js";
import {getWorkplaces} from "./getWorkplaces.js";


setInterval(() => {
    getWorkplaces();
    getCustomers();
}, 5 * Math.pow(10, 3));


$(document).ready(function() {
    $(".navbar-text").text(getTime());
})


setInterval(() => {
    $(".navbar-text").text(getTime());
}, 10 * Math.pow(10, 3));