# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the users table from our database
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.username = data['username']
        self.location = data['location']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('rezoforge_db').query_db(query)
        # Create an empty list to append our instances of users
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append( cls(user) )
        return users


# class User:

#     def __init__(self, username, name, age, email_address, location):
#         self.username = username
#         self.name = name
#         self.age = age
#         self.email = email_address
#         self.location = location
#         self.groups = [] #game groups user belongs to
#         self.armies = [] #list of armies user has

#     def send_game_req(self, req_username):
#         self.req_username = req_username
#         print(f'You sent a game request to {req_username}')
    
#     def create_new_army(self):
#         pass #placeholder
# class Army:
#     def __init__(self, army_name, army_race, army_pts_amount):
#         self.army_name = army_name
#         self.army_race = army_race
#         self.army_pts_amount = army_pts_amount

# ursa_user = User("Ursa", "Bryton", 29, "b@b.com", "Seattle", "none", "none", "none")
# hartlok_user = User("Hartlok", "Dave", 30, "dave@dave.com", "Seattle", "none", "none")