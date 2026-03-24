async function starWarsName() {
  let x = await fetch('https://swapi-api.hbtn.io/api/people/5/?format=json');
  let y = await x.json();
  document.getElementById('character').innerText = y['name'];
}
starWarsName();
