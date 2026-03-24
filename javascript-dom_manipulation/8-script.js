async function hello() {
  let x = await fetch('https://hellosalut.stefanbohacek.com/?lang=fr');
  let y = await x.json();
  document.getElementById('hello').innerText = y['hello']
}
hello();
