def file_len(fname):
  i = 0
  with open(fname) as f:
    for i, l in enumerate(f, i):
      pass
  return i

def parse_to_lists(fname):
  parsed_map = []
  map_file = open(fname)
  for i in range(file_len(fname)+1):
    line = map_file.readline()
    parsed_map.append(list(line.rstrip()))
  return parsed_map
