

def fetch_user(user_id):
    # fetching user data from database
    # user = db.get_user(user_id)

    user = None

    if user is None:
        raise Exception(f"user {user_id} is not found in database")
    else:
        return user


users = [123, 1234, 12345]
for user_id in users:
    try:
        fetch_user(user_id)
    except Exception as e:
        print("error found:", e)
