import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
						"A story of a boy and his toys that come to life.",
						"http://ecx.images-amazon.com/images/I/51NpxQ0ma8L.jpg",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print toy_story.storyline

avatar = media.Movie("Avatar",
					 "A marine on an alien planet",
					 "http://seat42f.com/images/stories/Movies/DVDArt/Avatar_DVD.jpg",
					 "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
#print avatar.storyline
#avatar.show_trailer()

pulp_fiction = media.Movie("Pulp Fiction",
						   "Jules Winnfield and Vincent Vega are two hitmen who are out to retrieve a suitcase stolen from their employer, mob boss Marsellus Wallace. Wallace has also asked Vincent to take his wife Mia out a few days later when Wallace himself will be out of town. Butch Coolidge is an aging boxer who is paid by Wallace to lose his next fight. The lives of these seemingly unrelated people are woven together comprising of a series of funny, bizarre and uncalled-for incidents.",
						   "http://www.starwarped.faketrix.com/files/other-roles/Samuel-L-Jackson/Pulp-Fiction-dvd-cover.jpg",
						   "https://www.youtube.com/watch?v=wZBfmBvvotE")

#pulp_fiction.show_trailer()

inception = media.Movie("Inception",
						"A thief who steals corporate secrets through use of dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.",
						"http://vignette3.wikia.nocookie.net/movieweapon/images/f/f1/Inception-Cover.jpg/revision/latest?cb=20110522002808",
						"https://www.youtube.com/watch?v=66TuSJo4dZM")

movies = [toy_story, avatar, pulp_fiction, inception]

#print media.Movie.__name__
#print media.Movie.__module__