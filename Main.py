
from Command import *

class Main:
    commands = {
        'p': 'CommandPeople',
        'l': 'CommandList',
        's': 'CommandShelf',
        'a': 'CommandAdd',
        'd': 'CommandDelete',
        'm': 'CommandMove',
        'as': 'CommandAddShelf'
    }
    keepRunning = True
    documents = []
    directories = {}
    currentCommand = None
    
    def __init__ (self, documents=[], directories={}):
        self.documents = documents
        self.directories = directories
    
    def run (self):
        while self.keepRunning:
            answer = input('Enter command: ')
            
            if answer == 'q':
                self.keepRunning = False
                continue

            if answer not in self.commands.keys():
                print('Unknown command')
            else:
                get_class = globals()[self.commands[answer]]
                self.currentCommand = get_class(self.documents, self.directories)
                (self.documents, self.directories) = self.currentCommand.run()
                print(self.documents)
                print(self.directories)