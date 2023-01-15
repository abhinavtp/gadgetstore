
function add_to_cart(p_id){
    $.ajax({
        url: "add_to_cart",
        type: "POST",
        data: {
            id:p_id,
            'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()

        },
        success: function (response) {
            alert(response.message)
        }
    })
}