$(document).ready(function(){

   $('.table').paging({limit:6});
   $(".datetimeinput").datepicker({changeYear: true, changeMonth: true, dateFormat: 'yyyy-mm-dd hh:mm'});

   $("#sidebar").mCustomScrollbar({
      theme: "minimal"
  });

  $('#dismiss, .overlay').on('click', function () {
      // hide sidebar
      $('#sidebar').removeClass('active');
      // hide overlay
      $('.overlay').removeClass('active');
  });

  $('#sidebarCollapse').on('click', function () {
      // open sidebar
      $('#sidebar').addClass('active');
      // fade in the overlay
      $('.overlay').addClass('active');
      $('.collapse.in').toggleClass('in');
      $('a[aria-expanded=true]').attr('aria-expanded', 'false');
  });
});

// $(document).ready(function () {
  
// });