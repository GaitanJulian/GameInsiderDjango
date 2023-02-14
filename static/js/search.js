const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
const search = urlParams.get('search');


document.getElementById("search").setAttribute('value', search);