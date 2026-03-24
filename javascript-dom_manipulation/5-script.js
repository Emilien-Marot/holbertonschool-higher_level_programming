function update_header() {
  const header = document.querySelector('header');
  header.innerText = "New Header!!!";
}
document.querySelector('#update_header').addEventListener("click", update_header);
