
print("############################################################")
print("                   WELCOME TO DO LIST!!                                             ")
print("############################################################")
todoli = []
stop = True
while (stop):
    print("1. Todo list 추가\n2. Todo list 삭제\n3. 프로그램 종료")
    act = input("행동을 선택해주세요(1~3) : ")
    while True:
        if (act == "1"):
            if len(todoli) == 5:
                print("Todo list는 최대 5개까지 작성 가능합니다. Todo list를 삭제해주세요.초기화면으로 돌아갑니다.")
                break
            else:
                add_todo = input("Todo를 입력해주세요 : ")
                todoli.append(add_todo)
                print("추가되었습니다.")
                print(todoli)
                act2 = input("계속 하시겠습니까?(Y/N) : ")
                if (act2.casefold() == "y"):
                    act = "1"
                elif (act2.casefold() == "n"):
                    break
        elif (act == "2"):
            if len(todoli) == 0:
                print("Todo list 목록이 없습니다. 초기화면으로 돌아갑니다.")
                break
            else:
                del_todo = input("삭제하고 싶은 Todo의 번호를 입력해주세요 : ")
                todoli.pop(int(del_todo))
                print(todoli)
                act2 = input("계속 하시겠습니까?(Y/N) : ")
                if (act2.casefold() == "y"):
                    act = "1"
                elif (act2.casefold() == "n"):
                    break
        elif (act == "3") :
            print("프로그램을 종료합니다.\n")
            stop=False
            break
        else:
            print("잘못된 입력값입니다. 다시 입력해주세요.\n")
            break
        

print("\n############################################################")
print(todoli)
print("############################################################")



