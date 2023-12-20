import os

def RemoveFileExtension(FileName):
    position = FileName.rfind('.')
    if position != -1:
        OnlyFileName = FileName[:position]
    else:
        OnlyFileName = FileName
    return OnlyFileName

def RemoveFileExtensionForArray(FileArray):
    return [RemoveFileExtension(file) for file in FileArray]

path = "C:/Users/RA/Desktop/github clones/drone_comp/data/images/train"
to_remain = "C:/Users/RA/Desktop/github clones/drone_comp/data/jsons"

target_files = os.listdir(path)
lookup_files = os.listdir(to_remain)

count = 0

for i in range(len(target_files)):
    check_file = target_files[i]
    if RemoveFileExtension(check_file) not in RemoveFileExtensionForArray(lookup_files):
        count = count + 1
        path_to_file = os.path.join(path, check_file)
        os.remove(path_to_file)

print(f"Total files without JSON: {count}")
