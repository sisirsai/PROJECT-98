def swapper():
  file_1 = input('Enter the path of first file\n')
  file_2 = input('Enter the path of second file\n')
  with open(file_1,'r') as a:
    data_1 = a.read()
  with open(file_2,'r') as a:
    data_2 = a.read()
  with open(file_1,'w') as a:
    a.write(data_2)
  with open(file_2,'w') as a:
    a.write(data_1)
  print('Now the data in the files is swapped.')
  print('Go and cheak')
swapper()