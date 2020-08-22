import registry, shortcuts
import applicationhandle as app

matchNames = matchDirs = []
uInput = ""
directory = names = []

def filterName_Dir(names, directories):
    f_names = []
    f_directories = []
    global uInput
    track_index = 0
    while track_index < len(names):
        name = names[track_index]
        directory = directories[track_index]
        if name.lower().find(uInput.lower()) > -1:
            f_names.append(name)
            f_directories.append(directory)
        track_index += 1
    return f_names, f_directories

def immenseFilter(names, directories):
    global uInput
    final_name = ''
    final_dir = ''
    a_acc = None
    index = 0
    for name in names:
        accuracy = len(name) - len(uInput)
        if a_acc == None:
            a_acc = accuracy
            final_name = name
            final_dir = directories[index]
        elif a_acc > accuracy:
            a_acc = accuracy
            final_name = name
            final_dir = directories[index]
        
        index += 1
    return final_name, final_dir



def inputFromUser(userInput):
    global uInput, names, directory
    uInput = userInput
    r_names, r_directory = registry.giveAllData()
    s_names, s_directory = shortcuts.giveAllData()
    #print(len(r_names), len(r_directory), len(s_names), len(s_directory))
    
    filter_names, filter_directory = filterName_Dir(s_names, s_directory)
    
    '''for index in range(len(filter_names)):
        print("{} | {}".format(filter_names[index], filter_directory[index]))
        '''

    if len(filter_names) > 1:
        filter_name, filter_directory = immenseFilter(filter_names, filter_directory)
        app.openApplication(filter_name, filter_directory)
    elif len(filter_names) == 1:
        app.openApplication(filter_names[0], filter_directory[0])
        
    else:
        filter_names, filter_directory = filterName_Dir(r_names, r_directory)
        if len(filter_names) > 1:
            filter_name, filter_directory = immenseFilter(filter_names, filter_directory)
            app.openApplication(filter_name, filter_directory)
        elif len(filter_names) == 1:
            app.openApplication(filter_names[0], filter_directory[0])
            
        else:
            print("Unable to find the application.")
            



