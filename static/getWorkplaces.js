export function getOperatorsNumber() {
      let currentUrl = window.location.href;
      let operatorsNumber = currentUrl.substring(currentUrl.lastIndexOf('/') + 1);
      
      return operatorsNumber;
}

export function getWorkplaces() {
    $.ajax({
        type: "POST",
        url: "/getWorkplaces",
        data: {"get": 1},
        success: function(response) {
            $("#operators_queue").empty();
            $("#operators_queue").append(
                `
                <div class="container text-center">
                      <div class="row">
                        <div class="col">
                              <p class="h3">Customer</p>
                        </div>
                    
                        <div class="col">
                              <p class="h3">Operator</p>
                        </div>
                      </div>
                </div>
                `
            );

            let keys = Object.keys(response);
            for (let i = 0; i < keys.length; i++) {
                if (keys[i] == getOperatorsNumber()) {
                  $("#cust_info").text("Customer: " + response[keys[i]]);
                }

                $("#operators_queue").append(
                `
                <div class="container text-center">
                      <div class="row">
                        <div class="col">
                              <p class="h3">${response[keys[i]]}</p>
                        </div>
                    
                        <div class="col">
                              <p class="h3">${keys[i]}</p>
                        </div>
                      </div>
                </div>
                `
                );
            }
        }
    });
}