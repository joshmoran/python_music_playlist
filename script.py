import sys
# Global variables 
name = '' 
addingTo = []
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
          searchInitial( 'track' )
        elif testInput == 2:
          searchInitial( 'artist' )
        elif testInput == 3:
          searchInitial( 'album' )
        elif testInput == 4:
          searchInitial( 'genre' )
        elif testInput == 5:
          searchInitial( 'all' )
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
  print('Add an item')
  print('')
  print('We will need these details:')
  print('1. Track name')
  print('2. Artist name')
  print('3. Album name')
  print('4. Genre')
  print('')
  addingMenu( 0, '' )


def addingMenu( workingNo, item='' ):
  
  if item != '':
    addingTo.append(item)

  if workingNo == 0:
    print('What is the track name')
    entry = validateAdd( workingNo )
    print(entry)
  elif workingNo == 1:
    print('What is the artists name')
    validateAdd( workingNo )
  elif workingNo == 2: 
    print('What is the albums name')
    validateAdd( workingNo )
  elif workingNo == 3:
    print('What is the genre')
    validateAdd( workingNo )
  elif workingNo == 4:
    playlist.append( {
      'artist': addingTo[0],
      'album': addingTo[1],
      'track': addingTo[2],
      'genre': addingTo[3]
    })
    current = []
    print('Successfully added to the playlist')
    validateAnyInput( amendMenu, 'amend menu') 

def validateAdd( workingNo ):
  running = True
  while running:

    testInput = input('>>> ')
    print('')

    if len(testInput) > 2:
      addingMenu(workingNo + 1 , testInput )
      running = False
    else:
      print('Please enter a string longer than 2 characters')
      validateAdd(workingNo)

def remove():
  print('remove')

def update():
  print('update')

def searchInitial( byWhat ):
  print('')
  print('Please enter what you want to search for')
  search(byWhat)

def search( byWhat ):
  running = True 
  print('')
  while running:
    testInput = input('>>> ')

    if len(testInput) > 2:
      if byWhat != 'all':
        searchItems( byWhat, testInput)
      else: 
        searchAll( testInput )
    else:
      print('Please enter a sentence over 2 characters ')
      search( byWhat )

def searchItems( byWhat, searchFor ):
  itemsFound = [] 
  correct = False
  lowered = searchFor.lower() 
  print('')
  for item in playlist:
    itemField = item[ byWhat ].lower()
    if lowered in itemField:
      correct = True
      print(item['track'] + ' --- ' + item['artist'] + ' --- ' + item['album'] + ' --- ' + item['genre'])
  if not correct:
    print('No items found ')
  validateAnyInput(searchMenu, 'search menu')

def searchAll( searchingFor ):
  lowered = searchingFor.lower()
  newList = []

  for item in playlist:
    for key, value in item.items():
      if lowered in value.lower():
        newList.append( item['track'] + ' --- ' + item['artist'] + ' --- ' + item['album'] + ' --- ' + item['genre'])
        break
  if len(newList) > 0:
    print('Track    ---     Artist     ---    Album     ---    Genre')
    print('-------------------------------------------------------------')
    for entry in newList:
      print(entry)
  else:
    print('')
    print('No items found')
  validateAnyInput(searchMenu, 'search menu')

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

add()

