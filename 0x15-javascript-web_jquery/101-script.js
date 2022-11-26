$(() => {
    $( "#add_item" ).click(() => {
        $( ".my_list" ).append("<li>item</li>");
    });
    $( "#remove_item" ).click(() => {
        const lis = $('UL.my_list').children().last();
        if (lis) {
            lis.remove();
        }
    });
    $( "#clear_list" ).click(() => {
        $('UL.my_list').empty();
    });
})