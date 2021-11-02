$(function () {

    $(".menu").on({

        mouseover: function () {

            $(this).css("color", "green");

        },
        mouseleave: function () {

            $(this).css("color", "antiquewhite");

        }

    });


    animasyon();


    function animasyon() {

        var say = 1;

        setInterval(function () {

            var a = "spor" + say + ".jpg";


            $("#h_goruntu").fadeOut(3000, function () {

                $(this).queue(function () {

                    $(this).attr("src", a);
                    $(this).dequeue();

                });

                $(this).fadeIn(3000);


            });

            say++;

            if (say == 6) {

                say = 1;
            }



        },6000);




    }


    $("#kapama").on({

        mouseover: function () {

            $(this).css("cursor", "pointer");


        },

        click: function () {

            $("#cerez").css("display", "none");


        }


    });


    $(".kır").on({

        mouseover: function () {

            $(this).css("color", "red");

        },
        mouseleave: function () {

            $(this).css("color", "gray");

        }




    });

    $(".mavi").on({

        mouseover: function () {

            $(this).css("color", "blue");

        },
        mouseleave: function () {

            $(this).css("color", "gray");

        }




    });





});