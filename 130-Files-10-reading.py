f = open("130-Files-10-data.txt", "r")
print(f"File mode is '{f.mode}'")

print(f"Current File reader position: {f.tell()}")
file_contents = f.read()
print(f"Content: {file_contents}")
print(f"Current File reader position: {f.tell()}")

print(f"Reading the file again when file position is at EOF: '{f.read()}'")

f.seek(0)
count = 10
while True:
    data = f.read(count)
    print(f"Read: '{data}' => file poistion is at {f.tell()}")
    datalength = len(data)
    if (datalength < count):
        # EOF is indicated when read data length < count.
        print("EOF reached. Exiting")
        break


f.seek(0)
print("Read one line at a time:")
print("========================")
print(f"First Line:  '{f.readline()}'")
print(f"Second Line: '{f.readline()}'")
print(f"Third Line:  '{f.readline()}'")
print(f"Fourth Line:  '{f.readline()}'")

f.close()

print("Demo: Automatic File closing using 'with open' keyword")
print("======================================================")
with open("130-Files-10-data.txt") as f:
    print(f"Is file closed? {f.closed}")        # FALSE => as we are inside "with" block
    print(f"File content: '{f.read()}'")
print(f"Is file closed? {f.closed}")            # TRUE => as we are outside "with block"


print("DEMO: file writing")
print("==================")
with open("130-Files-10-data2.txt", "w") as f2:
    f2.write("Python is a very friendly language. Easy to Learn.\n")
    f2.write("C is powerful but not that friendly. It is RAW.")
with open("130-Files-10-data2.txt", "r") as f2:
    print(f"Data from file 2: '{f2.read()}'");


print("DEMO: Binary files")
print("==================")
with open("130-Files-10-dog.jpg", "rb") as dog_picture:
    dog_picture.seek(10)
    dog_picture.read(4)
    print(f"File poistion: {dog_picture.tell()}")
    print(f"File mode is {dog_picture.mode}")


# Install pillow package, which is a fork of PIL (Python Image Library)
import PIL
im = PIL.Image.open("130-Files-10-dog.jpg")
im.show()

