import shutil
'''
FOR TRIAL PURPOSE;
enter first file as f1.txt,
second file as f2.txt,
and destination file as merged.txt
'''
file1 = input("Enter the name of first file: ")
file2 = input("Enter the name of second file: ")
destination = input("Enter the name of destination file: ")

with open(destination, 'wb') as d:
    for files in (file1, file2):
        with open(files, 'rb') as f:
            shutil.copyfileobj(f, d)

check = open(destination, 'r')
print(check.read())
check.close()
