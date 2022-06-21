$(document).ready(function () {
    $(function () {
        $("#id_event_start_date").datepicker();
        $("#id_event_end_date").datepicker();
    });
    $(".contactus").click(function(){
        alert("your response saved we will get back to you soon ");
    })

    $(document).on('submit','#event-comment')
    // $("#eventsubmit").click(function(){
    //     alert("for sumbmiting event you need to pay")
    // });
    //   validation in addeventform
    var username = $("#id_username").val();
    console.log(username,"username");
    // $("#id-addevent-form").submit(function () {
    //     var username = $('#username').val();
    //     if (username == '') {
    //         alert('please enter username');
    //         return false;
    //     }

    //     $.ajax({
    //         type: "POST",
    //         url: "{% url user-login %}",
    //         data: { 'username': $('#username').val(), 'csrfmiddlewaretoken': '{{csrf_token}}' },
    //         dataType: "text",
    //         success: function (response) {
    //             var response = $.parseJSON(response);
    //             if (response.success) {
    //                 return true;
    //             }
    //             else {
    //                 alert(response.error);
    //             }
    //         },
    //         error: function (rs, e) {
    //             alert(rs.responseText);
    //         }
    //     });
    // });
});