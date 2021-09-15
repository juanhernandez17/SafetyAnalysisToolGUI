$(document).ready(function () {
    var csrftoken = getCookie('csrftoken');
$('button[id^="delete"]').on('click', function () {
    var id = $(this).attr('id').replace('delete-', '')
    $.ajax({
        url: '/api/system/' + id,
        method: 'DELETE',
        data: {},
        contentType: 'application/json',
        dataType: 'text',
        beforeSend: function (xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        },
        success: function () {
            $("div[id='card-" + id + "']").html(
                "<h5>Deleted</h5><div class='spinner-border' role='status'> <span class='sr-only'> Loading... </span></div>"
            )
            setTimeout(location.reload.bind(location), 2000);
        },
        // handle a non-successful response
        error: function (xhr, errmsg, err) {
            $('#sysList div').html(
                "<div class = 'alert alert-danger' ><strong > Error </strong> Couldn\'t delete <div class='spinner-border' role='status'> <span class='sr-only'> Loading... </span></div></div> "
            )
            setTimeout(location.reload.bind(location), 2000);
        }
    })
})
    // using jQuery to get csrftoken
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

});