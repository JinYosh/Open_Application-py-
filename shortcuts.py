import os

shortcut_links_names = []
shortcut_links_dirs = []

shortcuts_dir = ["C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\", "C:\\Users\\%username%\\Desktop\\", "C:\\Users\\%username%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\"]
#shortcuts_dir = ["C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\"]
def getAllShortcuts(directory):
    global shortcut_links_names, shortcut_links_dirs
    list_all_file = os.listdir(directory)

    for file_or_dir in list_all_file:
        if file_or_dir != "desktop.ini":
            try:
                if os.path.isfile(directory + file_or_dir):
                    if file_or_dir.find(".lnk") > -1 or file_or_dir.find(".exe") > -1:
                        if file_or_dir not in shortcut_links_names:
                            shortcut_links_names.append(file_or_dir)
                            shortcut_links_dirs.append(directory)
                            #print(file_or_dir)
                else:
                    temp_directory = directory + file_or_dir + "\\"
                    getAllShortcuts(temp_directory)
            except Exception as e:
                print("Error: ",e)

def evaluateLinks():
    global shortcuts_dir
    new_list = []
    for link in shortcuts_dir:
        temp_link = "echo " + link
        data = os.popen(temp_link).read()
        data = data.replace('\n', "")
        new_list.append(data)
    return new_list

def giveAllData():
    global shortcut_links_dirs, shortcut_links_names
    shortcuts_dir = evaluateLinks()
    for link in shortcuts_dir:
        getAllShortcuts(link)
    return (shortcut_links_names, shortcut_links_dirs)

if __name__ == "__main__":
    names, dirs = giveAllData()
    index = 0 
    while index < len(dirs):
        print(names[index]+" | " +dirs[index])
        index += 1

