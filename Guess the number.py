import random
list = [1,2,3,4,5,6,7,8,10]
com_choose = int(random.choice(list))
score = 10
chan = 10
game_over = 0
sec_error = False
third_error = False

while(True):
    print("Enter your number between 1-10:-")
    user_inp = int(input())
    if user_inp>10:
        print("Inavild Number")
        break

    if com_choose == user_inp and chan != game_over:
        print("Congrate! You enter the correct one...")
        chan -= 1
        print("Your score is ",score)
        break

    else:
        sec = False
        third = False
        four = False
        five = False
        alldone = True
        alldone2 = True
        if sec_error:
            list_err = [1,2,3,4]
            com_like = random.choice(list_err)
            if com_like==1:
                sec = True

            elif com_like==2:
                third = True
            elif com_like==3:
                four =True
            else:
                five =True
        if sec and chan != game_over:
            if com_choose == 0:
                ly2 = com_choose + 3
                print("The expected Number is lay between", 0, "-", ly2)
                score -= 1
                chan -= 1
                print("chance Left=", chan)
                alldone = False
            if com_choose> 7 :
                ly1 = com_choose - 3
                print("The expected Number is lay between", ly1, "-", 10)
                score -= 1
                chan -= 1
                print("chance Left=", chan)
                alldone = False
            if alldone:
                ly1 = com_choose - 3
                ly2 = com_choose + 3
                print("The expected Number is lay between", ly1, "-", ly2)
                score -= 1
                chan -= 1
                print("chance Left=", chan)


        elif third and chan != game_over:
            if com_choose==0:
                ly2 = com_choose + 3
                print("The expected Number is lay between", 0, "-", ly2)
                score -= 1
                chan -= 1
                print("chance Left=", chan)
                alldone2 = False
            if com_choose>7:
                ly1 = com_choose - 3
                print("The expected Number is lay between", ly1, "-", 10)
                score -= 1
                chan -= 1
                print("chance Left=", chan)
                alldone2 = False
            if alldone2:
                ly1 = com_choose - 3
                ly2 = com_choose + 3
                print("The expected Number is lay between", ly1, "-", ly2)
                score -= 1
                chan -= 1
                print("chance Left=", chan)

        elif four and chan != game_over:
            print("The percentage of Your number with expected number is ",user_inp/com_choose*100)
            score -= 1
            chan -= 1
            print("chance Left=", chan)
        elif five and chan != game_over:
            print("The average of three consecutive number and total Four number, In which starting with your number and Addition include expected Number ",(user_inp+user_inp+1+user_inp+2+com_choose)/4)
            score -= 1
            chan -= 1
            print("chance Left=", chan)
        elif user_inp>com_choose and chan != game_over:
            print("Enter number is Greater than expectation")
            score -= 1
            chan -= 1
            print("chance Left=", chan)
            sec_error = True
        elif user_inp<com_choose and chan != game_over:
            print("Enter number is samller than expectation")
            score -= 1
            chan -= 1
            print("chance Left=", chan)
            sec_error = True
        else:
            print("Game Over")
            print('SCORE IS', score)
            print("chance Left=", chan)
            break

