// Get the modal
//var modal = document.getElementById('myModal');
var modal = document.getElementsByClassName('modal');

// Get the button that opens the modal
var ObjBtn = document.getElementsByClassName("myBtnObj");


var plaBtn = document.getElementsByClassName("myBtnPla");


// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close");

// When the user clicks on the button, open the modal
function getId(objBtn_id) { //Retrieves the ID of the picture, and compares it to the ID of the modals, if a match is found, the modal is displayed
    for (var i = 0; i < modal.length; i += 1) {
        if (modal[i].id === objBtn_id) {
            modal[i].style.display = "block";
        }
    }
}


// When the user clicks on <span> (x), close the modal
for (var i = 0; i < span.length; i += 1) {
    span[i].onclick = function() {
        for (var j = 0; j < modal.length; j += 1) {    
            modal[j].style.display = "none";
        }
    }
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    for (var i = 0; i < modal.length; i += 1) {
        if (event.target === modal[i]) {
            modal[i].style.display = "none";
        }
    }
    
}





