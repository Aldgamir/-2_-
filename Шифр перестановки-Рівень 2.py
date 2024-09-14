def create_permutation_key(phrase):
    sorted_phrase = sorted(list(phrase))
    key_map = {}
    
    # Створюємо словник, який відповідає кожному символу його позиції в відсортованій фразі
    for i, char in enumerate(sorted_phrase):
        if char not in key_map:
            key_map[char] = []
        key_map[char].append(i + 1)
    
    # Формуємо ключ перестановки
    permutation_key = []
    for char in phrase:
        permutation_key.append(key_map[char].pop(0))
    
    return permutation_key

def transpose(matrix):
    # Транспонування матриці
    return [''.join(row) for row in zip(*matrix)]

def apply_permutation(matrix, key):
    # Застосування перестановки до рядків або стовпців матриці
    permuted_matrix = [''] * len(matrix)
    for index, new_index in enumerate(key):
        permuted_matrix[new_index - 1] = matrix[index]  # Використання правильного індексу
    return permuted_matrix

def encrypt_double_permutation(text, key1, key2):
    # Розраховуємо розміри матриці
    rows = len(key1)
    cols = len(key2)
    block_size = rows * cols
    encrypted_text = ""

    # Обробляємо текст блоками
    for block_start in range(0, len(text), block_size):
        block = text[block_start:block_start + block_size]
        block = block.ljust(block_size)  # Заповнюємо пробілами, якщо потрібно

        # Формуємо початкову матрицю
        matrix = []
        for i in range(0, len(block), cols):
            matrix.append(block[i:i + cols])
        
        # Застосовуємо першу перестановку (по стовпцях)
        matrix = transpose(matrix)
        matrix = apply_permutation(matrix, key2)
        
        # Застосовуємо другу перестановку (по рядках)
        matrix = transpose(matrix)
        matrix = apply_permutation(matrix, key1)
        
        # Додаємо зашифрований блок до загального результату
        encrypted_text += ''.join(matrix)

    return encrypted_text

def decrypt_double_permutation(text, key1, key2):
    rows = len(key1)
    cols = len(key2)
    block_size = rows * cols
    decrypted_text = ""

    # Обробляємо текст блоками
    for block_start in range(0, len(text), block_size):
        block = text[block_start:block_start + block_size]

        matrix = []
        for i in range(0, len(block), cols):
            matrix.append(block[i:i + cols])

        reverse_key1 = [key1.index(i + 1) + 1 for i in range(len(key1))]
        matrix = apply_permutation(matrix, reverse_key1)
        matrix = transpose(matrix)
        
        reverse_key2 = [key2.index(i + 1) + 1 for i in range(len(key2))]
        matrix = apply_permutation(matrix, reverse_key2)
        matrix = transpose(matrix)
        
        decrypted_text += ''.join(matrix)

    return decrypted_text.strip()

# Використання функцій для перестановки за двома ключовими словом
key1_phrase = "SECRET"
key2_phrase = "CRYPTO"
key1 = create_permutation_key(key1_phrase)
key2 = create_permutation_key(key2_phrase)

plain_text = ("The artist is the creator of beautiful things. To reveal art and conceal the artist is art's aim. The critic is he who can translate into another manner or a new material his impression of beautiful things. The highest, as the lowest, form of criticism is a mode of autobiography. Those who find ugly meanings in beautiful things are corrupt without being charming. This is a fault. Those who find beautiful meanings in beautiful things are the cultivated. For these there is hope. They are the elect to whom beautiful things mean only Beauty. There is no such thing as a moral or an immoral book. Books are well written, or badly written. That is all. The nineteenth-century dislike of realism is the rage of Caliban seeing his own face in a glass. The nineteenth-century dislike of Romanticism is the rage of Caliban not seeing his own face in a glass. The moral life of man forms part of the subject matter of the artist, but the morality of art consists in the perfect use of an imperfect medium. No artist desires to prove anything. Even things that are true can be proved. No artist has ethical sympathies. An ethical sympathy in an artist is an unpardonable mannerism of style. No artist is ever morbid. The artist can express everything. Thought and language are to the artist instruments of an art. Vice and virtue are to the artist materials for an art. From the point of view of form, the type of all the arts is the art of the musician. From the point of view of feeling, the actor's craft is the type. All art is at once surface and symbol. Those who go beneath the surface do so at their peril. Those who read the symbol do so at their peril. It is the spectator, and not life, that art really mirrors. Diversity of opinion about a work of art shows that the work is new, complex, vital. When critics disagree the artist is in accord with himself. We can forgive a man for making a useful thing as long as he does not admire it. The only excuse for making a useless thing is that one admires it intensely. All art is quite useless.")

encrypted_text = encrypt_double_permutation(plain_text, key1, key2)
decrypted_text = decrypt_double_permutation(encrypted_text, key1, key2)

print(f"Original text: {plain_text}")
print(f"Encrypted text: {encrypted_text}")
print(f"Decrypted text: {decrypted_text}")