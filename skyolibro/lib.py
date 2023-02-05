def doesContainWord(mode, word, str):
  if mode == "begin":
    if str.startswith(word) == True:
      output = True
    else:
      output = False
  if mode == "anywhere":
    if word in str:
      output = True
    else:
      output = False
  if mode == "end":
    if str.endswith(word) == True:
      output = True
    else:
      output = False
  return output