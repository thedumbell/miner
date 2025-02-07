import base64
import zlib,random
from cryptography.fernet import Fernet
def encode(n,code):
    def base64_encode_n_times(input_string, n):
        encoded_string = input_string
        for _ in range(n):
            encoded_string = base64.b64encode(encoded_string.encode('utf-8')).decode('utf-8')
        return encoded_string
    print("[*]bilgiler kod parçacığna enjekte edilyor.....")
    code = ""

    def key():
        return Fernet.generate_key()

    def encrypt_message(plain_text, key):
        fernet = Fernet(key)
        encrypted = fernet.encrypt(plain_text.encode())
        return encrypted
    encoded_result = base64_encode_n_times(code, n) 
    print(f"[*]belirlenen  şifreleme sayısı tamamlandı...")
    gkey = key()
    print("[*] anahtar belirlendi....")
    sahtekeyler= []
    for x in range(10):
        sahtekeyler.append(key().decode())
    sahtekeyler[random.randint(0,len(sahtekeyler))] = gkey.decode()
    print("[*] anahtar sahte anahtarlara gizlendi....")
    for x in sahtekeyler:
        print("[#] "+x+" anahtar listesi")
    print("[*] anahtarlı şifreleme başladı...")
    encoded_result = encrypt_message(encoded_result, gkey)
    encoded_result = encoded_result.decode()
    print("[*] arşivleme işlemi başladı...")
    encoded_result = zlib.compress(encoded_result.encode())  
    print("[*] son base64 kodlandı...")
    encoded_result = base64.b64encode(encoded_result).decode()  


    code = f"""
import base64
import zlib
from cryptography.fernet import Fernet

sk = {sahtekeyler}
code ='{encoded_result}'

def dm(encrypted_text, key):
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_text)
    return decrypted.decode()

code = base64.b64decode(code)
code = zlib.decompress(code).decode('utf-8')

for x in range(len(sk)):
    try:

        code = dm(code,sk[x])
        break
    except:
        pass
for x in range({n}):
    code = base64.b64decode(code)


exec(code)


    """

    print("[*] dosya yazılyor....")

    return code
    print("[*] Hazır...")
