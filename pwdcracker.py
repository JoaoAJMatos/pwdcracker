import hashlib

hashType = str(input('[+] Enter hash type: '))
filePath = str(input('[+] Enter path to password file: '))
inputHash = str(input('[+] Enter hash value to reverse: ')).lower()
print('\n')

with open(filePath, 'r') as file:
    for line in file.readlines():
        
        if hashType == 'md5':
            hashObject = hashlib.md5(line.strip().encode())
            word = hashObject.hexdigest()
            print(f'[-] {line.strip()} : {word}')

            if word == inputHash:
                print(f'\n[+] Hash successfully reversed, password: {line.strip()}')
                exit(0)

        if hashType == 'sha1':
            hashObject = hashlib.sha1(line.strip().encode())
            word = hashObject.hexdigest()
            print(f'[-] {line.strip()} : {word}')

            if word == inputHash:
                print(f'\n[+] Hash successfully reversed, password: {line.strip()}')
                exit(0)

    
    print("[-] Unable to reverse hash")