import numpy as np

def handleResponse(message) -> str:
  p_message = message.lower()

  if p_message[0] == '~':
    if p_message.__contains__('create preseason'):
      # do randomization function
      return schedule

    if p_message.__contains__('head to head'):
      message = p_message.split(' ')[1:]
      if p_message.__contains__('display') or p_message.__contains__('show'):
        record = readRecord(message)
        return record
      else if p_message.__contains__('update')
        record = updateRecord(message)
        return record
      else if p_message.__contains__('add')
        addRecord(message)
        return 'Added new head to head matchup'

    if p_message.__contains('user'):
      user = p_message.split(' ')[2:]
      if p_message.__contains__('add'):
        addUser(user)
        return 'Added user %s to player list' %user
      else if  p_message.__contains__('remove')
        removeUser(user)
        return 'Removed user %s from player list' %user

    if p_message.__contains__('vote'):
      recordVote(p_message)
      return 'Vote is recorded'

    if p_message.__contains__('winner'):
      winner = totalVotes()
      return winner

    if p_message.__contains__('reset'):
      newSeason()
      return 'Heisman ballot is reset for a new year!'

    return 'I don't recognize that command'

#=========================================
# Function to record Heisman Votes
# Syntax: ~Heisman Vote [player name] [school]
#=========================================

def recordVote(message):
  ballot = open("HeismanVoting.txt","a")
  voteName = message.split(' ')[1:]
  ballot.write(voteName)
  ballot.close()

  return

#=========================================
# Function to output Heisman winner
# Syntax: ~Heisman Winner
# ========================================

def totalVotes() -> str:
  ballot = open("HeismanVoting.txt","r")
  names = ballot.readlines()
  results = np.unique(names, return_counts=True)
  winner = results[0][max(enumerate(results[1]),key=lambda x: x[1])[0]]
  winner = winner.title()  
  ballot.close()

  return winner

#========================================
# Function to reset Heisman voting
# Syntax: ~reset
#========================================
  
def newSeason():
    open("HeismanVoting.txt","w").close()
    return

#=========================================
# Function to output Head to Head records
# Syntax (all): ~Show Head to Head
# Syntax (specified): ~Show Head to Head [user1] [user2]
#=========================================

def readRecord(message) -> str:
  history = open("HeadToHead.txt","r")
  # find matchup, return line
  return record

#========================================
# Function to update Head to Head records
# Syntax: ~Update Head to Head [winning user] [losing user]
#========================================

def updateRecord(message) -> str:
  history = open("HeadToHead.txt","r+")
  #find matchup, determine new w/l, return line
  return

#=======================================
# Function to add new Head to Head match-up
# Syntax: ~Add Head to Head [user1] [user2]
#=======================================

def addRecord(message) -> str:
  matchup = message[0]+' vs. '+message[1]
  history = open("HeadToHead.txt","r")
  # attempt to find matchup
  history.close()
  if (foundMatchup):
    return 'Matchup already exists in records, did you mean to use the "~Update head to head" command?'
  else:
    history = open("HeadToHead.txt","a")
    matchup = message[0]+' vs. '+message[1]+' 0 - 0'
    history.write(matchup)
    history.close()
    
  return 'Added new head to head matchup'

  #=====================================
  # Function to add new user to player list
  # Syntax: ~Add [user name] [school]
  #=====================================

  def addUser(user):

    return

  #=====================================
  # Function to remove users from player list
  # Syntax: ~Remove [user name]
  #=====================================

  def removeUser(user):

    return
