from database.queries import get_users, delete_user


def main():
    print("Before deleting:")

    users = get_users()

    for user in users:
        print(user)

    delete_user(3)

    print()
    print("After deleting:")

    users = get_users()

    for user in users:
        print(user)


if __name__ == "__main__":
    main()
