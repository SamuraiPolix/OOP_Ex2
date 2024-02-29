# Social Network Project 
## Assignment #2 in Object-Oriented Programming @ Ariel University


## Overview
This project is an implementation of a social network in Python, focusing on object-oriented programming principles and design patterns. The social network allows users to register, connect with each other, upload posts, comment, like posts, and more. The implementation adheres to the specified requirements, utilizing three design patterns: Singleton, Observer, and Factory.

## Project Structure
### Main Components

1. **Network**: Manages user registration, connection, disconnection, and activity tracking. Enforces constraints such as unique usernames and password length. Implements the Singleton pattern to ensure only one network instance exists.

2. **Users**: Represents individual users in the social network. Users can follow each other, upload posts, like/comment on posts, and receive notifications. The Observer pattern is implemented to notify users of relevant activities.

3. **Posts**: Represents different types of posts: TextPost, ImagePost, and SalePost. Each post type has specific functionalities. The Factory pattern is utilized to create instances of different post types.

### Design Patterns
1. **Singleton**:
The Singleton pattern is applied in  the SocialNetwork class and the PostFactory class, ensuring that only one network and one post-factory instance are created throughout the program's execution.

3. **Observer**:
The Observer pattern is used in the User class, to notify users of relevant activities, such as receiving notifications when someone they follow uploads a post or when someone likes/comments on their post.

4. **Factory**:
The Factory pattern is used in the Post class, to create instances of different post types (TextPost, ImagePost, SalePost) based on the specific requirements of each post type.

### UML Diagram
# Social Network Project 
## Assignment #2 in Object-Oriented Programming @ Ariel University


## Overview
This project is an implementation of a social network in Python, focusing on object-oriented programming principles and design patterns. The social network allows users to register, connect with each other, upload posts, comment, like posts, and more. The implementation adheres to the specified requirements, utilizing three design patterns: Singleton, Observer, and Factory.

## Project Structure
### Main Components

1. **Network**: Manages user registration, connection, disconnection, and activity tracking. Enforces constraints such as unique usernames and password length. Implements the Singleton pattern to ensure only one network instance exists.

2. **Users**: Represents individual users in the social network. Users can follow each other, upload posts, like/comment on posts, and receive notifications. The Observer pattern is implemented to notify users of relevant activities.

3. **Posts**: Represents different types of posts: TextPost, ImagePost, and SalePost. Each post type has specific functionalities. The Factory pattern is utilized to create instances of different post types.

### Design Patterns
1. **Singleton**:
The Singleton pattern is applied in  the SocialNetwork class and the PostFactory class, ensuring that only one network and one post-factory instance are created throughout the program's execution.

3. **Observer**:
The Observer pattern is used in the User class, to notify users of relevant activities, such as receiving notifications when someone they follow uploads a post or when someone likes/comments on their post.

4. **Factory**:
The Factory pattern is used in the Post class, to create instances of different post types (TextPost, ImagePost, SalePost) based on the specific requirements of each post type.

### UML Diagram
![classes](https://github.com/SamuraiPolix/OOP_Ex2/blob/master/uml_diagram/classes.png?raw=true)
![packages](https://github.com/SamuraiPolix/OOP_Ex2/blob/master/uml_diagram/packages.png?raw=true)

## Running the Project
Use the provided main.py file to simulate social network activities.
