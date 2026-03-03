-- comment
SELECT tv_genres.name AS name, COUNT(*) AS number_of_shows FROM tv_show_genres INNER JOIN tv_genres ON tv_genres.id=tv_show_genres.genre_id GROUP BY tv_genres.id ORDER BY number_of_shows DESC;
