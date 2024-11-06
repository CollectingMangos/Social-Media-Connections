# Social Media Connections Manager
This app is for Question 2 of ITDPA2-44 (Data Structures & Algorithms in Python) Project.

This Python application provides a simple social media network manager where users can create profiles in the form of usernames, establish connections, and visualize the network of said connections. It includes functionality for adding users, connecting users, viewing the network, and displaying it graphically.

## Project Structure

- `social_media.py`: The main Python script containing all classes and logic for managing users and their connections.
- `requirements.txt`: A text file listing required packages (`networkx` and `matplotlib`).

## Classes

### ConnectionsManager
The `ConnectionsManager` class is responsible for managing users and their connections in a social network graph. It provides methods to add users, create connections, view users and connections, and display the network.

#### Methods:
- `addUser(username)`: Adds a user node to the graph.
- `addConnection(user1, user2)`: Connects two existing users with an edge in the graph.
- `viewUsers()`: Prints a list of all users.
- `viewConnections()`: Prints all connections between users.
- `displayGraph()`: Displays a graphical representation of the network.

## How It Works

1. **Add a user**: Adds a new user to the network.
2. **Add a connection between users**: Connects two users, if they both exist in the network.
3. **View all current users**: Displays a list of all users in the network.
4. **View all current connections**: Lists all connections (edges) in the network.
5. **Display connections graph**: Shows a visual representation of the user network using `matplotlib`.
6. **Exit the program**: Closes the application.

## Getting Started

### Prerequisites
- Python 3.6+
- Required packages (`networkx` and `matplotlib`) listed in `requirements.txt`

### Running the Application
1. Clone or download the project folder.
2. Open a terminal in the project directory.
3. Create a Virtual Environment with "python3 -m venv venv"
4. Activate the Virtual Environment with "source venv/bin/activate"
5. Install the necessary packages with "pip3 install -r requirements.txt"
6. Run the following command to start the application:
   ```bash
   python3 socialmedia.py