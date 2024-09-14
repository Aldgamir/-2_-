def create_table(key_phrase):
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # J зазвичай ігнорується або поєднується з I
    table = []
    used_chars = set()
    
    # Додаємо літери з ключової фрази до таблиці
    for char in key_phrase.upper():
        if char not in used_chars and char in alphabet:
            used_chars.add(char)
            table.append(char)
    
    # Додаємо решту літер алфавіту
    for char in alphabet:
        if char not in used_chars:
            table.append(char)
    
    return [table[i:i+5] for i in range(0, 25, 5)]  # Використаємо таблицю 5x5

def find_position(table, char):
    for row_idx, row in enumerate(table):
        if char in row:
            return (row_idx, row.index(char))
    return None

def encrypt_text(text, table):
    text = text.upper().replace('J', 'I')
    encrypted_text = ""
    
    for char in text:
        if char == ' ':
            encrypted_text += ' '  # Зберігаємо пробіли
        else:
            pos = find_position(table, char)
            if pos:
                encrypted_text += table[pos[0]][(pos[1] + 1) % 5]  # Сдвиг вправо
            else:
                encrypted_text += char  # Не змінюємо символи, яких немає в таблиці
    
    return encrypted_text

def decrypt_text(text, table):
    text = text.upper()
    decrypted_text = ""
    
    for char in text:
        if char == ' ':
            decrypted_text += ' '  # Зберігаємо пробіли
        else:
            pos = find_position(table, char)
            if pos:
                decrypted_text += table[pos[0]][(pos[1] - 1) % 5]  # Сдвиг вліво
            else:
                decrypted_text += char  # Не змінюємо символи, яких немає в таблиці
    
    return decrypted_text

# Використання функцій
key_phrase = "MATRIX"
table = create_table(key_phrase)

plain_text = "The artist is the creator of beautiful things. To reveal art and conceal the artist is art's aim. The critic is he who can translate into another manner or a new material his impression of beautiful things. The highest, as the lowest, form of criticism is a mode of autobiography. Those who find ugly meanings in beautiful things are corrupt without being charming. This is a fault. Those who find beautiful meanings in beautiful things are the cultivated. For these there is hope. They are the elect to whom beautiful things mean only Beauty. There is no such thing as a moral or an immoral book. Books are well written, or badly written. That is all. The nineteenth-century dislike of realism is the rage of Caliban seeing his own face in a glass. The nineteenth-century dislike of Romanticism is the rage of Caliban not seeing his own face in a glass. The moral life of man forms part of the subject matter of the artist, but the morality of art consists in the perfect use of an imperfect medium. No artist desires to prove anything. Even things that are true can be proved. No artist has ethical sympathies. An ethical sympathy in an artist is an unpardonable mannerism of style. No artist is ever morbid. The artist can express everything. Thought and language are to the artist instruments of an art. Vice and virtue are to the artist materials for an art. From the point of view of form, the type of all the arts is the art of the musician. From the point of view of feeling, the actor's craft is the type. All art is at once surface and symbol. Those who go beneath the surface do so at their peril. Those who read the symbol do so at their peril. It is the spectator, and not life, that art really mirrors. Diversity of opinion about a work of art shows that the work is new, complex, vital. When critics disagree the artist is in accord with himself. We can forgive a man for making a useful thing as long as he does not admire it. The only excuse for making a useless thing is that one admires it intensely. All art is quite useless."
encrypted_text = encrypt_text(plain_text, table)
decrypted_text = decrypt_text(encrypted_text, table)

print(f"Оригінальний текст: {plain_text}")
print(f"Зашифрований текст: {encrypted_text}")
print(f"РОзшифрований текст: {decrypted_text}")