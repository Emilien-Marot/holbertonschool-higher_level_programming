async function starWarsName() {
  let x = await fetch('https://swapi-api.hbtn.io/api/films/?format=json');
  let y = await x.json();
  listMovie = y['results'];
  let html = '';
  listMovie.forEach(element => {
    html += '<li>' + element['title'] + '</li>';
  });
  document.querySelector('ul#list_movies').innerHTML = html;
}
starWarsName();
