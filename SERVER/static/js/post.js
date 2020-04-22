function openForm() {
    document.getElementById("myForm").style.display = "block";
}

function closeForm() {
    document.getElementById("myForm").style.display = "none";
}


//action write post when price and cotations open
$('#cotation').on('change',function(){
    if(!$('#price').val() == ""){
        cote()
    }
});

$('#price').on('change',function(){
    if(!$("#cotation").val() == ""){
        cote()
    }
});


//write a pari
function cote() {
    var cotation = parseFloat($('#cotation').val()).toFixed(1)
    var price = parseFloat($('#price').val()).toFixed(2)
    var calcul = (cotation*price).toFixed(2);
    $('#calcul-cote').text("Cote : " + cotation + " Gain potentiel : " + calcul + " Perte potentielle : " + price);

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
            $('#action-take').css("display", "none");

            $('#action-take-result').text("Vous avez pariez " + json.price)

        },

        // handle a non-successful response
        error: function (xhr, errmsg, err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}
