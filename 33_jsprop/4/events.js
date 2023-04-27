// demo 4
// JS event propagation

// Name the collections of TDs, TRs, and overall table
var tds = document.getElementsByTagName('td');
var trs = document.getElementsByTagName('tr');
var table = document.getElementsByTagName('table')[0];


var clicky = function(e) {
  alert( this.innerHTML );
  //Q: What will happen when next line is uncommented?
  // e.stopPropagation();
  // Whereas before it showed three pop-ups from the three nested event listeners, now it only shows one pop-up from the event listener that was clicked on.  
};


//Q: Does the order in which the event listeners are attached matter?
// It does not seem to change anything. 

//Predict, then test...
//Q: What effect does the boolean arg have in each?
//   (Leave exactly 1 version uncommented to test...)
//  true prioritizes the alert in a queue-y esque way(table, tr, td is the order when all eventlistners are true), false deprioritizes the alert(puts it where it would naturally be among non-prioritized alerts)

for (var x=0; x < tds.length; x++) {
  tds[x].addEventListener('click', clicky, true);
  //tds[x].addEventListener('click', clicky, false);
}

for (x=0; x < trs.length; x++) {
  trs[x].addEventListener('click', clicky, true);
  //trs[x].addEventListener('click', clicky, false);
}

table.addEventListener('click', clicky, true);
//table.addEventListener('click', clicky, false);
