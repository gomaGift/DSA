def potentialOfWinningPlayer(arr, k):
    prevWinner = None
    decidingFactor = 0
    curr_winner = None
    while decidingFactor < k:
        
        player1 = arr[0]
        player2 = arr[1]
        if player1 > player2:
           curr_winner = player1
           arr.remove(player2)
           arr.append(player2)
        else:
            curr_winner = player2
            arr.remove(player1)
            arr.append(player1)

        if not prevWinner:
            decidingFactor += 1
        elif curr_winner == prevWinner:
             decidingFactor +=1
        prevWinner = curr_winner
    return curr_winner




print(potentialOfWinningPlayer([3,2,1,4], 2))
        


    