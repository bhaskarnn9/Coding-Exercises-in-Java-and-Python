import hashlib
import json
import requests

traits = ["Craftsman", "Pragmatic", "Curious", "Methodical", "Driven", "Collaborator"]
key = b"Close-264ab183"  # Convert key to bytes

# Function to compute Blake2b hash with the key as a salt
def blake2b_hash(text, key):
    return hashlib.blake2b(text.encode('utf-8'), digest_size=64, key=key).hexdigest()

hashed_traits = [blake2b_hash(trait, key) for trait in traits]

# POST request
url = "https://api.close.com/buildwithus/"
headers = {"Content-Type": "application/json"}
response = requests.post(url, data=json.dumps(hashed_traits), headers=headers)

print("Response Code:", response.status_code)
print("Response Body:", response.text)
