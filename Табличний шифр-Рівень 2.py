def create_vigenere_table():
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # J зазвичай ігнорується або поєднується з I
    table = []
    for i in range(25):
        row = alphabet[i:] + alphabet[:i]
        table.append(row)
    return table

def vigenere_encrypt(plain_text, key):
    table = create_vigenere_table()
    key = key.upper().replace('J', 'I')
    plain_text = plain_text.upper().replace('J', 'I')
    
    encrypted_text = []
    key_length = len(key)
    
    for i, char in enumerate(plain_text):
        if char == ' ':
            encrypted_text.append(' ')
        elif char in 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
            row = key[i % key_length]
            col = char
            row_idx = ord(row) - ord('A')
            col_idx = ord(col) - ord('A')
            if 0 <= row_idx < 25 and 0 <= col_idx < 25:
                encrypted_text.append(table[row_idx][col_idx])
            else:
                encrypted_text.append(char)
        else:
            encrypted_text.append(char)  # Не змінюємо символи, які не є літерами
    
    return ''.join(encrypted_text)

def create_table(key_phrase):
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    table = []
    used_chars = set()
    
    for char in key_phrase.upper():
        if char not in used_chars and char in alphabet:
            used_chars.add(char)
            table.append(char)
    
    for char in alphabet:
        if char not in used_chars:
            table.append(char)
    
    return [table[i:i+5] for i in range(0, 25, 5)]

def find_position(table, char):
    for row_idx, row in enumerate(table):
        if char in row:
            return (row_idx, row.index(char))
    return None

def tabular_encrypt(text, table):
    text = text.upper().replace('J', 'I')
    encrypted_text = []
    
    for char in text:
        if char == ' ':
            encrypted_text.append(' ')
        else:
            pos = find_position(table, char)
            if pos:
                encrypted_text.append(table[pos[0]][(pos[1] + 1) % 5])
            else:
                encrypted_text.append(char)
    
    return ''.join(encrypted_text)

def vigenere_and_tabular_encrypt(text, vigenere_key, tabular_key):
    vigenere_encrypted = vigenere_encrypt(text, vigenere_key)
    tabular_table = create_table(tabular_key)
    final_encrypted = tabular_encrypt(vigenere_encrypted, tabular_table)
    return final_encrypted

# Задаємо ключові фрази і текст, який маємо зашифрувати
vigenere_key = "CRYPTO"
tabular_key = "CRYPTO"
plain_text = "The artist is the creator of beautiful things. To reveal art and conceal the artist is art's aim. The critic is he who can translate into another manner or a new material his impression of beautiful things. The highest, as the lowest, form of criticism is a mode of autobiography. Those who find ugly meanings in beautiful things are corrupt without being charming. This is a fault. Those who find beautiful meanings in beautiful things are the cultivated. For these there is hope. They are the elect to whom beautiful things mean only Beauty. There is no such thing as a moral or an immoral book. Books are well written, or badly written. That is all. The nineteenth-century dislike of realism is the rage of Caliban seeing his own face in a glass. The nineteenth-century dislike of Romanticism is the rage of Caliban not seeing his own face in a glass. The moral life of man forms part of the subject matter of the artist, but the morality of art consists in the perfect use of an imperfect medium. No artist desires to prove anything. Even things that are true can be proved. No artist has ethical sympathies. An ethical sympathy in an artist is an unpardonable mannerism of style. No artist is ever morbid. The artist can express everything. Thought and language are to the artist instruments of an art. Vice and virtue are to the artist materials for an art. From the point of view of form, the type of all the arts is the art of the musician. From the point of view of feeling, the actor's craft is the type. All art is at once surface and symbol. Those who go beneath the surface do so at their peril. Those who read the symbol do so at their peril. It is the spectator, and not life, that art really mirrors. Diversity of opinion about a work of art shows that the work is new, complex, vital. When critics disagree the artist is in accord with himself. We can forgive a man for making a useful thing as long as he does not admire it. The only excuse for making a useless thing is that one admires it intensely. All art is quite useless."

# Шифрування тексту
encrypted_text = vigenere_and_tabular_encrypt(plain_text, vigenere_key, tabular_key)

print(f"Наданий текст: {plain_text}")
print(f"Зашифрований текст: {encrypted_text}")