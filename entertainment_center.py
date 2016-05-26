import fresh_tomatoes
import media
# the following codes create 6 instances of the class Movie, each representing
# one of my favourite movies. #Information about these movies include movie
# name, storyline, box art imagery and a movie trailer URL.

forrest_gump = media.Movie("Forrest Gump",
                     "A story of a slow-witted but kind-hearted,"
                     "good-natured and athletically prodigious man"
                     "becoming a national hero",
                     "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=bLvqoHBptjg")

into_the_wild = media.Movie("Into The Wild",
                     "A story of a Emory graduate embarking on a prestigious"
                     "and profitable career and set out on a journey to the"
                     "Alaskan wilderness",
                     "https://upload.wikimedia.org/wikipedia/en/8/8a/Into-the-wild.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=2LAuzT_x8Ek")

good_will_hunting = media.Movie("Good Will Hunting",
                     "Mental struggle of a genius kid",
                     "http://www.impawards.com/1997/posters/good_will_hunting_xxlg.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=PaZVjZEFkRs")

The_Pursuit_of_Happiness = media.Movie("The Pursuit of Happiness",
                     "Life is a struggle for a single father who tried to"
                     "give his son a better life",
                     "https://upload.wikimedia.org/wikipedia/en/8/81/Poster-pursuithappyness.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=00uTFVnWJMw")

The_Shawshank_Redemption = media.Movie("The Shawshank Redemption",
                     "A innocent man was sentenced to two consecutive"
                     "life terms in prison. While there, he formed a"
                     "friendship with Red, experienceed brutality of prison,"
                     "life,adapted, helped the warden, etc., all in 19 years.",
                     "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=zdWZBvd0-pg")

Zootopia = media.Movie("Zootopia",
                     "How the first female rabbit police officer solved"
                     "a mysterious case with a wily fox who makes her job"
                     "even harder",
                     "https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=WWFB-zrxn7o")

Transformers3 = media.Movie("Transformers 3",
                     "Optimus Prime freed ancient Transformer Sentinel Prime,"
                     "once the leader of the Autobots, which led to"
                     "devastating consequences.",
                     "https://upload.wikimedia.org/wikipedia/en/b/bf/Transformers_dark_of_the_moon_ver5.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=EkqdO8dhptc")


VforVendetta = media.Movie("V for Vendetta",
                     "How V saved a young woman named Evey from the secret"
                     "police and discovered an ally in his fight against"
                     "England's oppressors",
                     "https://upload.wikimedia.org/wikipedia/en/9/9f/Vforvendettamov.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=k_13fFIrhPk")


# here we created an array to store my favourite movies
movies = [forrest_gump, into_the_wild, good_will_hunting,
          The_Pursuit_of_Happiness, The_Shawshank_Redemption, Zootopia,
          Transformers3, VforVendetta]
# This function reads the list of my movies and turn it into a website.
fresh_tomatoes.open_movies_page(movies)

