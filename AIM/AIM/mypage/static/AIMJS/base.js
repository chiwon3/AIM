var $window = $(window),
    $mainnav = $('.mainnav'),
    $defaultLogo = '/static/AIMimage/logo.svg',
    $smallLogo = '/static/AIMimage/logo-small2.svg';

    $window.scroll(function(){
        if($(this).scrollTop() > 5){
            if(!$mainnav.hasClass('small')){
                $mainnav.addClass('small');
                switchImages($smallLogo);
            }
        }
        else {
            if($mainnav.hasClass('small')){
                $mainnav.removeClass('small');
                switchImages($defaultLogo);
            }            
        }
    })

    function switchImages(scrollImage){
        var $logo = $('#mainlogo');
        $logo.fadeOut(500, function(){
            $logo.attr('src', scrollImage);
            $logo.fadeIn(500);
        });

    }