//index.html
function sendName() {
  var name = document.getElementById("myName").value;
  document.getElementById("greet").innerHTML = "Welcome, " + name + ".";
}

var counter = 0;

function like() {
  counter++;
  document.getElementById("likeCount").innerHTML = "like count:" + counter;

}

function disLike() {
  counter--;
  document.getElementById("likeCount").innerHTML = "like count:" + counter;
}

function squareLike() {
  counter *= counter;
  document.getElementById("likeCount").innerHTML = "like count:" + counter;
}

function sqrtLike() {
  counter = Math.sqrt(counter);
  document.getElementById("likeCount").innerHTML = "like count:" + counter;
}
//End




//super-villains.html

function characterFill() {
  var username = document.getElementById("villainsUsername").value;
  var character = document.getElementById("villainsCharacter").value;
  if (username.length > 0 & character.length > 0) {
    document.getElementById("username").innerHTML = "Username: " + username;
    document.getElementById("character").innerHTML = "Character: " + character;
    document.getElementById("villainsFillSuccess").innerHTML = "<span style= 'color: green;'><strong>Success!</strong></span>";

  } else if (username.length > 0) {
    document.getElementById("villainsFillSuccess").innerHTML = "<span style= 'color: red;'><em>Please provide a character</em></span>";
  } else if (character.length > 0) {
    document.getElementById("villainsFillSuccess").innerHTML = "<span style= 'color: red;'><em>Please provide a username</em></span>";

  } else {
    document.getElementById("villainsFillSuccess").innerHTML = "<span style= 'color: red;'><strong>Failed!</strong></span>";

  }

}
//End







//Math expirements
