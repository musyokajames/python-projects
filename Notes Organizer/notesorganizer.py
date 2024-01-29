
from notes import Notes

class NotesOrganizer:
    def __init__(self):
        self.notes = []
        self.categories = {
            'PERSONAL_NOTES' : [],
            'IDEAS' : [],
            'TO-DO_LIST' : [],
            'RANDOM_THOUGHTS' : [],
            'UNCATEGORIZED' : []
        }
            
            

    def add_notes(self,title,content,category):
        notes = Notes(title,content,category)
        self.notes.append(notes)
        if category in self.categories:
            self.categories[category].append(notes)
            
        else:
            self.categories['UNCATEGORIZED'].append(notes)

        return notes
       
        

    def view_notes(self):
        for categories,notes_list in self.categories.items():
            print(f"{categories}")
            for note in notes_list:
                print(note)

    def edit_notes(self,title,content,new_title,new_content,category,new_category):
        pass

            
            





def main():
    system = NotesOrganizer()

    while True:
        print("NOTES ORGANIZER")
        print("1.ADD NOTES")
        print("2.VIEW NOTES")
        print("3.EDIT NOTES")
        print("4.DELETE NOTES")
        print("5.SEARCH NOTES")
        
        print("6.EXIT")



        choice = input("Enter your choice: ")

        if choice == '1':
            print("FOLDERS")
            print("----------")
            print("1. Personal Notes")
            print("2. Ideas")
            print("3. To-do Lists")
            print("4. Random Thoughts")
            print("5. Add Category")
            category = input("Enter Category:")
            title=input("Enter Title:")
            content = input("Enter Content:")

            notes=system.add_notes(title,content,category)

            if category == '1':
                system.categories['PERSONAL_NOTES'].append(notes)
                
            elif category == '2':
                system.categories['IDEAS'].append(notes)
                
            elif category == '3':
                system.categories['TO-DO_LIST'].append(notes)
                
                
            elif category == '4':
                system.categories['RANDOM_THOUGHTS'].append(notes)
                
            elif category == '5':
               pass
            else:
                print("Invalid Category!Try Again:)")

        elif choice == '2':
            system.view_notes()

        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '5':
            pass


        elif choice == '6':
            print("EXITING...")
            break
        
        else:
            print("Invalid Input!Try Again:)")




if __name__ == "__main__":
    main()