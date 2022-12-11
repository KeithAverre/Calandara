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
    function making_event() {
    var dialog, form,

      // From http://www.whatwg.org/specs/web-apps/current-work/multipage/states-of-the-type-attribute.html#e-mail-state-%28type=email%29

      name = $( "#name" ),
      start_date = $( "#start_date" ),
      start_time = $( "#start_time" ),
      end_date = $( "#end_date" ),
      end_time = $( "#end_time" ),
      allFields = $( [] ).add( name ).add( start_date ).add( end_date ).add( start_time ).add( end_time ),
      tips = $( ".validateTips" );





    function e_addEvent(name, start_date, start_time, end_date, end_time ) {
      //this is where I fetch to django server
      console.log("hi")
      dialog.dialog( "close" );
      return {"name": name,
              "start_date": start_date,
              "start_time": start_time,
              "end_date": end_date,
              "end_time": end_time};






    }

    dialog = $( "#dialog-form" ).dialog({
      autoOpen: false,
      height: 400,
      width: 350,
      modal: true,
      buttons: {
        "Create an Event": e_addEvent,
        Cancel: function() {
          dialog.dialog( "close" );
        }
      },
      close: function() {
        form[0].reset();
      }
    });

    form = dialog.find( "form" ).on( "submit", function( event ) {
      event.preventDefault();
      console.log("sad")
      return e_addEvent(name, start_date, start_time, end_date, end_time);
    });
      dialog.dialog( "open" );


  } ;


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
      select: function(arg) {
        //var title = prompt('Event Title:');
          //document.getElementById("#start_date").setAttribute('value',arg.start);
          //document.getElementById("#end_date").setAttribute('value',arg.end);
        console.log(document.getElementById("#end_date").value)
          document.getElementById("#end_date").value = arg.end;
        //if (title) {
        var eve = making_event();
        console.log(eve)
          calendar.addEvent({ //intercept here
            title: eve['name'],
            start: eve['start_date'],
            end: eve['end_date'],
            //allDay: true
          })
       // }
        calendar.unselect()
      },
      eventClick: function(arg) {
        if (confirm('Are you sure you want to delete this event?')) {
          arg.event.remove()
        }
      },
      editable: true,
      dayMaxEvents: true, // allow "more" link when too many events
      events: {
        url: 'ics/feed.ics',
        format: 'ics',
        failure: function() {
          document.getElementById('script-warning').style.display = 'block';
        }
      },
      loading: function(bool) {
        document.getElementById('loading').style.display =
          bool ? 'block' : 'none';
      }
    });

    calendar.render();
  });