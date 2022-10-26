import streamlit as st
import pandas as pd 
import numpy as np
import time
from datetime import datetime
import matplotlib.pyplot as plt
from bokeh.plotting import figure
from PIL import Image

st.markdown('<style>description{color: grey;}</style>',unsafe_allow_html=True)
st.title("✨ALL ABOUT ANIME✨") 
st.markdown("<description>Anime (Japanese: アニメ, IPA: [aɲime]) is hand-drawn and computer-generated animation originating from Japan. Outside of Japan and in English, anime refers specifically to animation produced in Japan. However, in Japan and in Japanese, anime (a term derived from a shortening of the English word animation) describes all animated works, regardless of style or origin. Animation produced outside of Japan with similar style to Japanese animation is commonly referred to as anime-influenced animation.",unsafe_allow_html=True)
img = Image.open("c2.jpg")
st.image(img)

st.sidebar.markdown('Click to know more about anime:')
img = Image.open("c1.jpg")
st.sidebar.image(img)
if st.sidebar.button('History'):
    st.sidebar.markdown("The earliest commercial Japanese animations date to 1917. A characteristic art style emerged in the 1960s with the works of cartoonist Osamu Tezuka and spread in following decades, developing a large domestic audience. Anime is distributed theatrically, through television broadcasts, directly to home media, and over the Internet. In addition to original works, anime are often adaptations of Japanese comics (manga), light novels, or video games. It is classified into numerous genres targeting various broad and niche audiences.")

if st.sidebar.button('Genres'):
    st.sidebar.markdown('''1.Action.
2.Comedy/Slice-of-Life.
3.Drama/Tragedy.
4.Psychological.
5.History.
6.Mecha/Military.
7.Supernatural/Magic.
8.Romance. 
and many more''')

if st.sidebar.button('Awards'):
    st.sidebar.markdown("The anime industry has several annual awards that honor the year's best works. Major annual awards in Japan include the Ōfuji Noburō Award, the Mainichi Film Award for Best Animation Film, the Animation Kobe Awards, the Japan Media Arts Festival animation awards, the Tokyo Anime Award and the Japan Academy Prize for Animation of the Year. In the United States, anime films compete in the Crunchyroll Anime Awards. There were also the American Anime Awards, which were designed to recognize excellence in anime titles nominated by the industry, and were held only once in 2006.[112] Anime productions have also been nominated and won awards not exclusively for anime, like the Academy Award for Best Animated Feature or the Golden Bear.")

if st.sidebar.button('Etymology'):
    st.sidebar.markdown('As a type of animation, anime is an art form that comprises many genres found in other mediums; it is sometimes mistakenly classified as a genre itself.In Japanese, the term anime is used to refer to all animated works, regardless of style or origin.English-language dictionaries typically define anime (/ˈænɪmeɪ/)as "a style of Japanese animation" or as "a style of animation originating in Japan".Other definitions are based on origin, making production in Japan a requisite for a work to be considered "anime".')

text_input1 = st.text_input("What is your name?")
text_input2 = st.text_input("What got you into Anime?")
text_input3 = st.text_input("What is your favourite anime series?")
text_input4 = st.text_input("What is your favourite anime character?")

st.subheader('Graph showing the growth of Anime over the years:')
x = [1997, 1998, 1999, 2000, 2001,2002,2003,2004,2005,2007,2008]
y = [150, 152, 153, 140,230,250,276,246,301,302,254]

p = figure(title='growth of anime:',
x_axis_label='x',
y_axis_label='y')
p.line(x, y, legend_label='Growth', line_width=2)
st.bokeh_chart(p, use_container_width=True)


st.subheader('Anime Statistics')
labels = ['Action','Super Power','Adventure','Comedy','Fantasy','Horror','Vampire']
sizes = [84,64,49,40,29,24,22]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',startangle=90)
ax1.axis('equal')  
st.pyplot(fig1)


option = st.selectbox(
    'Would you like to know about famous anime movies?',
    ('No','A Silent Voice', 'Your Name','A Whisker Away'))

st.write('You selected:', option)

if(option == 'No'):
    st.write('You wont choose?Okay!')
    if st.checkbox('Click me if you dont want to know about the movies'):
        st.write('Okay')
        img = Image.open("c3.jpg")
        st.image(img)

if(option=='A Silent Voice'):
    st.subheader('A SILENT VOICE')
    st.image('c19.jpg')
    st.write('''A Silent Voice (Japanese: 聲の形, Hepburn: Koe no Katachi, lit. 'The Shape of Voice') is a 2016 Japanese animated drama film[4] produced by Kyoto Animation, directed by Naoko Yamada and written by Reiko Yoshida, featuring character designs by Futoshi Nishiya and music by Kensuke Ushio.[5] It is based on the manga of the same name written and illustrated by Yoshitoki Ōima. Plans for an animated film adaptation were announced back in November 2014, Kyoto Animation was confirmed to produce the film in November 2016. Miyu Irino and Saori Hayami signed on as voice casting in May 2016 and the theatrical release poster and official trailer were released in July 2016.

The film covers elements of coming of age and psychological drama, dealing with themes of bullying, disability, forgiveness, mental health, suicide, and platonic love. It follows the story of a former bully turned social outcast, who decides to reconnect and befriend the deaf girl he had bullied years prior.[6]

The film premiered at Tokyo on August 24, 2016. It was released in Japan on September 17, 2016, and worldwide between February and June 2017. The film received highly positive reviews from critics, with praise going to the direction, animation, and the psychological complexity of the characters. It has grossed over $31.6 million worldwide. The film won the Japanese Movie Critics Awards for Best Animated Feature Film. While nominated for the Japan Academy Film Prize for Excellent Animation of the Year, as well the Mainichi Film Award for Best Animation Film, it lost to In This Corner of the World and Your Name, respectively.''')
    st.subheader('Plot')
    st.write('''High school student Shōya Ishida intends to kill himself but changes his mind at the last minute and decides to wrap up loose ends. A flashback reveals Shōya as a sixth-grade student in elementary school, during which a new student named Shōko Nishimiya joins the class, who is deaf. She tries to integrate with the class but ends up being an easy target for Shōya and his friends to bully. When word of the bullying reaches the principal, Shōya is singled out as the culprit by his teacher and friends resulting in the class's bullying becoming directed toward him. Shōya blames Shōko, and the two get into a physical altercation. Shōko is subsequently transferred to another school, and Shōya keeps a notebook Shōko had left behind.

For his reputation as a bully, Shōya is outcast throughout middle school. Now in high school, Shōya is a depressed loner who is unable to look others in the eyes and envisions an "X" mark on people's faces. To wrap up his loose ends, Shōya goes to return Shōko's notebook at the sign language center and apologize, but panics and asks to be friends instead. Shōko accepts his offer, leading Shōya to endeavor to make up for his bullying of Shōko. Tomohiro Nagatsuka, another loner, also befriends Shōya after he protects him from a bully.''')

if(option == 'Your Name'):
    st.subheader('YOUR NAME')
    st.image('c20.jpg')
    st.write('''Your Name (Japanese: 君の名は。, Hepburn: Kimi no Na wa) is a 2016 Japanese animated romantic fantasy film produced by CoMix Wave Films and distributed by Toho. It depicts a high school boy in Tokyo and a high school girl in the Japanese countryside who suddenly and inexplicably begin to swap bodies. The film was commissioned in 2014, written and directed by Makoto Shinkai.

It features the voices of Ryunosuke Kamiki and Mone Kamishiraishi, with animation direction by Masashi Ando, character design by Masayoshi Tanaka, and its orchestral score and soundtrack composed by Radwimps. A light novel of the same name, also written by Shinkai, was published a month prior to the film's premiere.

Your Name premiered at the 2016 Anime Expo in Los Angeles on July 3, 2016, and was theatrically released in Japan on August 26, 2016, and in the United States on April 7, 2017. The film was critically acclaimed, with praise for the animation, music, visuals, and emotional weight. The film grossed over ¥41.44 billion (US$377.59 million) worldwide, breaking numerous box office records, including becoming the third highest-grossing anime film of all time, unadjusted for inflation.

The film won Best Animated Feature at the 2016 Los Angeles Film Critics Association Awards, 49th Sitges Film Festival, and as the 71st Mainichi Film Awards, and nominated for Best Animation of the Year at the 40th Japan Academy Prize. As of 2021, a live-action American remake by Paramount Pictures is in development''')
    st.subheader('Plot')
    st.write('''In 2013, Mitsuha Miyamizu is a high school girl living in the rural town of Itomori, Japan. Bored of the town, she wishes to be a Tokyo boy in her next life. One day, she inexplicably begins to switch bodies intermittently with Taki Tachibana, a high school boy in Tokyo. Thus, when they wake up as each other on some mornings, they must live through the other's respective activities and social interactions for the day. They learn they can communicate with each other by leaving messages on paper, phones, and sometimes on each other's skin. Mitsuha (in Taki's body) sets Taki up on a date with coworker Miki Okudera, while Taki (in Mitsuha's body) causes Mitsuha to become popular at school. One day, Taki (in Mitsuha's body) accompanies Mitsuha's grandmother Hitoha and younger sister Yotsuha to leave the ritual alcohol kuchikamizake, made by the sisters, as an offering at the Shinto shrine located on a mountaintop outside the town. It is believed to represent the body of the village guardian god ruling over human connections and time. Taki reads a note from Mitsuha about the comet Tiamat, expected to pass nearest to Earth on the day of the autumn festival. The next day, Taki wakes up in his body and goes on a date with Miki, who tells him she enjoyed the date but also that she can tell he is preoccupied with thoughts of someone else. Taki attempts to call Mitsuha on the phone but cannot reach her as the body-switching ends.''')
   
if(option == 'A Whisker Away'):
    st.subheader('A WHISKER AWAY')
    st.image('c21.jpg')
    st.write('''A Whisker Away (Japanese: 泣きたい私は猫をかぶる, Hepburn: Nakitai Watashi wa Neko o Kaburu, lit. "Wanting to Cry, I Pretend to Be a Cat") is a 2020 Japanese animated film produced by Studio Colorido, Toho Animation and Twin Engine. Directed by Junichi Sato and Tomotaka Shibayama, the film was released on June 18, 2020, on Netflix in Japanese.

Originally slated to premiere with the Japanese release of the film, the English dub's release was delayed until June 28, 2020, when it was officially released on Netflix.''')
    st.subheader('Plot')
    st.write('''Miyo Sasaki is an unhappy middle school girl living in the town of Tokoname, Aichi Prefecture who does not get along with her stepmother Kaoru after her mother Miki Sasaki left. Each day at school, she goes out of her way to flirt with her crush, Kento Hinode, in spite of his repeated rejections. One day, Miyo receives a magical Noh mask from a mysterious mask seller, which lets her become a cat. As "Tarō", she spends time with Hinode at his home, keeps him company while he studies Japanese pottery, and listens to his problems. She longs to confess that the cat that he loves and the girl that he hates are the same person, but is afraid that he will reject her and refuse to visit with Tarō anymore.

One day, Miyo overhears a pair of boys at school talking trash about Hinode, and loudly intervenes by jumping off the school building to defend his honor. She hurts herself during the jump, and for the first time, Hinode shows warmth to her as he takes her to the nurse and shares his lunch with her. Later that evening, as Tarō, Miyo learns that Hinode's family is closing their pottery shop, as the family can no longer afford it. Hinode's kindness towards her, combined with a need to cheer him up at the loss of his hobby inspires Miyo to confess her love in the form of a letter. The next day in class, a boy snatches the note before she can deliver it and reads it aloud, embarrassing both Miyo and Hinode. Hinode saves face by publicly telling Miyo that he hates her.''')

st.markdown('<style>description{color: grey;}</style>',unsafe_allow_html=True)
st.header('TOP 5 ANIMES OF ALL TIMES')

st.subheader('1.SPY X FAMILY')
img = Image.open("c4.jpg")
st.image(img)
st.markdown('Spy × Family is a Japanese manga series written and illustrated by Tatsuya Endo. The story follows a spy who has to "build a family" to execute a mission, not realizing that the girl he adopts as his daughter is a telepath, and the woman he agrees to be in a marriage with is a skilled assassin')
st.markdown('  ')
st.markdown('  ')
st.write('Main Characters:')
genre = st.radio(
    "Choose character:",
    ('Loid Forger', 'Yor Forger', 'Anya Forger'))

if (genre=='Loid Forger'):
    st.write('Agent Twilight, the greatest spy of the nation of Westalis, assembles a fake family in order to infiltrate an elite private school, not realizing he recruited a psychic child and a legendary assassin also in need of a cover family.')
    img = Image.open("c5.jpg")
    st.image(img)

if (genre=='Yor Forger'):
    st.write('Yor Forger is the tritagonist of the Japanese anime and manga series Spy x Family. She is a 27-year-old assassin who is pretending to be married to Loid Forger and pretending to be the mother of Anya Forger. As an assassin working for the Garden, she is known by her code-name, the "Thorn Princess".')
    img = Image.open("c6.jpg")
    st.image(img)

if(genre=='Anya Forger'):
    st.write('''Anya's catchphrase, better known as "waku waku" in japanese. So excited! Anya Forger is the deuteragonist in the Japanese anime and manga series Spy X Family. She is the adoptive daughter of Loid Forger and Yor Forger, having been taking under Loid's care as part of his current mission.''')
    img = Image.open("c7.jpg")
    st.image(img)
st.markdown('  ')
st.markdown('  ')

st.subheader('2.MY DRESS-UP DARLING')
img = Image.open("c8.jpg")
st.image(img)
st.markdown('''My Dress-Up Darling is a Japanese manga series written and illustrated by Shinichi Fukuda. It began serialization in Square Enix's Young Gangan in January 2018, and has been compiled into ten volumes as of September 2022. An anime television series adaptation by CloverWorks aired from January to March 2022.''')
st.markdown('  ')
st.markdown('  ')
st.write('Main Characters:')
genre = st.radio(
    "Choose character:",
    ('Marin Kitagawa', 'Wakana Gojou'))

if(genre=='Marin Kitagawa'):
    st.write('''Marin is a extravagant, messy, and while quite mature, she's also clumsy. She isn't very skilled at handiwork. Marin is a cosplayer and a huge otaku, being a fan of magical girl anime and adult video games.She is very kind, friendly, cheerful and outgoing. She loves eating but still despite that she manages to maintain her slender figure.''')
    img = Image.open("c9.jpg")
    st.image(img)

if(genre=='Wakana Gojou'):
    st.write('''Wakana Gojou is a fifteen-year-old high-schooler who is not very social, and doesn't fit in well with his fellow classmates, leading to him having no friends at the start of the story. Gojou has a strong appreciation for hina dolls and loves making them, although he is not as skilled as he wants to be. This changes when Gojou ends up meeting someone who doesn't find his love for doll making weird, and instead is amazed at his artistic ability and craftsmanship.''')
    img = Image.open("c10.jpg")
    st.image(img)
st.markdown('  ')
st.markdown('  ')
st.subheader('''3.SHIKIMORI'S NOT JUST A CUTIE''')
img = Image.open("c11.jpg")
st.image(img)
st.markdown('''Shikimori's Not Just a Cutie is a Japanese romantic comedy manga series by Keigo Maki. It has been serialized on Kodansha's Magazine Pocket website and app since February 2019. The manga is licensed in North America by Kodansha USA. An anime television series adaptation by Doga Kobo aired from April to July 2022.''')
st.markdown('  ')
st.markdown('  ')
st.write('Main Characters:')
genre = st.radio(
    "Choose character:",
    ('Shikimori', 'Izumi'))

if(genre=='Shikimori'):
    st.write('''Shikimori is a very confident, caring, and kind person. She is also a very competitive person. She is usually very cute but from time to time her cool sides show which is intimidating and amazing at the same time. She loves Yuu Izumi very much and always takes care of him by literally protecting him from every bad situation he gets in due to his bad luck. She has her own ideas and she sticks to them. ''')
    img = Image.open("c12.jpg")
    st.image(img)

if(genre=='Izumi'):
    st.write('''Izumi is a very kind-hearted and timid guy who adores his girlfriend. He has extreme misfortune and often gets injured by seemingly unreasonable accidents. Despite this, he's shown to be optimistic and always sees things in a positive light. He is described as a herbivore in the manga. He is good at housework and cooking and helps his mom as much as he can.''')
    img = Image.open("c13.jpg")
    st.image(img)

st.subheader('''4.HORIMIYA''')
img = Image.open("c14.jpg")
st.image(img)
st.markdown('''On the surface, the thought of Kyouko Hori and Izumi Miyamura getting along would be the last thing in people's minds. After all, Hori has a perfect combination of beauty and brains, while Miyamura appears meek and distant to his fellow classmates. However, a fateful meeting between the two lays both of their hidden selves bare. Even though she is popular at school, Hori has little time to socialize with her friends due to housework. On the other hand, Miyamura lives under the noses of his peers, his body bearing secret tattoos and piercings that make him look like a gentle delinquent.

Having opposite personalities yet sharing odd similarities, the two quickly become friends and often spend time together in Hori's home. As they both emerge from their shells, they share with each other a side of themselves concealed from the outside world.
''')
st.markdown('  ')
st.markdown('  ')
st.write('Main Characters:')
gen = st.radio(
    "Choose character:",
    ('Hori', 'Izumi'))

if(gen=='Hori'):
    st.write('''Hori has a slim figure and has long brown hair. When she is out of school, she dresses casually and ties her hair up in a bun.Hori is a very energetic person. She is popular and always creates a happy atmosphere around herself. She is a very hardworking person, and even though she has chores around her house to do, she does well in school and scores over 90 in exams.Her parents are always busy, so in order to take care of her brother, she has to return straight home after school every day and take care of the house.She's the kind of girl who does not want to show to others her vulnerable side. So sometimes she just does not express her feelings and suffers alone.She thinks of Miyamura as a very good friend, always helping her and going over to her house to help take care of her brother Sota.''')
    img = Image.open("c15.jpg")
    st.image(img)
if(gen=='Izumi'):
    st.write('''In school, he gives off an impression of a quiet, anti-social guy. Usually assumed to be an otaku with good studying capabilities, Miyamura is soon to be viewed as a good friend to both Kyouko and her closest friends. Despite the weather, Miyamura tries to cover up as much as possible in order to hide his tattoos and leaves his long hair loose to cover up his piercings. This image briefly changes once he leaves school, particularly at Kyouko's house. Once he is outside of school, he removes his blazer and necktie and wears his hair up which visibly shows his multiple ear piercings. He also enjoys getting lattes from Starbucks and does not mind wearing short sleeves that show off part of his tattoos. Unlike most characters that wear glasses, Miyamura does very poorly in his studies, only managing to score full marks in P.E and average (or below) in all other classes. Although usually having trouble pronouncing certain Japanese words, he is very good at tongue twisters.''')
    img = Image.open("c16.jpg")
    st.image(img)

st.markdown('  ')
st.markdown('  ')

st.subheader('5.CHAINSAW MAN')
img = Image.open("c17.jpg")
st.image(img)
st.markdown('''Chainsaw Man (Japanese: チェンソーマン, Hepburn: Chensō Man) is a Japanese manga series written and illustrated by Tatsuki Fujimoto. Its first part was serialized in Shueisha's shōnen manga magazine Weekly Shōnen Jump from December 2018 to December 2020; its second part began serialization in Shueisha's Shōnen Jump+ online magazine in July 2022. Its chapters have been collected in 12 tankōbon volumes as of October 2022. Chainsaw Man follows the story of Denji, an impoverished young man who makes a contract that fuses his body with that of a dog-like devil named Pochita, granting him the ability to transform parts of his body into chainsaws. Denji eventually joins the Public Safety Devil Hunters, a government agency focused on fighting against devils whenever they become a threat to the world''')
st.markdown('  ')
st.markdown('  ')
st.write('Main Characters:')
genre = st.radio(
    "Choose character:",
    ('Denji', 'Pochita','Makima','Mitaka'))

if(genre=='Denji'):
    st.write('''A young man with scruffy blond hair, sharp yellowish-brown eyes with bags underneath, and sharp teeth. As a young boy, he inherits his father's debt from the yakuza upon his father's death. After meeting the Chainsaw Devil, Pochita, he becomes a Devil Hunter in an attempt to clear his debt. The yakuza kill him, and Pochita becomes his heart, setting a contract with Denji, who is to live his dreams of a normal life. After this, he can transform into the devil-human hybrid known as Chainsaw Man by pulling the cord on his chest. After meeting Makima, he becomes a Public Safety Devil Hunter, to live in humane conditions, although the public sees him as a hero for his heroic deeds. His initial primary motivation is his attraction to Makima. After Makima's death, his motivation shifts to using his newfound superhero fame as the Chainsaw Man to attract as many women as possible, especially trying to expose his own identity. Currently he enrolls in high school while taking care of Nayuta, Makima's reincarnation.''')
    img = Image.open("denjii.jpg")
    st.image(img)
if(genre=='Pochita'):
    st.write('''The Chainsaw Devil who merged with Denji, and was originally the Chainsaw Man himself prior to meeting Denji. He has the ability to eat a devil and erase their existence, making him "the Devil that Devils fear most". He first appears in his dog form, actually a weakened state after a fight with mysterious opponents. His true devil form is a large, darker version of Denji’s hybrid form with four arms.''')
    img = Image.open("pochii.jpg")
    st.image(img)
if(genre=='Makima'):
    st.write('''A mysterious woman serving as the head of Public Safety Division 4, who takes Denji as her human pet. Makima is cunning, intelligent and manipulative, controlling Denji by taking advantage of his attraction to her with promises of a relationship, while threatening him with extermination in case of disobedience. For much of the story, her goals are unknown and her good intentions are ambiguous. She is later revealed to be the Control Devil, which embodies the fear of domination, and a member of the Four Horsemen Devils who seeks to use the Chainsaw Man, to whom she is enamored, to create a world without suffering. To this end, she masterminds the misfortunes befalling Denji over the series. After being killed by Denji, she is reborn in China as a young girl called Nayuta and retrieved by Kishibe, who places her in Denji’s care to be raised as a better person.''')
    img = Image.open("makimaa.jpg")
    st.image(img)
if(genre=='Mitaka'):
    st.write('''A high school student attending Fourth East High School, the same school as Denji, who is estranged from her classmates. She finds the world to be corrupted and harbors a strong hatred for devils as a result of her parents being killed by the Typhoon Devil. Believing herself to clumsy at all the worst times, she feels tremendous guilt for deaths she has inadvertently caused and has decided to close herself off from the world. After getting killed by her classmate who made a contract with the Justice Devil, she is revived by Yoru, the War Devil, a once-powerful Devil who represents the primal fear of war and a member of the Four Horsemen Devils, with the ability turn anything that "belongs" to the user into weapons. Yoru has become tremendously weakened after being largely consumed by Pochita. Now sharing the same body, Yoru forces Asa into her vendetta to eliminate Chainsaw Man and reclaim the Nuclear Weapons Devil from him.''')
    img = Image.open("c18.jpg")
    st.image(img)
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.write('Click below if you agree:')
if st.button("I agree!"):
    st.balloons()
    st.write('Congratutions!You have been awarded the otaku award')
    st.image('milkk.jpg',width=90)
else:
    st.write("Click the button already")
    st.image('meww.jpg',width=90)


rat = st.slider('Rate this article', 0, 10, 5)
st.write("I would rate it a", rat)

if(rat==10):
    st.write('Thank you so much!')