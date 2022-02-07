import string
import collections
import sets, sys

# 11 unknown ciphertexts (in hex format), all encrpyted with the same key

c1='00011111 00000011 00010100 01000111 00001000 00001100 01011111 00101010 00000010 01010100 01010100 00101100 00000110 00001010 00000000 00010011 00010011 00011101 00111000 00000011 00010001 01011001 00011101 01001110 00001010'
c2='00000011 00001101 00010101 01000111 00011010 01000100 01011100 00110000 00011010 00010000 00011011 00111001 01010010 00010101 00010001 01000000 00010101 00010101 01111111 00011011 00001001 00011100 00010010 01010010 00011000'
c3='00001011 00010101 01000001 00001011 00011110 00001010 01010111 00101011 00000110 00010000 00011101 00101100 01010010 00010001 00011000 01010110 01000001 00000111 00111110 00000110 00000000 01011001 00000111 01001110 00010010'
c4='00001001 00000100 01000001 00000110 00010101 00000000 00010000 00101011 00000110 01010101 00001101 01111111 00000101 00000000 00000010 01010110 01000001 00000110 00110000 00000100 00001000 00011000 00000111 01000100 00001110'
ciphers = [c1, c2, c3, c4]
# The target ciphertext we want to crack
#target_cipher = "0529242a631234122d2b36697f13272c207f2021283a6b0c7908"

# XORs two string
def strxor(a, b):     # xor two strings (trims the longer input)
    return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b)])

def target_fix(target_cipher):
    # To store the final key
    final_key = [None]*150
    # To store the positions we know are broken
    known_key_positions = set()

    # For each ciphertext
    for current_index, ciphertext in enumerate(ciphers):
        counter = collections.Counter()
        # for each other ciphertext
        for index, ciphertext2 in enumerate(ciphers):
            if current_index != index: # don't xor a ciphertext with itself
                for indexOfChar, char in enumerate(strxor(ciphertext.decode('hex'), ciphertext2.decode('hex'))): # Xor the two ciphertexts
                    # If a character in the xored result is a alphanumeric character, it means there was probably a space character in one of the plaintexts (we don't know which one)
                    if char in string.printable and char.isalpha(): counter[indexOfChar] += 1 # Increment the counter at this index
        knownSpaceIndexes = []

        # Loop through all positions where a space character was possible in the current_index cipher
        for ind, val in counter.items():
            # If a space was found at least 7 times at this index out of the 9 possible XORS, then the space character was likely from the current_index cipher!
            if val >= 7: knownSpaceIndexes.append(ind)
        #print knownSpaceIndexes # Shows all the positions where we now know the key!

        # Now Xor the current_index with spaces, and at the knownSpaceIndexes positions we get the key back!
        xor_with_spaces = strxor(ciphertext.decode('hex'),' '*150)
        for index in knownSpaceIndexes:
            # Store the key's value at the correct position
            final_key[index] = xor_with_spaces[index].encode('hex')
            # Record that we known the key at this position
            known_key_positions.add(index)

    # Construct a hex key from the currently known key, adding in '00' hex chars where we do not know (to make a complete hex string)
    final_key_hex = ''.join([val if val is not None else '00' for val in final_key])
    # Xor the currently known key with the target cipher
    output = strxor(target_cipher.decode('hex'),final_key_hex.decode('hex'))

    print "Fix this sentence:"
    print ''.join([char if index in known_key_positions else '*' for index, char in enumerate(output)])+"\n"

    # WAIT.. MANUAL STEP HERE 
    # This output are printing a * if that character is not known yet
    # fix the missing characters like this: "Let*M**k*ow if *o{*a" = "cure, Let Me know if you a"
    # if is too hard, change the target_cipher to another one and try again
    # and we have our key to fix the entire text!

    #sys.exit(0) #comment and continue if u got a good key

    target_plaintext = "cure, Let Me know if you a"
    print "Fixed:"
    print target_plaintext+"\n"

    key = strxor(target_cipher.decode('hex'),target_plaintext)

    print "Decrypted msg:"
    for cipher in ciphers:
        print strxor(cipher.decode('hex'),key)

    print "\nPrivate key recovered: "+key+"\n"
    
for i in ciphers:
    target_fix(i)
