function display_friends(){
    $('.card').removeClass("active");
    $('#followers').css("display","none");
    $('#posts').css("display","none");
    $('#missions').css("display","none");

    $('#friends').css("display","block");
    $('.friends').addClass("active");
}

function display_followers(){
    $('.card').removeClass("active");
    $('#posts').css("display","none");
    $('#friends').css("display","none");
    $('#missions').css("display","none");

    $('#followers').css("display","block");
    $('.followers').addClass("active");
}

function display_posts(){
    $('#friends').css("display","none");
    $('#followers').css("display","none");
    $('#missions').css("display","none");
    $('.card').removeClass("active");

    $('#posts').css("display","block");
    $('.posts').addClass("active");
}

function display_missions(){
    $('.card').removeClass("active");
    $('#friends').css("display","none");
    $('#followers').css("display","none");
    $('#posts').css("display","none");

    $('#missions').css("display","block");
    $('.missions').addClass("active");
}