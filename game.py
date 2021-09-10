import random
print('welcome to my computer basics test')
playing = input('do you want to play? ')

if playing != 'yes':
    quit()
elif playing == 'yes':
    print('Lets start, I do hope you studied')

print('this test consists of 10 simple computer basics questions')
print('at the end there is a way to bring you grade up but..... its interesting')

start = input('type continue to start ')
if start != 'continue':
    print('Cya another day')
    quit()

#question one
print('to start off easy, lets start with a clasic.')
print('which of all of these is the main component that powers the whole computer?')
print('A. GPU')
print('B. CPU')
print('C. PSU')
print('D. MOBO')
print('E. none of the above')

answer_for_question_1 = input('A, B, C, D, or E?')
if answer_for_question_1 != 'C':
    print('well, better luck next time.')
    print('Take the L for now')
elif answer_for_question_1 == 'C':
    print('interesting response.')
    print('guess youll have to wait till the end to find out if youre right:)')

#question 2

print('moving on to the next question')

print('this is a simple one')
print('what is the component that takes charge of all the Graphics?')
print('A. Power Supply')
print('B. CPU')
print('C. Graphics Card')
print('D. Motherboard')
print('E. None of the above')

answer_for_question_2 = input('A, B, C, D, or E?')
if answer_for_question_2 != 'C':
    print('Man, it even says it in its name......')
    print('You really get the biggest L in history')
elif answer_for_question_2 == 'C':
    print('Well this one was very easy so dont get excited')
    print('just making sure you atleast dont get a 0')

print('well either way lets move on to the next question')

#question 3

print('just sayin, this one will really mess you up if you arent a computer nerd')
print('what is the theoretical most powerfull GPU available?')
print('A. RTX')
print('B. Quadro')
print('C. GT')
print('D. Titan')
print('E. GTX')

answer_for_question_3 = input('A, B, C, D, or E?')
if answer_for_question_3 != 'B':
    print('well... you aint a nerd I can tell')
    print('just makin shure you dont get that 100 HEH:)')
elif answer_for_question_3 == 'B':
    print('WASSUP NERDDDDDD')
    print('it was quite easy, you just had to have basic Nvidea knowledge')

print('well after that some of you dont got that perfect score anymore so ignoring')
print('that, lets move on to the next question')

#question 4
print('after the last one I think you dserve a free one...')
print('yea.... not hapinin, so lets ruin that score even more with another hard question')
print('in a laptop, what does a processor with 5 numbers and HK followed by it mean?')
print('(this is sure to mess up even some big nerds)')
print('A. Its good')
print('B. its bad')
print('C. its got 5 cores')
print('D. it can overclock')
print('E. its fast af')

answer_for_question_4 = input('A, B, C, D, or E?')
if answer_for_question_4 != 'D':
    print('well, you arent a nerd thats for sure')
    print('anyways lets move on')
elif answer_for_question_4 == 'D':
    print('Biggest nerd in history right here')
    print('anyways lets move on')

#question 5
print('im running out of ideas on what to put here so.... dont expect too much anymore')
print('anyways this question is one of my favs')
print('its easy but u have to have basic intel knowledge')
print(' ')
print('Truth or False?')
print('a Core-i3 cant be better than a Core-i7')
print('A. True')
print('B. False')

answer_for_question_5 = input('A or B? ')
if answer_for_question_5 != 'B':
    print('better luck next time:/')
    print('anyways lets move on')
elif answer_for_question_5 == 'B':
    print('U prolly guessed, or you knew it. Idk, cant read your face')
    print('anyways lets move on')

#question 6
print('So this is an easy one')
print('you just have to have processor knowledge(again)')
print('Which of these 2 campanies is the one that has been on top of the CPU market for the past 20 years?')
print('A. AMD')
print('B. Intel')

answer_for_question_6 = input('A or B? ')
if answer_for_question_6 != 'B':
    print('AMD only peaked about once above intel in the past 20 years')
    print('just sayin, pay attention to your history classes')
elif answer_for_question_6 == 'B':
    print('So.... you know your history')
    print('anyways lets move on')

#question 7
print('a simple storage question')
print('which of these components is responsible for storage?')
print('A. RAM')
print('B. CHASIS')
print('C. SSD')
print('D. CPU')

answer_for_question_7 = input('A, B, C, or D?')
if answer_for_question_7 != 'C':
    print('you should go watch a quick youtube video after this')
    print('anyways moving on')
elif answer_for_question_7 == 'C':
    print('easyyyyyy one right')
    print('movin on')

#question 8
print('this one has a bit of connection with the last one')
print('after the last one, what do you think SSD means?')
print('A. Silent Saturation device')
print('B. Solid state drive')
print('C. Stealth simulative device')
print('D. Saturative state Drive')

answer_for_question_8 = input('')
if answer_for_question_8 != 'B':
    print('Man, I even told you it had to do with the last one')
    print('how could you get it wrong???')
elif answer_for_question_8 == 'B':
    print('yea it was easy')
    print('I ran out of ideas for the other options')

print('anyways moving on')

#question 9
print('k so this is another easy one')
print('what si the most popular graphics card on the market?')
print('A. 1660 SUPER')
print('B. RTX 3080')
print('C. RTX 3090')
print('D. RTX 3070')

answer_for_question_9 = input('A, B, C, or D')
if answer_for_question_9 != 'C':
    print('Man thats ez, you takin a big L again')
    print('anywasy movin on to the last question')
elif answer_for_question_9 == 'C':
    print('told ya it was easy')
    print('movin on to the next question')

#question 10
print('so this is the last question so it has to be super speacial')
print('What year was Nvidia Founded?')
print('A. 1999')
print('B. 1990')
print('C. 1996')
print('D. 1993')

answer_for_question_10 = input('A, B, C, or D')
if answer_for_question_10 != 'D':
    print('yea that was a hard one so i dont blame you for it')
    print('tho im glad u didnt search it up')
elif answer_for_question_10 == 'D':
    print('YOOOOOOOOOOO ur going in history books one day')
    print('or you searched it up....... anyways lets continue')

#-----------------------------------------------------------------------------------------------------------------------

#endgame decider
print('well congrats, you finnished')
print('Lets see how bad you did:)')

value_for_question_1 = False
value_for_question_2 = False
value_for_question_3 = False
value_for_question_4 = False
value_for_question_5 = False
value_for_question_6 = False
value_for_question_7 = False
value_for_question_8 = False
value_for_question_9 = False
value_for_question_10 = False

if answer_for_question_1 == 'C':
    value_for_question_1 = True

if answer_for_question_2 == 'C':
    value_for_question_2 = True

if answer_for_question_3 == 'B':
    value_for_question_3 = True

if answer_for_question_4 == 'D':
    value_for_question_4 = True

if answer_for_question_5 == 'B':
    value_for_question_5 = True

if answer_for_question_6 == 'B':
    value_for_question_6 = True

if answer_for_question_7 == 'C':
    value_for_question_7 = True

if answer_for_question_8 == 'B':
    value_for_question_8 = True

if answer_for_question_9 == 'C':
    value_for_question_9 = True

if answer_for_question_10 == 'D':
    value_for_question_10 = True


#devaluation variable
devaluation = 0
#variable to start the grade
finnal_grade_before_devaluation = 100

if value_for_question_1 == False:
    devaluation += 10

if value_for_question_2 == False:
    devaluation += 10

if value_for_question_3 == False:
    devaluation += 10

if value_for_question_4 == False:
    devaluation += 10

if value_for_question_5 == False:
    devaluation += 10

if value_for_question_6 == False:
    devaluation += 10

if value_for_question_7 == False:
    devaluation += 10

if value_for_question_8 == False:
    devaluation += 10

if value_for_question_9 == False:
    devaluation += 10

if value_for_question_10 == False:
    devaluation += 10

finnal_grade = finnal_grade_before_devaluation - devaluation
#---------------------------------------------------------------------------------------------------------------------
if finnal_grade <= 60:
    print('well just sayin your grade aint lookin too good')

if finnal_grade >= 60:
    print('your grade lookin... decent')

print('this is your grade')
print(finnal_grade)

#---------------------------------------------------------------------------------------------------------------------
#grade fixing

print('remember how i said you had an interesting way to fix your grade?')
print('well this is how this will work')
print('there is a random number generator here. you will be able to try to guess the number 1-9')
print('if you guess it correctly your finnal grade will go up 15 points')
print('tho one you use it your finnal grade goes down 5 points')
print('so teachnicaly your just earning 10 points')
print('either way type continue if you want to do this or type leave to stop the test')
value_continue = input('')
if value_continue != 'continue':
    quit()
elif value_continue == 'continue':
    print('well then lets start')

random_number = random.randint(1, 9)
guess = input('type a number 1-9 ')
if guess == random_number:
    print('turns out lucks on your side today')
    finnal_grade += 10
elif guess != random_number:
    finnal_grade - 5
print('this is now your actual finnal grade')
print(finnal_grade)