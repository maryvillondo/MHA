function sorhSignIn() {
  var x = document.getElementById("signin-box");
  if(x.style.display === "block"){
    x.style.display = "none";
  } else if (x.style.display === "none"){
    x.style.display = "block";
  }
}


function showCustomerSummary() {
  var dvdSummarySec = document.getElementById("dvdSummary");
  var customerSummarySec = document.getElementById("customerSummary");
  dvdSummarySec.style.display = 'none';
  customerSummarySec.style.display = 'block';
}


function showDVDSummary() {
  var dvdSummarySec = document.getElementById("dvdSummary");
  var customerSummarySec = document.getElementById("customerSummary");
  dvdSummarySec.style.display = 'block';
  customerSummarySec.style.display = 'none';
}

function showOverallSummary() {
  var dvdSummarySec = document.getElementById("dvdSummary");
  var customerSummarySec = document.getElementById("customerSummary");
  dvdSummarySec.style.display = 'block';
  customerSummarySec.style.display = 'block';
}

$(document).ready(function() {
  //DASHBOARD
  // Date range filter datepicker
  $('.input-daterange input').each(function() {
    $(this).datepicker({
       uiLibrary: 'bootstrap4'
     });
   });

  // Initializing datatable
  var table = $('#tableCustomer').DataTable( {
    dom:  "<'row'<'col-sm-12 col-md-1'B><'col-sm-12 col-md-4'l><'col-sm-12 col-md-5'f>>" +
          "<'row'<'col-sm-12'tr>>" +
          "<'row'<'col-sm-12 col-md-5'i><'col-sm-12 col-md-7'p>>",
    buttons: ['excel'],
    'columns': [
      { data: 'cit' }, // index - 0
      { data: 'date_registered' }, // index - 1
      { data: 'firatName' }, // index - 2
      { data: 'lastName' }, // index - 3
      { data: 'date_birth' }, // index - 4
      { data: 'address_city' }, // index - 5
    ],
    'columnDefs': [ {
      'targets': [6], 
      'orderable': false, // set orderable false for vud
    }]
  } );
  
  // Extend dataTables search
  $.fn.dataTable.ext.search.push(
    function(settings, data, dataIndex) {
      var min = $('#min-date').val();
      var max = $('#max-date').val();
      var createdAt = data[1] || 0; // The column containing the date to be filtered
      if ((min == "" || max == "") || (moment(createdAt).isSameOrAfter(min) && moment(createdAt).isSameOrBefore(max))) {
        return true;
      }
      return false;
    }
  );

  // Re-draw the table when the a date range filter changes
  $('.date-range-filter').change(function() {
    table.draw();
  });

} );
