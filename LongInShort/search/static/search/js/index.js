
var i = 0;
var txt = "Don't have time to watch long video?\n  Don't worry, get short and efficient summary of your video here !";
var speed = 50;
function typeWriter() {
    if (i < txt.length) {
      document.querySelector(".front-text h1").innerHTML += txt.charAt(i);
      i++;
      setTimeout(typeWriter, speed);
    }
}

typeWriter();