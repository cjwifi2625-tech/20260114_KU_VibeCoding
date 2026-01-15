# 실행 python cal.py
# 더하는 함수
def add(a, b):
    return a + b

# 빼기 함수
def subtract(a, b):
    return a - b

# 곱하기 함수
def multiply(a, b):
    return a * b

# 나누기함수
def divide(a, b):
    if b == 0:
        return "Error: 0으로 나눌 수 없습니다."
    return a / b