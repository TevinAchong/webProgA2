// Get the modal
//var modal = document.getElementById('myModal');
var modal = document.getElementsByClassName('modal');
console.log(modal.length);

// Get the button that opens the modal
var ObjBtn = document.getElementsByClassName("myBtnObj");
console.log(ObjBtn.length);

var plaBtn = document.getElementsByClassName("myBtnPla");
console.log(plaBtn.length);

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close");
console.log(span.length);

// When the user clicks on the button, open the modal
for (var i = 0; i < ObjBtn.length; i += 1) {
    ObjBtn[i].onclick = function() {
        console.log(i);
    }
}

modal[29].style.display = "block";

for (var i = 0; i < plaBtn.length; i += 1) {
    plaBtn[i].onclick = function() {
        console.log(plaBtn[i]);
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