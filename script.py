import sys
# Global variables 
name = '' 
playlist = [
  { 'artist': 'Psyconaut 4', 'album': 'Dipsoma', 'track': 'Personal Forest', 'genre': 'Depressive Black Metal'},
  { 'artist': 'Nyktalgia', 'album': 'Peisanthesis', 'track': 'Peisanthesis', 'genre': 'Black Metal'},
  { 'artist': 'Slayer', 'album': 'Welcome to Hell ', 'track': 'Raining Blood', 'genre': 'Thrash Metal'}  
]

def init():
  print('')
  print('What is your name')
  print('')
  while True:
    username = input('>>> ')

    if len(username) >= 4 and isinstance(username, str):
      name = username
      print('')
      print(f"Hello, {name}")
      print('')
      mainMenu()
      return False
    else: 
      print('')
      print('Please enter your name')
      print('')
    

def mainMenu():
  print('Welcome to the main menu')
  print('')
  print('1. Amend')
  print('2. Search')
  print('3. List')
  print('4. Exit ')
  print('')
  print('Pick an option ')
  mainMenuValidate()

def mainMenuValidate():
  running = True

  while running:
    testInput = int( input('>>> ') )

    try:
      if testInput in range(1,5,1):
        if testInput == 1:
          amendMenu()
        elif testInput == 2:
          searchMenu()
        elif testInput == 3:
          listMenu()
        elif testInput == 4:
          print('')
          print('Exiting now')
          print('')
          sys.exit()
        running = False 
      else:
        print('')
        print('Pick a valid number')
        mainMenuValidate()
    except ValueError:
      print('')
      print('Please enter a number')
      mainMenuValidate()
      
def amendMenu():
  print('')
  print('Make changes menu')
  print('')
  print('1. Add')
  print('2. Remove')
  print('3. Update')
  print('4. Back to main menu ')
  print('')
  print('Pick an option')
  amendMenuValidate()

def amendMenuValidate():
  running = True 

  while running:
    testInput =int( input('>>> ') )

    try:
      if testInput in range(1,5,1):
        if testInput == 1:
          print('Adding an entry')
          add()
        elif testInput == 2:
          print('Removing an entry')
          remove()
        elif testInput == 3:
          print('Updating an entry')
          update()
        elif testInput == 4:
          mainMenu()
        running = False
      else:
        print('')
        print('Enter a valid number')
        amendMenuValidate()
    except ValueError:
      print('')
      print('Please enter a number')
      amendMenuValidate()
    
def searchMenu():
  print('')
  print('Search menu')
  print('')
  print('1. By track')
  print('2. By artist')
  print('3. By album')
  print('4. By genre')
  print('5. All fields')
  print('6. Back to main menu ')
  print('')
  print('Pick an option ')
  searchMenuValidate()

def searchMenuValidate():
  running = True 

  while running:
    testInput = int( input('>>> '))

    try:
      if testInput in range(1,7,1):
        if testInput == 1:
          searchTrack()
        elif testInput == 2:
          searchArtist()
        elif testInput == 3:
          searchAlbum()
        elif testInput == 4:
          searchGenre()
        elif testInput == 5:
          searchAll()
        elif testInput == 6: 
          mainMenu()
        running = False
      else:
        print('')
        print('Pick a valid number')
        searchMenuValidate()
    except ValueError:
      print('')
      print('Please enter a number')
      searchMenuValidate()

def listMenu():
  print('')
  print('List menu')
  print('')
  print('1. Show tracks')
  print('2. Show artists')
  print('3. Show albums')
  print('4. Show genres')
  print('5. Show all ')
  print('6. Back to main menu ')
  print('')
  print('Pick an option ')
  listMenuValidate()

def listMenuValidate():
  running = True 

  while running:
    testInput = int(input('>>> '))
    print('')
    
    try:
      if testInput in range(1,7,1):
        if testInput == 1:
          showInitial( showTracks, 'tracks')
        elif testInput == 2:
          showInitial( showArtists, 'artists')
        elif testInput == 3:
          showInitial( showAlbums, 'albums')
        elif testInput == 4:
          showInitial( showGenres, 'genres')
        elif testInput == 5:
          showInitial( showAll, 'all fields')
        elif testInput == 6:
          mainMenu()
        running = False
      else:
        print('Enter a valid number')
        amendMenuValidate()
    except ValueError:
      print('Please enter a number')
      listMenuValidate()

def add():
  print('add')

def remove():
  print('remove')


def update():
  print('update')


def searchTrack():
  print('search treac')


def searchArtist():
  print('search artist')

def searchAlbum():
  print('search album')

def searchGenre():
  print('search genre')


def searchAll(): 
  print('search all ')


def showInitial( destination, caption ):
  print('')
  print(f"Showing all {caption}")
  print('')
  destination() 

def showTracks():
  print('Tracks')
  print('-------')
  new = []
  for item in playlist:
    new.append(item['track'] )
  toPrint = sorted(new, key=str.lower)
  for i in toPrint:
    print(i)
  print('')
  print(f"Returning to the list menu")
  validateAnyInput( listMenu, 'list menu' )

def showArtists():
  print('Artist')
  print('-------')
  new = []
  for item in playlist:
    new.append(item['artist'] )
  toPrint = sorted(new, key=str.lower)
  for i in toPrint:
    print(i)
  print('')
  print(f"Returning to the list menu")
  validateAnyInput( listMenu, 'list menu' )

def showAlbums():
  print('Albums')
  print('-------')
  new = []
  for item in playlist:
    new.append(item['album'] )
  toPrint = sorted(new, key=str.lower)
  for i in toPrint:
    print(i)
  print('')
  print(f"Returning to the list menu")
  validateAnyInput( listMenu, 'list menu' )

def showGenres():
  print('Genres')
  print('-------')
  new = []
  for item in playlist:
    new.append(item['genre'] )
  toPrint = sorted(new, key=str.lower)
  for i in toPrint:
    print(i)
  print('')
  print(f"Returning to the list menu")
  validateAnyInput( listMenu, 'list menu' )

def showAll():
  print('Track    ---     Artist     ---    Album     ---    Genre')
  print('-------------------------------------------------------------')
  for item in playlist:
    print(item['track'] + ' --- ' + item['artist'] + ' --- ' + item['album'] + ' --- ' + item['genre'])
  print('')
  print(f"Returning to the list menu")
  validateAnyInput( listMenu, 'list menu' )

def validateAnyInput( move_to, name_of ):
  print('')
  print('Press any key to continue ')
  running = True
  
  while running: 
    testInput = input('>>> ')

    if len(testInput) > 0:
      move_to()
      running = False
    else:
      validateAnyInput( move_to, name_of )

listMenu()

