// // full calendar
// document.addEventListener('DOMContentLoaded', function() {
//     var calendarEl = document.getElementById('calendar');
   
//     var calendar = new FullCalendar.Calendar(calendarEl, {
//       headerToolbar: {
//         start: 'title',
//         center: '',
//         end: 'prev,today,next'
//       },
//       initialView: 'dayGridMonth',
      
//       views: {
//         dayGridWeek: {
//           titleFormat: '{DD.{MM.}}YYYY'
//         },
//         listWeek: {
//           titleFormat: '{DD.{MM.}}YYYY'
//         }
//       },
//       events: [
//         {
//                   title: 'P',                
//                   start: '2022-04-01',
//                   backgroundColor: '#7fc27c',
//               },  
//               {
//                   title: 'P',                
//                   start: '2022-04-02',
//                   backgroundColor: '#7fc27c'
//               },
//               {
//                   title: 'P',                
//                   start: '2022-04-03',
//                   backgroundColor: '#7fc27c'
//               },  
//                 {
//                   title: 'A',
//                   start: '2022-04-04',
//                   backgroundColor: '#ea9595'
//               }
//               ,  
//                 {
//                   title: 'H',
//                   start: '2022-04-15',
//                   backgroundColor: '#333'
//               }
//               ,  
//                 {
//                   title: 'H',
//                   start: '2022-04-16',
//                   backgroundColor: '#333'
//               }
//               ,
//                 {
//                     title: 'H',
//                     start: '2022-05-11',
//                     backgroundColor: '#333'
//                 }
//       ],
       
   
//       windowResize: function(view) {
//         var current_view = view.type;
//         var expected_view = $(window).width() > 800 ? 'dayGridMonth' : 'listWeek';
//         if (current_view !== expected_view) {
//           calendar.changeView(expected_view);
//         }
//       },
//     });
   
//     calendar.render();
   
//     if ($(window).width() < 800) {
//       calendar.changeView('listWeek');
//     }
   
//     $('input[class=event_filter]').change(function() {
//       calendar.render();
//     });
      
//    });