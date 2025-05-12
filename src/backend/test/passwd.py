from cryptography.fernet import Fernet

secret_key = 'TI31VYJ-ldAq-FXo5QNPKV_lqGTFfp-MIdbK2Hm5F1E='


def encrypt_token(token: str) -> str:
    """使用Fernet对称加密算法加密字符串"""
    return Fernet(secret_key).encrypt(token.encode()).decode()


def decrypt_token(encrypted_token: str) -> str:
    """使用Fernet对称加密算法解密字符串"""
    return Fernet(secret_key).decrypt(encrypted_token.encode()).decode()


# 测试加密和解密
password_original = "aa123456"
encrypted = encrypt_token(password_original)
decrypted = decrypt_token(encrypted)

print(f"原始密码: {password_original}")
print(f"加密后: {encrypted}")
print(f"解密后: {decrypted}")
