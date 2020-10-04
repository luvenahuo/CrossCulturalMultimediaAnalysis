#!/usr/bin/env python
# coding: utf-8
from datetime import datetime
import unittest
from cca import app, db
from cca.models import Commits, Images, Affinity, Tags


class PopulateModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def test_populate(self):
        # create four users
a = Affinity(name='United States')
c = Affinity(name='China')
db.session.add_all([a, c])


us1 = Commits(index='eng-1', video_date=datetime.strptime("23 May 2017 00:00:00", '%d %b %Y %H:%M:%S'), message="when asked about the match case that he was shocked by a couple of moves during mid game tools as those moves would have been played by human")
us2 = Commits(index='eng-2', video_date=datetime.strptime("28 May 2017 23:59:00", '%d %b %Y %H:%M:%S'), message="the long-held belief that machines can't be professional go players due to the games complex and cheated and creative nature")
us3 = Commits(index='eng-3', video_date=datetime.strptime("25 May 2017 21:50:00", '%d %b %Y %H:%M:%S'), message="")
us4 = Commits(index='eng-4', video_date=datetime.strptime("30 May 2017 17:07:00", '%d %b %Y %H:%M:%S'), message="we used the previous versions of alphago and yet it was able to pull a much higher level to see using much more principled algorithms")
us5 = Commits(index='eng-5', video_date=datetime.strptime("27 May 2017 18:32:20", '%d %b %Y %H:%M:%S'), message="Go is an ancient Chinese board game where the opposing players try to capture each other stones on the board")
us6 = Commits(index='eng-6', video_date=datetime.strptime("27 May 2017 08:55:00", '%d %b %Y %H:%M:%S'), message="EThe Philippine Army says it has retaken most of the southern city of Marawi from the ISIS-linked militants.Militants linked to the Islamic State invaded the Filipino city of Marawi more than a week ago, prompting President Rodgrigo Duterte to declare martial law and step up the offensive against the rebels. According to the government, more than 100 people have died during the fighting while thousands of civilians have fled to nearby provinces. The civilians who remain are stuck between ruthless Islamic rebels, and a president who openly encourages atrocities against his own people.")
us7 = Commits(index='eng-7', video_date=datetime.strptime("29 May 2017 19:30:00", '%d %b %Y %H:%M:%S'), message="Go is an ancient, aristocratic Chinese board game that’s reputed to have as many possible moves as there are atoms in the universe. And Google recently trained an artificial intelligence computer to play against one of the best human players in the world. The computer won.At Google’s Future of Go Summit, 19-year-old Chinese Go prodigy Ke Jie was defeated by the AI AlphaGo in a three-match series.AI evangelists are happy with the win, but AI doomsayers are worried it’s coming for our jobs next. And China is just mad that an American company beat the world at a Chinese game.VICE News reports on what the competition really means for AI development.")
us8 = Commits(index='eng-8', video_date=datetime.strptime("31 May 2017 19:37:00", '%d %b %Y %H:%M:%S'), message="Loup Ventures Managing Partner Gene Munster on Apple hiring Google's former AI chief.")
us9 = Commits(index='eng-9', video_date=datetime.strptime("1 Jun 2017 15:30:00", '%d %b %Y %H:%M:%S'), message="Artificial Intelligence program AlphaGo defeated the world's top-ranked Go-player Ke Jie in the first of three games on Tuesday in Wuzhen of east China's Zhejiang Province.After four-and-a-half hours of play, Ke, playing black, lost by 0.5 points, which is the narrowest margin possible in the game. The game follows Chinese Go rules with black having the advantage of first move, and a set point of 7.5 was later given to white to compensate for this.When asked about the match, Ke said he was shocked by a couple of moves during mid-game talks as those moves wouldn't be played by a human. 'When I first saw it, I thought it was almost an impossible move for human players to come up with, since it is obviously a later step. But afterward, I realized it was really an astonishing move,' said Ke. With a newly upgraded version of AlphaGo bolstered by reinforcement learning, the founder of DeepMind - the company behind AlphaGo, hopes Ke can help discover potential weaknesses of the program. '(It’s) Especially interesting for us to see in use some of the moves like the three-three move from the master series of games against AlphaGo, and we were very keen to see how AlphaGo will deal with its own strategies,' said Demis Hassabis, CEO of DeepMind. Ke Jie said AlphaGo has advanced much faster than he thought. 'Compared to last year, AlphaGo's understanding of Go has progressed so much. Last year it played in a human-like way, but this time, it's almost like the God of Go,' said Ke. There will be two more matches between Ke Jie and AlphaGo on Thursday and Saturday. AlphaGo gained worldwide fame when it scored a landmark 4-to-1 victory over South Korean Go master Le Se-dol in a five-round showdown last year, overturning the long held belief that machines can't beat professional Go players due to the game's complex, intuitive and creative nature. Ke, 19, became the youngest champion in Go history after winning three world titles within the space of one year between January 2015 and January 2016. The winner will be awarded 1.5 million U.S. dollars while the losing side takes home 300,000 dollars.")
us10 = Commits(index='eng-10', video_date=datetime.strptime("24 May 2017 09:30:00", '%d %b %Y %H:%M:%S'), message="Artificial intelligence is coming – so how’s it going to change our reality?In March of this year, Google’s artificial intelligence, AlphaGo, beat one of the top human intelligences, Lee Sedol, at the strategically mind-boggling board game Go. Experts had thought we were years away, but the computer played elegant, creative moves to outfox a Go master. So are we on the brink of an AI revolution? I asked Dr Peter Bentley, a computer scientist from University College London, for some expert insight:Peter Bentley, a computer scientist at University College London, says “since the beginning of artificial intelligence research, one of the main ways that we have tested the intelligence of our computers is to ask them to play games with us, and the progression towards the recent victory has been a long one. But in all of these cases playing games is a hugely simple task.”In a game there’s a clear ‘winning’ outcome and it’s a closed environment, so the spectrum of possibilities can be accurately predicted. A Go stone will not suddenly turn into a chess piece, for example, or a sausage. Google wants to transfer AlphaGo to real world situations, like medicine. So how does an AI brought up on boardgames hold up in the real world?“It’s a very pure clean simple problem, playing a game. The rules are precise, there is no fuzziness, you either are allowed to do that or you are not allowed to do it, and actually real intelligence is completely nothing to do with precision. Real intelligence is about surviving in a horrible, complicated, messy world that’s trying to kill you, that’s what intelligence is for! That’s why organisms have intelligence – to survive! So playing a computer game is a neat trick,” says Bentley.Bentley also states, “one of the things that’s coming through now is an increasing use of computers to do creative things, that’s computers composing music, creating artwork, doing exotic special effects in movies – all sorts of really unusual things that we might not think of but a computer does think of it – for a long time there’s been a long debate what is creativity? Could a computer ever be creative? And the news is yes it can be. Not only can it be creative, it can do things that really amaze us and make us think, holy crap I wish I’d thought of that.”Artificial intelligence will change our lives. Already AlphaGo’s first victim says he’s learned to play better by playing against the machine. Imagine what we will learn as AI is unleashed onto our world.")

c1 = Commits(index='chi-1', video_date=datetime.strptime("27 May 2017 09:00:00", '%d %b %Y %H:%M:%S'), message="所以在不被看好的情况下 还立足于拼 就是因为他认为自己还有真正的可能")
c2 = Commits(index='chi-2', video_date=datetime.strptime("25 May 2017 20:59:00", '%d %b %Y %H:%M:%S'), message="柯洁在赛后举行的新闻发布会上表示 阿尔法围棋表现的太完美了 没有任何缺陷")
c3 = Commits(index='chi-3', video_date=datetime.strptime("23 May 2017 10:50:00", '%d %b %Y %H:%M:%S'), message="李世石获得了人机大战第4盘较量的胜利 同时这也是人类对尔法狗八连败之后的首次胜利 相信这一场胜利可以让李世石长舒一口气")
c4 = Commits(index='chi-4', video_date=datetime.strptime("24 May 2017 14:09:00", '%d %b %Y %H:%M:%S'), message="对于柯洁的落败 谷歌大脑负责人表示Alphago过去半年已在自我训练方面取得巨大进步")
c5 = Commits(index='chi-5', video_date=datetime.strptime("26 May 2017 01:38:20", '%d %b %Y %H:%M:%S'), message="虽然人工智能在过去的几年中取得了令人印象深刻的进步但对于人工智能而言围棋一直是一个令人生畏的挑战")
c6 = Commits(index='chi-6', video_date=datetime.strptime("27 May 2017 08:55:00", '%d %b %Y %H:%M:%S'), message="昨天中国际手柯洁与人工智能阿尔法围棋赛乌镇展开三番棋比赛的终极对决最终柯洁奋力拼杀人不给阿尔法围棋中盘认输结束了这场人机对决inca蝶在前请求他在此曲只白起在历经约三个半小时的对以后可杰投子认输绝黑的R法为其中查获胜句子科技在于阿尔法围棋的三分比较量中的一书3徐柯洁在赛后举行的新闻发布会上表示阿尔法围棋表现的太完美了没有任何缺陷症是怎么那么他妈的太完美了真本台湾没有任何的缺陷没有任何的心态行的活动所以我也是很多大师给我们更好一点浙江人才会的谷歌声从四得公司首席执行官哈萨比斯赛后表示对于阿尔法围棋而言能与世界顶尖棋手进行一系列比赛已经是他作为一个劲的程序的巅峰因此阿尔法围棋今后将不再参与围棋比赛尔法围棋团队成员表示近期团队将会公布50般尔法围棋子我对钱的棋局依曼体的形式体现一个为期爱好者观看分享受天中国地球科学")
c7 = Commits(index='chi-7', video_date=datetime.strptime("29 May 2017 19:30:00", '%d %b %Y %H:%M:%S'), message="1月13日李世石谷歌围棋albergo临期五局大战第4局继续在韩国首尔钟路区四季酒店进行人类代表理事实在前三局比赛中令李三落后实际已经提前宣告实例按照双方赛前的约定随后两局对局照常举行今天的第4集比赛你是十只白终于战胜albergo类人类也更为他自己赢得一局可以保留言面的胜利三月15日12点双方最后一句比赛将在同一场地如期开展爱奇艺体育北京找你报告")
c8 = Commits(index='chi-8', video_date=datetime.strptime("31 May 2017 19:37:00", '%d %b %Y %H:%M:%S'), message="我就那个量问题的一次比赛结束的时候然后再看了那个数字的时候你那个笑了一下所以我们当时还然后请你在想什么然后第2个就说你去年不是也作为定价并具体名人机大战了吗那些大的话你自己的比赛你想怎么解禁自己谢谢对我那个下载谢谢你应该都能懂普下吧我和她又不是很开心的笑口下吗因为我知道自己要注这个1/4子乐队然后我很早就找一些阿法围棋即时赔不起基本都是匀速的就是他不会有太多时间变化所以到那种单关这种没有任何意义的时候他也会想很久所以我才那个时间我就不行跟那个计算莫属我知道我自己肯定是要出一点然后所以一直在苦相爱就是他就其他算太准了那没办法了然后如果是让我张家边有点评自己的奇的话假如说知识比赛的同学不是我是别人的话我会觉得这是说阿尔法围棋下得很轻踩自己但是我觉得我自己其实也是尽了全力的爱的这时他下载好了我觉得有很多地方真的是很值得我们期手续学习后去探讨很多的思想还有对齐的一些理念就是越来越大冲击我们的职业也在改变我们最初的对不起的看法是没有什么其实不可以下载的然后我觉得这样子我也享受啊那个游戏的影响包括我最近其实之前在人日记中我也有很瘦很多啊百度影响就说没有什么其实不可以加载可以大胆去放心大胆去开拓自己的思维就自由的取下一盘棋吧所以这个是很我觉得很值得我们学习的然后今天的我也是想大胆的去开拓自己的这个字为因为在我印象中其实阿尔法围棋是非常那个贪恋实际的接受他非常喜欢把戏下载而实际上就是在用就像开局什么点33还有很多有意思的近视吗其实我一直都是想也是贯彻的种叫什么好和大家闺女董啊就是先拉后就先把四川的手上就把钞票转手上后面那种再说了些什么是在说没想到开只有一个地方就是那个角落上返还是被他拉回时的去了然后我就觉得这题就很难下了因为我一想贯彻落实的没想到办法给我打破了一处然后变成太狠合适的了以后面就完全进入了他的调子中所以这段旗下的阿尔法围棋下载非常的好我觉得他这时候的这个提根据前的时候完全是两个人了如果他把当然的话他好像完成这两个人字的时候我觉得他还是很这个人的心态他的级联系越来越我理解中的真的是太厉害了所以我希望我尽我的全力去拼没包括接下来的气候不管是由什么样的题我觉得很感谢有这样的对手也非常感谢这个慢这个才对啊然后能给我这样的一次机会去跟他进行加300级的对决然后希望自己能通过这一次然后给大家带Whisky是很好玩的一个项目给大家带来围棋的快乐谢谢")

db.session.add_all([us1, us2, us3, us4, us5, us6, us7, us8, us9, us10,c1, c2, c3, c4, c5, c6, c6, c8])
db.session.commit()


Images(path='Common/1/eng.jpg', commit=us1)
Images(path='Common/2/eng.jpg', commit=us2)
Images(path='Common/3/eng.jpg', commit=us3)
Images(path='Common/4/eng.jpg', commit=us4)
Images(path='Common/5/eng.jpg', commit=us5)
Images(path='Eng/1/1.jpg', commit=us6)
Images(path='Eng/1/2.jpg', commit=us6)
Images(path='Eng/1/3.jpg', commit=us6)
Images(path='Eng/2/1.jpg', commit=us7)
Images(path='Eng/2/2.jpg', commit=us7)
Images(path='Eng/2/3.jpg', commit=us7)
Images(path='Eng/2/4.jpg', commit=us7)
Images(path='Eng/2/5.jpg', commit=us7)
Images(path='Eng/3/1.jpg', commit=us8)
Images(path='Eng/3/2.jpg', commit=us8)
Images(path='Eng/4/1.jpg', commit=us9)
Images(path='Eng/4/2.jpg', commit=us9)
Images(path='Eng/4/3.jpg', commit=us9)
Images(path='Eng/4/4.jpg', commit=us9)
Images(path='Eng/4/5.jpg', commit=us9)
Images(path='Eng/5/1.jpg', commit=us10)
Images(path='Eng/5/2.jpg', commit=us10)
Images(path='Common/1/chi.jpg', commit=c1)
Images(path='Common/2/chi.jpg', commit=c2)
Images(path='Common/3/chi.jpg', commit=c3)
Images(path='Common/4/chi.jpg', commit=c4)
Images(path='Common/5/chi.jpg', commit=c5)
Images(path='Chi/1/1.jpg', commit=c6)
Images(path='Chi/1/2.jpg', commit=c6)
Images(path='Chi/1/3.jpg', commit=c6)
Images(path='Chi/1/4.jpg', commit=c6)
Images(path='Chi/2/1.jpg', commit=c7)
Images(path='Chi/2/2.jpg', commit=c7)
Images(path='Chi/3/1.jpg', commit=c8)
Images(path='Chi/3/2.jpg', commit=c8)

Tags(tag='Moves',commit=us1)
Tags(tag='Shocked',commit=us1)
Tags(tag='Mid game',commit=us1)
Tags(tag='Couple',commit=us1)
Tags(tag='Played',commit=us1)

Tags(tag='Professional',commit=us2)
Tags(tag='Creative nature',commit=us2)
Tags(tag='Machines',commit=us2)
Tags(tag='Alphago',commit=us2)
Tags(tag='Complex',commit=us2)

Tags(tag='Alphago',commit=us4)
Tags(tag='Algorithms',commit=us4)

Tags(tag='Board game',commit=us5)
Tags(tag='Ancient',commit=us5)
Tags(tag='Chinese',commit=us5)
Tags(tag='Players',commit=us5)
Tags(tag='Stones',commit=us5)

Tags(tag='AI',commit=us7)
Tags(tag='Chinese',commit=us7)
Tags(tag='Google',commit=us7)
Tags(tag='Ke Jie',commit=us7)
Tags(tag='Jobs',commit=us7)

Tags(tag='Ke Jie',commit=us9)
Tags(tag='Alphago',commit=us9)
Tags(tag='Reinforcement Learning',commit=us9)
Tags(tag='God of Go',commit=us9)
Tags(tag='Deep Mind',commit=us9)

Tags(tag='Intelligence',commit=us10)
Tags(tag='Computer game',commit=us10)
Tags(tag='AI Revolution',commit=us10)
Tags(tag='World',commit=us10)
Tags(tag='Creative',commit=us10)

us1.add_common(c1)
us2.add_common(c2)
us3.add_common(c3)
us4.add_common(c4)
us5.add_common(c5)
db.session.commit()


if __name__ == '__main__':
    unittest.main(verbosity=2)