//display action mission
function displayValidate(missionId) {
    var id = "display-validate-"+missionId
    document.getElementById(id).style.display = "block";
}

function closeValidate(missionId) {
    var id = "display-validate-"+missionId
    document.getElementById(id).style.display = "none";
}

function displayDetail(missionId) {
    var id = "display-detail-"+missionId
    document.getElementById(id).style.display = "block";
}

function closeDetail(missionId) {
    var id = "display-detail-"+missionId
    document.getElementById(id).style.display = "none";
}

function displayResult(missionId) {
    var id = "display-result-"+missionId
    document.getElementById(id).style.display = "block";
}

function closeResult(missionId) {
    var id = "display-result-"+missionId
    document.getElementById(id).style.display = "none";
}

function validate(missionId) {
    $.ajax({
        url: window.location.href + "/validate", // the endpoint
        type: "POST", // http method
        data: {
            csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
            missionId :missionId,
        },
        success: function (json) {
            $('.title').text("Valider le résultat")
            $('.content-popup').empty()
            $('.content-popup').html(
                "<div class='action-validate'>"+
                json.result +
                "</div>"+
                "<input class='button send' type='submit' onclick='finish("+ missionId +")' value='Accepté'>"+
                "<input class='button cancel' value='Annuler' onclick='closeConfirm()'>")
            $('#popup').css("display", "block");
        },
        error: function (xhr, errmsg, err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}


function finish(missionId) {
    $.ajax({
        url: window.location.href + "/finish", // the endpoint
        type: "POST", // http method
        data: {
            csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
            missionId :missionId,
        },

        success: function (json) {
            var id = "#display-result-"+missionId
            $('#popup').css("display", "none");
            $(id).css("display","none");
            $(".action-results").css("display","none");
            $("#action-result-text").text("Vous avez conclu le pari");
            location.reload()
        },

        error: function (xhr, errmsg, err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}


function refuse(authorId,missionId) {
    $.ajax({
        url: window.location.href + "/confirm", // the endpoint
        type: "POST", // http method
        data: {
            csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
            missionId :missionId,
            winnerId : authorId
        },
        success: function (json) {
            $('.content-popup').empty()
            $('.content-popup').html(
                "<div class='action-confirm'>"+
                json.result +
                "</div>"+
                "<input class='button send' type='submit' onclick='result("+ authorId +"," + missionId +")' value='Accepté'>"+
                "<input class='button cancel' value='Annuler' onclick='closeConfirm()'>")
            $('#popup').css("display", "block");
        },
        error: function (xhr, errmsg, err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}


function confirm(authorId,missionId) {
    $.ajax({
        url: window.location.href + "/confirm", // the endpoint
        type: "POST", // http method
        data: {
            csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
            missionId :missionId,
            winnerId : authorId
        },

        success: function (json) {
            $('.title').text("Confirmer le résultat")
            $('.content-popup').empty()
            $('.content-popup').html(
                "<div class='action-confirm'>"+
                json.result +
                "</div>"+
                "<input class='button send' type='submit' onclick='result("+ authorId +"," + missionId +")' value='Accepté'>"+
                "<input class='button cancel' value='Annuler' onclick='closeConfirm()'>")
            $('#popup').css("display", "block");
        },

        error: function (xhr, errmsg, err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}

function closeConfirm() {
    document.getElementById("popup").style.display = "none";
}


function result(authorId,missionId) {
    $.ajax({
        url: window.location.href + "/deposit", // the endpoint
        type: "POST", // http method
        data: {
            csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
            missionId :missionId,
            winnerId : authorId
        },
        success: function (json) {
            var id = "#display-result-"+missionId
            $('#popup').css("display", "none");
            $(id).css("display","none");
            $(".action-results").css("display","none");
            $("#action-result-text").text("Vous avez désigné le gagnant");
            location.reload()
        },
        error: function (xhr, errmsg, err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}