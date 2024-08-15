let count = 0;
let name;

function sayHello() {
  const alertNameInput = document.getElementById("alert-name");
  userName = alertNameInput.value;
  count++;
  if (userName == "") {
    alert("Hello, world! - Clicks: " + count);
  } else {
    alert(`Hello ${userName}`);
  }

  const clickCount = document.getElementById("h1-click-count");
  clickCount.innerText = `Clicks: ${count}`;
}

document.addEventListener("DOMContentLoaded", () => {
  document.querySelector("button").onclick = sayHello;
});
