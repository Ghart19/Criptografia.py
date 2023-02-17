import string

def encrypt(message, key):
    # Validação de entrada
    if not isinstance(message, str):
        raise TypeError("message deve ser uma string")
    if not isinstance(key, str):
        raise TypeError("key deve ser uma string")
    if not message:
        raise ValueError("message não pode ser vazio")
    if not key:
        raise ValueError("key não pode ser vazio")
    for letter in string.ascii_lowercase:
        if letter not in key:
            raise ValueError(f"A chave deve conter todas as letras do alfabeto. Faltando {letter}")

    # Define alfabeto de entrada
    alphabet = string.ascii_lowercase

    # Cria dicionário para mapear caracteres do alfabeto original para caracteres criptografados
    mapping = {}
    for i, char in enumerate(alphabet):
        mapping[char] = key[i]

    # Criptografa mensagem
    encrypted_message = ""
    for char in message:
        if char in alphabet:
            encrypted_message += mapping[char]
        else:
            encrypted_message += char

    return encrypted_message

def decrypt(encrypted_message, key):
    # Validação de entrada
    if not isinstance(encrypted_message, str):
        raise TypeError("encrypted_message deve ser uma string")
    if not isinstance(key, str):
        raise TypeError("key deve ser uma string")
    if not encrypted_message:
        raise ValueError("encrypted_message não pode ser vazio")
    if not key:
        raise ValueError("key não pode ser vazio")
    for letter in key:
        if letter not in string.ascii_lowercase:
            raise ValueError(f"A chave deve conter apenas letras do alfabeto. Encontrado {letter}")

    # Define alfabeto de entrada
    alphabet = string.ascii_lowercase

    # Cria dicionário para mapear caracteres criptografados para caracteres do alfabeto original
    mapping = {}
    for i, char in enumerate(key):
        mapping[char] = alphabet[i]

    # Descriptografa mensagem
    decrypted_message = ""
    for char in encrypted_message:
        if char in key:
            decrypted_message += mapping[char]
        else:
            decrypted_message += char

    return decrypted_message

# Exemplo de uso
message = "hello world"
key = "qwertyuiopasdfghjklzxcvbnm"
encrypted_message = encrypt(message, key)
print("Mensagem criptografada: ", encrypted_message)
decrypted_message = decrypt(encrypted_message, key)
print("Mensagem descriptografada: ", decrypted_message)
