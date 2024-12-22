import hashlib

def verify_file(file_path, expected_hash, hash_type="sha256"):
    hash_func = getattr(hashlib, hash_type)()
    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            hash_func.update(chunk)
    return hash_func.hexdigest() == expected_hash

file_path = "example.txt"  # Replace with your file path
expected_hash = "your_expected_hash_here"  # Replace with the hash to verify
print("Integrity Verified" if verify_file(file_path, expected_hash) else "Integrity Check Failed")
