
if(document.getElementById("saved_id").innerText != null){
document.addEventListener('DOMContentLoaded', function() {


    function create_event() {

        fetch(`/api_event_create/${document.getElementById("saved_id").innerText}`)
            .then(response => response.json())
            .then(data => {

                dialog_box()
            })
            .catch(error => {
                console.log("*** api_create_event **", error);
            })

    }

    function dialog_box() {
        var dialog
        dialog = $("#event_form").dialog({
                autoOpen: false,
                height: 800,
                width: 700,
                modal: true,
                buttons: {
                    "Create Event": function () {
                        document.getElementById("submit_new_event").click()
                    },
                    Cancel: function () {
                        dialog.dialog("close");
                    }
                },
                close: function () {
                }
            },
        );
        dialog.dialog("open");
    };

    function click_catcher() {

    }

    var calendarEl = document.getElementById('calendar');

    var calendar = new FullCalendar.Calendar(calendarEl, {
        displayEventTime: true,
        initialDate: '2022-12-11',
        headerToolbar: {
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek,timeGridDay,listMonth'
        },

        navLinks: true, // can click day/week names to navigate views
        selectable: true,
        selectMirror: true,
        //events: [],
        select: function (arg) {
            create_event()
            //if (title) {
            // var helper;
            // document.getElementById("submit_new_event").addEventListener("click", function () {
            //     //credit to https://www.youtube.com/watch?v=P-jKHhr6YxI for exactly what I needed to get formdata out of form
            //     helper = Array.from(document.querySelectorAll('#event_form input')).reduce((acc, input) => ({
            //         ...acc,
            //         [input.id]: input.value
            //     }), {});
            //     console.log(helper);


                // calendar.addEvent({ //intercept here
                //     title: helper.id_title,
                //     start: helper.id_start_day,
                //     end: helper.id_end_day,
                //     //allDay: true
                // })
                calendar.unselect()
            // })
        },


        eventClick: function (arg) {
            if (confirm('Are you sure you want to delete this event?')) {
                arg.event.remove()
            }
        },
        editable: true,
        dayMaxEvents: true, // allow "more" link when too many events
        events: {
            url: 'ics/feed.ics',
            format: 'ics',
            failure: function () {
                document.getElementById('script-warning').style.display = 'block';
            }
        },
        loading: function (bool) {
            document.getElementById('loading').style.display =
                bool ? 'block' : 'none';
        }
    });
    var holder;
    fetch(`/api_get_events/${document.getElementById("saved_id").innerText}`)
        .then(response => response.json())
        .then(data => {

            holder = data
            var i = 0;

            while(holder[`${i}`] != null){

                calendar.addEvent({"title": `${holder[`${i}`].title}`,
                                        "start": `${holder[`${i}`].start_day}T${holder[`${i}`].start_time}`,
                                        "end":    `${holder[`${i}`].end_day}T${holder[`${i}`].end_time}`});
                i = i +1;
            }
        })
        .catch(error => {
            console.log("*** api_create_event **", error);
        })

    calendar.render();
})};
