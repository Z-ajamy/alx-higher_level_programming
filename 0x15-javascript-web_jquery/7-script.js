$(document).ready(function() {
    $.ajax({
        url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
        method: 'GET',
        success: function(data) {
            $('#character').text(data.name);
        },
        error: function() {
            $('#character').text('Failed to retrieve character data.');
        }
    });
});
