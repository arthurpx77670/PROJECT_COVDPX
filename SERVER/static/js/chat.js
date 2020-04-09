$('#chat-form').on('submit',function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    chat();
});

function chat() {
    $.ajax({
        url : window.location.href+"/chat", // the endpoint
        type : "POST", // http method
        data : {
            chat_text : $('#chat-text').val(),
            csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
        }, // data sent with the post request

        // handle a successful response
        success : function(json) {

            $('#talk').html(
                $('#talk').html() + "<br><ul><li>De : "+json.chatSender+"</li><li>Pour :"+json.chatReceiver+"</li><li>"+json.chatText+"</li></ul>"
            )
            $('#chat-text').val('')
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};




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

