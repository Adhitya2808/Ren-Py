# Define Character:
define Robert   = Character("Robert")
define Teacher  = Character("Mrs.Catherine")
define Mother   = Character("Lucy (Mother)")
define Clara    = Character("Clara (Sister)")
define Student  = Character("Student")
define Stranger = Character("????")
define Player   = Character("[P]")

# Define emotion:
# Robert:
image RNormal   = ("Robert_Smile1.png")
image RSad      = ("Robert_Sad.png")
image RSmile    = ("Robert_Smile2.png")

# Catherine:
image CatNormal = ("Catherine_normal.png")
image CatSmile  = ("Catherine_Smile.png")
image CatSad    = ("Catherine_Sad.png")

# Clara:
#Sekolah:
image CNromal   = ("clara_normal.png")
image CMad      = ("clara_mad.png")
image CSmile    = ("clara_smile.png")
image CSleepy   = ("clara_sleepy.png")
image CDelight  = ("clara_delighted.png")


# lucy:
#rumah:
image LNormal   = ("Lucy_Normal.png")
image LSad      = ("Lucy_Sad.png")
image LSmile    = ("Lucy_Smile.png")

# Define Background:
# Transisi Chapter:
image chapter1  = ("chapter1.png")
image chapter2  = ("chapter2.png")
image chapter3  = ("chapter3.png")
image end       = ("ending.png")

# Di Sekolah:
image classroom = ("Classroom_Day.png")
image Cafetaria = ("Cafeteria_Day.png")
image Dsekolah  = ("School_Hallway_Day.png")

# Di Rumah:
image RTamupagi     = ("Livingroom_Day.png")
image RTamumalam    = ("Livingroom_Night.png")
image Rtidurpagi    = ("Bedroom_Day.png")
image Rtidursore    = ("Bedroom_Evening.png")
image Rtidurmalam   = ("Bedroom_Night.png")

init :
    $ skor = 0

label start:
#Scene Chapter1:
    show chapter1 with fade
    with Pause(1.5)
    ""
    hide chapter1 with fade
    show classroom
    with Pause(1.5)
    play music "1_Menu_Master.mp3" fadeout 1.0 fadein 1.0 volume 0.1
    "Teacher Enters the Class"
    show CatNormal at right with moveinright
    play sound "Teacher1-1.mp3" 
    Teacher "Good Morning Class"
    stop sound 
    play sound "student1-1.mp3"
    Student "Good Morning Mrs" 
    stop sound
    hide CatNormal
    show CatSmile at right
    play sound "Teacher1-2.mp3"
    Teacher "Before we start study. we have a new friend, please come in and introduce yourself"
    stop sound
    "You Come to Class"
    $P = renpy.input("Enter Your Name")
    Player "Hello everyone, my name is [P] I just moved to this city because my father started working here, nice to meet you all"
    play sound "student1-2.mp3"
    Student "hi [P] nice to meet you too"
    stop sound
    play sound "Teacher-seat.mp3"
    Teacher "[P] you can seat in there"
    stop sound
    "You seat in empty chair"
    hide CatSmile
    show CatNormal at right
    play sound "Teacher-occupation.mp3"
    Teacher "let's continue our lessons and now we learn about occupation"
    stop sound
#Scene Contoh Materi Ch1
    play sound "TeacherSoal1-1.mp3"
    menu soal1:
        Teacher "Fixing a car is a job for..."
        "Pilot":
            stop sound
            show CatSad at right
            play sound "wrong-answer.mp3"
            Teacher "Wrong answer"
            stop sound
            hide CatSad
            jump soal1
        "Mechanic":
            stop sound
            play sound "good-answer.mp3"
            Teacher "good, your answer is correct"
            stop sound
            play sound "TeacherSoal1-2.mp3"
            jump soal2

    menu soal2:
        Teacher "next, Adjudicating cases and determining sentence terms is a job for.. "
        "judje":
            stop sound
            play sound "good-answer.mp3"
            Teacher "good, your answer is correct"
            stop sound
            play sound "TeacherSoal1-3.mp3"
            jump soal3
        "Doctor":
            stop sound
            show CatSad at right
            play sound "wrong-answer.mp3"
            Teacher "Wrong answer"
            stop sound
            hide CatSad
            jump soal2
        
    menu soal3:
        Teacher "next, Controlling an airplane is a job for.."
        "Pilot":
            stop sound
            play sound "good-answer.mp3" 
            Teacher "good, your answer is correct"
            stop sound
        "Driver":
            show CatSad at right
            stop sound
            play sound "wrong-answer.mp3"
            Teacher "Wrong answer"
            stop sound
            hide CatSad
            jump soal2
        
    "You Follow the lessons in Class Until Break Time"
    play sound "SchoolBel.mp3"
    "Break Time"
    with Pause (0.11)
    play sound "Teacher1-3.mp3"
    Teacher "since it's already break time, I think I can finish our lesson this time. Don't be late for class after break time"
    stop sound
    play sound "student1-3.mp3"
    Student "yes mrs. Thank you"
    stop sound
    play sound "Teacher1-4.mp3"
    Teacher "you're welcome"
    stop sound
    "Mrs.Catherine Left the class"
    hide CatNormal with fade
    show RNormal at left with moveinright
    play sound "Robert1-1.mp3"
    Stranger "Hello, My Name is Robert. nice to meet you"
    stop sound
    Player "Hi Robert, Nice to meet you too"
    play sound "Robert1-2.mp3"
    Robert "By the way, where are you from?"
    stop sound
    $D = renpy.input("Enter Your Region")
    Player "I come from [D]"
    play sound "Robert1-3.mp3"
    menu alur1:
        Robert "after this do you have free time?"
        "Yes, I have free time":
            jump opsi1
        "Sorry, I'm busy after this ":
            hide RSmile
            hide RNormal
            show RSad at left
            play sound "Robert1-4Sad.mp3"
            Robert "Oh, Okay see you later"
            stop sound
            hide RSad at left with fade
            "Robert also left you"
            play sound "SchoolBel.mp3"
            "The class bell rings"
            with Pause (0.11)
            stop sound
            jump endch1
    label opsi1:
        hide RNormal    
        show RSmile at left
        play sound "Robert1-4Happy.mp3"
        Robert "nice, I'll show you around this school"
        stop sound
        play sound "Robert1-5.mp3"
    menu alur2:
        Robert "first, you want to go to cafeteria or school yard?"
        "School Yard":
            play sound "Robert1-6.mp3"
            Robert "Okay follow me"
            stop sound
            jump SchoolYard
            "you also follow Robert"
            hide classroom
        "Cafetaria":
            play sound "Robert1-6.mp3"
            Robert "Okay follow me"
            stop sound
            jump Cafetaria
            "you also follow Robert"
            hide classroom

    label SchoolYard:
        show Dsekolah
        hide RSmile
        "You and Robert arrive at the Schoolyard"
        show RNormal at left with moveinright
        play sound "Robert1-7Schoolyard.mp3"
        Robert "this is the school yard, usually if there is a sports class then we will gather in the school yard for sports"
        stop sound
        Player "ohh... okay"
        play sound "Robert1-8Schoolyard.mp3"
        Robert "By the way. Are you hungry?"
        stop sound
        Player "Yes, I'm Hungry"
        hide RNormal
        show RSmile at left
        play sound "Robert1-9Schoolyard.mp3"
        Robert "let's go to the school cafeteria. follow me"
        stop sound
        Player "Sure"
        hide RSmile at left
        hide Dsekolah
        "You and Robert walk towards the cafeteria"
        jump Cafetaria

    label Cafetaria:
        hide RSmile at left
        show Cafetaria
        show RNormal at left with moveinright
        show CNromal at right with moveinright
        play sound "Clara1.mp3"
        Stranger "hi [P]"
        stop sound
        Player "Hello Clara, what are you doing in here?"
        hide CNromal
        show CMad at right
        play sound "Clara1-2.mp3" 
        Clara  "hmph, of course I want to eat with you"
        stop sound
        Player "hehe, don't be mad sister"
        play sound "Robert1-7Cafetaria.mp3"
        Robert "who is this girl? [P]"
        stop sound
        Player "owh, let me introduce to you, this is clara my elder sister"
        play sound "Robert1-8Cafetaria.mp3"
        hide RNormal
        show RSmile at left
        Robert "nice to meet you clara, my name is robert. I was a classmate with your little brother"
        stop sound
        hide CMad
        show CSmile at right
        play sound "Clara1-3.mp3"
        Clara "nice to meet you too Robert. please take care my little brother"
        stop sound
        play sound "Robert1-9Cafetaria.mp3"
        Robert "Sure"
        hide RSmile
        show RNormal at left
        stop sound
        hide CSmile
        show CNromal at right
        play sound "SchoolBel.mp3"
        "The class bell rings"
        with Pause (0.11)
        Player "oh no... The bell has rung, let's go back to class"
        play sound "Clara1-4.mp3"
        Clara "okay"
        stop sound
        play sound "RObert1-10Cafetaria.mp3"
        Robert "okay"
        stop sound
        hide CNromal with fade
        hide RNormal with fade
        "Clara also left you. You and Robert head back to class"
        hide Cafetaria with fade
        jump endch1

    label endch1:
        show classroom with fade 
        with Pause(1.5)
        show CatSmile at right with moveinright
        play sound "Teacher1-5.mp3"
        Teacher "are any of your friends still outside?"
        Student "No Mrs"
        hide CatSmile
        show CatNormal at right
        play sound "Teacher1-6.mp3"
        Teacher "okay, if everything is in. let's continue our lesson today"
        stop sound
        Student "yes Mrs"
#Scene soal Chapter1
        play sound "TeacherLatihan1.mp3"
        Teacher "now I will give an exercise about occupations names"
        stop sound
        label Tugas:
        menu:
            "What do you call a person who treats patients and prescribes medication?"
            "Doctor":
                $ skor += 10
                jump latihan2
            "Lawyer":
                "wrong answer"
                jump latihan2

        menu latihan2:
            "Who is responsible for maintaining the financial records of a company?"
            "Actor":
                "wrong answer"
                jump latihan3
            "Accountant":
                $ skor += 10
                jump latihan3

        menu latihan3:
            "What is the term for someone who designs buildings and oversees their construction?"
            "Web Developer":
                "wrong answer"
                jump latihan4
            "Architect":
                $ skor += 10
                jump latihan4

        menu latihan4:
            "What occupation involves creating and managing websites and online content?"
            "Web Developer":
                $ skor += 10
                jump latihan5
            "Teacher":
                "wrong answer"
                jump latihan5
        
        menu latihan5:
            "What is the term for someone who writes news articles for newspapers or magazines?"
            "Driver":
                "wrong answer"
                jump latihan6
            "Journalist":
                $ skor += 10
                jump latihan6

        menu latihan6:
            "Who is responsible for capturing and editing photographs for various purposes?"
            "Photographer":
                $ skor += 10
                jump latihan7
            "Architect":
                "wrong answer"
                jump latihan7

        menu latihan7:
            "What do you call someone who takes care of people's teeth"
            "Dentist":
                $ skor += 10
                jump latihan8
            "Doctor":
                "wrong answer"
                jump latihan8

        menu latihan8:
            "Who is in charge of performing surgeries in a hospital"
            "Nurse":
                "wrong answer"
                jump latihan9
            "Surgeon":
                $ skor += 10
                jump latihan9

        menu latihan9:
            "What do you call someone who prepares and serves food in a restaurant"
            "Chef":
                $ skor += 10
                jump latihan10
            "Accountant":
                "wrong answer"
                jump latihan10
                                        
        menu latihan10:
            "Who is responsible for repairing and maintaining electrical systems in buildings?"
            "Teacher":
                "wrong answer"
                jump TotalSkor
            "Electrician":
                $ skor += 10
                jump TotalSkor

        label TotalSkor:
            "Hi [P] Total Skor Latihan pertama anda adalah = [skor]" 
            $ skor = 0
            menu :
                "Apakah anda ingin mengulang latihan"
                "Iya":
                    jump Tugas
                "Tidak":
                    "You Follow the lessons in Class Until time to go home"
        play sound "SchoolBel.mp3"
        "The class bell rings"
        with Pause (0.11)
        play sound "Teacherlast.mp3"
        Teacher "because the bell has rung. so I'm enough for today lessons and see you tomorrow"
        stop sound
        play sound "student1-3.mp3"
        Student "Okay mrs thank you"
        stop sound
        play sound "Teacher1-4.mp3"
        Teacher "You're welcome"
        hide CatNormal
        hide classroom with fade

#Scene Chapter2:
    show chapter2 with fade
    with Pause(1.5)
    ""
    hide chapter2 with fade
    show RTamumalam
    show CSleepy at left with moveinright
    play sound "Clara2-1.mp3"
    Clara "Phew, finally home! I can't believe how tiring today was" 
    stop sound
    Player "Yeah, I feel the same way, sis. School felt like it lasted forever"
    show LSmile at right with moveinright
    play sound "Mother2-1.mp3"
    Mother "Welcome home, my dear ones! I've prepared some snacks and drinks for you. Sit down and tell me about your day"
    stop sound
    hide LSmile at right with moveinright
    hide CSleepy
    "Clara and You sit on the couch as Mrs. Lucy brings out a tray of snacks and glasses of juice."
    show CSmile at left
    show LSmile at right with moveinright
    play sound "Clara2-2.mp3"
    Clara "Thanks, Mom. You always know how to make us feel better"
    stop sound
    Player "Yeah, Mom, you're the best!"
    hide CSmile 
    show CDelight at left
    play sound "Mother2-2.mp3"
    Mother "Aw, thank you, my little ones. So, tell me, how was your day at school?"
    stop sound
    play sound "Clara2-3.mp3"
    Clara  "Well, Mom, I had a really interesting science experiment in class today. I got to mix different chemicals and observe the reactions."
    stop sound
    Player "It was so cool sister!"
    play sound "Mother2-3.mp3"
    Mother "That sounds amazing! I'm glad you enjoyed it. Science is such an important subject."
    stop sound
    play sound "Clara2-4.mp3"
    Clara  "Yeah, and I also had a math test today. It was a bit challenging, but I think I did okay."
    stop sound
    Player "I was learning about occupation and all my annswer are correct"
    play sound "Mother2-4.mp3"
    Mother "That's the spirit, It's important to seek help when needed. I'm proud of both of you for working hard."
    stop sound
    hide CDelight
    show CNromal at left
    play sound "Clara2-4.mp3"
    Clara  "Mom, did anything interesting happen while we were at school?"
    stop sound
    play sound "Mother2-5.mp3"
    Mother "Well, while you were away, I received a phone call from your father. He will be going home next month"
    stop sound
    hide CNromal
    show CSmile at left
    play sound "Clara2-5.mp3"
    Clara "yes, dad will be home next month. I really miss him"
    stop sound
    Player "me too sis"
    Player "Hoam, I'm very tired. I'm going to the bedroom first"
    play sound "Mother2-6.mp3"
    Mother "See you tomorrow [P]"
    stop sound
    play sound "Clara2-6.mp3"
    Clara "see you tomorrow little brother"
    stop sound
    hide LSmile
    hide CSmile
    "you go to the bedroom"
    hide RTamumalam
    show Rtidurmalam
    Player "fiuh. I can't belive how tired was. I'd better sleep now"
    "you sleep tightly"
    hide Rtidurmalam with fade

#Scene Chapter3:
    show chapter3
    with Pause (1.5)
    ""
    hide chapter3
    "Tomorrow"
    show Rtidurpagi
    Player "I slept well last night"
    play sound "Clara3-1.mp3"
    Clara "little brother, hurry up or we're late for school"
    stop sound
    Player "I better hurry get ready to go to school"
    hide Rtidurpagi
    show RTamupagi
    show CSmile at left with moveinright
    show LSmile at right with moveinright
    Player "Good morning clara, mom"
    play sound "Clara3-2.mp3"
    Clara  "Good morning little brother"
    stop sound
    play sound "Mother3-1.mp3"
    Mother "Good morning, hurry up eat your breakfast and go to school"
    stop sound
    Player "Okay mom"
    play sound "Clara1-4.mp3"
    Clara  "Okay"
    stop sound
    "You and clara finish breakfast"
    Player "Fiuh, I'm very full"
    play sound "Clara3-3.mp3"
    Clara "come on little brother we're going to school or we will be late"
    stop sound
    Player "Okay sis"
    play sound "Mother3-2.mp3"
    Mother "you two, please be careful"
    stop sound
    play sound "Clara3-4.mp3"
    Clara "Yes mom"
    stop sound
    hide CSmile with fade
    hide LSmile with fade
    hide RTamupagi with fade
    "You go to school"
    show classroom
    show CatNormal at right with moveinright
    play sound "Teacher1-1.mp3"
    Teacher "Good morning class"
    stop sound
    play sound "student1-1.mp3"
    Student "good morning mrs"
    stop sound
    play sound "Teachermateri3.mp3"
    Teacher "Today we will learn about conjunction"
    stop sound
    play sound "soal31.mp3"
#Scene Contoh Materi Ch3    
    menu soal31:
        Teacher "Example. She studied hard _____ she passed the exam."
        "Or":
            stop sound
            show CatSad at right
            play sound "wrong-answer.mp3"
            Teacher "Wrong answer"
            stop sound
            hide CatSad
            jump soal31
        "So":
            stop sound
            play sound "good-answer.mp3"
            Teacher "good, your answer is correct"
            stop sound
            play sound "soal32.mp3"
            jump soal32

    menu soal32:
        Teacher "He loves playing soccer.___ He hates basketball."
        "But":
            stop sound
            play sound "good-answer.mp3"
            Teacher "good, your answer is correct"
            stop sound
            play sound "soal33.mp3"
            jump soal33
        "And":
            stop sound
            show CatSad at right
            play sound "wrong-answer.mp3"
            Teacher "Wrong answer"
            stop sound
            hide CatSad
            jump soal32
        
    menu soal33:
        Teacher "I want to eat ice cream, _____ I'm on a diet"
        "So":
            stop sound
            show CatSad at right
            play sound "wrong-answer.mp3" 
            Teacher "wrong answer"
            stop sound
            hide CatSad
            jump soal33
        "But":
            stop sound
            play sound "good-answer.mp3"
            Teacher "good, your answer is correct"
            stop sound
#Scene Soal Chapter3
    play sound "TeacherLatihan3.mp3"
    Teacher "now I will give an exercise about Conjunction"
    stop sound
    label Tugas3:
        menu:
            "I will buy a new car.___ I will save more money."
            "Or":
                "Wrong answer"
                jump latihan32
            "So":
                $ skor += 10
                jump latihan32

        menu latihan32:
            "She is talented _____ hardworking."
            "And":
                "Wrong answer"
                jump latihan33
            "But":
                $ skor += 10
                jump latihan33

        menu latihan33:
            "I want to go shopping, _____ I don't have enough money."
            "But":
                $ skor += 10
                jump latihan34
            "And":
                "Wrong answer"
                jump latihan34

        menu latihan34:
            "He is tall _____ he is also very strong."
            "And":
                $ skor += 10
                jump latihan35
            "But":
                "wrong answer"
                jump latihan35
        
        menu latihan35:
            "She likes to read books _____ she also enjoys watching movies."
            "Because":
                "wrong answer"
                jump latihan36
            "And":
                $ skor += 10
                jump latihan36

        menu latihan36:
            "I love coffee, _____ I don't drink it in the evenings."
            "But":
                $ skor += 10
                jump latihan37
            "And":
                "wrong answer"
                jump latihan37

        menu latihan37:
            "He is tall _____ he plays basketball very well."
            "Because":
                $ skor += 10
                jump latihan38
            "So":
                "wrong answer"
                jump latihan38

        menu latihan38:
            "He bought a new car, _____ he needed reliable transportation."
            "And":
                "wrong answer"
                jump latihan39
            "Because":
                $ skor += 10
                jump latihan39

        menu latihan39:
            "He enjoys playing basketball, _____ he also likes swimming."
            "And":
                $ skor += 10
                jump latihan40
            "But":
                "wrong answer"
                jump latihan40
                                        
        menu latihan40:
            "He was tired, _____ he stayed up late to finish his project."
            "So":
                "wrong answer"
                jump TotalSkor3
            "And":
                $ skor += 10
                jump TotalSkor3

        label TotalSkor3:
            "Hi [P] Total Skor Latihan pertama anda adalah = [skor]" 
            $ skor = 0
            menu :
                "Apakah anda ingin mengulang latihan"
                "Iya":
                    jump Tugas3
                "Tidak":
                    "You Follow the lessons in Class Until time to go home"
        play sound "SchoolBel.mp3"
        "The class bell rings"
        with Pause (0.11)
        play sound "Teacherlast.mp3"
        Teacher "because the bell has rung. so I'm enough for today lessons and see you tomorrow"
        stop sound
        play sound "student1-6.mp3"
        Student "Okay mrs thank you"
        stop sound
        play sound "Teacher1-4.mp3"
        Teacher "You're welcome"
        "You going to home"
        hide CatNormal
        hide classroom with fade
#Closing
    "You arrive at home"
    show Rtidursore
    Player "fiuh, today was so much fun at school"
    Player "tomorrow I have to be better than today"
    Player "I have to study hard to be the best"
    hide Rtidursore
    show end
    with Pause (1.5)
    "Terima kasih sudah memainkan game ini"
    hide end
    return