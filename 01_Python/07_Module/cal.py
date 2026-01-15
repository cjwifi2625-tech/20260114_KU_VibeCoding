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

def main():
    while True: # -> 무한반복
        print("\n=== 계산기 ===")
        print("1. 더하기")
        print("2. 빼기")
        print("3. 곱하기")
        print("4. 나누기")
        print("5. 종료")
        choice = input("원하는 기능의 번호를 입력하세요: ")

        if choice == '5':
            print("프로그램을 종료합니다!")
            break

        # 예외 
        if choice not in ['1','2','3','4']:
            print("잘못된 입력입니다. 다시 시도해주세요.")
            continue

        # try : 예외사항
        try:
            num1 = float(input("첫 번째 숫자를 입력하세요: "))
            num2 = float(input("두 번째 숫자를 입력하세요: "))
        except ValueError:
            print("숫자를 정확히 입력해주세요.")
            continue # 문제가 생겼을때 반복문 맨 처음으로 돌아가게

        if choice == '1':
            result = add(num1, num2)
            print(f"결과: {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"결과: {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"결과: {result}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"결과: {result}")

# .py 파이썬 파일
if __name__ == "__main__":
    main()