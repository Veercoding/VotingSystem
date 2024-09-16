#First we will take input of what nominee what we want to keep
nominee1 = input("Enter the first nominee name: ")
nominee2 = input("Enter the second nominee name: ")
nominee3 = input("Enter the third nominee name: ")


#intially vote count for both must be 0
nm1_votes = 0
nm2_votes = 0
nm3_votes = 0

voter_id = [1,2,3,4,5,6,7,8,9,10]

no_of_voter = len(voter_id)


while True:
    if voter_id == []: # to check when voter list is complete
        print("Voting session is over")
        if nm1_votes > nm2_votes:
            percent= (nm1_votes/no_of_voter)*100
            print(nominee1, "has won the election with", percent, "% of votes")
            break
        elif nm2_votes> nm1_votes:
            percent= (nm2_votes/no_of_voter)*100
            print(nominee2, "has won the election with", percent, "% of votes")
            break
        else:
            print("Both the nominees have same votes")
            break






    voter = int(input("Enter the voter id: "))
    if voter in voter_id:
        print("you are a voter")
        voter_id.remove(voter)
        print("--------------------------------------")
        print("To give vote to,",nominee1,"press 1")
        print("To give vote to,",nominee2,"press 2")
        print("To give vote to,",nominee3,"press 3")
        print("--------------------------------------")
        vote = int(input("Enter your vote: "))
        if vote == 1:
            nm1_votes += 1
            print(nominee1, "thanks for your vote")
        elif vote == 2:
            nm2_votes += 1
            print(nominee2, "thanks for your vote")
        elif vote > 2:
            print("check your pressed key")
        else :
            print("you are not a voter OR you have already voted")
           

