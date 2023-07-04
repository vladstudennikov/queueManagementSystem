import {getTime} from "./timeProcessing.js";
import {getCustomers} from "./getCustomers.js";
import {getWorkplaces} from "./getWorkplaces.js";


export function getOperatorsNumber() {
    let currentUrl = window.location.href;
    let operatorsNumber = currentUrl.substring(currentUrl.lastIndexOf('/') + 1);
    
    return operatorsNumber;
}


$("#busy-btn").click(function(){
    let number = getOperatorsNumber();
    $.ajax({
        type: "get",
        url: "/setState",
        data: {
            id: number,
            status: "busy"
        },
        success: function() {
            $("#state_info").text("State: busy").css("color", "#D24B4B");
            getCustomers();
            getWorkplaces();
        }
    });
})


$("#busy-btn").hover(function() {
    $("#busy-btn").animate({
        color: "red"
    }, 300);
})


$("#free-btn").click(function(){
    let number = getOperatorsNumber();
    $.ajax({
        type: "get",
        url: "/setState",
        data: {
            id: number,
            status: "free"
        },
        success: function() {
            $("#state_info").text("State: free").css("color", "#588E57");
            getCustomers();
            getWorkplaces();
        }
    });
})


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

