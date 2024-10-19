#a visual novel by R. L. Ramos
#game jam edition
#THE EXILED PRINCE (the final version, that is) should have around five to six chapters, the prologue not included.
#Note to self: Choices have subchoices. One "choice" per chapter, multiple "subchoices" per "choice".
#characters that won't appear in the game jam version are disabled.


define d = Character("Daniel", color="6495ed")  #Daniel Justin Miroslav Seung-Jun Corre, color=cornflower blue
define s = Character("Seok-Jin", color="1e90ff")   #Seok-Jin Ji-Beom Yun-Ho Arthur Corre, color=dodger blue
##define c = Character("Cornelia", color="82eefd")   #Cornelia Korniliyevna Reedus, color=arctic blue
##define h = Character("Hosu", color="4682b4") #Kang Hosu, color=steel blue
define km = Character("Kalmar", color="4169e1")  #Kalmar Dorcas, color=royal blue
##define k = Character("Korain", color="fcd12a")  #Im Korain, color=tuscany
##define a = Character("Ae-Cha", color="6f2da8")  #Song Ae-Cha, color=grape
##define z = Character("Zeha", color="355e3b")    #Zeha Levi Jordan Corre, color=hunter green
##define tm = Character("The Twin Moons", color="db0f27")  #Feray and Nuray - conjoined and twisted form, color=ruby
##define j = Character("Jacobo", color="743089")  #Jacobo Ibañez, color=luxury purple


init:

   $ flash  = Fade(.25, 0, .75, color="ffffff")



# The game starts here.

label start:
 
   scene bg textscreen
   with fade

   pause 3.5


   #Prologue - "Brothers Corre"

   scene bg living room
   with fade

   "It is late in the afternoon. A few more minutes and it will be evening."

   show daniel normal
   with dissolve
   
   "Daniel Justin Miroslav Seung-Jun Corre lies on the beige couch, listening to the cracking flames in the fireplace, feeling the sun's warmth through the windows."
   
   show daniel surprised
   with dissolve

   "He hears heavy footsteps coming down the stairs and heading in his direction. His brother is going somewhere."

   hide daniel surprised
   with dissolve

   "He sits up."
   
   
   show seokjin normal
   with dissolve

   "Seok-Jin Ji-Beom Yun-Ho Arthur Corre walks over to him dressed in an all-black outfit. Indeed, he is going somewhere. Somewhere...important. And dangerous."
   "Seok-Jin is a {u}stalker{/u} (pronounced 'stull-ker'), a scavenger of bizarre items found in the sites of a nuclear explosion and abandoned mines."
   "He had been working as one for over five years now, earning triple the standard wages of an average white-collar employee for each artifact he finds."

   show seokjin talking

   s "I have to go, Daniel. Duty calls."
   
   hide seokjin talking
   with dissolve

   show daniel surprised
   with dissolve
   
   "Daniel drops his jaw in mild surprise."

   d "You're heading into the Trench again? {i}Kuya{/i}, don't you think it's--"
   
   show daniel normal
   with dissolve
   
   "He stops and shakes his head."
   
   show daniel talking
   with dissolve

   d "Let me come with you. I wanna be a stalker."

   hide daniel talking
   with dissolve

   show seokjin surprised
   with dissolve

   pause 1.5

   show seokjin serious
   with dissolve

   s "Daniel, even after what happened to your eye, you still want to go with me? I'm not letting you get in trouble again."

   hide seokjin serious
   with dissolve

   show daniel talking
   with dissolve

   d "I just want to help. You got busted the last time and had to spend six months in jail."
   d "I just want to make things easier for us. Don't you think it will be if we help each other with this?"

   hide daniel talking
   show seokjin serious
   with dissolve

   s "The Trench isn't just a foggy place, Daniel. Many of the stalkers who entered its grounds never came back."

   hide seokjin serious
   with dissolve

   show daniel normal
   with dissolve

   pause .8

   show daniel talking

   d "I'm aware of the danger, {i}kuya{/i}. Still, I wanna help you."
   d "Think about it. If you get in trouble, you have me to depend on. I'll get you out of danger. I think it's time I do something for this family."

   hide daniel talking
   with dissolve

   show seokjin serious
   with dissolve

   pause .8
    
   "Seok-Jin raised Daniel alone for nearly half of his brother's teenage years."
   "He went through hell in jail and many dangerous sites to provide for Daniel's future."

   hide seokjin serious
   show daniel normal
   with dissolve

   "Daniel never knew of what ordeals Seok-Jin had to survive."
   "He does not want to look ungrateful, so he thinks it will be fair to pay his brother back for all his sacrifices."

   show seokjin serious
   with dissolve

   "Seok-Jin sighs."
   pause 2

   s "If you insist. I guess I do need help with this mission."
   s "Get your gear on, the best that you can have. Our task is to retrieve as many stone chips as we can."
   s "And if we get lucky, we can get soul gems."

   scene bg twilight sky
   with fade

   pause .8

   "It is already twilight."
   "The stars are already beginning to sparkle bright in the sky. The noises on the roads have died down."
   "People are heading home now. Soon, cops will patrol the streets on foot and by car for suspicious individuals, most likely stalkers, who have been frequenting the Trench day and night."

   scene bg front gate view
   with dissolve

   pause .8

   scene bg front gate
   with dissolve

   "Daniel meets with Seok-Jin outside their home once he finished dressing up."

   s "Ready to go?"

   "Daniel nods."

   "The brothers walk in the shadows to avoid suspicion, talk in hushed voices, and make hand gestures."

   scene bg trench
   with fade

   pause .8

   "The forbidden zone where the Trench is located is a kilometer away from their neighborhood, sealed off from the public with high walls and chicken wire fences reinforced with barbed wires."
   "However, nobody guards these barriers and patrols often overlook the area, so stalkers are always able to enter unnoticed."

   scene bg arrival
   with dissolve

   "Since Daniel is very unfamiliar with the place (and going around in the dark with one eye proves tedious), he can barely keep up with his brother during the trek."
   "Seok-Jin has to stop and wait for him and make sure he doesn't attract unwanted attention."
   "He is nearly out of breath by the time they reached the hidden passage in the chicken-wire fence. They decide to stop for a moment to gather themselves."

   s "You need a nickname."
   
   "Daniel sits down next to Seok-Jin."

   d "Why?"

   s "For anonymity, of course. I'll call you {b}Scar{/b}."

   d "Isn't that name overused?"

   s "What else should I call you?"
   s "Behind your eye patch is a huge scar that you can't--"

   "Seok-Jin stops."

   pause 1

   s "Sorry. That wasn't very nice."

   "Daniel is not offended. What his brother said is the truth after all."

   pause .5

   d "What do they call you?"

   s "{b}Skif{/b}."

   d "What kind of nickname is that?"

   s "It comes from an anti-tank guided missile."

   d "Skif."

   pause 1

   d "Who gave you that nickname?"

   s "{b}Hojeo{/b}."

   "That word translates to 'Porcupine'."

   d "Another stalker?"

   s "Of course."

   "Seok-Jin rubs his forearm and looks thoughtful for a time."

   s "He was my teacher."

   s "The greatest stalker of his generation--and the wisest. We used to call him {b}Teacher{/b}."

   d "Is he still around?"

   pause 1

   scene bg trench
   show seokjin normal
   with dissolve

   pause 1.5

   show seokjin serious
   with dissolve

   pause .6

   "Seok-Jin suddenly looks grim and shakes his head."

   scene bg arrival
   hide seokjin serious
   with dissolve

   "Daniel wonders why. He does not ask, though, thinking it might be inappropriate for his brother to talk about."
   "He can merely guess that Hojeo met an ill fate."
   "Stalkers die almost every day in the Trench or after their trip to the Trench."

   scene bg trench
   show seokjin serious
   with dissolve

   pause .7

   s "Want me to tell you what happened? I can spare a few minutes."

   menu: #story_flag

      "Listen to Seok-Jin's story":

         jump choice1_story

      "Skip it":

         jump choice1_skip

               
label choice1_story:

   $ story_flag = True

   scene bg arrival
   hide seokjin serious
   with dissolve

   s "Okay."

   pause .5

   s "Teacher... Um, Hojeo..."
   s "He was the very best of us. Younger stalkers looked up to him and always sought his guidance. I was lucky enough to be his student."
   s "But then, he started obsessing over the Trench after his mentor {b}Strelka{/b} and the older stalkers claimed to have discovered what they called {b}Ophanim{/b}."

   d "What's that?"

   s "It's said to be a wish-granting artifact. A giant orb surrounded by six wheels, like the so-called chariot wheels people in the ancient days claimed to have seen."

   pause .5

   scene bg trench
   show seokjin serious
   with dissolve

   s "You see..."
   s "{b}Korain{/b}... Ah..."

   hide seokjin serious
   show daniel surprised
               
   d "Korain. That's his name, I assume?"

   hide daniel surprised
   show seokjin normal
   with dissolve

   pause .5

   show seokjin talking

   s "Yeah. I'll call him by his name, then."
   s "Korain had a younger brother named {b}Hak-Kun{/b}, who was a gifted poet and a published author. He loved Hak-Kun, but he was said to have always been jealous of his brother's achievements."
   s "He never finished school due to poverty. He raised his brother alone after their parents died."
   s "I think Korain simply couldn't accept the fact he wasn't given the chance to achieve his dreams."

   hide seokjin talking
   show daniel surprised
               
   d "What happened?"

   hide daniel surprised
   show seokjin normal
   with dissolve

   pause .5

   show seokjin serious

   s "One day, Hak-Kun got curious about Ophanim and asked Korain to take him there. I don't know whether or not Korain knew about Ophanim's location and simply never told anyone about it, but he and Hak-Kun left to find it."
   s "They stumbled upon the meat-grinder on the way."

   hide seokjin serious
   show daniel surprised
                              
   d "The meat-grinder? Is it some kind of artifact or something?"

   hide daniel surprised
   show seokjin serious

   s "No. It's one of the Trench's many oddities. An invisible phenomenon that can mangle a person's body in a few seconds. Only experienced or irradiated stalkers such as myself can detect it."

   hide seokjin serious
   show daniel normal
   with dissolve

   pause .3

   show daniel talking

   d "I see."
   d "Go on, {i}kuya{/i}."

   hide daniel talking
   show seokjin serious
   with dissolve

   pause .5

   s "Korain..."
   s "He..."

   show daniel talking
   hide seokjin serious

   d "He what, {i}kuya{/i}?"

   show daniel normal

   pause .5

   show seokjin serious
   hide daniel normal
   with dissolve

   pause .8

   show seokjin meh

   "Seok-Jin lets out a sigh."

   s "Korain pushed Hak-Kun into the meat-grinder."

   show daniel normal
   hide seokjin meh
   with dissolve

   pause .6

   show daniel surprised

   pause 1

   d "But...how? How could he?"

   show seokjin meh
   hide daniel surprise
   with dissolve

   pause .5

   show seokjin serious
   
   "Seok-Jin shakes his head."

   s "Jealousy is the obvious reason."
   s "But I know Korain had another reason."
   s "Obviously, he wanted to make a wish to Ophanim."
   s "The meat-grinder was blocking the room that contained Ophanim and the only way to stop it was to throw something big enough to jam its maw."
   s "Temporarily."

   show daniel surprised
   hide seokjin serious
   with dissolve

   pause .5

   d "Temporarily...?"
   d "Then, there must always be a sacrifice in order to reach Ophanim?"

   show seokjin serious
   hide daniel surprised
   with dissolve

   pause .3

   s "Unfortunately, yes."

   show daniel surprised
   hide seokjin serious

   d "Is there no other way?"

   show seokjin serious
   hide daniel surprised

   s "We don't know yet. Nobody has ever made it that far in the Trench."
   s "Only Korain had."
   s "Maybe Kalmar Dorcas, too."

   show seokjin normal
   
   pause .5

   s "And maybe our dad as well?"

   show daniel normal
   hide seokjin normal
   with dissolve

   pause .5

   show daniel surprised

   pause 1.2

   show seokjin normal
   hide daniel surprised
   with dissolve

   pause .5

   s "Anyway, I'll continue."
   s "Korain was immediately consumed by guilt upon seeing his brother die a brutal death."
   s "Once he reached Ophanim, he abandoned whatever he initially dreamed of asking from it and wished for Hak-Kun to be brought back to life."
   s "However..."

   pause .5

   show seokjin serious

   pause .5

   scene bg trench pathway
   hide seokjin serious
   show kalmar scowl
   with flash

   km "You have no idea what is going on here!"
   
   pause .5

   km "Why do you think Korain killed himself?"

   show seokjin normal
   hide kalmar scowl
   with dissolve

   pause .3

   show seokjin talking

   s "He was..."
   s "He came to find Ophanim with mercenary aims..."
   s "...and killed his brother for money."

   show kalmar scowl
   hide seokjin talking

   km "Yes, but why did he kill himself?"
   km "Why did he go back not for money, but for his brother?"

   show seokjin normal
   hide kalmar scowl

   pause .3

   s "He... He wanted to... But Ophanim gave him a pile of money instead of bringing back his brother."

   hide seokjin normal
   show kalmar scowl

   pause .3

   show kalmar rabid

   km "Because he realized that it's {i}not merely a desire{/i}, but one's {i}most secret desire{/i} that is granted by Ophanim."

   show seokjin normal
   hide kalmar rabid
   with dissolve

   pause .3

   show seokjin surprised

   pause 1

   km "Ophanim showed Korain an essence of himself."
   km "And it broke him."
   km "He thought he could simply ask for his brother back, which was why he pushed Hak-Kun into the meat-grinder without hesitation."
   
   pause .8

   s "Kalmar..."
   s "How do you know all this?"

   show kalmar scowl
   hide seokjin surprised
   with dissolve

   pause 1

   show kalmar normal
   with dissolve

   "Kalmar said nothing."
   "He could only frown."
   
   scene bg trench
   show seokjin serious
   hide kalmar normal
   with flash

   pause 1

   show daniel surprised
   hide seokjin serious

   pause .3

   d "{i}Kuya{/i}..."
   d "Did Kalmar ever tell you where to find Ophanim?"

   show seokjin serious
   hide daniel surprised
   with dissolve

   pause .5

   show seokjin meh

   s "No, he didn't."
   s "But he obviously had good reason."

   show seokjin normal
   with dissolve

   pause .3

   show seokjin talking

   s "Even if he did tell me, I would never go there. And I would never take anyone there, even if they paid me."
   s "Ophanim is just not worth the risk, regardless of how coveted it is for its wish-granting powers."

   show daniel normal
   hide seokjin talking

   d "Hm."

   show seokjin normal
   hide daniel normal

   pause .5

   show seokjin talking

   s "Before we proceed, is there anything else you'd want to know?"

   show daniel normal
   hide seokjin talking
   with dissolve

   menu: #subchoices1
      "Kalmar Dorcas":
         
         jump subchoice1_kalmar

      "Zeha Levi Jordan Corre, our dad":
         
         jump subchoice1_zeha

      "No. Let's get going.":

         jump choice1_done

label subchoice1_kalmar:

   show daniel talking

   d "Who is Kalmar Dorcas, exactly?"

   show daniel normal

   s "Kalmar."
   s "He goes by the nickname 'Wolf'...because that's what he is: a wolf."
   s "An old colleague of Korain and our father."
   s "He's smart and wise, just like Korain. Except that he was never obsessed with the Trench."
   
   show seokjin talking
   hide daniel normal
   with dissolve

   s "Kalmar is a family man with five daughters. Quintuplets --  can you believe that?"  #"Limang kambal -- biruin mo 'yon?"
   s "He used to own a farm that he inherited from his great-grandparents. However, when the Cataclysm struck, he and his family lost everything."
   s "He attempted suicide by drowning once, but had a change of heart when he realized he would be able to get back on his feet now that his mate and kids thought he was dead."
   s "He became a stalker. Then he tried to return to his family. But his mate wouldn't take him back."
   s "His youngest daughter Holly, though, was very accepting of him. She stays with him sometimes."

   show daniel normal
   hide seokjin talking
   with dissolve

   pause .5

   show daniel talking

   d "I see."

   hide daniel talking
   show seokjin normal
   
   pause .3

   show seokjin talking

   s "Any more questions?"

   show daniel normal
   hide seokjin talking
   with dissolve

   menu:
      "Zeha Levi Jordan Corre, our dad":

         jump subchoice1_zeha

      "That's enough for now.":

         jump choice1_done


label subchoice1_zeha:

   show daniel talking

   d "I don't understand, {i}kuya{/i}."
   d "Dad was a stalker?"
   d "I thought..."

   show daniel panic

   d "I mean, how could he be one?"
   d "I thought he was a desert soldier."

   show seokjin talking
   hide daniel panic

   s "He was a desert soldier, Daniel."
   s "But after he retired, he became a stalker."

   show daniel surprised
   hide seokjin talking

   d "Why would he become one?"

   show seokjin normal

   "Seok-Jin gives that a long thought."

   show seokjin meh

   "Then he sighs."

   show seokjin serious

   s "That we'll never know."

   show daniel normal

   pause .3

   show daniel sad

   pause .3

   d "Oh, man..."

   show seokjin normal
   hide daniel sad

   pause .5

   show seokjin talking

   s "Any more questions?"

   show daniel normal
   hide seokjin talking
   with dissolve

   menu:
      "Kalmar Dorcas":

         jump subchoice1_kalmar

      "That's enough for now.":

         jump choice1_done


label choice1_skip:

   $ story_flag = False

   hide seokjin serious
   show daniel normal
   with dissolve

   d "Hmm."

   show daniel talking

   d "I think I'll hear that story later."

   hide daniel normal
   show seokjin serious

   s "All right, then."

   hide seokjin serious
   with dissolve

   jump choice1_done


label choice1_done:

   scene bg arrival
   with dissolve


   pause 1

   "Seok-Jin fishes out a silver cylinder around ten inches in length and hands it to Daniel."

   s "You'll need this."

   scene bg gift
   with fade

   pause .5

   "Daniel takes it and studies its distinctive form."
   "It has two buttons on one end, where there is a pommel cap and some kind of emitter on the other. Its black grip is stable and equipped with a thin ring for whatever reasons."

   d "What is it?"

   s "An E-blade."
   s "Stand back when you ignite it."

   "Daniel feels tempted to test the weapon, but he forgoes the idea, reminding himself of their mission."

   d "I think I'll try this one out later when we get back."

   "Seok-Jin nods in agreement."

   s "Be careful when you use it. Its laser can cut and burn and melt almost any substance with little resistance."

   "Daniel stuffs the E-blade in his shoulder holster."

   scene bg entry
   play sound "audio/walkingintheforest.wav" volume 1.5
   with dissolve

   "Seok-Jin pulls out a PDA and taps the screen. A map of the Trench pops up."

   d "Where are we heading?"

   "Seok-Jin zooms in on the center of the Trench's map and taps the glowing orange dot marking the image of a subway."

   s "Metro."

   "They push on afterward."
   "After a five-minute walk into the center of the forbidden zone, they finally reach the gigantic abyss."

   scene bg crack
   stop sound
   with dissolve

   "A dense purple aura lifts from the wide opening, along with an eerie noise created by the passing winds underground. There is a steel ladder hanging from the edge of the largest rock sticking out above the surface of the tremendous crack."
   "It is the only way down--and back."

   d "So, this is it?"

   s "Welcome to the Trench."

   "Seok-Jin goes for the ladder, and Daniel follows him."

   "The {u}Trench{/u} was created on the day the merging of Andromeda and the Milky Way was completed."
   "Earth did not burn when the sun increased its luminosity; however, for reasons yet to be known, the galactic collision opened a portal to a void-like dimension that allowed living anomalies into the world."
   "The Trench is more than what its name implies."

   scene bg tunnel
   play sound "audio/crunchyroadfastwalking.wav" volume 1.5
   with fade

   "Inside the Trench is a network of wide dirt and stone tunnels that leads to hundreds of explored and unexplored depths. Mines are a common find."
   "Old stalkers claimed that some of them lead to different dimensions, especially the stone tunnels; others said they are paths to ancient civilizations buried deep below the known world."

   pause 1

   "The brothers are now seventy-five feet below the surface. The very little light above the sky is nothing more than a faint streak of gray."
   "There are a couple of tunnels flanking them--one leads to a series of unexplored depths, the other had been explored quite a few times."
   "They take the tunnel on their left."
   "Once they are deep within it, the path slopes down to the next level below. There, they found eight more tunnels and take the one leading to the northeast."
   
   scene bg metro rail
   with dissolve

   "It leads to a destroyed subway that had been abandoned a decade before the creation of the Trench after two trains collided and swerved off the tracks, killing one hundred and eight people."
   "This is the Metro, and it is believed that mutated animals, specifically rodents, roam the darkest depths of its ruins."
   "Encounters with them are often fatal, and stalkers have little chance of surviving without serious injuries."

   "Seok-Jin stops at what used to be a railroad."

   show seokjin normal
   with dissolve

   pause .5

   show seokjin talking
   
   s "Okay, we begin our search here."
   s "I'll start with this spot. You can go wherever you like, just don't stray too far."
   s "Watch out for slimes. Don't get caught in them or they'll dissolve your bones."

   hide seokjin talking
   with dissolve

   "The brothers begin scavenging from the rubble that buried the station's platform."
   "Daniel follows the trail of rocks and shattered cement blocks as he searches for stone chips, not realizing he is already outside the Metro's proximity."

   stop sound
   pause 1

   "Agonized moans and grunts echo off the walls in a dimly lit room filled with glittering crystal shards and marble blocks."
   "Daniel hurries inside upon hearing that it was Seok-Jin's voice."

   scene bg slime
   play sound "audio/slimesquish.mp3" volume 1.5
   with fade

   "He finds him reclining on something between the mounds of beaten rocks and powdered crystals."

   s "{i}DANIEL, HELP ME!{/i}"

   "Daniel stumbles to his feet and ran towards his brother. He suddenly halts halfway to him."
   "Seok-Jin is caught in an enormous pool of slime pouring out of a large crack in the stone wall. He must have failed to see it forming at his feet."
   "It is no ordinary slime, for it can suffocate any creature to death and dissolve bones in over fourteen minutes."
   "Getting out of it alone is impossible, for each pulsating movement it made would drag one deeper into the muck."

   d "{i}Kuya{/i}, the slime--it's all over you!"

   "He does not know what to do."
   "The slime will eat him if he comes into contact with it. It looks alive! What if it suddenly grabs him while he is helping his brother get out of it?"
   "He cannot risk that."

   "Seok-Jin heaves and wriggles through the thickening gob."

   s "Daniel... Please...you have to--"

   "Daniel does not think."

   scene bg run away
   play sound "audio/running.mp3" volume 3
   with dissolve

   "Once his instincts tell him to run, he takes the opportunity and never looks back at the appalling sight."
   "He runs as fast as he can, following where the tunnel leads him."
   "His brother's voice thunder against the walls, crying his name."

   pause 1.5

   "He keeps going."
   "He has to escape this doom."

   scene bg tunnel
   with dissolve

   pause 1.5

   scene bg tunnel slime
   with dissolve

   "Slime oozes through the crevices in the walls and ceiling. It spreads on the floor as it drips, gradually filling the tunnel."
   "It might be pulsating too."

   scene bg run away
   play sound "audio/running.mp3" volume 3
   with dissolve

   "Daniel quickens his pace. His lungs begin to burn, his legs feel as if they are going to break soon."
   "He cannot risk getting even a single droplet of the slime on him. It can dig deep into his flesh and destroy his insides."

   scene bg tunnel slime
   with dissolve

   pause .8

   "The surrounding darkness thickens; it is getting harder and harder to see."
   "Daniel wants to activate his night vision, but he thinks closing his eyes for one second is not worth the risk."

   scene bg run away
   play sound "audio/running.mp3" volume 3
   with dissolve

   "Fear and hope clash in his heart. He cannot see the intersection where the opening above is."
   "What if he had gone past them and entered a different tunnel? He cannot go back and find another way."
   "All his worries disappear in a blink when he sees the faint form of the rusty extension ladder clinging to a high wall of sand-colored rock."
   "His heart lurches."
   "Daniel kicks and leaps toward the ladder and runs up the steps."

   scene bg crack
   stop sound
   with dissolve

   "At last, he is on the surface."
   "He sprints away from the Trench's mouth."

   scene bg remorse
   with fade

   pause 1

   "Once he is beyond the gates, Daniel collapses on his knees. With great relief that he is finally outside of danger."
   "Loneliness clutches his shoulders. He entered the Trench with his brother...but came out of it alone."
   "Tears burst from his eyes and fall in huge droplets. Heartbreaking, guttural sobs escape his throat."

   pause 1

   "Daniel never thought he could ever do the unlikeliest."
   "His brother had sacrificed his own future just for him and was ready to sacrifice more without asking for anything in return."
   "Seok-Jin never once raised a finger or hit him in the days when Daniel was still a problem child. Despite their frequent intense arguments in the past years, he loved Daniel more than anything else in the universe."
   
   pause .5

   "Daniel didn't want to leave him behind. He was going to save Seok-Jin."
   "However, when he saw him stuck in the slime earlier, he was frozen by hesitation for a short time because his fear of death and his love for his brother were fighting."
   "In the end, fear took over him."

   pause .5

   "Because {i}he let it{/i} consume him."

   pause .8

   d "{i}Why? Why did I leave him?"

   scene bg surrender
   with fade

   pause 1.2

   "He has no idea how much time has passed while he simply sits on the ground, staring at his feet."
   "He is suddenly numb to his environment."

   pause 1

   play sound "audio/runningandthud.mp3" volume 1.3
   "Footsteps approach his direction."

   pause .3

   "He knows these come from the police and his first instinct is to run, like what he did earlier."
   "But he ignores this urge."
   "What right has he to evade the law when he just killed his brother by leaving him to die in the slime?"

   pause .8

   "Two officers materialize before him and draw out their pistols."
   "Daniel remains calm in their presence. He is too deep in his guilt and shame to worry about going to prison."
   "He deserves this anyway."
   "He willingly surrenders to them, and one of the officers declare that it will be six months for him in jail."

   #lol, my sister laughed at the part where Daniel ran away instead of saving his brother!
   #she found Daniel's cowardice to be hilarious. Can't blame her one bit
   #my readers at BUS were distressed. Coel commented that if she were in Daniel's place, she would rather die saving Seok-Jin than live with the guilt!
   #my sister was like, "the lil' shit [Daniel] promised to help, then ran away when the time came!"

   scene bg prison
   play sound "audio/jaildoorclose.mp3" volume 1.5
   with fade

   "He is thrown into an empty holding cell."
   "The police let him keep his stalker gear for the duration of his stay, but not his bag and holster. They searched his stuff for stolen items or artifacts."
   "He hoped they didn't take his E-blade. It is Seok-Jin's last gift to him."

   pause .8

   scene bg cry to sleep
   with dissolve

   pause 5

   "Sometime in the evening, Daniel is overcome once again by his memories of what happened in the Metro."
   "Guilt eats at him. His brother's cries ring and echo in his ears without end."
   "He spends the rest of the night grieving until he grows tired and falls asleep."

   scene bg walk home
   with fade

   "He is released a month earlier on grounds of good behavior. His freedom does not feel like freedom at all."
   "As he leaves the precinct, he imagines heading outside the school grounds at the end of his classes for the day and meeting Seok-Jin at the front gate. His brother would then ask if he wanted to go somewhere before returning home."
   
   pause 1

   "Once he is outside, Daniel is alone, apart from the police officers going in and out of the precinct."

   pause .5

   "Nobody is waiting for him."
   "Nobody to take him home after a long day of school."
   "Only {cps=30}emptiness{/cps}."
   "And the world he has shut himself from in shame."
   "He stands by the stairs, staring out into the distance for some time."
   "Wondering."
   "Waiting."
   "Hoping."

   pause 1

   "In the end, Daniel pulls himself out of his head. He lets the truth sink in."
   "No use fooling himself. His brother is not coming. Not anymore."
   "Because he had abandoned him to die months ago."

   pause 1

   "From this day forward, he walks alone."


   #Chapter 1 - What If...?

   scene bg pathway
   with fade

   "{i}One month later...{/i}"

   show daniel sad
   play sound "audio/walking.mp3" volume 4
   with dissolve

   "Daniel walks his way home on the empty road beneath the highway, flanked by mud-brick walls of two abandoned corporate buildings."
   "He began taking this route not long after his release from jail in order to avoid unwanted attention, especially from the law."
   "Having become a stalker three months ago makes him an outcast, an eternal jailbird."
   "He would have eyes looking down on him every now and then."

   stop sound
   pause .5

   play sound "audio/punchboxing.mp3" volume 1.5
   pause .5
   show daniel surprised
   with dissolve

   "Something fell a few meters behind him."

   scene bg a_book
   with dissolve

   "Daniel looks back over his shoulder. He sees..."

   pause .5

   "There's a book. In the middle of the street."

   pause .3

   d "Interesting."

   scene bg mysterious_book1
   with dissolve

   "Daniel picks it up and examines the cover for a moment before turning to a random page."

   play sound "audio/singlebookpaging.wav" volume 1.5

   "The book's cover appears to be made of wood wrapped in old leather. He can't place what kind of paper the pages were made of, but he can tell it's nothing like the ones being used today or even in the previous century."
   "Turning a few pages, he sees that the book seems to be a journal with multiple sections, and each section belongs to a different person."
   "He can tell by the differences in the handwriting."
   "An interesting to note is that the text has no erasures and no grammatical or spelling errors. As if this book was made to be perfect."
   
   play sound "audio/browsingbookbypages.wav" volume 1.5
   pause .5

   "Reading some passages from a select few sections, even a few words from the pages he skimmed, Daniel notices that most, if not all, of the entries came from troubled individuals," #continue on the next line below
   "many of whom had brought misfortune upon themselves and others and regretted their actions deeply, as they wrote in their entries."
   pause .5

   scene bg blankpages
   with dissolve
   play sound "audio/singlebookpaging.wav" volume 1.5
   "Turning a few more pages, he sees that half of the book's pages is blank, so he goes back to the filled half."

   scene bg book_entries
   with dissolve
   play sound "audio/singlebookpaging.wav" volume 1.5

   pause .5

   "The last two sections catch his eye."

   stop sound

   menu: #book_entries
      "Polina":
         jump polina_bogdanovna_golubeva

      "The Exiled Prince":
         jump the_exiled_prince

label polina_bogdanovna_golubeva:

   scene bg pathway
   show daniel normal
   with dissolve

   play sound "audio/singlebookpaging.wav" volume 1.5

   "Daniel sorts through the pages of the section belonging to {b}Polina Bogdanovna Golubeva{/b}."
   "Polina's entries are written in Russian."
   "Daniel doesn't speak a word of Russian, but he is quite fluent. His father Zeha himself was part Russian through his father Arseny and sometimes spoke the language when interacting with some of his colleagues."

   d "Hmm."
   
   pause .5

   "Polina introduces herself as 'a daughter of the apothecary Bogdan Golubev, born at the time when the Russian Empire was to meet its impending doom,"
   "a combat nurse during the Second World War, and a descendant of a virtually extinct race of magically gifted people called Mystics'."
   "She claims that she didn't really wish to serve in the war and that nobody had coerced her into serving. She just felt it was her duty to. If not for her country, then for her beloved {b}Akim Pavlovich Medvedev{/b}."

   show daniel surprised
   with dissolve
   play sound "audio/singlebookpaging.wav" volume 1.5

   pause .5

   "At the mention of Akim, Polina begins to tell her story in the following passages, writing:"

   scene bg polina_and_akim
   hide daniel surprised
   with flash

   "{i}...I was first acquainted with Akim Pavlovich when I took up apprenticeship at my father's apothecary shop under his tutelage. Akim was a frequent customer and the son of Papa's old colleague, Pavlov Lvovich."
   "{i}When our eyes met, I saw a sparkle in Akim's eye as he smiled at me. I then felt a funny feeling in my chest. I knew at that point that I was in love with him. So was he, with me."
   "{i}Our meetings became regular at the shop, but I did not want Papa or anyone to suspect. So, our meet-ups took place often at an old park near the suburbs."
   "{i}Our love blossomed there, and we have come to the point where we realized we were ready to spend the rest of our lives together."
   "{i}Then the Second World War broke out."

   scene bg polina_sadscene
   with flash

   "{i}Akim served as a soldier and I as a combat nurse throughout the duration of the war. We kept contact through letters. Our love remained strong despite our being apart from each other."
   "{i}At the near end of the war, my mother confronted me about my relationship with Akim."
   "{i}She had always known, but did not say anything about it. Until that very day."
   "{i}She requested that I end my contacts with him. I was not surprised that she would make such a request, for I had always thought she and Papa would not approve of my relationship with Akim."
   "{i}But Mama told me it was not because she did not like Akim. Rather it was because of our future together, which she claimed to have already known how it would turn out."
   "{i}She said that we were still too different in spite of everything. She did not directly state it, but I could tell that the issue had something to do with our magical lineage."
   "{i}Our family belonged to a long line of magically gifted people, which our kind referred to as Mystics, and that if we mated with the ungifted, like Akim,"
   "{i}the consequences are... let us simply say, they are least favorable."

   pause .5

   "{i}I was without a choice."
   "{i}Some time after Akim got back from the war, I met up with him and..."

   pause .3

   "{i}I ended our relationship."
   "{i}Akim broke down in tears and demanded why. I could not tell him about my heritage, as it should be kept a secret at all cost. So, instead, I told him that my parents found out about our relationship and were furious."
   "{i}I had to tell him that my parents threatened to hurt him and disown me if we kept seeing each other."
   "{i}Akim insisted that he could take the risk, stating that he had survived the worst during the War. But I was adamant on my decision to end things between us."

   scene bg pathway
   show daniel crying
   with flash

   pause .3

   "Daniel stops reading and looks up from the pages, realizing that he had been shedding tears as he read."

   pause .5
   
   show daniel normal
   with dissolve

   d "Hmm."
   
   play sound "audio/browsingbookbypages.wav" volume 1.5
   d "There's more of her entries."
   d "I think I'll read them later."

   scene bg book_entries
   with dissolve

   pause .5

   menu: #subchoices2
      "The Exiled Prince":
         jump the_exiled_prince


label the_exiled_prince: #important! subchoices will loop unless this third option is picked

   scene bg pathway
   show daniel normal
   with dissolve
   play sound "audio/browsingbookbypages.wav" volume 1.5

   "Daniel goes for the final section in the book, strangely titled 'The Exiled Prince'."
   "It's the only one titled like that, while the rest are all named after their authors."

   play sound "audio/singlebookpaging.wav" volume 1.5

   pause .8

   show daniel surprised
   with dissolve

   pause .3

   d "What?"

   hide daniel surprised
   scene bg blankpages
   with dissolve

   pause .5

   "To Daniel's surprise, the pages are blank."
   
   play sound "audio/browsingbookbypages.wav" volume 1.5

   "He flips through every single page, hoping to find a single text in one of them."
   "But there is none."

   scene bg pathway
   show daniel sad
   with dissolve
   stop sound

   pause .3

   d "Aw, man."

   pause .3

   "As he is about to close the book,"
   
   show daniel surprised
   play sound "audio/magicallightaura.wav" volume 2
   "he feels a strange aura coming from the blank pages."

   hide daniel surprised
   scene bg closeup
   with dissolve

   pause .7

   scene bg closeup_magic
   with dissolve

   "It is then followed by a faint purple glow."
   "And then, one by one, words begin to form on each page, and Daniel proceeds to read them as they go."
   "And with every word he reads, he sees clear images of what the text is trying to say."
   "He sees..."
   
   
   scene bg exiled_prince
   with flash
   play sound "audio/magicsparkleswoosh.wav" volume 4

   "{i}...a young man of royalty..."
   "{i}A prince."
   "{i}One-eyed."
   "{i}Broken."
   "{i}Torn between the chaos of his reality and dreams,"
   "{i}immobilized by multiple dilemmas,"
   "{i}stuck in the middle of a clash between two fates."
   "{i}His fate and that of everyone around him."

   pause .5

   "{i}To alleviate his suffering,"
   "{i}he sought means that no one in the Mystical world would."
   
   scene bg exiled_prince2
   with dissolve

   "{i}He tore open a hole in reality and brought in two clashing forces--two sisters of different nature,"
   "{i}neither gods nor demons. Just forces unimaginable, taking the humble forms of cats."
   "{i}They were the hands that forged his reality and a billion others that exist alongside it on a different plane."

   pause .3

   "{i}The prince demanded their assistance, and the sisters granted what he asked."
   "{i}Like everything else, however, it came with a price that he could not pay."
   "{i}Or rather, a price that he was unwilling to pay."

   pause .3

   "{i}He would come to regret that soon enough."
   

   scene bg exile
   with flash

   "{i}Deemed foul and unfit to rule,"
   "{i}the prince was stripped of his title and royal garbs,"
   "{i}forced into rags, and was paraded around the sandy streets of what was left of his realm,"
   "{i}which had been destroyed by war multiple times during his reign."
   "{i}Then, he was thrown out of the Wall, his once glorious kingdom,"
   "{i}shoved into the wastelands beyond and locked out forever."
   
   pause .5

   "{i}The prince was last seen running into the woods in the distance,"
   "{i}bound by thorned cuffs, looking back at the Wall once as he ran,"
   "{i}and then, he was gone.{/i}"

   scene bg pathway
   with flash
   show daniel surprised

   pause .5

   d "Wait."
   d "That vision in my head..."
   d "I saw the prince."

   show daniel panic

   d "Why-- Why does he...{i}look like me{/i} somehow?"
   
   
   hide daniel panic
   scene bg closeup
   with dissolve

   pause .5

   play sound "audio/browsingbookbypages.wav" volume 1.5

   "Daniel turns the pages to see more of this supposed prince's entries."
   "Rather than written in prose and in first person, the entries are done in verses and in third person."
   "It's as if someone else had written this instead of the person this section is about."
   "Daniel wonders if the accounts in the Exiled Prince happened in real life. Or if this was just a fictional account of a supposed figure said to have existed in 'a long-forgotten past'."

   pause .5

   scene bg blankpages
   with dissolve

   pause .5

   menu: #subchoices2
      "Return to Polina's entries":
         jump polina_bogdanovna

      "???":
         jump secret_pages



label secret_pages: #only available when the second option is picked

   "The following pages are blank."
   "Not much has been written about the prince, other than the ones he saw in his mind."

   scene bg closeup
   with dissolve

   "But Daniel keeps sorting through the pages, hoping that the book works its magic once again."

   pause .6

   play sound "audio/singlebookpaging.wav" volume 1.5

   scene bg closeup_magic
   with dissolve
   
   "And it does."

   pause .5

   play sound "magicallightaura.wav" volume 2
   scene bg book_pages
   with flash
   
   "Elaborate sketches of the moon and its two faces and those of two cats appear on the empty pages."

   pause .3

   "Atop the sketch of the moon are the words 'The Twin Moons', followed by a long description below."
   "However, it is written in a language unfamiliar to Daniel."
   "It doesn't seem like any of the languages spoken by other nations."

   pause .3

   "The next page shows the sketches of a black cat and a white cat, both of them odd-eyed and female."
   "The black cat is said to be named {b}Nuray{/b}, illustrated as an all-black feline with a sleek body and steel claws."
   "Below her is {b}Feray{/b}, a plump, all-white cat with folded ears and long fur."
   "The description below them is, unfortunately, also written in the same foreign language."

   pause .5

   d "These cats..."
   d "Why do they look familiar?"

   pause .3

   d "I think..."
   d "I think I've seen them in my vision earlier of the prince..."


   scene bg pathway
   show daniel normal
   with dissolve

   "Daniel feels a presence somewhere."

   "He glances toward the tunnel on his left."

   "He sees two pairs of lights: one is blue and green, the other green and blue."
   
   pause .5

   "Wait."
   "They're moving."
   "They don't look like ordinary lights."

   pause .5

   show daniel surprised
   "They're..."
   play sound "audio/sweetkittymeow.wav" volume 2

   pause .8

   "Cats?"

   scene bg cats
   with dissolve

   play sound "audio/littlecatpainmeow.wav" volume 2

   pause 1.5

   play sound "audio/angrykittymeow.wav" volume 2

   pause 3

   scene bg endscene #this is only for the game jam edtion
   with flash

   pause 5

   scene bg comingsoon
   with fade

   pause 5

   scene bg chapter title
   with dissolve

   pause 1

   menu:
      "Replay the Story":
         jump start
      "Back to Main Menu":
         return

return
