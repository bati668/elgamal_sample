from sympy import mod_inverse
from random import randint

# Function to perform modular exponentiation
def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

# Key generation
def generate_keys(p, g):
    private_key = randint(1, p-2)
    public_key = mod_exp(g, private_key, p)
    return private_key, public_key

# Encryption
def encrypt(p, g, public_key, m):
    y = randint(1, p-2)
    c1 = mod_exp(g, y, p)
    c2 = (m * mod_exp(public_key, y, p)) % p
    return c1, c2

# Decryption
def decrypt(p, private_key, c1, c2):
    s = mod_exp(c1, private_key, p)
    s_inv = mod_inverse(s, p)
    m = (c2 * s_inv) % p
    return m

# Parameters
p = 467
g = 2

# Key generation
private_key, public_key = generate_keys(p, g)

# Messages
m1 = 123
m2 = 456

# Encryption
c1_m1, c2_m1 = encrypt(p, g, public_key, m1)
c1_m2, c2_m2 = encrypt(p, g, public_key, m2)

# Homomorphic property: Ciphertext multiplication results in plaintext addition
c1_h = (c1_m1 * c1_m2) % p
c2_h = (c2_m1 * c2_m2) % p

# Decryption of the homomorphic result
m_h = decrypt(p, private_key, c1_h, c2_h)

# Original messages and their sum
print(f"Original message 1: {m1}")
print(f"Original message 2: {m2}")
print(f"Sum of messages: {(m1 * m2) % p}")
print(f"Decrypted homomorphic result: {m_h}")
