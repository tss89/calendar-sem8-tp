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
        url         : "/flogin/token/",
        type        : "post",
        contentType : 'aplication/json',
        dataType    : 'json',
        data        : {
            response : response
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
    jQuery('.facebook__status-response').html(response);
}

var currentYear = new Date().getFullYear();

jQuery(function() {
    jQuery('.calendar').calendar({
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
        dataSource: [
            {
                id: 0,
                name: 'Michał',
                location: 'Urodziny',
                startDate: new Date(currentYear, 11,6),
                endDate: new Date(currentYear, 11, 6)
            },
            {
                id: 1,
                name: 'Kozioł',
                location: 'Urodziny',
                startDate: new Date(currentYear, 0, 20),
                endDate: new Date(currentYear, 0, 20)
            },
            {
                id: 2,
                name: 'Oskar',
                location: 'Urodziny',
                startDate: new Date(currentYear, 7, 25),
                endDate: new Date(currentYear, 7, 25)
            },
            {
                id: 3,
                name: 'Tomek',
                location: 'Urodziny',
                startDate: new Date(currentYear, 1, 13),
                endDate: new Date(currentYear, 1, 13)
            },
        ]
    });
} );