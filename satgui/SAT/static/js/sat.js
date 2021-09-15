$(document).ready(function () {
  var csrftoken = getCookie('csrftoken');
  // listen to a system selection
  $('#sysList div').on('click', function (e) {
    e.preventDefault()
    var id = $(this).attr('id').replace('list-', '')
    $('input[name="name"]').val($.trim($('#name-' + id).text()));
    $('textarea[name="description"]').val($.trim($('#description-' + id).text()));
    $('input[name="system_id"]').val(id);
    $('#startanal').prop('disabled', false);
    $('#startanal').css('background', '#007bff');
  })
  // listen for button click to clear form parameters
  $('#clear').on('click', function () {
    $('#sysList div').removeClass('active')
    $("#createS")[0].reset()
    $('input[name="system_id"]').val('');
  })
  // listen for button click to delete system
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
        $("#sysList div[aria-controls=" + id + "]").html("<h5>Deleted</h5><div class='spinner-border' role='status'> <span class='sr-only'> Loading... </span></div>")
        $("#createS")[0].reset()
        $('input[name="system_id"]').val('');
        setTimeout(location.reload.bind(location), 2000);
      },
      // handle a non-successful response
      error: function (xhr, errmsg, err) {
        $('#sysList div').html("<div class = 'alert alert-danger' ><strong > Error </strong> Couldn\'t delete <div class='spinner-border' role='status'> <span class='sr-only'> Loading... </span></div></div> ")
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