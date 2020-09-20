// Functions:

//DASHBOARD
// Add Cast:
// Create a "close" button and append it to each list item (cast)
var myNodelist = document.getElementsByTagName("LI");
var i;
for (i = 0; i < myNodelist.length; i++) {
  var span = document.createElement("SPAN");
  var txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  myNodelist[i].appendChild(span);
}
// Click on a close button to hide the current list item (cast)
var close = document.getElementsByClassName("close");
var i;
for (i = 0; i < close.length; i++) {
  close[i].onclick = function() {
    var div = this.parentElement;
    div.style.display = "none";
  }
}
// Create a new list item (cast) when clicking on the "Add" button
function newElement() {
  var li = document.createElement("li");
  var inputValue = document.getElementById("castInput").value;
  var t = document.createTextNode(inputValue);
  li.appendChild(t);
  if (inputValue === '') {
    alert("You must write something!");
  } else {
    document.getElementById("myUL").appendChild(li);
  }
  document.getElementById("castInput").value = "";
  var span = document.createElement("SPAN");
  var txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  li.appendChild(span);
  for (i = 0; i < close.length; i++) {
    close[i].onclick = function() {
      var div = this.parentElement;
      div.style.display = "none";
    }
  }
}

// Image Previews:
// Image preview customer modal
var loadImgPreviewCustModal = function(event) {
  var readerImgPreviewCustModal = new FileReader();
  readerImgPreviewCustModal.onload = function(){
    var imgPreviewCustModal = document.getElementById('imgPreviewCustModal');
    imgPreviewCustModal.src = readerImgPreviewCustModal.result;
  };
  readerImgPreviewCustModal.readAsDataURL(event.target.files[0]);
};

// Image preview dvd modal
// img1
var loadImgPreviewDvdModal1 = function(event) {
  var readerImgPreviewDvdModal1 = new FileReader();
  readerImgPreviewDvdModal1.onload = function(){
    var imgPreviewDvdModal1 = document.getElementById('imgPreviewDvdModal1');
    imgPreviewDvdModal1.src = readerImgPreviewDvdModal1.result;
  };
  readerImgPreviewDvdModal1.readAsDataURL(event.target.files[0]);
};
// img2
var loadImgPreviewDvdModal2 = function(event) {
  var readerImgPreviewDvdModal2 = new FileReader();
  readerImgPreviewDvdModal2.onload = function(){
    var imgPreviewDvdModal2 = document.getElementById('imgPreviewDvdModal2');
    imgPreviewDvdModal2.src = readerImgPreviewDvdModal2.result;
  };
  readerImgPreviewDvdModal2.readAsDataURL(event.target.files[0]);
};
//img3
var loadImgPreviewDvdModal3 = function(event) {
  var readerImgPreviewDvdModal3 = new FileReader();
  readerImgPreviewDvdModal3.onload = function(){
    var imgPreviewDvdModal3 = document.getElementById('imgPreviewDvdModal3');
    imgPreviewDvdModal3.src = readerImgPreviewDvdModal3.result;
  };
  readerImgPreviewDvdModal3.readAsDataURL(event.target.files[0]);
};






//DVD REGISTRATION
//Image previews:
// Image preview dvd modal
// img1
var loadImgPreviewDvdReg1 = function(event) {
  var readerImgPreviewDvdReg1 = new FileReader();
  readerImgPreviewDvdReg1.onload = function(){
    var imgPreviewDvdReg1 = document.getElementById('imgPreviewDvdReg1');
    imgPreviewDvdReg1.src = readerImgPreviewDvdReg1.result;
  };
  readerImgPreviewDvdReg1.readAsDataURL(event.target.files[0]);
};
// img2
var loadImgPreviewDvdReg2 = function(event) {
  var readerImgPreviewDvdReg2 = new FileReader();
  readerImgPreviewDvdReg2.onload = function(){
    var imgPreviewDvdReg2 = document.getElementById('imgPreviewDvdReg2');
    imgPreviewDvdReg2.src = readerImgPreviewDvdReg2.result;
  };
  readerImgPreviewDvdReg2.readAsDataURL(event.target.files[0]);
};
// img3
var loadImgPreviewDvdReg3 = function(event) {
  var readerImgPreviewDvdReg3 = new FileReader();
  readerImgPreviewDvdReg3.onload = function(){
    var imgPreviewDvdReg3 = document.getElementById('imgPreviewDvdReg3');
    imgPreviewDvdReg3.src = readerImgPreviewDvdReg3.result;
  };
  readerImgPreviewDvdReg3.readAsDataURL(event.target.files[0]);
};






//CUSTOMER REGISTRATION
// Image Preview:
// Image preview customer registration
var loadImgPreviewCustReg = function(event) {
  var readerImgPreviewCustReg = new FileReader();
  readerImgPreviewCustReg.onload = function(){
    var imgPreviewCustReg = document.getElementById('imgPreviewCustReg');
    imgPreviewCustReg.src = readerImgPreviewCustReg.result;
  };
  readerImgPreviewCustReg.readAsDataURL(event.target.files[0]);
};






$(document).ready(function() {
  //DASHBOARD
  // Date range filter datepicker
  $('.input-daterange input').each(function() {
    $(this).datepicker({
       uiLibrary: 'bootstrap4'
     });
   });

  // Initializing datatable
  var table = $('#dvdReportSummary').DataTable( {
    dom:  "<'row'<'col-sm-12 col-md-1'B><'col-sm-12 col-md-5'l><'col-sm-12 col-md-6'f>>" +
          "<'row'<'col-sm-12'tr>>" +
          "<'row'<'col-sm-12 col-md-5'i><'col-sm-12 col-md-7'p>>",
    buttons: ['excel'],
    'columns': [
      { data: 'sku' }, // index - 0
      { data: 'date_registered' }, // index - 1
      { data: 'genre' }, // index - 2
      { data: 'title' }, // index - 3
      { data: 'release_date' }, // index - 4
      { data: 'price' }, // index - 5
      { data: 'num_of_items' }, // index - 6
      { data: 'vud' } // index - 7
    ],
    'columnDefs': [ {
      'targets': [7], 
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

  // Birthday datepicker customer modal
  $('#datepickerBdayCustModal').datepicker({
    uiLibrary: 'bootstrap4'
  });

  // Release date datepicker
  $('#datepickerRelDateDvdModal').datepicker({
    uiLibrary: 'bootstrap4'
  });

  //DVD REGISTRATION
  //Release date datepicker dvd registration
  $('#datepickerRelDateDvdReg').datepicker({
    uiLibrary: 'bootstrap4'
  });

  //CUSTOMER REGISTRATION
  //Birthday datepicker customer registration
  $('#datepickerBdayCustReg').datepicker({
    uiLibrary: 'bootstrap4',
    format: "yyyy-mm-dd  "
  });
} );

