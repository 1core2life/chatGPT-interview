import os
import sys
import openai


class ChatGPTInterview():
    def __init__(self, key):
        self.answer = "[CHAT]"
        self.job = ["Frontend Engineering", "Backend Engineering", "Devops Engineering", "Data Engineering"]
        self.job_input = 0
        self.language = 0
        openai.api_key = key

    def print_language(self):
        print("\n**************************************")
        print("Choose Langauge")
        print("1. Korean")
        print("2. English")
        print("**************************************")
        self.language = int(input(">> ")) - 1
        os.system('clear')


    def print_summary(self):
        print("\n**************************************")
        if self.language == 0:
            print("GPT 모의 면접에 오신 것을 환영합니다.")
            print("지원하시는 직무의 숫자를 입력 해주세요.")
        else:
            print("Welcome to GPT virtual interview.")
            print("Enter number for job group")
        print()
        print(" 1. {0} ".format(self.job[0]))
        print(" 2. {0} ".format(self.job[1]))
        print(" 3. {0} ".format(self.job[2]))
        print(" 4. {0} ".format(self.job[3]))
        print("**************************************")
        self.job_input = int(input(">> ")) - 1
        os.system('clear')

    def start_interview(self):
        content = "I want you to act as an {0} tech interviewer.\
                    I will be the junior candidate and you will ask me the interview questions for the position position.\
                    I want you to only reply as the interviewer. Do not write all the conservation at once.\
                    I want you to only do the interview with me. Ask me the only one question and wait for my answers.\
                    Ask me first about tech knowledge about {1}.\
                    When an interviewee mentions a particular skill, ask a detailed question about it.\
                    Do not write explanations. Ask me the questions one by one like an interviewer does and wait for my answers.".format(self.job[self.job_input], self.job[self.job_input])
        if self.language == 0:
            print("{0} 직무에 대한 모의 면접을 진행하겠습니다. 잠시만 기다려 주세요.".format(self.job[self.job_input]))
            content += "Speak language only korean. Do not speak english"
        else:
            print("Starting virtual interview for {0}. Please wait a moment".format(self.job[self.job_input]))
            

        messages = [{"role": "system", "content": content}]

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        print()
        print("{0}".format(self.answer), response.choices[0].message.content)
        messages.append({"role": "assistant", "content": response.choices[0].message.content})

        while True:
            print()
            print()

            user_input = input(">> ")

            print()
            print()
            user_input = user_input.lower()
            if user_input == "exit":
                break
            else:
                messages.append({"role": "user", "content": user_input})

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )

            messages.append({"role": "assistant", "content": response.choices[0].message.content})

            print("{0}".format(self.answer), response.choices[0].message.content)



def main(key):
    gpt = ChatGPTInterview(key)
    gpt.print_language()
    gpt.print_summary()
    gpt.start_interview()


if __name__ == '__main__':
    main(sys.argv[1])