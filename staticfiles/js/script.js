document.addEventListener('DOMContentLoaded', function() {
    fetchMovies();
    fetchNews();
});

// fetches the movies and dynamically creates the slides.
function fetchMovies() {
    fetch('/api/movies/')
        .then(response => response.json())
        .then(data => {
            const slidesContainer = document.getElementById('slides-container');
            data.movies.forEach(movie => {
                const slide = document.createElement('div');
                slide.className = 'slide';
                slide.innerHTML = `
                    <a href="/movie/${movie.id}/">
                        <img src="https://image.tmdb.org/t/p/w500${movie.poster_path}" alt="${movie.title}">
                    </a>
                `;
                slidesContainer.appendChild(slide);
            });
        });
}

function fetchNews() {
    fetch('/api/news/')
        .then(response => response.json())
        .then(data => {
            const newsItems = data.news.slice(0, 12); // Limit to 12 articles
            const itemsPerPage = 4;
            const totalPages = Math.ceil(newsItems.length / itemsPerPage);
            let currentPage = 1;

            function renderNews(page) {
                const start = (page - 1) * itemsPerPage;
                const end = start + itemsPerPage;
                const newsToRender = newsItems.slice(start, end);

            const newsContainer = document.getElementById('news-container');
                newsContainer.innerHTML = '';

                newsToRender.forEach(article => {
                    const newsItem = document.createElement('div');
                    newsItem.className = 'col-md-4 mb-4';
                    newsItem.innerHTML = `
                        <div class="card">
                            <img src="${article.urlToImage}" class="card-img-top" alt="${article.title}">
                            <div class="card-body">
                                <h5 class="card-title">${article.title}</h5>
                                <p class="card-text">${article.description}</p>
                                <a href="${article.url}" class="btn btn-primary" target="_blank">Read more</a>
                            </div>
                        </div>
                    `;
                    newsContainer.appendChild(newsItem);
                });
                renderPagination();
            }

            function renderPagination() {
                const paginationContainer = document.getElementById('pagination-container');
                paginationContainer.innerHTML = '';

                for (let i = 1; i <= totalPages; i++) {
                    const pageButton = document.createElement('button');
                    pageButton.innerText = i;
                    pageButton.className = 'btn btn-secondary mx-1';
                    pageButton.onclick = () => {
                        currentPage = i;
                        renderNews(currentPage);
                    };
                    paginationContainer.appendChild(pageButton);
                }
            }

            renderNews(currentPage);
        });
}

let currentSlide = 0;

// changes the currentSlide index and updates the transform property 
// of the .slides div to show the correct slide
function moveSlide(direction) {
    const slides = document.querySelector('.slides');
    const totalSlides = document.querySelectorAll('.slide').length;
    const slidesPerView = 5;
    const maxSlideIndex = totalSlides - slidesPerView;

    currentSlide = Math.min(Math.max(currentSlide + direction, 0), maxSlideIndex);
    slides.style.transform = `translateX(-${(currentSlide / totalSlides) * 100}%)`;
}