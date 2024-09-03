import tkinter as tk
from tkinter import ttk, messagebox
import random

class RecordSearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Record Search')

        # Sample data for demonstration purposes
        self.artists = ['100gecs', 'Ahmad Jamal Trio', 'Akoya Afrobeat Ensemble', 'Al Green', 'Amon Duul II', 'Art Blakey',
            'Arthur Fiedler and the Boston Pops Orchestra', 'Atlantik', 'Augustus Pablo', 'Average White Band',
            'Azymuth', 'Baja Marimba Band', 'Baja Marimba Band', 'Bee Gees', 'Bert van de Broek', 'Bill Evans',
            'Billy Williams', 'Blondie', 'Blotto', 'Blotto', 'Bob Crewe & Charles Fox', 'Bob James', 'Bob James',
            'Bob Marley & The Wailers', 'Bobbi Humphrey', 'Bobby Hutcherson', 'Bobby Hutcherson', 'Bobby Hutcherson', 'Bobby Hutcherson',
            'Bobby Hutcherson', 'Bonzo Dog Band', 'Boots Randolph', 'Bootsy Collins', 'Bram Tchaikovsky', 'Brenton Wood',
            'Bruce Haack', 'Burt Bacharach', 'Burt Bacharach', 'Burt Bacharach', 'Burt Bacharach', 'Burt Bacharach',
            'Burt Bacharach', 'Buttley Moore', 'C.O.S', 'Cal Tjader', 'Cal Tjader', 'Cal Tjader', 'Cameo', 'Can', 'Can',
            'Cannonball Adderley', 'Captain Beefheart', 'Captain Beefheart', 'Captain Beefheart & His Magic Band',
            'Captain Beefheart & His Magic Band', 'Captain Beefheart & His Magic Band', 'Carole King', 'Carole King',
            'Casiopea', 'Celebration', 'Chalice and Lovindeer', 'Charles Lloyd', 'Charles Mingus', 'Charles Mingus',
            'Charles Mingus', 'Charles Mingus', 'Charles Mingus', 'Charles Mingus', 'Charles Mingus', 'Charles Tolliver',
            'Charlie Byrd', 'Charlie Mingus', 'Chet Atkins', 'Chet Atkins', 'Chet Atkins', 'Chet Atkins', 'Chi-Lites',
            'Chicago', 'Chick Corea & Gary Burton', 'Chuck Berry', 'Crowd Pleasers', 'Das Damen', 'Dave Brubeck',
            'David Axelrod', 'David Bowie', 'De La Soul', 'Devo', 'Devo', 'Dick Hyman', 'Dick Hyman', 'Dimension',
            'Dionne Warwick', 'Dionne Warwick', 'Dionne Warwick', 'Dionne Warwick', 'Dionne Warwick', 'Django Reinhardt',
            'Dollar Brand', 'Don Ellis', 'Don Ellis', 'Don Ellis', 'Donald Byrd', 'Donald Byrd', 'Donald Byrd',
            'Donald Fagen', 'Donna Summer', 'Donna Summer', 'Donna Summer', 'Dorival Caymmi', 'Double D',
            'Duke Ellington & John Coltrane', 'Duke Harris', 'Eberhard Weber', 'Edwin Birdsong', 'Electric Light Orchestra',
            'Electric Light Orchestra', 'Elton John', 'Elton John', 'Elton John', 'Emil Dimitrov', 'Enoch Light and the Light Brigade',
            'Erasmo Carlos', 'Eric Dolphy', 'Eric Dolphy', 'Experience Unlimited', 'Experience Unlimited', 'Fat Boys and The Beach Boys',
            'Faust', 'Felbm', 'Ferrante & Teicher', 'Fleetwood Mac', 'Flo & Eddie', 'Foehammer', 'Frank Zappa', 'Frank Zappa',
            'Frank Zappa', 'Frank Zappa', 'Frank Zappa', 'Frank Zappa', 'Frank Zappa & Captain Beefheart', 'Frankie Lymon & The Teenagers',
            'Freddie Hubbard', 'Freddie Hubbard', 'Freddie Hubbard', 'Freddie Hubbard', 'Funkadelic', 'Gato Barbieri',
            'Gentle Giant', 'George Benson', 'George Duke', 'George Duke', 'George Russell Sextet', 'Gil Scott-Heron',
            'Giorgio Moroder', 'Glen Campbell', 'Glen Campbell', 'Glen Campbell', 'Glen Campbell', 'Gordon Parks',
            'Hadley Caliman', 'Hailu Mercia', 'Hailu Mergia', 'Hailu Mergia', 'Hailu Mergia', 'Harpers Bizarre',
            'Henry Mancini', 'Henry Mancini', 'Henry Mancini', 'Henry Mancini', 'Herb Alpert', 'Herb Alpert & the Tijuana Brass',
            'Herb Alpert & the Tijuana Brass', 'Herb Alpert & the Tijuana Brass', 'Herb Alpert & the Tijuana Brass',
            'Herb Alpert & the Tijuana Brass', 'Herb Alpert & the Tijuana Brass', 'Herb Alpert & the Tijuana Brass',
            'Herb Alpert & the Tijuana Brass', 'Herb Alpert & the Tijuana Brass', 'Herb Alpert & the Tijuana Brass',
            'Herb Alpert\'s Tijuana Brass', 'Herbie Hancock', 'Herbie Hancock',
            'Herbie Hancock', 'Herbie Hancock', 'Herbie Hancock', 'Herbie Hancock', 'Herbie Hancock', 'Herbie Hancock',
            'Herbie Hancock', 'Hugh Masekela', 'Idris Muhammad', 'Inside Israel', 'Isaac Hayes', 'Isaac Hayes', 'Isao Tomita',
            'Jack Nitzsche', 'Jan & Dean', 'Jan & Dean', 'Jean-Luc Ponty', 'Jean-Luc Ponty', 'Jerry Butler', 'Jethro Tull',
            'Jethro Tull', 'Jethro Tull', 'Joe Henderson Quintet', 'Joe Hisaishi', 'Joe Jackson', 'Joe Jackson', 'John Abercrombie', 'John Barry',
            'John Barry', 'John Coltrane', 'John Coltrane', 'John Coltrane', 'John Coltrane & Eric Dolphy',
            'John Coltrane Featuring Pharoah Sanders', 'John McLaughlin, John Surman, Dave Holland, Karl Berger, & Stu Martin',
            'Johnny Hammond', 'Johnny Pate', 'Joni Mitchell', 'Joni Mitchell', 'Keith Jarrett', 'King Crimson', 'King Crimson',
            'King Crimson', 'Kitaro', 'Laura Nyro', 'Led Zeppelin', 'Les McCann', 'Les McCann', 'Les McCann & Houston Person',
            'Lijadu Sisters', 'Lilys', 'Little Feat', 'Lonnie Liston Smith and the Cosmic Echoes', 'Los Admiradores',
            'Lynyrd Skynyrd', 'Mahavishnu Orchestra', 'Makaya McCraven', 'Manfred Mann Chapter Three', 'Manfred Mann Chapter Three',
            'Martin Denny', 'Martin Denny', 'Martin Denny', 'Martin Denny', 'Marvin Gaye', 'Marvin Gaye & Tammy Terrell',
            'Masayoshi Takanaka', 'Masayoshi Takanaka', 'Matching Mole', 'McCoy Tyner', 'McCoy Tyner', 'McCoy Tyner', 'Meco',
            'Mike Love & Dean Torrence', 'Mikis Theodorakis', 'Miles Davis', 'Miles Davis', 'Miles Davis', 'Miles Davis',
            'Miles Davis', 'Milton Nascimento', 'Mint Tattoo', 'Minzoso Ya Zaire', 'Mitch Miller and the Gang', 'Mort Garson',
            'Mother 2', 'Motherlode', 'MSPAINT', 'Muzak', 'Neil Young', 'Neil Young', 'Neil Young', 'Neil Young',
            'Neil Young With Crazy Horse', 'Nelson', 'Nelson', 'New Riders of the Purple Sage', 'Nilsson', 'Nino Rota',
            'Noxis / Cavern Womb', 'Obnox', 'Ornette Coleman', 'Osibisa', 'Osiris', 'Parliament', 'Parliament',
            'Passion Fruit', 'Pat Metheny', 'Pat Metheny & Lyle Mays', 'Paul Hardcastle', 'Paul McCartney', 'Paul McCartney',
            'Paul McCartney', 'Peter Green\'s Fleetwood Mac', 'Pharoah Sanders', 'Pharoah Sanders', 'Pharoah Sanders',
            'Prince', 'Ramsey Lewis', 'Ramsey Lewis', 'Ramsey Lewis', 'Return to Forever', 'Return to Forever', 'Ringo Starr',
            'Risk of Rain 2', 'Roberta Flack', 'Ronnie Laws', 'Ronnie Laws', 'Roy Ayers & Wayne Henderson', 'Ruth Brown',
            'Sam Cooke', 'Santana', 'Santana', 'Scorpio Universel', 'Senator Flux', 'Sir Victor Uwaifo (Member of the Order of the Niger)',
            'Sisqo', 'SJ Esau', 'Sly & The Family Stone', 'Sly & The Family Stone', 'Smokey Robinson', 'Smokey Robinson',
            'Soft Machine', 'Soft Machine', 'Soft Machine', 'Soft Machine', 'Sonny Rollins', 'Sopwith Camel', 'Stan Getz & João Gilberto',
            'Stanley Cowell', 'Stanley Cowell Trio', 'Steamboat\'s A-Comin\'', 'Steely Dan', 'Steely Dan', 'Steely Dan',
            'Steely Dan', 'Steely Dan', 'Stereolab', 'Steve Lacy', 'Stevie Wonder', 'Stevie Wonder', 'Stevie Wonder',
            'Stevie Wonder', 'Stevie Wonder', 'Sun Ra and His Arkestra', 'Sun Ra and His Arkestra', 'Taj Mahal',
            'Talking Heads', 'Talking Heads', 'Talking Heads', 'Tears for Fears', 'Terry Riley', 'The 5th Dimension',
            'The Alan Parsons Project', 'The Alkaholiks', 'The Association & Charles Fox', 'The Band', 'The Beach Boys',
            'The Beach Boys', 'The Beach Boys', 'The Beach Boys', 'The Beach Boys', 'The Beach Boys', 'The Beach Boys', 'The Beach Boys',
            'The Beach Boys', 'The Beach Boys', 'The Beach Boys', 'The Beach Boys', 'The Beach Boys', 'The Beatles', 'The Beatles',
            'The Beatles', 'The Beatles', 'The Blackbyrds', 'The Blackbyrds', 'The Byrds', 'The Byrds', 'The Byrds',
            'The Cannonball Adderley Quintet', 'The Cars', 'The Charles Lloyd Quartet', 'The Coasters', 'The Command All-Stars',
            'The Dave Brubeck Quartet', 'The Delfonics', 'The Dells', 'The Doobie Brothers', 'The Electronic Moog Orchestra',
            'The Esso Trinidad Steel Band', 'The Feelies', 'The Flaming Lips', 'The Go-Go\'s', 'The Grateful Dead',
            'The High Llamas', 'The Intruders', 'The Isley Brothers', 'The Isley Brothers', 'The Jimmy Castor Bunch',
            'The Kinks', 'The Kinks', 'The Kinks', 'The Kinks', 'The Love Unlimited Orchestra', 'The Mamas & The Papas',
            'The Mothers', 'The Mothers', 'The Mothers of Invention', 'The Mothers of Invention', 'The Mothers of Invention',
            'The Mothers of Invention', 'The Mothers of Invention', 'The Oak Ridge Boys', 'The Olivia Tremor Control',
            'The Producers', 'The Residents', 'The Residents', 'The Rolling Stones', 'The S.O.S. Band',
            'The Soft Machine', 'The Sopwith Camel', 'The Sound Effects', 'The Spinners', 'The Stark Reality', 'The Supremes',
            'The Supremes', 'The Tornadoes', 'The Turtles', 'The Turtles', 'The Turtles', 'The Two Tons', 'The Who',
            'The Who', 'The Who', 'The Zero Zero Seven Band', 'The Zombies', 'Todd Rundgren', 'Todd Rundgren', 'Utopia',
            'Van Morrison', 'Vangelis', 'Vangelis', 'Various Artists', 'Various Artists', 'Various Artists', 'Various Artists',
            'Various Artists', 'Various Artists', 'Various Artists', 'Various Artists', 'Various Artists', 'Various Artists',
            'Various Artists', 'Various Artists', 'Various Artists', 'Various Artists', 'Various Artists', 'Various Artists', 'Various Artists,' 'Wade Hester', 'Walter Wanderley',
            'Wayne Shorter', 'Wayne Shorter', 'Wayne Shorter', 'Weather Report', 'Weather Report', 'Weather Report', 'Weather Report',
            'Weather Report', 'Weird Al Yankovic', 'Wes Montgomery', 'Wire', 'World Wrestling Federation', 'XTC',
            'Xzibit', 'Yes', 'Zawinul', 'Zumpano'
        ]
        self.albums = [
            '10000gecs','The Ahmad Jamal Trio','Introducing The Akoya Afrobeat Ensemble','Im Still In Love With You','Phallus Dei','Ugetsu','Saturday Night Fiedler','Caribbean Party','King Tubby Meets Rockers Uptown','Soul Searching','Telecommunication','Fowl Play','Do You Know the Way to San Jose','Bee Gees Greatest','Hawaii en Krontjongkelodieën','Symbiosis','The Billy Williams Revue Featuring Billy Williams','Parallel Lines','Hello My Name is Blotto Whats Yours','Across and Down','Barbarella','H','Sign of the Times','Rastaman Vibration','Satin Doll','Head On','Cirrus','Un Poco Loco', 'Happenings', 'San Francisco','The Doughnut in Grannys Greenhouse','Yakety Sax','Bootsy Player of the Year','Strange Man Changed Man','Baby You Got It','The Way-Out Record For Children','Burt Bacharach','Make It Easy On Yourself','Casino Royale','After the Fox','Butch Cassidy and the Sundance Kid','Reach Out','Happy Merry Music','LightWarmPM','Solar Heat','Soul Sauce','Breeze From the East','Secret Omen','Future Days','Monster Movie','The Cannonball Adderley Quintet in San Francisco Featuring Nat Adderley','Unconditionally Guaranteed','The Spotlight Kid','Mirror Man','Strictly Personal','Trout Mask Replica','Tapestry','Writer','Eyes of the Mind','Almost Summer Music from the Original Motion Picture Score','Happy Again  Version Dub','Forest Flower','Shoes of the Fishermans Wife','Wonderland','Mingus Mingus Mingus Mingus Mingus','Changes One','Three or Four Shades of Blues','Charles Mingus and Friends in Concert','Let My Children Hear Music','The Ringer','Delicately','Tiajuana Moods','The Guitar Genius','Hi-Fi in Focus','At Home','Nashville Gold','Half a Love','Chicago IX Chicagos Greatest Hits','Crystal Silence','Chuck Berrys Greatest Hits','Crowd Pleasers','Jupiter Eye','Adventures in Time','Song of Innocence','Low','Me Myself and I Single','Freedom of Choice','Q Are We Not Men A We Are Devo','Moog The Electric Eclectics of Dick Hyman','Electrodynamics','Dimension 7','Make Way For Dionne Warwick','Go With Love','Ill Never Fall in Love Again','Here I Am','The Windows of the World','The Versatile Giant','The Children of Africa','Live in 3⅔4 Time','Live at Monterey','Tears of Joy','Street Lady','Places and Spaces','Stepping Into Tomorrow','The Nightfly','I Remember Yesterday','The Wanderer','Once Upon a Time','Caymmi Também é de Rancho','Cocktails For Two','Duke Ellington & John Coltrane','Fun Under Jamaica Sun','Silent Feet','Dance of Survival','Time','Discovery','Rock of the Westies','Greatest Hits','Goodbye Yellow Brick Road','Emil Dimitrov','Provocative Percussion Vol III','Carlos Erasmo','Out to Lunch','Iron Man','EU Live 2 Places at the Same Time','Da Butt','Wipeout','Freispiel','Cycli Infini','Soundproof','Rumours','Flo & Eddie','Second Sight','WakaJawaka','Apostrophe','Sheik Yerbouti','Over-Nite Sensation','Sleep Dirt','Hot Rats','Bongo Fury','The Teenagers featuring Frankie Lymon','Keep Your Soul Together','Red Clay','Hub-Tones','Straight Life','Cosmic Slop','Under Fire','Playing the Fool','Breezin','A Brazilian Love Affair','Reach For It','1 2 3 4 5 6extet','Pieces of a Man','Midnight Express','Wichita Lineman','The Best of Glen Campbell','By the Time I Get to Phoenix','Galveston','Shafts Big Score','Iapetus','Tche Belew','Yene Mircha','Wede Harer Guzo','Tezeta','The Secret Life of Harpers Bizarre','Mr Lucky','The Music from Peter Gunn','Mr Lucky Goes Latin','More Music From Peter Gunn','Rise','What Now My Love','Whipped Cream & Other Delights','The Beat of the Brass','South of the Border','Going Places','Sounds Like','The Lonely Bull','Greatest Hits','Herb Alperts Ninth','SRO','Volume 2','Feets Dont Fail Me Now','Lite Me Up','Maiden Voyage','Mwandishi','VSOP','Thrust','Head Hunters','Mr Hands','Man-Child','The Boys Doin It','Turn This Mutha Out','The Most Important Record Album Ever Recorded in Israel','To Be Continued','Shaft','Snowflakes Are Dancing','The Lonely Surfer','Command PerformanceLive in Person','The Little Old Lady From Pasadena','Aurora','King Kong Jean-Luc Ponty Plays the Music of Frank Zappa','The Ice Man Cometh','This Was','Thick as a Brick','Aqualung', 'At the Lighthouse: If You\'re Not Part of the Solution, You\'re Part of the Problem', 'Futari Daka Music Selection 2','Night and Day','Joe Jacksons Jumpin Jive','Timeless','Thunderball Soundtrack','Goldfinger Original Motion Picture Score','A Love Supreme','Olé Coltrane','More Lasting Than Bronze','Two Giants Together - Rare Live Performance 1962','Live in Seattle','Where Fortune Smiles','Gamblers Life','Shaft in Africa','Hejira','Mingus','Belonging','Starless and Bible Black','Red','In the Court of the Crimson King','Toward the West','Eli and the Thirteenth Confession','Led Zeppelin','Layers','Hustle to Survive','Road Warriors','Double Trouble','Zero Population Growth Bliss Out Volume 15','Feats Dont Fail Me Now','Visions of a New World','Bongos Bongos Bongos','Pronounced Lĕh-nérd Skin-nérd','Birds of Fire','In These Times','Manfred Mann Chapter Three','Manfred Mann Chapter Three Volume Two','Sayonara','The Very Best of Martin Denny','Primitiva','Quiet Village The Exotic Sounds of Martin Denny','Whats Going On','United','Seychelles','The Rainbow Goblins','Matching Mole','Sahara','Extensions', 'Today and Tomorrow', 'Star Wars and Other Galactic Funk','Listen to the Air','Z','Kind of Blue','Bitches Brew','Water Babies','Miles in the Sky','Jack Johnson Original Soundtrack Recording','Milton','Mint Tattoo','Zaire Folk Pop','Sentimental Sing Along With Mitch','Mother Earths Plantasia','Mother 2 Soundtrack','When I Die','Post-American','New Dimensions Volume 2','Harvest','Trans','Comes a Time','Zuma','Everybody Knows This is Nowhere','The Chief Breakin For 85','We Like It','Powerglide','Son of Schmilsson','The Godfather','Communion of Corrupted Minds','Corrupt Free Enterprise','Ornette On Tenor','Osibisa','Since Before Our Time','Chocolate City','Motor Booty Affair','The Rigga-Ding-Dong-Song','8081','As Falls Wichita So Falls Wichita Falls','Rain Forest','RAM','Band on the Run','McCartney II','Peter Greens Fleetwood Mac','Thembi','Jewels of Thought','Black Unity','Purple Rain','Tequila Mockingbird','Sun Goddess','The In Crowd','Hymn of the Seventh Galaxy','Romantic Warrior','Ringo the 4th','Risk of Rain 2 OST','Killing Me Softly','Pressure Sensitive','Friends & Strangers','Step in to Our Life','Along Comes Ruth','The Best of Sam Cooke','Abraxas','Caravanserai','Map Mandé Courage  ViN Pran Piyay','Spectacles Testacles Wallet & Watch','No Palava - Delicate Lover','Thong Song Remix','Wrong Faced Cat Feed Collapse','A Whole New Thing','Greatest Hits','Smokey','A Quiet Storm','Third','Fourth','Six','Five', 'East Broadway Run Down', 'The Miraculous Hump Returns from the Moon','GetzGilberto','Brilliant Circles','Illusion Suite','Steamboats A-Comin','Aja','Greatest Hits','Cant Buy a Thrill','The Royal Scam','Gold','The Groop Played Space Age Bachelor Pad Music','Epistrophy','Stevie Wonders Journey ThroughThe Secret Life of Plants','My Cherie Amour','Talking Book','Innervisions','Music of My Mind','On Jupiter','Super-Sonic Jazz','The Real Thing','More Songs About Buildings and Food','Remain in Light','Little Creatures','Songs from the Big Chair','A Rainbow in Curved Air','Up Up and Away','Eye in the Sky','21 & Over','Music From The Sound Track Of The Paramount Motion PictureGoodbye Columbus','Stage Fright','Pet Sounds','Sunflower','Smile Sessions','Best of the Beach Boys Vol 2','All Summer Long','Dance Dance Dance','The Beach Boys Love You','High Water','Surfin USA','Holland','15 Big Ones', 'Friends', 'The Beach Boys Greatest Hits 1961-1963', 'Hey Jude','Meet the Beatles','Revolver','Magical Mystery Tour','Action','The Blackbyrds','The Notorious Byrd Brothers','Untitled','Turn Turn Turn','Mercy Mercy Mercy Live atThe Club','The Cars','Journey Within','That Is Rock & Roll','Provocative Percussion','Time Out','The Delfonics','The Mighty Mighty Dells','Minute By Minute','Cinemoog','The Esso Trinidad Steel Band On Tour','Crazy Rhythms','Transmissions from the Satellite Heart','Beauty and the Beat','American Beauty','Here Come the Rattling Trees','The Intruders Are Together','Inside You','3+3','Butt of Course','Golden Hour of the Kinks','Preservation Act 2','Something Else by The Kinks','Lola Versus Powerman and the Moneygoround Part One','Rhapsody in White','If You Can Believe Your Eyes and Ears','The Grand Wazoo','Fillmore East - June 1971','Uncle Meat','Roxy & Elsewhere','Burnt Weeny Sandwich','Absolutely Free','Were Only In It for the Money','Fancy Free','Black Foliage Animation Music Volume 1','The Producers','Meet the Residents','Commercial Album','Let it Bleed','On the Rise','Volume 2','The Sopwith Camel in Hello Hello','Cross Country','The Best of Spinners','Discovers Hoagy Carmichaels Music Shop','Where Did Our Love Go','More Hits by The Supremes','The Original Telstar The Sounds of the Tornadoes','Happy Together Again The Turtles Greatest Hits','Happy Together','The Best of The Turtles','Backatcha','The Who Sell Out','Tommy','Whos Next','James Bond Thrillers','Odessey and Oracle','A Wizard a True Star','Back to the Bars','Swing to the Right','Moondance','China','Albedo 039','Nalle Puh','Dynamite Doo Wopps Volume 1','Gotta Lot of Booty','Jazz Super Hits Vol 2','Dias Felices','Esta Es Mi Tierra','Nutty Numbers','Goofy Greats','Dr Dementos Delights','WAVA FM 105 Washington Rocks','Tunes for Teens','Motown Superstars Sing Motown Superstars','I Like Jazz','Eccentric Soul The Bandit Years','Good Old Days 4 1963-64', 'The Motown Sound Vol. 5', 'The Motown Sound Vol. 6', 'Nocahoma Murphy','Rain Forest','Super Nova','Schizophrenia', 'The All Seeing Eye', 'Sweetnighter','Mr Gone','Black Market','Mysterious Traveler','Heavy Weather','Weird Al Yankovic In 3D','Movin Along','Kidney Bingos','The Wrestling Album','Black Sea','Hey Now Mean Muggin','Fragile','Zawinul','Goin Through Changes'
        ]
        # Create and pack widgets
        self.create_widgets()

    def create_widgets(self):
        # Entry widget for search
        self.search_entry = tk.Entry(self.root, width=50)
        self.search_entry.pack(pady=10)
        self.search_entry.bind('<KeyRelease>', self.update_list)

        # Listbox to display results
        self.result_listbox = tk.Listbox(self.root, width=80, height=20)
        self.result_listbox.pack(pady=10)

        # Button to select a random entry
        self.random_button = tk.Button(self.root, text="Select Random Entry", command=self.select_random_entry)
        self.random_button.pack(pady=10)

        # Populate listbox with initial records
        self.update_list()

    def update_list(self, event=None):
        # Get search term
        search_term = self.search_entry.get().lower()
        
        # Clear the listbox
        self.result_listbox.delete(0, tk.END)
        
        # Add matching records to the listbox
        for artist, album in zip(self.artists, self.albums):
            if search_term in artist.lower() or search_term in album.lower():
                self.result_listbox.insert(tk.END, f"{artist}: {album}")

    def add_record(self, artist, album):
        self.artists.append(artist)
        self.albums.append(album)
        self.update_list()

    def remove_record(self, index):
        if 0 <= index < len(self.artists):
            del self.artists[index]
            del self.albums[index]
            self.update_list()
        else:
            messagebox.showerror("Error", "Invalid index")

    def select_random_entry(self):
        if self.artists and self.albums:  # Ensure there are records to choose from
            index = random.randint(0, len(self.artists) - 1)
            artist = self.artists[index]
            album = self.albums[index]
            messagebox.showinfo("Random Record", f"{artist}: {album}")
        else:
            messagebox.showwarning("No Records", "No records available to select.")

# Create the main window
root = tk.Tk()
app = RecordSearchApp(root)
root.mainloop()