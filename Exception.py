try:
  f = open(r"demofile.txt", 'w')
  f.write("Ishan Mitra")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()
