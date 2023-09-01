import keyring

def store_secret(service_id, username, secret):
    """Store a secret using keyring."""
    keyring.set_password(service_id, username, secret)
    print(f"Secret for {username} under {service_id} stored successfully.")

def retrieve_secret(service_id, username):
    """Retrieve a secret using keyring."""
    secret = keyring.get_password(service_id, username)
    if secret:
        print(f"Retrieved secret for {username} under {service_id}: {secret}")
    else:
        print(f"No secret found for {username} under {service_id}.")

def delete_secret(service_id, username):
    """Delete a stored secret using keyring."""
    try:
        keyring.delete_password(service_id, username)
        print(f"Secret for {username} under {service_id} deleted successfully.")
    except keyring.errors.PasswordDeleteError:
        print(f"No secret found for {username} under {service_id}.")

if __name__ == "__main__":
    print("Keyring Secret Manager")
    print("-----------------------")
    print("-----------------------")
    
    SERVICE_ID = input("Enter service ID (e.g., name of your app): ").strip()
    USERNAME = input("Enter username or identifier for the secret: ").strip()

    print("\nChoose an operation:")
    print("1. Store secret")
    print("2. Retrieve secret")
    print("3. Delete secret")
    
    choice = input("Enter the number of your choice: ").strip()

    if choice == "1":
        SECRET = input("Enter the secret to store: ").strip()
        store_secret(SERVICE_ID, USERNAME, SECRET)
    elif choice == "2":
        retrieve_secret(SERVICE_ID, USERNAME)
    elif choice == "3":
        delete_secret(SERVICE_ID, USERNAME)
    else:
        print("Invalid choice!")
