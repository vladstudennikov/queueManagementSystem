function changeOperatorsStatesStyle() {
    $(".operstates").each(function() {
        if ($(this).text().endsWith("busy")) {
            $(this).css("color", "#D24B4B");
        }
        else {
            $(this).css("color", "#588E57");
        }
    });
}

export function getStates() {
    $.ajax({
        type: "GET",
        url: "/getStates",
        data: {"get": 1},
        success: function(response) {
            $("#workplace_states").empty();
            $("#workplace_states").append(`<p class="h3">Operator's states</p>`)
            let keys = Object.keys(response);

            for (let i = 0; i < keys.length; i++) {
                $("#workplace_states").append(`<p class="h5 operstates">${keys[i]} - ${response[keys[i]]}</p>`);
            }
            changeOperatorsStatesStyle();
        }
    });
}