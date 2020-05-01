//display comment negociate
function displayComment(postId) {
    var id = "display-comment-"+postId
    document.getElementById(id).style.display = "block";
}

function closeComment(postId) {
    var id = "display-comment-"+postId
    document.getElementById(id).style.display = "none";
}



// display take popup
function negociatePopup(postId) {
    var id = '#display-comment-' +postId
    $.ajax({
        url: window.location.href + "/negociate/"+postId, // the endpoint
        type: "POST", // http method
        data: {
            csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
            price: $(id).find('input[name="price"]').val(),
        },

        success: function (json) {
            $('.content-popup').empty()
            $('.content-popup').html(
                "<div class='action-take-result'>"+
                            "Prix : "
                            +  $(id).find('input[name="price"]').val()
                            +"<br>Nouvelle côte : "
                            + json.newCotation
                            + "<br>Nouvelle côte adversaire : "
                            + json.newCotationUser +
                        "</div>"+
                        "<input class='button send' type='submit' onclick='comment("+ postId +")' value='Accepté'>"+
                        "<input class='button cancel' value='Annuler' onclick='closeNegociate()'>")

            $('#negociate-popup').css("display", "block");
        },

        error: function (xhr, errmsg, err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}



//close take popup
function closeNegociate() {
    $('#negociate-popup').css("display", "none");
}


//action write post when price and cotations open
function comment(postId) {
    var id = '#display-comment-' +postId
    $.ajax({
        url: window.location.href + "/comment/"+postId, // the endpoint
        type: "POST", // http method
        data: {
            csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
            price: $(id).find('input[name="price"]').val(),
            text: $(id).find("textarea[name='text']").val()
        },

        // handle a successful response
        success: function (json) {
            $('#negociate-popup').css("display", "none");
            $('#action-take-confirm').text("Vous avez négocier")
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

