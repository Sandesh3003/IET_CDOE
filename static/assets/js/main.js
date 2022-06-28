/*
  Theme Name: Edubin - LMS Education HTML Template
  Author: PixelCurve
  Author URL: https://themeforest.net/user/pixelcurve
  Support: help.pixelcurve@gmail.com
  Description: Creative  HTML5 template.
  Version: 5.0
*/

document.querySelectorAll('.nav-link').forEach(link=>{
    if(link.href === window.location.href)
    {
        link.classList.add('active-nav-link')
        if(link.classList.contains('sub-nav-link')){
            console.log(link.parentNode.parentNode);
        }
    }
})


$(function() {

    "use strict";

    //===== Prealoder

    $(window).on('load', function(event) {
        $('.preloader').delay(500).fadeOut(500);
    });



    //===== Sticky

    $(window).on('scroll', function(event) {
        var scroll = $(window).scrollTop();
        if (scroll < 245) {
            $(".navigation").removeClass("sticky");
            $(".header-three .navigation img").attr("src", "images/logo-2.png");
        } else {
            $(".navigation").addClass("sticky");
            $(".header-three .navigation img").attr("src", "images/logo.png");
        }
    });


    //===== Mobile Menu

    $(".navbar-toggler").on('click', function() {
        $(this).toggleClass("active");
    });

    var subMenu = $('.sub-menu-bar .navbar-nav .sub-menu');

    if (subMenu.length) {
        subMenu.parent('li').children('a').append(function() {
            return '<button class="sub-nav-toggler"> <i class="fa fa-chevron-down"></i> </button>';
        });

        var subMenuToggler = $('.sub-menu-bar .navbar-nav .sub-nav-toggler');

        subMenuToggler.on('click', function() {
            $(this).parent().parent().children('.sub-menu').slideToggle();
            return false
        });

    }



    //===== Slick Slider

    function mainSlider() {

        var BasicSlider = $('.slider-active');

        BasicSlider.on('init', function(e, slick) {
            var $firstAnimatingElements = $('.single-slider:first-child').find('[data-animation]');
            doAnimations($firstAnimatingElements);
        });

        BasicSlider.on('beforeChange', function(e, slick, currentSlide, nextSlide) {
            var $animatingElements = $('.single-slider[data-slick-index="' + nextSlide + '"]').find('[data-animation]');
            doAnimations($animatingElements);
        });

        BasicSlider.slick({
            autoplay: true,
            autoplaySpeed: 10000,
            pauseOnHover: false,
            dots: false,
            fade: true,
            arrows: true,
            prevArrow: '<span class="prev"><i class="fa fa-angle-left"></i></span>',
            nextArrow: '<span class="next"><i class="fa fa-angle-right"></i></span>',
            responsive: [{
                breakpoint: 767,
                settings: {
                    dots: false,
                    arrows: false
                }
            }]
        });

        function doAnimations(elements) {
            var animationEndEvents = 'webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend';
            elements.each(function() {
                var $this = $(this);
                var $animationDelay = $this.data('delay');
                var $animationType = 'animated ' + $this.data('animation');
                $this.css({
                    'animation-delay': $animationDelay,
                    '-webkit-animation-delay': $animationDelay
                });
                $this.addClass($animationType).one(animationEndEvents, function() {
                    $this.removeClass($animationType);
                });
            });
        }
    }
    mainSlider();


    //===== Back to top

    // Show or hide the sticky footer button
    $(window).on('scroll', function(event) {
        if ($(this).scrollTop() > 600) {
            $('.back-to-top').fadeIn(200)
        } else {
            $('.back-to-top').fadeOut(200)
        }
    });


    //Animate the scroll to yop
    $('.back-to-top').on('click', function(event) {
        event.preventDefault();

        $('html, body').animate({
            scrollTop: 0,
        }, 1500);
    });


    //===== Nice Select

    $('select').niceSelect();


});

// Useful links carousel
$(document).ready(function(){

    if($('.brands_slider').length)
         {
             var brandsSlider = $('.brands_slider');
 
             brandsSlider.owlCarousel(
             {
                 loop:true,
                 autoplay:true,
                 autoplayTimeout:2000,
                 nav:false,
                 dots:false,
                 autoWidth:true,
                 margin:42
             });
 
         }
 
 
     });


     // Scroll to Nav Search

     function scrollToSearch() {
        let e = document.getElementById("gcse-search");
        e.scrollIntoView({
          block: 'start',
          behavior: 'smooth',
          inline: 'start'
        });
      }
