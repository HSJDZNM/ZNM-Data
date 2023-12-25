import random


class Homework:
    def __init__(self, count):
        self.count_max = count

    def generate_question(self):
        num1 = random.randint(0, 20)
        num2 = random.randint(0, 20)
        op = random.choice(['+', '-', '*', '/'])
        if op == '-':
            if num1 < num2:
                num1, num2 = num2, num1
        elif op == '/':
            if num1 == 0:
                num1, num2 = num2, num1
        return num1, op, num2

    def check_answer(self, num1, op, num2, answer):
        if op == '+':
            if num1 + num2 == answer:
                return True
        elif op == '/':
            if num1 / num2 == answer:
                return True
        elif op == '*':
            if num1 * num2 == answer:
                return True
        else:
            if num1 - num2 == answer:
                return True
        return False

    def counter(self):
        count_right = 0
        count = 0
        count_wrong = 0
        while count_right < self.count_max:
            count += 1
            num1, op, num2 = self.generate_question()
            print(f"第{count}题: {num1} {op} {num2} = ", end="")
            answer = input().strip()
            try:
                answer = int(answer)
            except:
                print("请输入整数！")
                continue
            if not self.check_answer(num1, op, num2, answer):
                print("很遗憾，答错了！")
                count_wrong += 1
                if count_wrong == 5:
                    print(f"答错五次,答案是{num1}{op}{num2}={answer}")
                    break
            else:
                print("恭喜你，答对了！")
                count_right += 1
        print(f"共{count}题，你答对了{count_right}题！")


homework = Homework(3)
homework.counter()
