function openForm() {
    document.getElementById("myForm").style.display = "block";
}

function closeForm() {
    document.getElementById("myForm").style.display = "none";
}


//action write post when price and cotations open
$('#cotation').on('change click',function(){
    if(!$('#price').val() == ""){
        cote()
    }
});

$('#price').on('change click',function(){
    if(!$("#cotation").val() == ""){
        cote()
    }
});


//write a pari
function cote() {
    var price = parseFloat($('#price').val()).toFixed(2)
    $.ajax({
        url: window.location.href + "/verify", // the endpoint
        type: "POST", // http method
        data: {
            csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
            priceUser : price
        },
        success: function (json) {
            var price = parseFloat($('#price').val()).toFixed(2)
            if (json.fund >= price){
                var cotation = parseFloat($('#cotation').val()).toFixed(1)
                var calcul = (cotation*price).toFixed(2);
                $('#calcul-cote').text("Cote : " + cotation + " Gain potentiel : " + calcul + " Perte potentielle : " + price);
                $('.send').attr("disabled", false);

            }
            else {
                $('#calcul-cote').text("Vous n'avez pas suffisamnet de fond")
                $('.send').attr("disabled", true);
            }
        },

        // handle a non-successful response
        error: function (xhr, errmsg, err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}



// display take popup (verify your money)
function takePopup(priceUser) {
    $.ajax({
        url: window.location.href + "/verify", // the endpoint
        type: "POST", // http method
        data: {
            csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
            priceUser : priceUser
        },

        // handle a successful response
        success: function (json) {
            if (json.fund >= priceUser){
                $('.action-take-result').text("Prix : " + priceUser);
                $('#take-popup').css("display", "block");
            }
            else {
                $('.action-take-result').text("Vous n'avez pas suffisament de fond");
                $('.send').css("display", "none");
                $('#take-popup').css("display", "block");
            }
        },

        // handle a non-successful response
        error: function (xhr, errmsg, err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });

}


//close take popup
function closeTake() {
    $('#take-popup').css("display", "none");
}

//take a pari
function take(postId) {
    $.ajax({
        url: window.location.href + "/take/"+postId, // the endpoint
        type: "POST", // http method
        data: {
            csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
        },

        // handle a successful response
        success: function (json) {
            $('#take-popup').css("display", "none");
            $('#action-take').css("display", "none");
            $('#action-take-confirm').text("Vous avez pariez")
            location.reload()
        },

        // handle a non-successful response
        error: function (xhr, errmsg, err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}