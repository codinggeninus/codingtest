from itertools import combination



def is_valid_password(password):
    vowels = set('aeiou')
    num_vowels = sum(1 for char in password if char in vowels)
    num_consonants = len(password) - num_vowels
    return num_vowels >= 1 and num_consonants >= 2

def generate_passwords(letters, length, password, idx):
    if len(password) == length:
        if is_valid_password(password):
            print(password)
        return
    
    for i in range(idx, len(letters)):
        generate_passwords(letters, length, password + letters[i], i + 1)

# itertools의 combination을 활용해서 풀 수 도 있음
def generate_passwords2(letters,length): # 미완
    combinations = combination(letters,length)
    for i in combinations:
      is_valid_password(list(i))
    return




L, C = map(int, input().split())
letters = input().split()
letters.sort()  # 정렬된 문자열을 선호하는 조건에 따라 정렬

generate_passwords(letters, L, '', 0)
