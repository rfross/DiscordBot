def handleResponse(message) -> str:
  p_message = message.lower()

if p_message.begins('~'):
  if p_message.contains('create preseason'):
    # do randomization function
    return schedule

  if p_message.contains('head to head'):
    # read player head to head record
    return record

  if p_message.contains('vote'):
    # record votes in documents
    return 'Vote is recorded'

  if p_message.contains('winner'):
    # total heisman votes and output winner
    return winner

  return 'I don't recognize that command'
