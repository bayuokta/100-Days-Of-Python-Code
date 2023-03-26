class User:
    def __init__(self, user_id: str, username: str):
        self.user_id = user_id
        self.username = username
        self.following = 0
        self.followers = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User('001', 'bayuokta463')
user_2 = User('002', 'pmarchelina')
user_3 = User('003', 'wulandm')
user_4 = User('004', 'anit.q')

user_2.follow(user_1)
user_3.follow(user_1)
user_4.follow(user_1)
user_1.follow(user_4)

print(f'Followers {user_1.username} ada {user_1.followers} sedangkan following nya ada {user_1.following}')

