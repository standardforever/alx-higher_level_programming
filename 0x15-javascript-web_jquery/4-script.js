$("#toggle_header").click(function() {
    if ($( ".red" ).length) {
        $("header").removeClass( "red" ).addClass( "green" )
    } else if($( ".green" ).length) {
        $("header").removeClass( "green" ).addClass( "red" );
    }
})