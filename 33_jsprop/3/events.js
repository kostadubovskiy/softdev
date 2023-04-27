// demo 3
// JS event propagation

var tds = document.getElementsByTagName('td');
var trs = document.getElementsByTagName('tr');
var table = document.getElementsByTagName('table')[0];

var clicky = function(e) {
  alert( this.innerHTML );
  //Q: What will happen when next line is uncommented?
  // e.stopPropagation();
  // Whereas before it showed three pop-ups from the three nested event listeners, now it only shows one pop-up from the event listener that was clicked on.  
};

for (var x=0; x < tds.length; x++) {
  tds[x].addEventListener('click', clicky);
}

for (x=0; x < trs.length; x++) {
  trs[x].addEventListener('click', clicky);
}

//Predict, then test...
//Q: What effect does the boolean arg have?
//   (Leave exactly 1 version uncommented to test...)
// The true parameter seems to indicate alert priority, so upon clicking the table the alert with the table pops up first. The false parameter seems to deprioritize, so upon clicking the table the alert with the table pops up in it's usual order.

table.addEventListener('click', clicky, true);
// table.addEventListener('click', clicky, false);

// Q: When user clicks on a cell, in what order will the pop-ups appear?
// A: table, tr, td when the table.addEventListener is true. td, tr, table when the table.addEventListener is false
