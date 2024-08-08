$(document).ready(function() {
    $('#add_item').click(function() {
        var newItem = $('<li>Item</li>');
        $('.my_list').append(newItem);
    });
});
