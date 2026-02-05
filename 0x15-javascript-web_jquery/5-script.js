$(document).ready(function() {
    $('DIV#add_item').click(function() {
        newEle = "<li>Item</li>";
        $("UL.my_list").append(newEle);
    });
});
