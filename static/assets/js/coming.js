$(function () {
  $(".notify-btn").click(function () {
    $(".notify-btn").addClass("active");
    $(input).addClass("active");
    $(".submit-btn").addClass("active");
  });
});

$(function () {
  $(".submit-btn").click(function () {
    $(this).removeClass("active");
    $("input").removeClass("active");
    $(".thanku-btn").addClass("active");
  });
});
