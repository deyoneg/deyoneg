def probability(dice_number, sides, target):
    # 1,2,3,4,5,6,7,8,9,10
    # 1,2,3,4,5,6,7,8,9,10
    # 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20

    # 1,2,3,4,5,6
    # 1,2,3,4,5,6
    # 1,2,3,4,5,6,7,8,9,10,11,12

    # 1,2,3,4,5
    # 1,2,3,4,5

    # 1, 2,3,4,5, 6 ,7,8,9,10

    chance1Dice = 1 / sides
    chance2Dice = chance1Dice*chance1Dice
    chans = [1/sides if x<sides else 0 for x in range(target - 1)]
    ch=[]
    for i in range(dice_number-1):
        
        for o in range(len(chans)):
            c=0
            o=o+1
            for z in chans[o:]:
                c += z * chance1Dice
            ch.append(c)
        print (ch)
        chans=ch


    # combos2Dice = sides - abs(sides + 1 - target)
    # chanceTargetDice = combos2Dice * chance2Dice
    # ch = []
    
    # for y in range(target - 1):
    #     combos2Dice = sides - abs(sides + 1 - target - y)
    #     ch.append(combos2Dice * chance2Dice)
    # print (str(ch))

    # chout = 0
    # ch3=[]
    # for i in range(dice_number - 2):

    #     for o in range(len(ch)-1+i):
    #         chout = 0
    #         o=o+1
    #         for z in ch[o:]:
    #             chout += z * chance1Dice
    #         ch3.append(chout)
    #     ch=ch3
    #     print(ch)
 

        
    # print(ch[0])
    # return ch[0]

if __name__ == "__main__":
    # These are only used for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision
    # assert almost_equal(probability(2, 6, 3), 0.0556), "Basic example"
    # assert almost_equal(probability(2, 6, 4), 0.0833), "More points"
    # assert almost_equal(probability(2, 6, 7), 0.1667), "Maximum for two 6-sided dice"
    # assert almost_equal(probability(2, 3, 5), 0.2222), "Small dice"
    # assert almost_equal(probability(2, 3, 7), 0.0000), "Never!"
    #assert almost_equal(probability(3, 6, 7), 0.0694), "Three dice"
    assert almost_equal(probability(3, 6, 15), 0.0463), "f"
   # assert almost_equal(probability(10, 10, 50), 0.0375), "Many dice, many sides"

