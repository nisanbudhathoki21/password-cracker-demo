import hashlib

def crack_md5_hash(hash_to_crack, wordlist_file):
    with open(wordlist_file, 'r') as f:
        for word in f:
            word = word.strip()
            hashed_word = hashlib.md5(word.encode()).hexdigest()

            if hashed_word == hash_to_crack:
                print(f"[+] Password found: {word}")
                return

    print("[-] Password not found in wordlist.")

if __name__ == "__main__":
    hash_input = input("Enter MD5 hash: ").strip()
    crack_md5_hash(hash_input, 'wordlist.txt')
