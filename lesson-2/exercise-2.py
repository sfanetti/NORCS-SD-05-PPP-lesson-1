def manyParams(**kwargs):
  strings = []
  numeric = []
  other = []
  for i in kwargs.values():
    if type(i) == str:
      strings.append(i)
    elif type(i) == int or type(i) == float:
      numeric.append(i + 3)
    else:
      other.append(i)  
	
  return strings, numeric, other