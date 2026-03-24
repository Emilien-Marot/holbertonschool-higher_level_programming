function add_item() {
  const ul = document.querySelector('ul.my_list');
  ul.innerHTML += "<li>Item</li>";
}
document.querySelector('#add_item').addEventListener("click", add_item);
