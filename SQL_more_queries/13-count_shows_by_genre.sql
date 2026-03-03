-- comment
SELECT tv_genres.name, COUNT(*) AS number_of_shows FROM tv_show_genres RIGHT JOIN tv_genres ON tv_genres.id=tv_show_genres.genre_id GROUP BY tv_genres.id ORDER BY number_of_shows DESC;
