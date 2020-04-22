//display comment negociate
function display_comment(postId) {
    var id = "display-comment-"+postId
    document.getElementById(id).style.display = "block";
}

function closeComment(postId) {
    var id = "display-comment-"+postId
    document.getElementById(id).style.display = "none";
}



//action write post when price and cotations open
function negociate() {


    // var cotation = parseFloat($('#cotation').val()).toFixed(1)
    // var price = parseFloat($('#price').val()).toFixed(2)
    // var calcul = (cotation*price).toFixed(2);
    // $('#calcul-cote-negociate').text("Cote : " + cotation + " Gain potentiel : " + calcul + " Perte potentielle : " + price);

}

