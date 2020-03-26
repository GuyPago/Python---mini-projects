function solveQuadEquation() {
var a = document.getElementById("aInput").value;
var b = document.getElementById("bInput").value;
var c = document.getElementById("cInput").value;

var x1 = (-b + Math.sqrt(Math.pow(b,2) - 4*a*c))/(2*a);
var x2 = (-b - Math.sqrt(Math.pow(b,2) - 4*a*c))/(2*a);

if (x1 === x2) {
  document.getElementById("quadricOutput").innerHTML = "x = " + x1;

}else {
  document.getElementById("quadricOutput").innerHTML = "x1 = " + x1 + "<br> x2 = " + x2;

}

}
