var c = document.getElementById('playground');
var dotButton = document.getElementById('buttonCircle');
var stopButton = document.getElementById('buttonStop');

var ctx = c.getContext("2d");

ctx.fillStyle = "#ff0000";

var requestID;

var clear = (e) => {
    ctx.clearRect(0, 0, c.width, c.height);
}

var radius = 0;
var growing = true;
var numProcesses = 0;

var drawDot = () => {
    numProcesses++;
    // if (numProcesses == 1) {
    clear();
    ctx.beginPath();
    ctx.arc(c.width / 2, c.height / 2, radius, 0, 2 * Math.PI);
    ctx.fillStyle = "red";
    ctx.fill();
    if (growing) {
        radius += 1;
    }
    else {
        radius -= 1;
    }
    if (radius == c.width / 2) {
        growing = false;
    }
    else if (radius == 0) {
        growing = true;
    }
    requestID = window.requestAnimationFrame(drawDot);
    if (radius%10 == 0) {console.log(radius);}
    // } else {
    //     numProcesses--;
    // }
}

var stopIt = () => {
    window.cancelAnimationFrame(requestID);
}

if (numProcesses == 0) {
    dotButton.addEventListener("click", drawDot);
    numProcesses++;
} else {
    stopButton.addEventListener("click", stopIt);
    numProcesses--;
}