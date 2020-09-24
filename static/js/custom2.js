// Functions:

//DASHBOARD
// Add Cast (modal):
// Create a new list item (cast) when clicking on the "Add" button
function newElementModal(castInputID,castListID,myULID) {
  var li = document.createElement("li");
  var inputValue = document.getElementById(castInputID).value;
  var t = document.createTextNode(inputValue);

  li.style.listStyleType = "none";
  li.style.border = "2px solid #919fb3";
  li.style.background = "transparent";
  li.style.color = "#919fb3";
  li.style.height = "37px";
  li.style.paddingLeft = "5px";
  li.style.paddingTop = "3px";
  li.style.marginBottom = "5px";

  // Add cast input to list
  var castArrList = document.getElementById(castListID).value.split(",");
  if(castArrList[0] == ''){
    castArrList[0] = inputValue;
  }
  else{
    castArrList.push(inputValue);
  }
  document.getElementById(castListID).value = castArrList;
  document.getElementById(castListID).innerHTML = castArrList;

  li.appendChild(t);
  li.setAttribute("value",inputValue);
  if (inputValue === '') {
    alert("You must write something!");
  } else {
    document.getElementById(myULID).appendChild(li);
  }
  document.getElementById(castInputID).value = "";

  // Create a "close" button and append it to each list item (cast)
  var span = document.createElement("SPAN");
  var txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  li.appendChild(span);

  span.onclick = function() {
    var div = this.parentElement;

    // Click on a close button to hide the current list item (cast)
    div.style.display = "none";

    // Delete cast from list
    var castArrList = document.getElementById(castListID).value.split(",");
    for(i = 0; i < castArrList.length; i++){ 
      if ( castArrList[i] == this.parentElement.getAttribute("value")) { 
        castArrList.splice(i, 1); 
        i--; 
      }
    }
    document.getElementById(castListID).value = castArrList;
    document.getElementById(castListID).innerHTML = castArrList;
  }
}


function updateCastListModal(castListID,myULID) {
  // Add cast input to list
  var castArrList = document.getElementById(castListID).value.split(",");
  for(i = 0; i < castArrList.length; i++){
    var li = document.createElement("li");
    var inputValue = castArrList[i];
    var t = document.createTextNode(inputValue);

    li.style.listStyleType = "none";
    li.style.border = "2px solid #919fb3";
    li.style.background = "transparent";
    li.style.color = "#919fb3";
    li.style.height = "37px";
    li.style.paddingLeft = "5px";
    li.style.paddingTop = "3px";
    li.style.marginBottom = "5px";

    li.appendChild(t);
    li.setAttribute("value",inputValue);
    document.getElementById(myULID).appendChild(li);

    // Create a "close" button and append it to each list item (cast)
    var span = document.createElement("SPAN");
    var txt = document.createTextNode("\u00D7");
    span.className = "close";
    span.appendChild(txt);
    li.appendChild(span);

    span.onclick = function() {
      var div = this.parentElement;

      // Click on a close button to hide the current list item (cast)
      div.style.display = "none";

      // Delete cast from list
      var castArrList = document.getElementById(castListID).value.split(",");
      for(i = 0; i < castArrList.length; i++){ 
        if ( castArrList[i] == this.parentElement.getAttribute("value")) { 
          castArrList.splice(i, 1); 
          i--; 
        }
      }
      document.getElementById(castListID).value = castArrList;
      document.getElementById(castListID).innerHTML = castArrList;
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
var loadImgPreviewDvdModal1 = function(event,id) {
  var readerImgPreviewDvdModal1 = new FileReader();
  readerImgPreviewDvdModal1.onload = function(){
    var imgPreviewDvdModal1 = document.getElementById(id);
    imgPreviewDvdModal1.src = readerImgPreviewDvdModal1.result;
  };
  readerImgPreviewDvdModal1.readAsDataURL(event.target.files[0]);
};
// img2
var loadImgPreviewDvdModal2 = function(event,id) {
  var readerImgPreviewDvdModal2 = new FileReader();
  readerImgPreviewDvdModal2.onload = function(){
    var imgPreviewDvdModal2 = document.getElementById(id);
    imgPreviewDvdModal2.src = readerImgPreviewDvdModal2.result;
  };
  readerImgPreviewDvdModal2.readAsDataURL(event.target.files[0]);
};
//img3
var loadImgPreviewDvdModal3 = function(event,id) {
  var readerImgPreviewDvdModal3 = new FileReader();
  readerImgPreviewDvdModal3.onload = function(){
    var imgPreviewDvdModal3 = document.getElementById(id);
    imgPreviewDvdModal3.src = readerImgPreviewDvdModal3.result;
  };
  readerImgPreviewDvdModal3.readAsDataURL(event.target.files[0]);
};






//DVD REGISTRATION
// Add Cast:
// Create a new list item (cast) when clicking on the "Add" button
function newElement() {
  var li = document.createElement("li");
  var inputValue = document.getElementById("castInput").value;
  var t = document.createTextNode(inputValue);

  // Add cast input to list
  var castArrList = document.getElementById("castList").value.split(",");
  if(castArrList[0] == ''){
    castArrList[0] = inputValue;
  }
  else{
    castArrList.push(inputValue);
  }
  document.getElementById("castList").value = castArrList;
  document.getElementById("castList").innerHTML = castArrList;

  li.appendChild(t);
  li.setAttribute("value",inputValue);
  if (inputValue === '') {
    alert("You must write something!");
  } else {
    document.getElementById("myUL").appendChild(li);
  }
  document.getElementById("castInput").value = "";

  // Create a "close" button and append it to each list item (cast)
  var close = document.getElementsByClassName("close");
  var span = document.createElement("SPAN");
  var txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  li.appendChild(span);
  for (i = 0; i < close.length; i++) {
    close[i].onclick = function() {
      var div = this.parentElement;

      // Click on a close button to hide the current list item (cast)
      div.style.display = "none";

      // Delete cast from list
      var castArrList = document.getElementById("castList").value.split(",");
      for(i = 0; i < castArrList.length; i++){ 
        if ( castArrList[i] == this.parentElement.getAttribute("value")) { 
          castArrList.splice(i, 1); 
          i--; 
        }
      }
      document.getElementById("castList").value = castArrList;
      document.getElementById("castList").innerHTML = castArrList;
    }
  }
}


// Image Previews:
// Image preview dvd registration
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
  var tableDVD = $('#dvdReportSummary').DataTable( {
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
    }],

    initComplete: function(){
      // Extend dataTables search
      $.fn.dataTable.ext.search.push(
        function(settings, data, dataIndex) {
          var min = $('#min-date-dvd').val();
          var max = $('#max-date-dvd').val();
          var createdAt = data[1] || 0; // The column containing the date to be filtered
          if ((min == "" || max == "") || (moment(createdAt).isSameOrAfter(min) && moment(createdAt).isSameOrBefore(max))) {
            return true;
          }
          return false;
        }
      );
      // Re-draw the table when the a date range filter changes
      $('.date-range-filter').change(function() {
        tableDVD.draw();
      });
    }
    
  } );

  // Birthday datepicker customer modal
  $('#datepickerBdayCustModal').datepicker({
    uiLibrary: 'bootstrap4',
    format: 'yyyy-mm-dd'
  });

  // Release date datepicker dvd modal
  $('#datepickerRelDateDvdModal').datepicker({
    uiLibrary: 'bootstrap4',
    format: 'yyyy-mm-dd'
  });

  



  //DVD REGISTRATION
  //Release date datepicker dvd registration
  $('#datepickerRelDateDvdReg').datepicker({
    uiLibrary: 'bootstrap4',
    format: 'yyyy-mm-dd'
  });





  //CUSTOMER REGISTRATION
  //Birthday datepicker customer registration
  $('#datepickerBdayCustReg').datepicker({
    uiLibrary: 'bootstrap4',
    format: 'yyyy-mm-dd'
  });
} );

