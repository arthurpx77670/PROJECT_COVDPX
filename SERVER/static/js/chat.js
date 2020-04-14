
function openChats() {
    $('#chats-popup-content').empty()
    document.getElementById("myChats").style.display = "block";
    $.ajax({
        url: window.location.href + "/chats", // the endpoint
        type: "POST", // http method
        data: {
            csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
        }, // data sent with the post request

        // handle a successful response
        success: function (json) {
            for (i=0;i< json.listChat.length;i++){
                $('#chats-popup-content').html(
                    $('#chats-popup-content').html() +
                    "<a id='link-notif'>"+
                        "<div id='notif'>"+
                            "<div id='date-notif'>"+ json.listDate[i] + "</div>" +
                            "<div class='chip' id='user-notif'>" +
                            "<img src='" + json.listUrl[i] +"' alt='Person' width='96' height='96'>" +
                             json.listUsername[i] +
                            "</div>" +
                            "<div id='chat-notif'>"+ json.listChat[i] + "</div>" +
                        "</div>" +
                    "</a>")
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


function closeChats() {
    document.getElementById("myChats").style.display = "none";
}

function openChat() {
    document.getElementById("myChat").style.display = "block";
}

function closeChat() {
    document.getElementById("myChat").style.display = "none";
}


function submitChat() {
    chat();
}


function chat() {
    $.ajax({
        url: window.location.href + "/chat", // the endpoint
        type: "POST", // http method
        data: {
            chat_text: $('#chat-text').val(),
            csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
        }, // data sent with the post request

        // handle a successful response
        success: function (json) {

            $('#talk').html(
                $('#talk').html() +
                "<div class='row'>"+
                "<span class='time'>"+ json.chatDate +"</span>"+
                "</div>"+
                "<div class='conversation request'>" +
                "<div id='chat-pict'>" +
                "</div>" +
                "<p>"+json.chatText+"</p>\n" +
                "</div>"
            )
            $('#chat-text').val('')
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error: function (xhr, errmsg, err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}



// $.ajax({
//     url : window.location.href +"/refresh_chat", // the endpoint
//     type : "POST", // http method
//     data : { lastChat : $('#count').text(),
//              csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),}, // data sent with the post request
//
//     success : function(json) {
//
//         $('#talk').html(
//                 $('#talk').html() + "<br><ul><li>De : "+json.chatSender+"</li><li>Pour :"+json.chatReceiver+"</li><li>"+json.chatText+"</li></ul>"
//             )
//
//         setTimeout(function(){// wait for 5 secs(2)
//            location.reload(); // then reload the page.(3)
//       }, 5000);
//         console.log("success"); // another sanity check
//     },
//
//     error : function(xhr,errmsg,err) {
//         console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
//     }
// });
//