import sys

filename = sys.argv[1]
number = int(sys.argv[2])

for i in range(number):
    print('    <p style="font-size:10px;"> ![{}](./JPG/{}/{}_{}.jpg) </p>'.format(i, filename, filename, i))
    print('    <img src="./JPG/{}/{}_{}.jpg" alt="Oops GG" width="100%" height="100%"><br>'.format(filename, filename, i))
