function toggle_class() {
  document.querySelector('header').classList.toggle('red');
  document.querySelector('header').classList.toggle('green');
}
document.querySelector('#toggle_header').addEventListener("click", toggle_class);
