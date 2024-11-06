import networkx as nx
import matplotlib.pyplot as plt

class ConnectionsManager:
    def __init__(self):
        self.graph = nx.Graph()

    def addUser(self, username):
        self.graph.addNode(username)
        print(f'User {username} added.')

    def addConnection(self, user1, user2):
        self.graph.addEdge(user1, user2)
        print(f'Connection added between {user1} and {user2}.')

    def viewUsers(self):
        print("All users:", list(self.graph.nodes))

    def viewConnections(self):
        print("Connections:", list(self.graph.edges))

    def displayGraph(self):
        nx.draw(self.graph, with_labels=True)
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
        
        choice = input("Select one of the optioins: ")
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
        
        elif choice == '6':
            print("\nCheers!\n")
            break
        else:
            print("\nPlease select a valid option!\n")
            
if __name__ == "__main__":
    main()