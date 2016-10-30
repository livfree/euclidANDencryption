# Olivia Liberti
# Finds greatest common divisor, Bezout coefficients, the inverse of a mod m,
# and uses Affine cipher to encrypt and decrypt phrases.

def gcd(a, b):
    """Uses Euclidian algorithm"""
    x = a
    y = b
    while(y!=0):
        r = x % y
        x = y
        y = r
    return x

def extendedGcd(a, b):
    """uses extended euclidian algorithm and finds Bezout coefficients of a and b"""
    x0 = 1
    x1 = 0
    y0 = 0
    y1 = 1

    while b != 0:
        p = a // b
        z = a % b
        a = b
        b = z

        w = x1
        x1 = x0 - p * x1
        x0 = w
        
        v = y1
        y1 = y0 - p * y1
        y0 = v
    print("returns: gcd, si, ti")
    return (gcd(a, b), x0, y0)


def multInverse(a, m):
    """checks existence of a multiplicative inverse of a mod m """
    x0 = 1
    x1 = 0
    y0 = 0
    y1 = 1

    while m != 0:
        p = a // m
        z = a % m
        a = m
        m = z

        w = x1
        x1 = x0 - p * x1
        x0 = w
        
        v = y1
        y1 = y0 - p * y1
        y0 = v
    if(x0):
       return(x0)
    else:
        print("multiplicative inverse does not exist")
        return 0

def encryptAffine(letter, a, b):
    """encrypts a letter or phrase using Affine cipher"""
    if(gcd(7, 26) != 1):
        return "Error, not a bijection"
    else:
       encrypted_letter = ""
       for i in range(len(letter)):
          if(ord(letter[i]) == 32):
              encrypted_letter += chr(ord(letter[i]))
          else:
              let = letter[i].lower()
              let = ord(let) - 97
              new_let = (((let* a) + b) % 26) + 97
              encrypted_letter += chr(new_let)
       return encrypted_letter

def decryptAffine(letter, a, b):
    """decrypts a letter or phrase using Affine cipher"""
    decrypted_letter = ""
    for i in range(len(letter)):
        if(ord(letter[i]) == 32):
              decrypted_letter += chr(ord(letter[i]))
        else:
          let = letter[i].lower()
          let = ord(let) - 97
          new_letter = let - b
          inverse = multInverse(a, 26)
          final_letter = ((new_letter * inverse) % 26) + 97
          decrypted_letter += chr(final_letter)
    return decrypted_letter


def test():
    """test cases"""
    print(gcd(3, 26))
    print(extendedGcd(5, 30))
    print(multInverse(10, 26))
    print(decryptAffine(encryptAffine("live the full life of the mind exhilarated by new ideas intoxicated by the romance of the unusual", 5, 3), 5, 3))
    
