const redHeader = document.querySelector('#red_header')
function color_change() {
  document.querySelector('header').classList.add('red');
}
redHeader.addEventListener("click", color_change);
