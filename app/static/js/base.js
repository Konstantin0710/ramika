$(document).ready(function () {
    $(".ramika-button input").hover(
        function () {
            $(".ramika-button img.top").animate({opacity: 100}, 200);
        },
        function () {
            $(".ramika-button img.top").animate({opacity: 0}, 200);
        }
    );

    $(".invitation-button a").hover(
        function () {
            $(".invitation-button img.top").animate({opacity: 100}, 200);
        },
        function () {
            $(".invitation-button img.top").animate({opacity: 0}, 200);
        }
    );

    $(".assist-button a").hover(
        function () {
            $(".assist-button img.top").animate({opacity: 100}, 200);
        },
        function () {
            $(".assist-button img.top").animate({opacity: 0}, 200);
        }
    );

    $(".not-assist-button a").hover(
        function () {
            $(".not-assist-button img.top").animate({opacity: 100}, 200);
        },
        function () {
            $(".not-assist-button img.top").animate({opacity: 0}, 200);
        }
    );

    $(".assist-button a").click(
        function () {
            $.get("/mapview/assist/", function (data) {
                $(".thanks").animate({opacity: 0}, 500);
                $(".selected-button").removeClass("selected-button");
                $(".assist-button").addClass("selected-button");
                $(".thanks").animate({opacity: 100}, 1500);
            });
        }
    );

    $(".not-assist-button a").click(
        function () {
            $.get("/mapview/not-assist/", function (data) {
                $(".thanks").animate({opacity: 0}, 500);
                $(".selected-button").removeClass("selected-button");
                $(".not-assist-button").addClass("selected-button");
                $(".thanks").animate({opacity: 100}, 1500);
            });
        }
    );
});