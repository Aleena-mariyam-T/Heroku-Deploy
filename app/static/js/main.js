jQuery(function ($) {
    'use strict';
    $(document).ready(async function () {
        
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