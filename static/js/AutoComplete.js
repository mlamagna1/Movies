$(document).ready(function () {
    $("#search").autocomplete({
        
        source: function (request, response) {
            $.ajax({
                method: "GET",
                dataType: "json",
                url: "http://www.omdbapi.com/?apikey=66405531&s=" + request.term,
                success: function (data) {
                    console.log(data);
                    // data.Search uses because we have `title`s in {"Search":[{..
                    var transformed = $.map(data.Search, function (el) {
                        return {
                            label: el.Title,
                            id: el.Years
                        };
                    });
                    response(transformed);
                },
                error: function () {
                    response([]);
                }
            });
        }
    });
});
