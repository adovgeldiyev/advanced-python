
def main():
    import random
    def startAmount(balance):
        while True:#using loop to continuously execute body
            try:#handling errors with try except to work function properly
                amount=eval(input("Enter bet: "))#evaluating amounts entered
                if amount<=0 or amount>balance:
                    print("Invalid amount. Place a valid amount")
                else:
                    return amount
            except:
                print("Invalid input. Try again.")

    def again():#implementing new function to repeat the game
        while True:
            play=input("Play second roll?(y/n): ")
            if play=='y'.lower():
                return 'y'
            elif play=='n'.lower():
                return 'n'
            else:
                print("Invalid choice. Type y/n only.")
        
    def randomNum(count):
        randomNumbers=[]#declaring new random variable
        for _ in range(count):
            randomNumbers.append(random.randint(1,6))
        return randomNumbers

    def current():
        balance=100
        while balance!=0: #checking if not equal to 0 given amount
            betAmount=startAmount(balance)#defining new variable with importing defined function
            dice=randomNum(2)#below sum of 2 rolled dice, and twice amount of bet
            print("Rolled {} and {}. Sum: {}".format(dice[0],dice[1],sum(dice)))
            if sum(dice)==7 or sum(dice)==12:
                print("You won ${}".format(betAmount*2))
                balance+=betAmount
            else:
                play=again()
                if play=='y'.lower() and 2*betAmount<=balance:
                    dice=randomNum(3)
                    print("Rolled {}, {}, {}. Sum: {}".format(dice[0], dice[1], dice[2], sum(dice)))
                    if sum(dice)==7 or sum(dice)==12:
                        print("You won ${}".format(betAmount*2))
                    else:
                        print("You lost")
                        balance-=2*betAmount
                else:
                    print("Thanks for playing")
                    balance-=betAmount
            print("Current amount ${}".format(balance))
    current()
    print("Thanks for playing!")

if __name__=="__main__":
    print("problem_3.py is being run directly")
