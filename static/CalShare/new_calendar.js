//
// document.addEventListener('DOMContentLoaded', function() {
//     var calendarEl = document.getElementById('calendar');
//
//     var calendar = new FullCalendar.Calendar(calendarEl, {
//       headerToolbar: {
//         left: 'prev,next today',
//         center: 'title',
//         right: 'dayGridMonth,timeGridWeek,timeGridDay'
//       },
//       initialDate: '2020-09-12',
//       navLinks: true, // can click day/week names to navigate views
//       selectable: true,
//       selectMirror: true,
//       select: function(arg) {
//         var title = prompt('Event Title:');
//         if (title) {
//           calendar.addEvent({
//             title: title,
//             start: arg.start,
//             end: arg.end,
//             allDay: arg.allDay
//           })
//         }
//         calendar.unselect()
//       },
//       eventClick: function(arg) {
//         if (confirm('Are you sure you want to delete this event?')) {
//           arg.event.remove()
//         }
//       },
//       editable: true,
//       dayMaxEvents: true, // allow "more" link when too many events
//       events: [
//         {
//           title: 'All Day Event',
//           start: '2020-09-01'
//         },
//         {
//           title: 'Long Event',
//           start: '2020-09-07',
//           end: '2020-09-10'
//         },
//         {
//           groupId: 999,
//           title: 'Repeating Event',
//           start: '2020-09-09T16:00:00'
//         },
//         {
//           groupId: 999,
//           title: 'Repeating Event',
//           start: '2020-09-16T16:00:00'
//         },
//         {
//           title: 'Conference',
//           start: '2020-09-11',
//           end: '2020-09-13'
//         },
//         {
//           title: 'Meeting',
//           start: '2020-09-12T10:30:00',
//           end: '2020-09-12T12:30:00'
//         },
//         {
//           title: 'Lunch',
//           start: '2020-09-12T12:00:00'
//         },
//         {
//           title: 'Meeting',
//           start: '2020-09-12T14:30:00'
//         },
//         {
//           title: 'Happy Hour',
//           start: '2020-09-12T17:30:00'
//         },
//         {
//           title: 'Dinner',
//           start: '2020-09-12T20:00:00'
//         },
//         {
//           title: 'Birthday Party',
//           start: '2020-09-13T07:00:00'
//         },
//         {
//           title: 'Click for Google',
//           url: 'http://google.com/',
//           start: '2020-09-28'
//         }
//       ]
//     });
//
//     calendar.render();
//   });
document.addEventListener('DOMContentLoaded', function() {
    //credit to https://www.youtube.com/watch?v=P-jKHhr6YxI for exactly what I needed to get formdata out of form
    var helper = Array.from(document.querySelectorAll('#event_form input' )).reduce((acc, input) =>({...acc,[input.id]:input.value}),{});
    document.getElementById("submit_new_event").addEventListener("click", function (){
        console.log(helper);
        fetch(`/api_async_create/${helper}`)
            .then(response => response.json())
            .then(data => {


            })
            .catch(error => {
                console.log("*** api_create_event **", error);
            })
    });


    function create_event() {

        fetch(`/api_event_create/${document.getElementById("saved_id").innerText}`)
            .then(response => response.json())
            .then(data => {

                add_form_thing(data)
            })
            .catch(error => {
                console.log("*** api_create_event **", error);
            })

    }
    function add_form_thing(data){
        let event_form = document.getElementById("event_form");
        console.log(data)
        //event_form.append(data.event_form);
        // event_form.onclick("submit",function (e){
        //     e.preventDefault();
        // } )
        dialog_box()
        return event_form
    }
    function dialog_box() {
        var dialog
        dialog = $("#event_form").dialog({
                autoOpen: false,
                height: 800,
                width: 700,
                modal: true,
                buttons: {
                    "Create Event": function(){
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
    function click_catcher(){

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
        select: function (arg) {
            //var title = prompt('Event Title:');
            //document.getElementById("#start_date").setAttribute('value',arg.start);
            //document.getElementById("#end_date").setAttribute('value',arg.end);
            create_event()
            //if (title) {

            // calendar.addEvent({ //intercept here
            //     title: ,
            //     start: ,
            //     end: ,
            //     //allDay: true
            // })
            // }
            calendar.unselect()
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

    calendar.render();
});