// Quadradic equation solver
function solveQuadEquation() {
  var a = document.getElementById("aInput").value;
  var b = document.getElementById("bInput").value;
  var c = document.getElementById("cInput").value;

  var x1 = (-b + Math.sqrt(Math.pow(b, 2) - 4 * a * c)) / (2 * a);
  var x2 = (-b - Math.sqrt(Math.pow(b, 2) - 4 * a * c)) / (2 * a);

  if (x1 === x2) {
    document.getElementById("quadricOutput").innerHTML = "x = " + x1;

  } else {
    document.getElementById("quadricOutput").innerHTML = "x1 = " + x1 + "<br> x2 = " + x2;

  }
}
//end


// Math series
function solveArithmeticProgression() {
  var a1 = parseFloat(document.getElementById("a1Input").value);
  var d = parseFloat(document.getElementById("dInput").value);
  var n = parseFloat(document.getElementById("nInput").value);

  var an = (a1 + (n-1)*d);

  document.getElementById("arithmeticOutput").innerHTML = "a"+n +" = " + an ;
}

  function solveGeometricprogression() {
    var a1 = parseFloat(document.getElementById("a1gInput").value);
    var q = parseFloat(document.getElementById("qInput").value);
    var n = parseFloat(document.getElementById("ngInput").value);

    var an = a1* Math.pow(q,(n-1));

    document.getElementById("geometricOutput").innerHTML = "a"+n +" = " + an ;
  }


//end
