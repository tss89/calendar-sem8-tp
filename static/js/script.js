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
        }
    });

    changeStatus(response.status);
}

function logoutFacebook(){
    FB.logout(function(response) {
        changeStatus(response.status);
    });    
}

function changeStatus(response){
    var facebook_status = jQuery('.facebook__status-response');
    facebook_status.html(response);
    if(response == "connected"){
        facebook_status.addClass("status-connected");  
    } else {
        facebook_status.removeClass("status-connected"); 
    }
}

jQuery(function() {
    jQuery('.calendar').calendar({
        style: 'background',
        mouseOnDay: function(e) {
            if(e.events.length > 0) {
                var content = '';
                
                for(var i in e.events) {
                    content += '<div class="event-tooltip-content">'
                                    + '<div class="event-name" style="color:' + e.events[i].color + '">' + e.events[i].name + '</div>'
                                    + '<div class="event-location">' + e.events[i].location + '</div>'
                                + '</div>';
                }
            
                $(e.element).popover({ 
                    trigger: 'manual',
                    container: 'body',
                    html:true,
                    content: content
                });
                
                $(e.element).popover('show');
            }
        },
        mouseOutDay: function(e) {
            if(e.events.length > 0) {
                $(e.element).popover('hide');
            }
        },
        dataSource: ArrayBrithday
    });
} );