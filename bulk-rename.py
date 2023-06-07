import sys
import os
import shutil

# Check if the user has put in enough arguements
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 bulk-rename.py [filepath/]")
    else:
        source_path = sys.argv[1]

        # uses a function to check validity of the filepath given.
        if os.path.isdir(source_path):
            new_path = new_pathing()

            # gives a source and destination to file copy from and to
            # First it sets doc and img_num to 0, which can be used to order and number the documents 
            doc_num = img_num = 0
            for file_name in os.listdir(source_path):
                source_file = (source_path + file_name)

                # Then we check if its either a JPG or a text document, if it's a recognized format, it will add one to either counter. Otherwise it'll skip over.
                # Change this into a function me
                if source_file.endswith(".txt"):
                    tail = ".txt"
                    new_name = "Document" + str(doc_num) + tail
                    doc_num += 1

                elif source_file.endswith(".jpg"):
                    tail = ".jpg"
                    new_name = "Image" + str(img_num) + tail
                    img_num += 1

                # New full filepath as a string.
                new_full = new_path + "/" + new_name

                # Copy only files
                if os.path.isfile(source_file):
                    shutil.copyfile(source_file, new_full)

        else:
            print(source_path, "is not a Folder.")

def new_pathing():
    # Make a new directory that the user can name
    new_path = input("Input a new file name: ")
    new_path = os.path.join(new_path)
    os.mkdir(new_path)
    return new_path

main()
