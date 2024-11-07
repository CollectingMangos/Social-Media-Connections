import networkx as nx
import matplotlib.pyplot as plt

class ConnectionsManager:
    def __init__(self):
        self.graph = nx.Graph()

    def addUser(self, username):
        self.graph.add_node(username)
        print(f'User {username} added.')

    def addConnection(self, user1, user2):
            if user1 in self.graph.nodes and user2 in self.graph.nodes:
                self.graph.add_edge(user1, user2)
                print(f"\nConnection added between {user1} and {user2}.")
            else:
                print("\nThe users need to exist first before adding a connection!")
                
    def viewUsers(self):
        print("All users:", list(self.graph.nodes))

    def viewConnections(self):
        print("\nConnections:", list(self.graph.edges))

    def displayGraph(self):
        nx.draw(self.graph, with_labels=True, node_color='lightblue', font_size=13, node_size=2000,font_weight='bold')
        plt.show()

def main():
    manager = ConnectionsManager()
    
    while True:
        print("\n1. Add a user")
        print("2. Add a connection between users")
        print("3. View all current users")
        print("4. View all current connections")
        print("5. Display connections graph")
        print("6. Exit the programme")
        
        choice = input("\nSelect one of the options: ")
        print("\n")
        
        if choice == "1":
            username = input("Enter a username: ")
            manager.addUser(username)
        
        elif choice == "2":
            user1 = input("Enter the first username: ")
            user2 = input("Enter the second username: ")
            manager.addConnection(user1,user2)
        
        elif choice == "3":
            manager.viewUsers()
        
        elif choice == "4":
            manager.viewConnections()
        
        elif choice == "5":
            manager.displayGraph()
        
        elif choice == "6":
            print("Cheers!\n")
            break
        else:
            print("Please select a valid option!\n")
            
if __name__ == "__main__":
    main()