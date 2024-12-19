phonebook={}

def add_contact(name,number):
    phonebook[name]=number
    print(f"\n{name} has been added in the phonebook.\n")
    
def del_contact(name):
    if name in phonebook:
        del phonebook[name]
        print(f"{name} has been deleted.\n")
    
    else:
        print(f"{name} not found\n")    
        
def search_contact(name):
    if name in phonebook:
        print(f"NAME:{name}, Phone:{phonebook[name]}\n")
    else:
        print(f"{name} not found.\n")  
        
def display_contacts():
    if not phonebook:
        print("phonebook is empty.\n")
        return
    else:
        print("\nAll Contacts")
        print("-"*30)
        for name,number in phonebook.items():
            print(f"Name:{name}, Phone:{phonebook[name]}\n")
        print("-"*30)   

def sort_contacts():
    if not phonebook:
        print("phonebook is empty.\n")
        return
    else:
        print("\nAll Contacts")
        print("-"*30)
        for name,number in sorted(phonebook.items()):
            print(f"Name:{name}, Phone:{phonebook[name]}\n")
        print("-"*30)        
        
def main():
    while True:
        print("Welcome to your phonebook.")
        print("1.Add/update contact")
        print("2.Delete contact")
        print("3.Search contact")
        print("4.Display contacts")
        print("5.Sort contacts") 
        print("6.Exit")   
        
        choice=input("Enter your choice(1-6):\n")   
        
        if choice=='1':
            name=input("\nEnter contact name:") 
            number=input("\nEnter the number:") 
            add_contact(name,number)     
        
        elif choice=='2':
            name=input("\nEnter contact name:") 
            del_contact(name)
            
        elif choice=='3':
            name=input("\nEnter contact name:") 
            search_contact(name)
        elif choice=='4':
            display_contacts()
        elif choice=='5':
            sort_contacts()
        elif choice=='6':
            print("\nExited")
            break    
            
        else:
            print("Invalid choice pick again.")            
                 
if __name__ == "__main__":
    main()         
                       
                
    
