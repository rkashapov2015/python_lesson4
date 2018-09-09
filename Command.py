class Command:
    documents = []
    directories = {}
    numberDocument = None

    def __init__(self, documents, directories):
        self.documents = documents
        self.directories = directories

    def run(self):
        return (self.documents, self.directories)

    def searchDocumentByNumber(self):
        if len(type(self.documents) != list or self.documents) == 0:
            return False
        for doc in self.documents:
            if doc['number'] == self.numberDocument:
                return doc
        return False
    
    def searchShelfByNumberDocument(self):
        if type(self.directories) != dict:
            return False
        for shelfKey in self.directories.keys():
            if self.numberDocument in self.directories[shelfKey]:
                return shelfKey
        return False
    
    def deleteDocument(self):
        doc = self.searchDocumentByNumber()
        if doc != False:
            self.documents.remove(doc)
        else:
            return False
        
        numberShelf = self.searchShelfByNumberDocument()
        if numberShelf != False:
            self.directories[numberShelf].remove(self.numberDocument)
        else:
            return False

        return True
        
    
class CommandPeople(Command):
    def run(self):
        self.numberDocument = input('Enter number document: ')
        result = self.searchDocumentByNumber()
        if result != False:
            print(result['name'])
        else:
            print('Document not found')

        return super().run()
        
class CommandList(Command):
    def run(self):
        if type(self.documents) == list:
            for doc in self.documents:
                print(f"{doc['type']} {doc['number']} {doc['name']}")

        return super().run()
        
class CommandShelf(Command):
    def run(self):
        self.numberDocument = input('Enter number document: ')
        result = self.searchShelfByNumberDocument()

        if result != False:
            print(result)
        else:
            print('Shelf not found')
        return super().run()

class CommandAdd(Command):
    def run(self):
        newDocumentNumber = input('Enter number for new document: ')
        newDocumentType = input('Enter type for new document: ')
        newDocumentName = input('Enter name Owner for new document: ')
        newDocumentShelf = input('Enter number shelf for new document: ')

        newDocument = {'type': newDocumentType, 'number': newDocumentNumber, 'name': newDocumentName}

        self.documents.append(newDocument)
        if newDocumentShelf not in self.directories.keys():
            self.directories[newDocumentShelf] = list()

        self.directories[newDocumentShelf].append(newDocumentNumber)

        print(f'New document {newDocumentNumber} created')

        return super().run()

class CommandDelete(Command):
    def run(self):
        self.numberDocument = input('Enter number document: ')
        doc = self.searchDocumentByNumber()

        if doc != False:
            if self.deleteDocument() == True:
                print(f'Document {self.numberDocument} has been deleted')
            else:
                print('An error occurred while deleting the document')
        else:
            print('Document not found')
        return super().run()

class CommandMove(Command):
    def run(self):
        self.numberDocument = input('Enter number document: ')
        numberShelf = input('Which shelf do you want to transfer: ')
        
        doc = self.searchDocumentByNumber()
        if doc != False:
            currentNumberShelf = self.searchShelfByNumberDocument()
            if numberShelf == currentNumberShelf:
                print('Document right now here')
            else:
                self.directories[currentNumberShelf].remove(self.numberDocument)

                if numberShelf not in self.directories.keys():
                    self.directories[numberShelf] = list()

                self.directories[numberShelf].append(self.numberDocument)
                print('Document moved')
        else:
            print('Document not found')
        return super().run()

class CommandAddShelf(Command):
    def run(self):
        numberShelf = input('Enter number new shelf: ')
        
        if numberShelf in self.directories.keys():
            print('Shelf is exist')
        else:
            self.directories[numberShelf] = list()
            print(f'Shelf {numberShelf} has been added')

        return super().run()
