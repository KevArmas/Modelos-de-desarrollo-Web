from fastapi import FastAPI
app = FastAPI()
from pydantic import BaseModel

class Peliculas(BaseModel):
    id: int
    Titulo: str
    Genero: str
    Año: int
    Director: str
    Oscares: int


peliculas_list=[ 
    Peliculas(id=1, Titulo= "The Shawshank Redemption", Genero="Drama" , Año=1994, Director= "Frank Darabont" , Oscares= 0), 
    Peliculas(id=2, Titulo= "The Godfather", Genero="Crime" , Año=1972, Director= "Francis Ford Coppola" , Oscares= 7), 
    Peliculas(id=3, Titulo= "The Dark Knight", Genero="Action" , Año=2008, Director= "Christopher Nolan" , Oscares= 2), 
    Peliculas(id=4, Titulo= "Schindler's List", Genero="Drama" , Año=1993, Director= "Steven Spielberg" , Oscares= 7), 
    Peliculas(id=5, Titulo= "Pulp Fiction", Genero="Crime" , Año=1994, Director= "Quentin Tarantino" , Oscares= 2), 
    Peliculas(id=6, Titulo= "12 Angry Men", Genero="Drama" , Año=1957, Director= "Sidney Lumet" , Oscares= 3), 
    Peliculas(id=7, Titulo= "The Lord of the Rings: The Return of the King", Genero="Adventure" , Año=2003, Director= "Peter Jackson" , Oscares= 11), 
    Peliculas(id=8, Titulo= "The Silence of the Lambs", Genero="Crime" , Año=1991, Director= "Jonathan Demme" , Oscares= 5), 
    Peliculas(id=9, Titulo= "Forrest Gump", Genero="Drama" , Año=1994, Director= "Robert Zemeckis" , Oscares= 6), 
    Peliculas(id=10, Titulo= "Titanic", Genero="Drama" , Año=1997, Director= "James Cameron" , Oscares= 11), 
    Peliculas(id=11, Titulo= "Inception", Genero="Action" , Año=2010, Director= "Christopher Nolan" , Oscares= 4), 
    Peliculas(id=12, Titulo= "The Departed", Genero="Crime" , Año=2006, Director= "Martin Scorsese" , Oscares= 4), 
    Peliculas(id=13, Titulo= "The Godfather Part II", Genero="Crime" , Año=1974, Director= "Francis Ford Coppola" , Oscares= 6), 
    Peliculas(id=14, Titulo= "The Good, the Bad and the Ugly", Genero="Western" , Año=1966, Director= "Sergio Leone" , Oscares= 1), 
    Peliculas(id=15, Titulo= "Whiplash", Genero="Drama" , Año=2014, Director= "Damien Chazelle" , Oscares= 3), 
    Peliculas(id=16, Titulo= "Parasite", Genero="Comedy" , Año=2019, Director= "Bong Joon-ho" , Oscares= 4), 
    Peliculas(id=17, Titulo= "Roma", Genero="Drama" , Año=2018, Director= "Alfonso Cuarón" , Oscares= 3), 
    Peliculas(id=18, Titulo= "The Shape of Water", Genero="Drama" , Año=2017, Director= "Guillermo del Toro" , Oscares= 4), 
    Peliculas(id=19, Titulo= "1917", Genero="War" , Año=2019, Director= "Sam Mendes" , Oscares= 3), 
    Peliculas(id=20, Titulo= "Moonlight", Genero="Drama" , Año=2016, Director= "Barry Jenkins" , Oscares= 3), 
    Peliculas(id=21, Titulo= "The King's Speech", Genero="Drama" , Año=2010, Director= "Tom Hooper" , Oscares= 4), 
    Peliculas(id=22, Titulo= "Argo", Genero="Thriller" , Año=2012, Director= "Ben Affleck" , Oscares= 3), 
    Peliculas(id=23, Titulo= "No Country for Old Men", Genero="Thriller" , Año=2007, Director= "Joel Coen, Ethan Coen" , Oscares= 4), 
    Peliculas(id=24, Titulo= "Slumdog Millionaire", Genero="Drama" , Año=2008, Director= "Danny Boyle" , Oscares= 8), 
    Peliculas(id=25, Titulo= "The Hurt Locker", Genero="War" , Año=2008, Director= "Kathryn Bigelow" , Oscares= 6), 
    Peliculas(id=26, Titulo= "Birdman or (The Unexpected Virtue of Ignorance)", Genero="Comedy" , Año=2014, Director= "Alejandro González Iñárritu" , Oscares= 4), 
    Peliculas(id=27, Titulo= "The Artist", Genero="Comedy" , Año=2011, Director= "Michel Hazanavicius" , Oscares= 5), 
    Peliculas(id=28, Titulo= "Spotlight", Genero="Drama" , Año=2015, Director= "Tom McCarthy" , Oscares= 2), 
    Peliculas(id=29, Titulo= "Green Book", Genero="Comedy" , Año=2018, Director= "Peter Farrelly" , Oscares= 3), 
    Peliculas(id=30, Titulo= "CODA", Genero="Drama" , Año=2021, Director= "Siân Heder" , Oscares= 3), 
    Peliculas(id=31, Titulo= "Parasite", Genero="Comedy" , Año=2019, Director= "Bong Joon-ho" , Oscares= 4), 
    Peliculas(id=32, Titulo= "All Quiet on the Western Front", Genero="War" , Año=1930, Director= "Lewis Milestone" , Oscares= 2), 
    Peliculas(id=33, Titulo= "It Happened One Night", Genero="Comedy" , Año=1934, Director= "Frank Capra" , Oscares= 5), 
    Peliculas(id=34, Titulo= "Gone with the Wind", Genero="Drama" , Año=1939, Director= "Victor Fleming" , Oscares= 10), 
    Peliculas(id=35, Titulo= "Casablanca", Genero="Drama" , Año=1942, Director= "Michael Curtiz" , Oscares= 3), 
    Peliculas(id=36, Titulo= "Lawrence of Arabia", Genero="Drama" , Año=1962, Director= "David Lean" , Oscares= 7), 
    Peliculas(id=37, Titulo= "West Side Story", Genero="Musical" , Año=1961, Director= "Robert Wise, Jerome Robbins" , Oscares= 10), 
    Peliculas(id=38, Titulo= "One Flew Over the Cuckoo's Nest", Genero="Drama" , Año=1975, Director= "Miloš Forman" , Oscares= 5), 
    Peliculas(id=39, Titulo= "Annie Hall", Genero="Comedy" , Año=1977, Director= "Woody Allen" , Oscares= 4), 
    Peliculas(id=40, Titulo= "Kramer vs. Kramer", Genero="Drama" , Año=1979, Director= "Robert Benton" , Oscares= 5), 
    Peliculas(id=41, Titulo= "Ordinary People", Genero="Drama" , Año=1980, Director= "Robert Redford" , Oscares= 2), 
    Peliculas(id=42, Titulo= "Terms of Endearment", Genero="Comedy" , Año=1983, Director= "James L. Brooks" , Oscares= 5), 
    Peliculas(id=43, Titulo= "Amadeus", Genero="Biography" , Año=1984, Director= "Miloš Forman" , Oscares= 8), 
    Peliculas(id=44, Titulo= "Platoon", Genero="War" , Año=1986, Director= "Oliver Stone" , Oscares= 4), 
    Peliculas(id=45, Titulo= "Rain Man", Genero="Drama" , Año=1988, Director= "Barry Levinson" , Oscares= 4), 
    Peliculas(id=46, Titulo= "Driving Miss Daisy", Genero="Comedy" , Año=1989, Director= "Bruce Beresford" , Oscares= 4), 
    Peliculas(id=47, Titulo= "Dances with Wolves", Genero="Western" , Año=1990, Director= "Kevin Costner" , Oscares= 7), 
    Peliculas(id=48, Titulo= "Unforgiven", Genero="Western" , Año=1992, Director= "Clint Eastwood" , Oscares= 4), 
    Peliculas(id=49, Titulo= "Braveheart", Genero="Drama" , Año=1995, Director= "Mel Gibson" , Oscares= 5), 
    Peliculas(id=50, Titulo= "The English Patient", Genero="Drama" , Año=1996, Director= "Anthony Minghella" , Oscares= 9), 
    Peliculas(id=51, Titulo= "Titanic", Genero="Drama" , Año=1997, Director= "James Cameron" , Oscares= 11), 
    Peliculas(id=52, Titulo= "Shakespeare in Love", Genero="Comedy" , Año=1998, Director= "John Madden" , Oscares= 7), 
    Peliculas(id=53, Titulo= "American Beauty", Genero="Drama" , Año=1999, Director= "Sam Mendes" , Oscares= 5), 
    Peliculas(id=54, Titulo= "Gladiator", Genero="Drama" , Año=2000, Director= "Ridley Scott" , Oscares= 5), 
    Peliculas(id=55, Titulo= "A Beautiful Mind", Genero="Biography" , Año=2001, Director= "Ron Howard" , Oscares= 4), 
    Peliculas(id=56, Titulo= "Chicago", Genero="Musical" , Año=2002, Director= "Rob Marshall" , Oscares= 6), 
    Peliculas(id=57, Titulo= "Lord of the Rings: The Return of the King", Genero="Adventure" , Año=2003, Director= "Peter Jackson" , Oscares= 11), 
    Peliculas(id=58, Titulo= "The Aviator", Genero="Biography" , Año=2004, Director= "Martin Scorsese" , Oscares= 5), 
    Peliculas(id=59, Titulo= "Million Dollar Baby", Genero="Drama" , Año=2004, Director= "Clint Eastwood" , Oscares= 4), 
    Peliculas(id=60, Titulo= "Crash", Genero="Drama" , Año=2005, Director= "Paul Haggis" , Oscares= 3), 
    Peliculas(id=61, Titulo= "Brokeback Mountain", Genero="Drama" , Año=2005, Director= "Ang Lee" , Oscares= 3), 
    Peliculas(id=62, Titulo= "Babel", Genero="Drama" , Año=2006, Director= "Alejandro González Iñárritu" , Oscares= 2), 
    Peliculas(id=63, Titulo= "The Departed", Genero="Crime" , Año=2006, Director= "Martin Scorsese" , Oscares= 4), 
    Peliculas(id=64, Titulo= "No Country for Old Men", Genero="Crime" , Año=2007, Director= "Joel Coen, Ethan Coen" , Oscares= 4), 
    Peliculas(id=65, Titulo= "Slumdog Millionaire", Genero="Drama" , Año=2008, Director= "Danny Boyle" , Oscares= 8), 
    Peliculas(id=66, Titulo= "The Hurt Locker", Genero="War" , Año=2008, Director= "Kathryn Bigelow" , Oscares= 6), 
    Peliculas(id=67, Titulo= "Avatar", Genero="Action" , Año=2009, Director= "James Cameron" , Oscares= 3), 
    Peliculas(id=68, Titulo= "The King's Speech", Genero="Drama" , Año=2010, Director= "Tom Hooper" , Oscares= 4), 
    Peliculas(id=69, Titulo= "The Artist", Genero="Comedy" , Año=2011, Director= "Michel Hazanavicius" , Oscares= 5), 
    Peliculas(id=70, Titulo= "Argo", Genero="Thriller" , Año=2012, Director= "Ben Affleck" , Oscares= 3), 
    Peliculas(id=71, Titulo= "12 Years a Slave", Genero="Drama" , Año=2013, Director= "Steve McQueen" , Oscares= 3), 
    Peliculas(id=72, Titulo= "Birdman or (The Unexpected Virtue of Ignorance)", Genero="Comedy" , Año=2014, Director= "Alejandro González Iñárritu" , Oscares= 4), 
    Peliculas(id=73, Titulo= "Spotlight", Genero="Drama" , Año=2015, Director= "Tom McCarthy" , Oscares= 2), 
    Peliculas(id=74, Titulo= "Moonlight", Genero="Drama" , Año=2016, Director= "Barry Jenkins" , Oscares= 3), 
    Peliculas(id=75, Titulo= "The Shape of Water", Genero="Drama" , Año=2017, Director= "Guillermo del Toro" , Oscares= 4), 
    Peliculas(id=76, Titulo= "Green Book", Genero="Comedy" , Año=2018, Director= "Peter Farrelly" , Oscares= 3), 
    Peliculas(id=77, Titulo= "Parasite", Genero="Comedy" , Año=2019, Director= "Bong Joon-ho" , Oscares= 4), 
    Peliculas(id=78, Titulo= "Nomadland", Genero="Drama" , Año=2020, Director= "Chloé Zhao" , Oscares= 3), 
    Peliculas(id=79, Titulo= "CODA", Genero="Drama" , Año=2021, Director= "Siân Heder" , Oscares= 3), 
    Peliculas(id=80, Titulo= "The Power of the Dog", Genero="Western" , Año=2021, Director= "Jane Campion" , Oscares= 12), 
    Peliculas(id=81, Titulo= "Dune", Genero="Science Fiction" , Año=2021, Director= "Denis Villeneuve" , Oscares= 6), 
    Peliculas(id=82, Titulo= "El Padrino", Genero="Drama" , Año=1972, Director= "Francis Ford Coppola" , Oscares= 3), 
    Peliculas(id=83, Titulo= "Titanic", Genero="Romance" , Año=1997, Director= "James Cameron" , Oscares= 11), 
    Peliculas(id=84, Titulo= "Star Wars", Genero="Science Fiction" , Año=1977, Director= "George Lucas" , Oscares= 7), 
    Peliculas(id=85, Titulo= "El Señor de los Anillos: La Comunidad del Anillo", Genero="Fantasy" , Año=2001, Director= "Peter Jackson" , Oscares= 4), 
    Peliculas(id=86, Titulo= "Matrix", Genero="Action" , Año=1999, Director= "The Wachowskis" , Oscares= 4), 
    Peliculas(id=87, Titulo= "Toy Story", Genero="Animation" , Año=1995, Director= "John Lasseter" , Oscares= 2), 
    Peliculas(id=88, Titulo= "Jurassic Park", Genero="Adventure" , Año=1993, Director= "Steven Spielberg" , Oscares= 3), 
    Peliculas(id=89, Titulo= "Avengers: Endgame", Genero="Superheroes" , Año=2019, Director= "Anthony y Joe Russo" , Oscares= 2), 
    Peliculas(id=90, Titulo= "El Rey León", Genero="Animation" , Año=1994, Director= "Roger Allers y Rob Minkoff" , Oscares= 2), 
    Peliculas(id=91, Titulo= "Regreso al futuro", Genero="Science Fiction" , Año=1985, Director= "Robert Zemeckis" , Oscares= 1), 
    Peliculas(id=92, Titulo= "Harry Potter y la Piedra Filosofal", Genero="Fantasy" , Año=2001, Director= "Chris Columbus" , Oscares= 1), 
    Peliculas(id=93, Titulo= "Forrest Gump", Genero="Drama" , Año=1994, Director= "Robert Zemeckis" , Oscares= 6), 
    Peliculas(id=94, Titulo= "Los Vengadores", Genero="Superheroes" , Año=2012, Director= "Joss Whedon" , Oscares= 1), 
    Peliculas(id=95, Titulo= "La La Land", Genero="Musical" , Año=2016, Director= "Damien Chazelle" , Oscares= 6), 
    Peliculas(id=96, Titulo= "Pulp Fiction", Genero="Crime" , Año=1994, Director= "Quentin Tarantino" , Oscares= 7), 
    Peliculas(id=97, Titulo= "El resplandor", Genero="Horror" , Año=1980, Director= "Stanley Kubrick" , Oscares= 2), 
    Peliculas(id=98, Titulo= "E.T. el Extraterrestre", Genero="Science Fiction" , Año=1982, Director= "Steven Spielberg" , Oscares= 4), 
    Peliculas(id=99, Titulo= "El caballero oscuro", Genero="Action" , Año=2008, Director= "Christopher Nolan" , Oscares= 2), 
    Peliculas(id=100, Titulo= "Los Increíbles", Genero="Animation" , Año=2004, Director= "Brad Bird" , Oscares= 2), 
    Peliculas(id=101, Titulo= "El Gran Gatsby", Genero="Drama" , Año=2013, Director= "Baz Luhrmann" , Oscares= 2), 
    Peliculas(id=102, Titulo= "Avatar", Genero="Science Fiction" , Año=2009, Director= "James Cameron" , Oscares= 3), 
    Peliculas(id=103, Titulo= "Gladiator", Genero="Action" , Año=2000, Director= "Ridley Scott" , Oscares= 5), 
    Peliculas(id=104, Titulo= "Cadena perpetua", Genero="Drama" , Año=1994, Director= "Frank Darabont" , Oscares= 1), 
    Peliculas(id=105, Titulo= "El silencio de los corderos", Genero="Suspense" , Año=1991, Director= "Jonathan Demme" , Oscares= 5), 
    Peliculas(id=106, Titulo= "El club de la lucha", Genero="Drama" , Año=1999, Director= "David Fincher" , Oscares= 1), 
    Peliculas(id=107, Titulo= "El Pianista", Genero="Drama" , Año=2002, Director= "Roman Polanski" , Oscares= 3), 
    Peliculas(id=108, Titulo= "Volver al futuro", Genero="Science Fiction" , Año=1985, Director= "Robert Zemeckis" , Oscares= 1), 
    Peliculas(id=109, Titulo= "Interestelar", Genero="Science Fiction" , Año=2014, Director= "Christopher Nolan" , Oscares= 5), 
    Peliculas(id=110, Titulo= "La Lista de Schindler", Genero="Drama" , Año=1993, Director= "Steven Spielberg" , Oscares= 7), 
    Peliculas(id=111, Titulo= "Misión: Imposible", Genero="Action" , Año=1996, Director= "Brian De Palma" , Oscares= 1), 
    Peliculas(id=112, Titulo= "Los juegos del hambre", Genero="Adventure" , Año=2012, Director= "Gary Ross" , Oscares= 1), 
    Peliculas(id=113, Titulo= "Shrek", Genero="Animation" , Año=2001, Director= "Andrew Adamson y Vicky Jenson" , Oscares= 2), 
    Peliculas(id=114, Titulo= "El Renacido", Genero="Adventure" , Año=2015, Director= "Alejandro González Iñárritu" , Oscares= 3), 
    Peliculas(id=115, Titulo= "El laberinto del fauno", Genero="Fantasy" , Año=2006, Director= "Guillermo del Toro" , Oscares= 3), 
    Peliculas(id=116, Titulo= "El cisne negro", Genero="Drama" , Año=2010, Director= "Darren Aronofsky" , Oscares= 5), 
    Peliculas(id=117, Titulo= "El discurso del rey", Genero="Drama" , Año=2010, Director= "Tom Hooper" , Oscares= 4), 
    Peliculas(id=118, Titulo= "Avatar", Genero="Science Fiction" , Año=2009, Director= "James Cameron" , Oscares= 3), 
    Peliculas(id=119, Titulo= "Gladiator", Genero="Action" , Año=2000, Director= "Ridley Scott" , Oscares= 5), 
    Peliculas(id=120, Titulo= "Cadena perpetua", Genero="Drama" , Año=1994, Director= "Frank Darabont" , Oscares= 1), 
    Peliculas(id=121, Titulo= "El silencio de los corderos", Genero="Suspense" , Año=1991, Director= "Jonathan Demme" , Oscares= 5), 
    Peliculas(id=122, Titulo= "El club de la lucha", Genero="Drama" , Año=1999, Director= "David Fincher" , Oscares= 1), 
    Peliculas(id=123, Titulo= "El pianista", Genero="Drama" , Año=2002, Director= "Roman Polanski" , Oscares= 3), 
    Peliculas(id=124, Titulo= "Interestelar", Genero="Science Fiction" , Año=2014, Director= "Christopher Nolan" , Oscares= 5), 
    Peliculas(id=125, Titulo= "La Lista de Schindler", Genero="Drama" , Año=1993, Director= "Steven Spielberg" , Oscares= 7), 
    Peliculas(id=126, Titulo= "Misión: Imposible", Genero="Action" , Año=1996, Director= "Brian De Palma" , Oscares= 1), 
    Peliculas(id=127, Titulo= "Los Juegos del Hambre", Genero="Adventure" , Año=2012, Director= "Gary Ross" , Oscares= 1), 
    Peliculas(id=128, Titulo= "Shrek", Genero="Animation" , Año=2001, Director= "Andrew Adamson y Vicky Jenson" , Oscares= 2), 
    Peliculas(id=129, Titulo= "El Renacido", Genero="Adventure" , Año=2015, Director= "Alejandro González Iñárritu" , Oscares= 3), 
    Peliculas(id=130, Titulo= "El Laberinto del Fauno", Genero="Fantasy" , Año=2006, Director= "Guillermo del Toro" , Oscares= 3), 
    Peliculas(id=131, Titulo= "El Cisne Negro", Genero="Drama" , Año=2010, Director= "Darren Aronofsky" , Oscares= 5), 
    Peliculas(id=132, Titulo= "El Discurso del Rey", Genero="Drama" , Año=2010, Director= "Tom Hooper" , Oscares= 4), 
    Peliculas(id=133, Titulo= "Los Vengadores: Infinity War", Genero="Superheroes" , Año=2018, Director= "Anthony y Joe Russo" , Oscares= 2), 
    Peliculas(id=134, Titulo= "El Señor de los Anillos: Las Dos Torres", Genero="Fantasy" , Año=2002, Director= "Peter Jackson" , Oscares= 2), 
    Peliculas(id=135, Titulo= "El Señor de los Anillos: El Retorno del Rey", Genero="Fantasy" , Año=2003, Director= "Peter Jackson" , Oscares= 11), 
    Peliculas(id=136, Titulo= "Star Wars: Episodio I - La Amenaza Fantasma", Genero="Science Fiction" , Año=1999, Director= "George Lucas" , Oscares= 1), 
    Peliculas(id=137, Titulo= "Star Wars: Episodio II - El Ataque de los Clones", Genero="Science Fiction" , Año=2002, Director= "George Lucas" , Oscares= 1), 
    Peliculas(id=138, Titulo= "Star Wars: Episodio III - La Venganza de los Sith", Genero="Science Fiction" , Año=2005, Director= "George Lucas" , Oscares= 2), 
    Peliculas(id=139, Titulo= "Star Wars: Episodio VII - El Despertar de la Fuerza", Genero="Science Fiction" , Año=2015, Director= "J.J. Abrams" , Oscares= 5), 
    Peliculas(id=140, Titulo= "Star Wars: Episodio VIII - Los Últimos Jedi", Genero="Science Fiction" , Año=2017, Director= "Rian Johnson" , Oscares= 2), 
    Peliculas(id=141, Titulo= "Star Wars: Episodio IX - El Ascenso de Skywalker", Genero="Science Fiction" , Año=2019, Director= "J.J. Abrams" , Oscares= 1), 
    Peliculas(id=142, Titulo= "Harry Potter y la Cámara Secreta", Genero="Fantasy" , Año=2002, Director= "Chris Columbus" , Oscares= 3), 
    Peliculas(id=143, Titulo= "Harry Potter y el Prisionero de Azkaban", Genero="Fantasy" , Año=2004, Director= "Alfonso Cuarón" , Oscares= 2), 
    Peliculas(id=144, Titulo= "Harry Potter y el Cáliz de Fuego", Genero="Fantasy" , Año=2005, Director= "Mike Newell" , Oscares= 1), 
    Peliculas(id=145, Titulo= "Harry Potter y la Orden del Fénix", Genero="Fantasy" , Año=2007, Director= "David Yates" , Oscares= 3), 
    Peliculas(id=146, Titulo= "Harry Potter y el Misterio del Príncipe", Genero="Fantasy" , Año=2009, Director= "David Yates" , Oscares= 2), 
    Peliculas(id=147, Titulo= "Harry Potter y las Reliquias de la Muerte: Parte 1", Genero="Fantasy" , Año=2010, Director= "David Yates" , Oscares= 2), 
    Peliculas(id=148, Titulo= "Harry Potter y las Reliquias de la Muerte: Parte 2", Genero="Fantasy" , Año=2011, Director= "David Yates" , Oscares= 3), 
    Peliculas(id=149, Titulo= "El Hobbit: Un viaje inesperado", Genero="Fantasy" , Año=2012, Director= "Peter Jackson" , Oscares= 3), 
    Peliculas(id=150, Titulo= "El Hobbit: La desolación de Smaug", Genero="Fantasy" , Año=2013, Director= "Peter Jackson" , Oscares= 3), 
    Peliculas(id=151, Titulo= "El Hobbit: La batalla de los cinco ejércitos", Genero="Fantasy" , Año=2014, Director= "Peter Jackson" , Oscares= 2), 
    Peliculas(id=152, Titulo= "En busca del arca perdida", Genero="Adventure" , Año=1981, Director= "Steven Spielberg" , Oscares= 1), 
    Peliculas(id=153, Titulo= "El templo maldito", Genero="Adventure" , Año=1984, Director= "Steven Spielberg" , Oscares= 1), 
    Peliculas(id=154, Titulo= "La última cruzada", Genero="Adventure" , Año=1989, Director= "Steven Spielberg" , Oscares= 2), 
    Peliculas(id=155, Titulo= "El reino de la calavera de cristal", Genero="Adventure" , Año=2008, Director= "Steven Spielberg" , Oscares= 1), 
    Peliculas(id=156, Titulo= "El legado", Genero="Adventure" , Año=2022, Director= "Steven Spielberg" , Oscares= 0), 
    Peliculas(id=157, Titulo= "Alien: El octavo pasajero", Genero="Science Fiction" , Año=1979, Director= "Ridley Scott" , Oscares= 1), 
    Peliculas(id=158, Titulo= "Aliens: El regreso", Genero="Science Fiction" , Año=1986, Director= "James Cameron" , Oscares= 2), 
    Peliculas(id=159, Titulo= "Alien 3", Genero="Science Fiction" , Año=1992, Director= "David Fincher" , Oscares= 0), 
    Peliculas(id=160, Titulo= "Alien: Resurrección", Genero="Science Fiction" , Año=1997, Director= "Jean-Pierre Jeunet" , Oscares= 0), 
    Peliculas(id=161, Titulo= "Prometheus", Genero="Science Fiction" , Año=2012, Director= "Ridley Scott" , Oscares= 1), 
    Peliculas(id=162, Titulo= "Alien: Covenant", Genero="Science Fiction" , Año=2017, Director= "Ridley Scott" , Oscares= 0), 
    Peliculas(id=163, Titulo= "Rápido y Furioso", Genero="Action" , Año=2001, Director= "Rob Cohen" , Oscares= 0), 
    Peliculas(id=164, Titulo= "2 Fast 2 Furious", Genero="Action" , Año=2003, Director= "John Singleton" , Oscares= 0), 
    Peliculas(id=165, Titulo= "Turbo Charged Prelude to 2 Fast 2 Furious", Genero="Action" , Año=2003, Director= "Rob Cohen" , Oscares= 0), 
    Peliculas(id=166, Titulo= "Fast & Furious: Aún más rápido", Genero="Action" , Año=2009, Director= "Justin Lin" , Oscares= 0), 
    Peliculas(id=167, Titulo= "Fast & Furious 5: In Control", Genero="Action" , Año=2011, Director= "Justin Lin" , Oscares= 0), 
    Peliculas(id=168, Titulo= "Fast & Furious 6: A todo gas", Genero="Action" , Año=2013, Director= "Justin Lin" , Oscares= 0), 
    Peliculas(id=169, Titulo= "Furious 7", Genero="Action" , Año=2015, Director= "James Wan" , Oscares= 1), 
    Peliculas(id=170, Titulo= "Fast & Furious 8", Genero="Action" , Año=2017, Director= "F. Gary Gray" , Oscares= 0), 
    Peliculas(id=171, Titulo= "Fast & Furious 9", Genero="Action" , Año=2021, Director= "Justin Lin" , Oscares= 0), 
    Peliculas(id=172, Titulo= "Misión Imposible", Genero="Action" , Año=1996, Director= "Brian De Palma" , Oscares= 1), 
    Peliculas(id=173, Titulo= "Misión Imposible 2", Genero="Action" , Año=2000, Director= "John Woo" , Oscares= 0), 
    Peliculas(id=174, Titulo= "Misión Imposible 3", Genero="Action" , Año=2006, Director= "J.J. Abrams" , Oscares= 1), 
    Peliculas(id=175, Titulo= "Misión Imposible: Protocolo fantasma", Genero="Action" , Año=2011, Director= "Brad Bird" , Oscares= 1), 
    Peliculas(id=176, Titulo= "Misión Imposible: Nación secreta", Genero="Action" , Año=2015, Director= "Christopher McQuarrie" , Oscares= 1), 
    Peliculas(id=177, Titulo= "Misión Imposible: Repercusión", Genero="Action" , Año=2018, Director= "Christopher McQuarrie" , Oscares= 0), 
    Peliculas(id=178, Titulo= "Acorralado", Genero="Action" , Año=1982, Director= "Ted Kotcheff" , Oscares= 1), 
    Peliculas(id=179, Titulo= "Rambo: Acorralado - Parte II", Genero="Action" , Año=1985, Director= "George P. Cosmatos" , Oscares= 1), 
    Peliculas(id=180, Titulo= "Rambo III", Genero="Action" , Año=1988, Director= "Peter MacDonald" , Oscares= 0), 
    Peliculas(id=181, Titulo= "Rambo", Genero="Action" , Año=2008, Director= "Sylvester Stallone" , Oscares= 1), 
    Peliculas(id=182, Titulo= "Rambo: Last Blood", Genero="Action" , Año=2019, Director= "Adrian Grunberg" , Oscares= 0), 
    Peliculas(id=183, Titulo= "Iron Man", Genero="Action" , Año=2008, Director= "Jon Favreau" , Oscares= 2), 
    Peliculas(id=184, Titulo= "Iron Man 2", Genero="Action" , Año=2010, Director= "Jon Favreau" , Oscares= 1), 
    Peliculas(id=185, Titulo= "Iron Man 3", Genero="Action" , Año=2013, Director= "Shane Black" , Oscares= 1), 
    Peliculas(id=186, Titulo= "Capitán América: El primer vengador", Genero="Action" , Año=2011, Director= "Joe Johnston" , Oscares= 1), 
    Peliculas(id=187, Titulo= "Capitán América: El soldado de invierno", Genero="Action" , Año=2014, Director= "Anthony y Joe Russo" , Oscares= 1), 
    Peliculas(id=188, Titulo= "Capitán América: Civil War", Genero="Action" , Año=2016, Director= "Anthony y Joe Russo" , Oscares= 2), 
    Peliculas(id=189, Titulo= "Thor", Genero="Action" , Año=2011, Director= "Kenneth Branagh" , Oscares= 1), 
    Peliculas(id=190, Titulo= "Thor: Un mundo oscuro", Genero="Action" , Año=2013, Director= "Alan Taylor" , Oscares= 1), 
    Peliculas(id=191, Titulo= "Thor: Ragnarok", Genero="Action" , Año=2017, Director= "Taika Waititi" , Oscares= 1), 
    Peliculas(id=192, Titulo= "Thor: Love and Thunder", Genero="Action" , Año=2022, Director= "Taika Waititi" , Oscares= 0), 
    Peliculas(id=193, Titulo= "Guardianes de la Galaxia", Genero="Adventure" , Año=2014, Director= "James Gunn" , Oscares= 1), 
    Peliculas(id=194, Titulo= "Guardianes de la Galaxia Vol. 2", Genero="Science Fiction" , Año=2017, Director= "James Gunn" , Oscares= 1), 
    Peliculas(id=195, Titulo= "Los Vengadores", Genero="Drama" , Año=2012, Director= "Joss Whedon" , Oscares= 5), 
    Peliculas(id=196, Titulo= "Los Vengadores: La era de Ultrón", Genero="Animation" , Año=2015, Director= "Joss Whedon" , Oscares= 2), 
    Peliculas(id=197, Titulo= "Los Vengadores: Infinity War", Genero="Action" , Año=2018, Director= "Anthony y Joe Russo" , Oscares= 2), 
    Peliculas(id=198, Titulo= "Los Vengadores: Endgame", Genero="Science Fiction" , Año=2019, Director= "Anthony y Joe Russo" , Oscares= 1), 
    Peliculas(id=199, Titulo= "Indiana Jones y los cazadores del arca perdida", Genero="Action" , Año=1981, Director= "Steven Spielberg" , Oscares= 1), 
    Peliculas(id=200, Titulo= "Volver al Futuro II", Genero="Action" , Año=1989, Director= "Robert Zemeckis" , Oscares= 1), 
    Peliculas(id=201, Titulo= "La Lista de Schindler", Genero="Science Fiction" , Año=1993, Director= "Steven Spielberg" , Oscares= 7), 
    Peliculas(id=202, Titulo= "El Rey León 2: El tesoro de Simba", Genero="Action" , Año=1998, Director= "Roger Allers" , Oscares= 1), 
    Peliculas(id=203, Titulo= "Misión Imposible: Fallout", Genero="Fantasy" , Año=2018, Director= "Christopher McQuarrie" , Oscares= 1), 
    Peliculas(id=204, Titulo= "Blade Runner", Genero="Drama" , Año=1982, Director= "Ridley Scott" , Oscares= 1), 
    Peliculas(id=205, Titulo= "Mujer Maravilla", Genero="Science Fiction" , Año=2017, Director= "Patty Jenkins" , Oscares= 1), 
    Peliculas(id=206, Titulo= "Batman: El caballero de la noche asciende", Genero="Action" , Año=2012, Director= "Christopher Nolan" , Oscares= 2), 
    Peliculas(id=207, Titulo= "Inception", Genero="Science Fiction" , Año=2010, Director= "Christopher Nolan" , Oscares= 4), 
    Peliculas(id=208, Titulo= "Mad Max: Fury Road", Genero="Action" , Año=2015, Director= "George Miller" , Oscares= 6), 
    Peliculas(id=209, Titulo= "La forma del agua", Genero="Fantasy" , Año=2017, Director= "Guillermo del Toro" , Oscares= 4), 
    Peliculas(id=210, Titulo= "El club de la lucha", Genero="Drama" , Año=1999, Director= "David Fincher" , Oscares= 1), 
    Peliculas(id=211, Titulo= "La llegada", Genero="Science Fiction" , Año=2016, Director= "Denis Villeneuve" , Oscares= 1), 

]

@app.get("/peliculas")
async def imprimir():
    return peliculas_list

@app.get("/peliculas/{id}")
async def Peliculasclass(id: int):
    Peliculas = filter (lambda Peliculas: Peliculas.id == id, peliculas_list)
    try:
        return list(Peliculas)[0]
    except:
        return{"error":"No se ha encontrado la pelicula que buscas"}

@app.get("/peliculas2/")
async def Peliculasclass(Titulo: str, Genero:str):
    Peliculas = filter (lambda Peliculas: Peliculas.Titulo == Titulo, peliculas_list) #Funcion Lamda para busqueda de titulo (orden superior)
    Peliculas1 = filter (lambda Peliculas: Peliculas.Genero == Genero, Peliculas) #Funcion Lamda para busqueda de genero (orden inferior)
    try:
        return list(Peliculas1) #Se borra el [0] para que la lista muestre todos los datos que coincidan y no solo muestre uno
    except:
        return{"error":"No se ha encontrado la pelicula por el titulo o genero que buscas"}


@app.get("/peliculas3/")
async def Peliculasclass(Titulo: str, Genero:str, Año:int):
    Peliculas = filter (lambda Peliculas: Peliculas.Titulo == Titulo, peliculas_list) #Funcion Lamda para busqueda de titulo (orden superior)
    Peliculas1 = filter (lambda Peliculas: Peliculas.Genero == Genero, Peliculas) #Funcion Lamda para busqueda de genero (orden inferior)
    Peliculas2 = filter (lambda Peliculas: Peliculas.Año == Año, Peliculas1)
    try:
        return list(Peliculas2) #Se borra el [0] para que la lista muestre todos los datos que coincidan y no solo muestre uno
    except:
        return{"error":"No se ha encontrado la pelicula por el titulo o genero que buscas"}

@app.get("/peliculas4/")
async def Peliculasclass(Titulo: str, Genero:str, Año:int, Director:str):
    Peliculas = filter (lambda Peliculas: Peliculas.Titulo == Titulo, peliculas_list) #Funcion Lamda para busqueda de titulo (orden superior)
    Peliculas1 = filter (lambda Peliculas: Peliculas.Genero == Genero, Peliculas) #Funcion Lamda para busqueda de genero (orden inferior)
    Peliculas2 = filter (lambda Peliculas: Peliculas.Año == Año, Peliculas1)
    Peliculas3 = filter (lambda Peliculas: Peliculas.Director == Director, Peliculas2)
    try:
        return list(Peliculas3) #Se borra el [0] para que la lista muestre todos los datos que coincidan y no solo muestre uno
    except:
        return{"error":"No se ha encontrado la pelicula por el titulo, genero, o año que buscas"}    
    

@app.get("/peliculas5/")
async def Peliculasclass(Titulo: str, Genero:str, Año:int, Director:str, Oscares:str):
    Peliculas = filter (lambda Peliculas: Peliculas.Titulo == Titulo, peliculas_list) #Funcion Lamda para busqueda de titulo (orden superior)
    Peliculas1 = filter (lambda Peliculas: Peliculas.Genero == Genero, Peliculas) #Funcion Lamda para busqueda de genero (orden inferior)
    Peliculas2 = filter (lambda Peliculas: Peliculas.Año == Año, Peliculas1)
    Peliculas3 = filter (lambda Peliculas: Peliculas.Director == Director, Peliculas2)
    Peliculas4 = filter (lambda Peliculas: Peliculas.Oscares == Oscares, Peliculas3)
    try:
        return list(Peliculas4) #Se borra el [0] para que la lista muestre todos los datos que coincidan y no solo muestre uno
    except:
        return{"error":"No se ha encontrado la pelicula por el titulo o genero, año o director que buscas"}    
    