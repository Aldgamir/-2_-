def create_permutation_key(phrase):
    # Отримуємо унікальні символи фрази та сортуємо їх за алфавітом
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

def encrypt(text, key):
    # Розбиваємо текст на блоки довжиною, що дорівнює довжині ключа
    block_size = len(key)
    ciphertext = ''
    
    # Проходимо по кожному блоку тексту
    for i in range(0, len(text), block_size):
        block = list(text[i:i + block_size])
        
        # Заповнюємо блок пробілами, якщо його довжина менша за довжину ключа
        if len(block) < block_size:
            block.extend([' '] * (block_size - len(block)))
        
        # Переставляємо символи в блоці відповідно до ключа
        permuted_block = [''] * block_size
        for j, pos in enumerate(key):
            permuted_block[pos - 1] = block[j]
        
        ciphertext += ''.join(permuted_block)
    
    return ciphertext

def decrypt(text, key):
    # Створення зворотнього ключа для дешифрування
    block_size = len(key)
    reverse_key = [0] * block_size
    for i, pos in enumerate(key):
        reverse_key[pos - 1] = i + 1
    
    plaintext = ''
    
    # Проходимо по кожному блоку тексту
    for i in range(0, len(text), block_size):
        block = list(text[i:i + block_size])
        
        # Дешифруємо символи в блоці за допомогою зворотнього ключа
        original_block = [''] * block_size
        for j, pos in enumerate(reverse_key):
            original_block[pos - 1] = block[j]
        
        plaintext += ''.join(original_block)
    
    return plaintext

# Використання функцій для перестановки за ключовим словом
key_phrase = "SECRET"
key = create_permutation_key(key_phrase)

plain_text = "The artist is the creator of beautiful things. To reveal art and conceal the artist is art's aim. The critic is he who can translate into another manner or a new material his impression of beautiful things. The highest, as the lowest, form of criticism is a mode of autobiography. Those who find ugly meanings in beautiful things are corrupt without being charming. This is a fault. Those who find beautiful meanings in beautiful things are the cultivated. For these there is hope. They are the elect to whom beautiful things mean only Beauty. There is no such thing as a moral or an immoral book. Books are well written, or badly written. That is all. The nineteenth-century dislike of realism is the rage of Caliban seeing his own face in a glass. The nineteenth-century dislike of Romanticism is the rage of Caliban not seeing his own face in a glass. The moral life of man forms part of the subject matter of the artist, but the morality of art consists in the perfect use of an imperfect medium. No artist desires to prove anything. Even things that are true can be proved. No artist has ethical sympathies. An ethical sympathy in an artist is an unpardonable mannerism of style. No artist is ever morbid. The artist can express everything. Thought and language are to the artist instruments of an art. Vice and virtue are to the artist materials for an art. From the point of view of form, the type of all the arts is the art of the musician. From the point of view of feeling, the actor's craft is the type. All art is at once surface and symbol. Those who go beneath the surface do so at their peril. Those who read the symbol do so at their peril. It is the spectator, and not life, that art really mirrors. Diversity of opinion about a work of art shows that the work is new, complex, vital. When critics disagree the artist is in accord with himself. We can forgive a man for making a useful thing as long as he does not admire it. The only excuse for making a useless thing is that one admires it intensely. All art is quite useless."
encrypted_text = encrypt(plain_text, key)
decrypted_text = decrypt(encrypted_text, key)

print(f"Original text: {plain_text}")
print(f"Encrypted text: {encrypted_text}")
print(f"Decrypted text: {decrypted_text}")