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
});