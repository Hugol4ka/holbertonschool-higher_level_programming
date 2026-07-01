const titleMovies = document.querySelector("#list_movies");

fetch("https://swapi-api.hbtn.io/api/films/?format=json")
    .then(response => response.json())
    .then(data => {
        const movies = data.results;
        for (const movie of movies) {
            const li = document.createElement("li");
            li.textContent = movie.title;
            titleMovies.appendChild(li);
        }
    });
