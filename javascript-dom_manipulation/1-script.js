const redHeader = document.querySelector('#red_header')
function color_change() {
  const header = document.querySelector('header');
  header.style.color = '#FF0000';
}
redHeader.addEventListener("click", color_change);
