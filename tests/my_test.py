from SocialNetwork import SocialNetwork


def additional_tests():
    # Creating the network
    network = SocialNetwork("Facebook")
    print()

    # Attempting to create another network (should print a message saying it already exists)
    duplicate_network = SocialNetwork("Facebook")
    print()

    # Creating users
    u1 = network.sign_up("John", "pass123")
    u2 = network.sign_up("Jane", "password")
    u3 = network.sign_up("Alice", "pass1")
    u4 = network.sign_up("Bob", "pass2")

    # Attempting to create a user with a duplicate username (should return None)
    duplicate_user = network.sign_up("John", "newpass")
    print()

    # Attempting to log in users (users are already logged in on signing up)
    network.log_in("John", "pass123")
    network.log_in("Jane", "password")

    # Attempting to log in with incorrect password (should print an error message)
    network.log_out("Alice")
    network.log_in("Alice", "wrongpass")
    print()

    # Creating followers (Alice's actions should fail - not logged in)
    u1.follow(u2)
    u2.follow(u3)
    u3.follow(u4)       # Should fail
    u4.follow(u1)
    print()

    # Creating more text posts
    p1 = u1.publish_post("Text", "This is a simple text post.")
    p2 = u2.publish_post("Text", "Another text post here.")
    print()

    # Attempting to create an image post with a non-existing file (should work? displaying won't work)
    u2.publish_post("Image", 'nonexistent.jpg')
    print()

    # Attempting to create a text post when logged out (should print an error message)
    u3.publish_post("Text", "This shouldn't get posted")
    print()

    network.log_in("Alice", "pass1")

    # Attempting to create a sale post with an invalid price (should print a warning but proceed?)
    u4.publish_post("Sale", "Invalid Sale", -10, "Location")
    print()

    # Displaying posts
    # Attempting to display a text post (should print an error message - no display() func for text)
    p1.display()

    # Displaying an image post
    p2.display()
    print()

    # Logging out and attempting to perform actions (should print an error message for each action)
    network.log_out("Jane")
    p1.like(u2)
    u2.unfollow(u3)         # Unfollow not followed - should fail
    u2.follow(u3)
    p1.comment(u2, "This is a secret!")
    u2.unfollow(u3)
    print()

    # Logging back in (should print "User is already logged in")
    network.log_in("John", "pass123")
    print()

    # Displaying notifications
    u1.print_notifications()
    u2.print_notifications()
    print()

    # Displaying network information
    print(network)


if __name__ == '__main__':
    additional_tests()
