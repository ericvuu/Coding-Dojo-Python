$(document).ready(function(){

  $("#meal_search_form").submit(function (e) {
    e.preventDefault();
    var query = $("#meal_search_input").val();
    $.ajax({
      url:
        "https://api.spoonacular.com/recipes/complexSearch?query=" + query + "&apiKey=ea993de9a73c40789069a174c4ce5977",
      method: "get",
      success: function(apiResponse) {
        console.log("Recieved this from the Spoonacular: ", apiResponse);
        meals = apiResponse
      },
    });
  });

});
