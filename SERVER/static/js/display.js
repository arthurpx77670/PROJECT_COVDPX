function display_friends(){
    $('#friends').css("display","block");
    $('.friends').addClass("active");

    $('#followers').css("display","none");
    $('#posts').css("display","none");
    $('.followers').removeClass("active");
    $('.posts').removeClass("active");

}

function display_followers(){

    $('#followers').css("display","block");
    $('.followers').addClass("active");

    $('#posts').css("display","none");
    $('#friends').css("display","none");
    $('.friends').removeClass("active");
    $('.posts').removeClass("active");

}

function display_posts(){

    $('#posts').css("display","block");
    $('.posts').addClass("active");

    $('#friends').css("display","none");
    $('#followers').css("display","none");
    $('.followers').removeClass("active");
    $('.friends').removeClass("active");

}