import media
import fresh_tomatoes

"""Displays a page of movies, their trailers, and other related information
such as synopsis and star rating."""

# Creating instances of actors to pass into the movie constructors
benedict_c = media.Actor(
    "Benedict Cumberbatch",
    "Alan Turing",
    "http://ia.media-imdb.com/images/M/MV5BMTQzMDEwNjUzNV5BMl5BanBnXkFtZTgwOTg2MzU0MzE@._V1_UX32_CR0,0,32,44_AL_.jpg")  # noqa
keira_k = media.Actor(
    "Keira Knightley",
    "Joan Clarke",
    "http://ia.media-imdb.com/images/M/MV5BMTYwNDM0NDA3M15BMl5BanBnXkFtZTcwNTkzMjQ3OA@@._V1_UX32_CR0,0,32,44_AL_.jpg")  # noqa
matthew_g = media.Actor(
    "Matthew Goode",
    "Huge Alexander",
    "http://ia.media-imdb.com/images/M/MV5BMTc0MzY2NjE0Nl5BMl5BanBnXkFtZTYwMDkxMDY0._V1_UX32_CR0,0,32,44_AL_.jpg")  # noqa
mao_i = media.Actor(
    "Mao Inoue",
    "Miki Shirono",
    "http://asianwiki.com/images/c/c0/Mao_Inoue-p4.jpg")
go_a = media.Actor(
    "Go Ayano",
    "Yuki Akahoshi",
    "http://asianwiki.com/images/d/d2/Gou_Ayano-p1.jpg")
nanao = media.Actor(
    "Nanao",
    "Noriko Miki",
    "http://asianwiki.com/images/5/5e/Nanao-p1.jpg")
idris_e = media.Actor(
    "Idris Elba",
    "Stacker Pentecost",
    "http://ia.media-imdb.com/images/M/MV5BNzEzMTI2NjEyNF5BMl5BanBnXkFtZTcwNTA0OTE4OA@@._V1_UX32_CR0,0,32,44_AL_.jpg")  # noqa
charlie_h = media.Actor(
    "Charlie Hunnam",
    "Raleigh Becket",
    "http://ia.media-imdb.com/images/M/MV5BMjE5NjE5Mzk2MV5BMl5BanBnXkFtZTcwODI5MDE1Ng@@._V1_UX32_CR0,0,32,44_AL_.jpg")  # noqa
rinko_k = media.Actor(
    "Rinko Kikuchi",
    "Mako Mori",
    "http://ia.media-imdb.com/images/M/MV5BMTI5NjE0MjcwN15BMl5BanBnXkFtZTYwMDcxNTA1._V1_UX32_CR0,0,32,44_AL_.jpg")  # noqa
john_r = media.Actor(
    "John C. Reilly",
    "Ralph",
    "http://ia.media-imdb.com/images/M/MV5BMTc4MDEzMDkzOF5BMl5BanBnXkFtZTYwNzQzNzcy._V1_UY44_CR3,0,32,44_AL_.jpg")  # noqa
jack_m = media.Actor(
    "Jack McBrayer",
    "Felix",
    "http://ia.media-imdb.com/images/M/MV5BMTIwNTA5OTIwN15BMl5BanBnXkFtZTYwMTA0NTc0._V1_UY44_CR1,0,32,44_AL_.jpg")  # noqa
jane_l = media.Actor(
    "Jane Lynch",
    "Calhoun",
    "http://ia.media-imdb.com/images/M/MV5BMTk4MDcwOTA1M15BMl5BanBnXkFtZTcwNTQ2Njg0Mw@@._V1_UX32_CR0,0,32,44_AL_.jpg")  # noqa
matt_d = media.Actor(
    "Matt Damon",
    "Mark Watney",
    "http://ia.media-imdb.com/images/M/MV5BMTM0NzYzNDgxMl5BMl5BanBnXkFtZTcwMDg2MTMyMw@@._V1_UY44_CR0,0,32,44_AL_.jpg")  # noqa
jessica_c = media.Actor(
    "Jessica Chastain",
    "Melissa Lewis",
    "http://ia.media-imdb.com/images/M/MV5BMTU1MDM5NjczOF5BMl5BanBnXkFtZTcwOTY2MDE4OA@@._V1_UX32_CR0,0,32,44_AL_.jpg")  # noqa
kristen_w = media.Actor(
    "Kristen Wiig",
    "Annie Montrose",
    "http://ia.media-imdb.com/images/M/MV5BMjM2MDIxOTA4N15BMl5BanBnXkFtZTcwODA2NzE3OQ@@._V1_UX32_CR0,0,32,44_AL_.jpg")  # noqa
melissa_m = media.Actor(
    "Melissa McCarthy",
    "Susan Cooper",
    "http://ia.media-imdb.com/images/M/MV5BMTg5NjA3ODkyMl5BMl5BanBnXkFtZTgwNTU4Mzg5NjE@._V1_UY44_CR1,0,32,44_AL_.jpg")  # noqa
rose_b = media.Actor(
    "Rose Byrne",
    "Rayna Boyanov",
    "http://ia.media-imdb.com/images/M/MV5BMTY4OTMxMDkwNV5BMl5BanBnXkFtZTcwOTQxOTg3NQ@@._V1_UY44_CR0,0,32,44_AL_.jpg")  # noqa
jude_l = media.Actor(
    "Jude Law",
    "Bradley Fine",
    "http://ia.media-imdb.com/images/M/MV5BMTMwOTg5NTQ3NV5BMl5BanBnXkFtZTcwNzM3MDAzNQ@@._V1_UX32_CR0,0,32,44_AL_.jpg")  # noqa
nozomu_s = media.Actor(
    "Nozomu Sasaki",
    "Tetsuo",
    "http://cdn.mydramalist.info/images/people/4684.jpg")
mitsuo_i = media.Actor(
    "Mitsuo Iwata",
    "Kaneda",
    "http://cdn.mydramalist.info/images/people/4714.jpg")
mami_k = media.Actor(
    "Mami Koyama",
    "Kei",
    "http://cdn.mydramalist.info/images/people/10901.jpg")
ivana_b = media.Actor(
    "Ivana Baquero",
    "Ofelia",
    "http://ia.media-imdb.com/images/M/MV5BMTEwNzI0OTMyNDheQTJeQWpwZ15BbWU4MDAyNjUwMDQx._V1_UY44_CR0,0,32,44_AL_.jpg")  # noqa
ariadna_g = media.Actor(
    "Ariadna Gil",
    "Carmen",
    "http://ia.media-imdb.com/images/M/MV5BMTYxODMxNjU4N15BMl5BanBnXkFtZTYwMTM1NjA0._V1_UX32_CR0,0,32,44_AL_.jpg")  # noqa
sergi_l = media.Actor(
    "Sergi Lopez",
    "Vidal",
    "http://ia.media-imdb.com/images/M/MV5BMTIzMDc3NzE4NV5BMl5BanBnXkFtZTYwNjQwODc1._V1_UX32_CR0,0,32,44_AL_.jpg")  # noqa
jake_g = media.Actor(
    "Jake Gyllenhaal",
    "Donnie Darko",
    "http://ia.media-imdb.com/images/M/MV5BMzM2MDgxNzkwN15BMl5BanBnXkFtZTcwNTAwOTc5OA@@._V1_UX32_CR0,0,32,44_AL_.jpg")  # noqa
jena_m = media.Actor(
    "Jena Malone",
    "Gretchen Ross",
    "http://ia.media-imdb.com/images/M/MV5BMTU0NDM5OTE0N15BMl5BanBnXkFtZTcwMzMzNjM0Nw@@._V1_UY44_CR2,0,32,44_AL_.jpg")  # noqa
mary_m = media.Actor(
    "Mary McDonnell",
    "Rose Darko",
    "http://ia.media-imdb.com/images/M/MV5BMjM5ODc4MTcwM15BMl5BanBnXkFtZTgwNjI2Njk3NTE@._V1_UX32_CR0,0,32,44_AL_.jpg")  # noqa


# Creating all movie instances to be displayed on page
imitation_game = media.Movie(
    "Imitation Game",
    "2014",
    "8.1/10",
    "During World War II, mathematician Alan Turing tries to crack the enigm" \
    "a code with help from fellow mathematicians.",
    [benedict_c, keira_k, matthew_g],
    "http://ia.media-imdb.com/images/M/MV5BNDkwNTEyMzkzNl5BMl5BanBnXkFtZTgwNTAwNzk3MjE@._V1_SX640_SY720_.jpg",  # noqa
    "https://www.youtube.com/watch?v=S5CjKEFb-sM")
snow_white = media.Movie(
    "Snow White Murder Case",
    "2014",
    "7.2/10",
    "A young woman working at a cosmetic company is interrogated with regar" \
    "ds to the murder of her beautiful co-worker.",
    [mao_i, go_a, nanao],
    "http://asianwiki.com/images/4/46/The_Snow_White_Murder_Case-p1.jpg",
    "https://www.youtube.com/watch?v=JhJctheblzs")
pacific_rim = media.Movie(
    "Pacific Rim",
    "2013",
    "7/10",
    "As a war between humankind and monstrous sea creatures wages on, a for" \
    "mer pilot and a trainee are paired up to drive a seemingly obsolete spe" \
    "cial weapon in a desperate effort to save the world from the apocalypse.",
    [idris_e, charlie_h, rinko_k],
    "https://upload.wikimedia.org/wikipedia/en/f/f3/Pacific_Rim_FilmPoster.jpeg",  # noqa
    "https://www.youtube.com/watch?v=5guMumPFBag")
wreck_it_ralph = media.Movie(
    "Wreck-It Ralph",
    "2012",
    "7.8/10",
    "A video game villain wants to be a hero and sets out to fulfill his" \
    " dream, but his quest brings havoc to the whole arcade where he lives.",
    [john_r, jack_m, jane_l],
    "https://upload.wikimedia.org/wikipedia/en/1/15/Wreckitralphposter.jpeg",
    "https://www.youtube.com/watch?v=87E6N7ToCxs")
martian = media.Movie(
    "The Martian",
    "2015",
    "8.3/10",
    "During a manned mission to Mars, Astronaut Mark Watney is presumed dead" \
    " after a fierce storm and left behind by his crew. But Watney has survi" \
    "ved and finds himself stranded and alone on the hostile planet. With on" \
    "ly meager supplies, he must draw upon his ingenuity, wit and spirit to " \
    "subsist and find a way to signal to Earth that he is alive.",
    [matt_d, jessica_c, kristen_w],
    "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=ej3ioOneTy8")
spy = media.Movie(
    "Spy",
    "2015",
    "7.2/10",
    "A desk-bound CIA analyst volunteers to go undercover to infiltrate the " \
    "world of a deadly arms dealer, and prevent diabolical global disaster.",
    [melissa_m, rose_b, jude_l],
    "http://www.impawards.com/2015/posters/spy_ver7_xlg.jpg",
    "https://www.youtube.com/watch?v=ltijEmlyqlg")
akira = media.Movie(
    "Akira",
    "1988",
    "8.1/10",
    "A secret military project endangers Neo-Tokyo when it turns a biker gan" \
    "g member into a rampaging psionic psychopath that only two kids and a g" \
    "roup of psionics can stop.",
    [nozomu_s, mitsuo_i, mami_k],
    "https://sonsofcorax.files.wordpress.com/2013/09/akira-001.jpg",
    "https://www.youtube.com/watch?v=7mdMtuGL7eg")
pans_labyrinth = media.Movie(
    "Pan's Labyrinth",
    "2006",
    "8.2/10",
    "In the falangist Spain of 1944, the bookish young stepdaughter of a sad" \
    "istic army officer escapes into an eerie but captivating fantasy world.",
    [ivana_b, ariadna_g, sergi_l],
    "http://www.impawards.com/2006/posters/pans_labyrinth_ver6.jpg",
    "https://www.youtube.com/watch?v=EqYiSlkvRuw")
donnie_darko = media.Movie(
    "Donnie Darko",
    "2001",
    "8.1/10",
    "A troubled teenager is plagued by visions of a large bunny rabbit that" \
    "manipulates him to commit a series of crimes, after narrowly escaping " \
    "a bizarre accident.",
    [jake_g, jena_m, mary_m],
    "http://wickedknights.org/wp-content/uploads/2015/10/donnie-darko-poster-1.jpg",  # noqa
    "https://www.youtube.com/watch?v=ZZyBaFYFySk")

# Array of movies will be passed into the open_movies_page function
# from fresh_tomatoes.py
movies = [imitation_game, snow_white, pacific_rim, wreck_it_ralph,
          martian, spy, akira, pans_labyrinth, donnie_darko]
fresh_tomatoes.open_movies_page(movies)
