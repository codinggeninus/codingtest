import re
import os
import random
import requests
from bs4 import BeautifulSoup

#   난이도 선정
#   1 = 브론즈 5
#   6 = 실버 5
#   11 = 골드 5 ...
select_difficulties = [10,10,10,10]


solved = []
problems = []

def main():
    
    #fetch solved
    with open("participants.txt", 'r', encoding='utf-8') as file:
        content = file.read()
    participants = []
    for line in content.split('\n') :
        if len(line) == 0 or line[0] == '#':
            continue
        handle, name = line.split()
        participants.append(handle[1:])
    for user in participants:
        fetch(user)
    global solved
    solved = list(set(solved))
    
    #fetch problems
    directory = 'raws/'
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            extract_data(os.path.join(directory, filename))
    problems.sort(key=lambda x: int(x[1]))
    
    #pick problem
    selected_problems = []
    for difficulty in select_difficulties:
        filtered_problems = [problem for problem in problems if int(problem[1]) == difficulty]
        if filtered_problems:
            selected_problem = random.choice(filtered_problems)
            selected_problems.append(selected_problem)

    for index,problem in enumerate(selected_problems):
        print(str(index+1) + '. ' + 'https://www.acmicpc.net/problem/' + str(problem[0]))
    
    
    

def fetch(username):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    # 사용자의 프로필 URL 생성
    url = f'https://www.acmicpc.net/user/{username}'
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return f"Error: The server returned a status code of {response.status_code}"

    soup = BeautifulSoup(response.content, 'html.parser')

    # 페이지 전체 텍스트에서 '맞은 문제' 부분 찾기
    text = soup.get_text()
    start = text.find('맞은 문제') + len('맞은 문제')
    text = text[start:]  # 첫 번째 '맞은 문제' 이후의 텍스트

    # 두 번째 '맞은 문제' 시작점 찾기
    start = text.find('맞은 문제') + len('맞은 문제')
    text = text[start:]  # 두 번째 '맞은 문제' 이후의 텍스트

    # 두 번째 '맞은 문제'와 '시도했지만 맞지 못한 문제' 사이의 텍스트 추출
    end = text.find('시도했지만 맞지 못한 문제')
    if end == -1:
        return "Error: Could not find the end marker for solved problems."
    problem_text = text[:end]

    # 해당 텍스트에서 모든 숫자(문제 번호) 추출
    problem_numbers = re.findall(r'\d+', problem_text)

    # 문자열 리스트를 정수 리스트로 변환
    global solved
    solved = solved + list(map(int,problem_numbers))

def extract_data(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()
    # 문제 번호와 난이도를 추출하기 위한 정규 표현식
    pattern = r'https://www.acmicpc.net/problem/(\d+).*?tier_small/(\d+).svg'
    results = re.findall(pattern, content)
    
    for problem_number,difficulty in results:
        if not (int(problem_number) in solved) :
            problems.append((int(problem_number),difficulty))


if __name__ == '__main__':
    main()