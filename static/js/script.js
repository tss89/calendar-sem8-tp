window.fbAsyncInit = function() {
    FB.init({
        appId      : '820950291432093',
        cookie     : true,
        xfbml      : true,
        version    : 'v2.12'
    });
        
    FB.AppEvents.logPageView();
};

(function(d, s, id){
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) {return;}
    js = d.createElement(s); js.id = id;
    js.src = "https://connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));

function checkLoginState() {
    FB.getLoginStatus(function(response) {
        statusChangeCallback(response);
    });
}

function statusChangeCallback(response){
    console.log(response);
    jQuery.ajax({
        url         : "/auth/flogin/token/",
        type        : "GET",
        contentType : 'aplication/json',
        dataType    : 'json',
        data        : {
            access_token: response.authResponse.accessToken,
            user_id: response.authResponse.userID,
        },
        success : function(data) {
            console.log(data);
        }
    });
}