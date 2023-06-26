export function getCustomers() {
    $.ajax({
        type: "POST",
        url: "/getCustomers",
        data: {"get": 1},
        success: function(response) {

            $("#customers").empty()

            for (let i = 0; i < response.data.length; i++) {
                $("#customers").append(
                    $("<p/>")
                        .text(response.data[i])
                        .addClass("h1")
                );
            }
        }
    })
}