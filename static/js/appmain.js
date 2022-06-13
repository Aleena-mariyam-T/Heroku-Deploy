jQuery(function ($) {
    'use strict';
    $(document).ready(async function () {

        $('#eventsubmit').click(function(){
            var result = confirm("for publishing event you need to pay?");
            console.log("insude event submit");
            if (result){
                $.ajax({
                    method : 'GET',
                    url :"'{% 'CheckPaymentView' %}",
                })
                
            }
        });
        
        $('#id_event_start_date').datepicker({
            weekStart: 1,
            daysOfWeekHighlighted: "6,0",
            autoclose: true,
            todayHighlight: true,
        });
        $('#id_event_end_date').datepicker({
            weekStart: 1,
            daysOfWeekHighlighted: "6,0",
            autoclose: true,
            todayHighlight: true,
        });
        
        $('#id_event_start_date', '#id_event_end_date').datepicker("setDate", new Date());


    });

});