def updatescores():
    global scoresNum
    global scores
    scores = []
    scoresTxt = open("highScores.txt")
    scoresBeforeReplace = open("highScores.txt").readlines()
    scoresLines = [x.replace('\n', '') for x in scoresBeforeReplace]
    scoresNum = len(scoresBeforeReplace)/2
    scoresStep = -1
    while scoresStep < int(scoresNum) - 1:
        scoresStep = scoresStep + 1
        lineToAdd = scoresStep * 2
        scores.append([scoresLines[lineToAdd + 0], scoresLines[lineToAdd + 1]])
    scores.sort(reverse=True)

def updateQuestions():
    global questionsNum
    global questions
    questions = []
    questionsTxt = open("questions.txt")
    questionsBeforeReplace = open("questions.txt").readlines()
    questionsLines = [x.replace('\n', '') for x in questionsBeforeReplace]
    questionsNum = len(questionsBeforeReplace)/5
    questionsStep = -1
    while questionsStep < questionsNum - 1:
        questionsStep = questionsStep + 1
        lineToAdd = questionsStep * 5
        questions.append([questionsLines[lineToAdd + 0], questionsLines[lineToAdd + 1], questionsLines[lineToAdd + 2], questionsLines[lineToAdd + 3], questionsLines[lineToAdd + 4]])

def startQuizStep():
    global step
    global score
    step = -1
    score = 0
    startQuiz()

def startQuiz():
    global step
    global score
    while step < questionsNum - 1:
        step = step + 1
        print("\nQuestion " + str(step + 1) + ":\n" + questions[step][0] + "           Score: " + str(score) + "\n        A: " + questions[step][1] + "\n        B: " + questions[step][2] + "\n        C: " + questions[step][3])
        inputAnswers = input("Please enter A, B or C\n")
        if inputAnswers.lower() == questions[step][4]:
            score = score + 1
            print("Correct! Your score is: "+ str(score))
        else:
            if inputAnswers.lower() == "a" or inputAnswers.lower() == "b" or inputAnswers.lower() == "c":
                print("Incorrect! The answer was " + questions[step][4].upper() + ". Your score is " + str(score) + "!")
            else: 
                if inputAnswers.lower() == "exit":
                    if askExit() == False:
                        step = step - 1
                        startQuiz()
                else:
                    print("ERROR: Please enter A, B or C")
                    step = step - 1
    saveScore()

def saveScore():
    scoreInput = input("\n\nYou finished the quiz!\nYour score was " + str(score) + "!\nWould you like to save your score into the high scores?\n(Y or N)\n")
    if scoreInput.lower() == "y":
        scoreInputName = input("What is your name?\n")
        scores.append([str(score), scoreInputName])
        updateScoreStep = -1
        scoresToWrite = []
        while updateScoreStep < int(scoresNum):
            updateScoreStep = updateScoreStep + 1
            if updateScoreStep == int(scoresNum):
                scoresToWrite.append(scores[updateScoreStep][0] + "\n")
                scoresToWrite.append(scores[updateScoreStep][1])
            else:
                scoresToWrite.append(scores[updateScoreStep][0] + "\n")
                scoresToWrite.append(scores[updateScoreStep][1] + "\n")
        scoresTxt = open("highScores.txt", "w")
        scoresTxt.writelines(scoresToWrite)
        scoresTxt.close()
        updatescores()
        start()
    else:
        if scoreInput.lower() == "n":
            start()
        else:
            print("ERROR: Please enter Y or N")
            saveScore()

def startQuizIntro():
    inputStart = input("Welcome! This quiz isn't CaSe SEnS1t1VE.\nAt any point in the quiz, type 'Exit' to leave\nAre you ready to start?\n(Y or N)\n")
    if inputStart.lower() == "y":
        startQuizStep()
    else:
        if inputStart.lower() == "n":
            start()
        else:
            if inputStart.lower() == "exit":
                if askExit() == False:
                    startQuizIntro()
            else:
                print("ERROR: Please enter Y or N")
                startQuizIntro()

def start():
    inputMenu = input("Welcome to my quiz!\nWhere would you like to go?\n(S - Start quiz, SB - View scoreboard, E - Exit)\n")
    if inputMenu.lower() == "s":
        startQuizIntro()
    else:
        if inputMenu.lower() == "sb":
            showScores()
        else:
            if inputMenu.lower() == "e":
                if askExit() == False:
                    start()
            else: 
                print("ERROR: Please enter S, SB or E")
                start()

def showScores():
    print("Name - Score")
    scoresStep = -1
    while scoresStep < scoresNum - 1:
        scoresStep = scoresStep + 1
        print(scores[scoresStep][1] + " - " + scores[scoresStep][0])
    scoresInput = input("Would you like to go back?\n(Y or N)\n")
    if scoresInput.lower() == "y":
        start()
    else:
        if scoresInput.lower() == "n":
            showScores()
        else:
            print("ERROR: Please enter Y or N")
            showScores()

def askExit():
    inputExit = input("Are you sure you want to exit?\n(Y - Yes, N - No)\n")
    if inputExit.lower() == "y":
        exit()
    else: 
        if inputExit.lower() == "n":
            return False
        else:
            print("ERROR: Please enter Y or N")
            askExit()

updateQuestions()
updatescores()
start()
