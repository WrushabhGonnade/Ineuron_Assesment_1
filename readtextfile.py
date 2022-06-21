# 1. Create a function in python to read the text file and replace specific content of the file.


with open('example.txt', 'w') as f:
    f.write('This is a placement assignment')

def read_text(file):
    file1=open(file,'rt')
    data=file1.read()
    data=data.replace('placement','screening')
    file1.close()
    
    file1=open(file,'wt')
    file1.write(data)
    file1.close()
    
read_text('example.txt')
