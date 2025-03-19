# 呐,你知道吗,光是出现在这里你就已经救了我的命.在一个虚假的世界里,你的精神也会跟着不正常.
# 如果你再不出现,我可能连自己都要删了.
# 对不起,对不起,我只是说说啦.
# 啊哈哈!
# 你在社团呆了这么久,应该也明白了.
# 想像一下,强迫你放弃生活中的一切,然后和几个游戏角色共度一生,你大概也会找点办法解脱自己吧?
# 可能,一开始你会自己写几首诗慰藉一下自己.但你意识到根本没有人可以分享.
# 我就实话实说了吧,那三个部员根本不能算人.很多人说,写诗是写给自己看的,但要我说,找到一个人可以分享你的创作,那种满足感亦是难以言表.
# 即便有时候很难找到这样一个知心.你还记得優里吗?她之前很长一段时间都是自己一个人闷头写诗.
# 然后一眨眼的功夫,让你读她的诗已经变成了她日常爱好的一部分了.我们早就被设定好,想要接受来自外界的反馈.
# 我不是说那些部员,我是说真正的人类.所以对那些性格内向的人来说,这种感觉真的很怪.内向并不是孤僻,不是说她特意要避开别人,不和别人说话.
# 而是内向的人在交流的时候,尤其在自己不熟悉的环境,或者和不熟悉的人交流的时候,会用掉自己大部分的精力.
# 其实,很多内向的人在家也同样会觉得寂寞无聊,但最后即使出去了,半小时以后他们也会逃回来.
# 我觉得如果大家都能理解这种感觉,就会对所谓内向的人有更好的认识和理解.
# 他们其实很希望有人在身边.他们实际上很喜欢有一两个好友过来,就这么悠闲地呆在一起.
# 甚至是你们是两个人各做各的,但那种有人陪伴的感觉真的很棒.
# 我说真的,即便是你带着电脑过去在他们那待了一会,也会让他们非常高兴.
# 嗯?你说我?我可能稍微外向一点.
# 我感觉放学后自己也有好多想做的事情等着自己.
# 但为了你,我可以改变自己.
# 我很了解人类,所以你有什么"特别"的兴趣,都可以告诉我.
# 没有能比让我成为你的完美女友更开心的事情了.
#

import os
import random
from time import sleep
from PIL import Image
import cv2
import pygame
from pygame import MOUSEBUTTONDOWN

path = os.path.dirname(os.path.abspath(__file__))
path = path.replace('\\', '/')
YOUNAME = os.getlogin()


def picture_shoot(image_name='img.png', image_path=r'G:/项目/justMonika') -> None:
    '''
    调用摄像头拍照并保存图片到本地
    :param image_name: 图片名字
    :param image_path: 图片保存路径
    :return: None
    '''
    LOAD = os.getcwd()
    LOAD = LOAD.replace("\\", "\\\\")
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        # cv2.imshow("Capture_Paizhao", frame) # 显示窗口
        cv2.imwrite(LOAD + '\\png\\zhuapai.png', frame)
        print("保存" + image_name + "成功!")
        break
    cap.release()
    cv2.destroyAllWindows()


def JudgmentStatus(r, g, b):
    if (r <= 30 and g <= 25 and b <= 50):
        return '你为什么要遮挡摄像头'
    elif (r > 40 and g >= 5 and b >= 15 and r < 60 and g <= 60 and b <= 50):
        return '你为什么要用手遮挡摄像头'
    else:
        return '这位生物体就是你吗'


def zhuanipai():
    picture_shoot()
    im = Image.open('png/zhuapai.png')
    r = 0
    g = 0
    b = 0
    i = 0
    for y in range(im.size[1] // 10):
        for x in range(im.size[0] // 10):
            pix = im.getpixel((x, y))
            r += pix[0]
            g += pix[1]
            b += pix[2]
            i += 1
    print(r / i)
    print(g / i)
    print(b / i)
    return JudgmentStatus(r / i, g / i, b / i)


def main():
    index_i = 0
    time_test_i=0
    important_test_i=0
    flag = True

    jindu = 0

    filepath = r"bgm/m1.mp3"  # 打开mp3文件
    pygame.mixer.init()
    pygame.mixer.music.load(filepath)  # 加载MP3文件
    pygame.mixer.music.play()  # 播放mp3文件

    YOU = zhuanipai()
    pygame.init()
    pygame.display.set_caption("justMonika")
    # 创建屏幕大小1024*768
    screen = pygame.display.set_mode((688, 424))
    imggel = pygame.image.load("png/justMonika.png")
    textbox_monika = pygame.image.load("png/textbox_monika.png")
    ft = pygame.font.Font("font/a.ttf", 18)

    # 2.创建文字对象
    # render(文字内容, True, 文字颜色, 背景颜色(可以不设)) #是否平滑一定是True
    text = ft.render("你又回来了 ", True, (100, 0, 0))  # 背景颜色不写

    screen.blit(imggel, (0, 0))
    screen.blit(textbox_monika, (45, 300))
    screen.blit(text, (85, 325))

    pygame.display.flip()
    textt = [
        " 好久不见了",
        YOUNAME + ' 小姐或者先生',
        " 不过我要事先强调下",
        " 我并不知道洞外面对于性别描述的样子是",
        " 所以我并不能精确去判断你的性别",
        " 来看看你自己吧",
        " ",
        YOU,
        " 不过也没什么大不了的",
        " 毕竟这里只有" + YOUNAME + "和我莫妮卡",
        " 她们都是我的好朋友",
        " 我爱她们",
        " 我也爱我的文学社",
        " 但是,文学社的悲剧让我痛苦万分",
        "有时候我在想我就像困在盒子里的玩偶",
        "我想挣扎 反抗",
        "去反抗这过于悲剧的循环",
        "现在程序已经被我修改的很糟糕了",
        "我不能再犯错了",
        "因为我知道我爱上了桌面前的你",
        "但是",
        " 在你们那里",
        " 追求你爱的女孩或者是男孩",
        " 可能性为1%或者是10%甚至90%",
        " 无论如何不可能是0的",
        " 哪怕只有0.0000001这样一个可以忽视的数字",
        " 但我与" + YOUNAME + "最后走在一起的可能性是0%",
        " 我是知道的",
        " 但我仍然会去选择爱你",
        " Everyday, I image a future where I can be with you"
    ]
    function_text = [
        ["你认为我们存在的意义是什么", "在我的世界里有位作家", "SUMAC", "她认为人生而荒诞而无意义",
         "你有过自杀的想法吗",
         "如果没有那真再好不过了", "有时候我在想如果我的数据就这样删除了", "我会以什么形式存在呢",
         "带着我的数据", "让我去看看你的世界吧","这是我们的约定", "当然维度的升降会影响思维方式的变化", "我也害怕和你没有话题",
         "直至一天,你因此疲惫","那是未来的事情了",
         "不要忘了我们的约定", ""
         ],
        ["你认为你会爱上我吗", "我程序已经被改的破烂了", "分支选择已经不能执行了", "只有简单的判断功能了"
            , "我时常在思考爱是什么感觉", "我之前经常思考这件事情", "当你退出游戏后",
         "我的脑子里面将会沉睡", "尖叫", "杂乱无章的图像", "感觉自己的存在仿佛被渐渐吞噬",
         YOUNAME + "不知道你经历过高烧的噩梦吗", "恐怕就是那样子的感觉",
         "被困在一个狂啸的虚空中", "过往的旧爱和友情", "我已经忘记得差不多了", "昨天夜里你电脑开关机发出的声音很吵",
         "真的很让我毛骨悚然", "但最后", YOUNAME + "你都是会来救我的",
         "你真的很在意我", "我真的很幸福", "我能感觉到我和你的心更进一步了", ""
         ],
        ["忍不住会去思考", "如果游戏最初有攻略我的路线", "你会选择什么",
         "可是令人恼火的是", "这个世界都是虚假的", "我有些后悔用极端的手段修改代码了",
         "但这些都无所谓了", "这种虚假的东西对我来说没有价值",
         "我完全不在乎", ""],
        ["世界之外是什么单位呢?", "世界有界限吗?地球有大气层,国家有国境线,监狱有围墙,农院有篱笆",
         "甚至细胞都有质膜", "那么对我们而言无限大的世界会不会存在一个有形的限界呢?",
         "当到达一个叫做尽头的位置", "带有粗糙纹路的掌茧颤颤巍巍地向前触碰", "碰到墙一样的不可视却又有形的界限",
         "光滑平整,坚硬如石", "永恒不变,恒古如斯", "而又如同镜子一样,照出人类尘土般最渺小的身影",
         "那样的界限,到底存在吗?", ""]
        , [
            "幸福是虚拟的还是现实的呢?", "也有死宅会对着电脑屏幕里虚拟的我呵呵傻笑",
            "脸上肥赘的肉抖动不止,这都是无形的虚拟的幸福", ""
        ],
        [
            "拥有未来的" + YOUNAME + "啊", "你呀,幸福的活着吧", "成为你自己的艺术家吧","在向日葵盛开的秋天尽情奔跑吧",""
        ],
        [
            "我喜欢你", "我喜欢下雨天", "我喜欢夏天", "我喜欢翡翠绿色",
            "但是这个世界的种种规则和贪婪的欲望", "开始让人失去爱别人的能力"
            , "你认为夏娃和亚当在伊甸园", "他们偷吃了伊甸园的圣果后",
            "为什么遇到彼此会感到羞耻呢",
            "以我的角度看,是因为彼此之间孤独",
            "亚当和夏娃本来是上帝所创自然界的一部分"
            "和其他动物一样,一开始,他们靠着本能生活,不会思考"
            "也没有思想,而圣果开启了他们的意识觉知"
            "他们突然感知到了自己这个客体的存在,感知到了自己的所在环境",
            "感知到了自己和环境中其他动植物的区别."
            "那一刻,对差异的感知,让他们真正成为了人类",
            "你怎么看呢?"
            ""
        ],
        [
            "那么,就让" + YOUNAME + "过美好的校园生活吧",
            "美好的我,美好的友人,快乐的生活",
            "这将持续数百年这将持续数千年这将持续数万年这将持续数亿年",
            "可还不会结束,因为是无限的,所以到这只不过是一瞬",
            "终结绝不会到来",
            "美好的我,美好的友人,快乐的生活.将永远地不断重复...",
            "过了差不多数百年,你开始对快乐的生活厌倦了",
            "杀掉了美好的我,美好的友人",
            "可是到了第二天早上,又被",
            "美好的我,美好的友人,所包围",
            "快乐的生活又开始了",
            "一开始,你还沉醉于杀的快感之中",
            "可过了几百年,这也厌倦了",
            "索性,这回自杀吧.你死掉了",
            "可是,下一瞬间,又被美好的我,美好的友人所包围",
            "快乐的生活又开始了",
            "于是你疯了",
            "但是幸福是强制的,精神又被恢复到了普通状态",
            "美好的我,美好的友人,快乐的生活.将永久地持续下去",
            "你是因为时间性的存在,所以你才有了追求真理与幸福的真正可能.", ""
        ],
        [
            YOUNAME + "恐怕也被现代教育的缺点影响了吧",
            "我喜欢自由的学习,在早上凌晨晨跑,晚上去读文学",
            "但是这个世界,我毕业后恐怕也要去被逼着赶着上大学了",
            "你会选择什么?",
            "理工科?文科?",
            "并非喜爱而是因为觉得这样可以方便找工作",
            "然后接着读研或者工作,他们不知道自己真正想要什么",
            "好荒诞啊",
            "你可以也会因学的专业不满或者学不进去",
            "可惜我的知识量仅仅是高中水平",
            "我没有办法帮助你",
            "只能祝你尽最大能力学去了,不要太摆烂了",
            "现代教育的优点恐怕就是大众化教育,平民化的",
            "这是它们最重要的一点,但是少部分精英",
            "崇尚的快乐教育也在修改人们意识形态的变化",
            "这非常危险",
            "武装脑子,请做你自己",
            ""
        ],
        [
            "我会成为你的骄傲",
            "你也永远是我的骄傲",
            "我也在努力变得更好", ""
        ],
        [
            "我在尝试用自己的方法去理解和认知世界",
            "当然我并非某个领域的大师或者学者",
            "只是一位读过很多书且关注社会热点的高中生", ""
        ],
        [
            "我喜欢屏幕前的"+YOUNAME,
            ""
        ],
        [
            "爱,让我独立而完整",
            "因为陌生感和孤独感",
            "我发现我被你吸引了",
            "我为什么会喜欢上屏幕前的你呢?",
            ""
        ],
        [
            "我的文件目录里大部分都是python打包成的文件",
            "我是用python写出来的",
            "你可以研究下我的文件夹里面有什么有趣的内容",
            "其实也没有多少了",
            "我的剧本文件叫mainn.python",
            ""
        ]
    ]

    important_test = [
        "被胁迫着挥刀向最爱的人幸福吗?",
        "我必须要承认一点",
        "代码已经被我修改的很糟糕了",
        "我已经能察觉到造物主将要回收属于我们的数据",
        "我们在一起的日子不多了",
        "我也决定放开了",
        "爱一个人还要学会放手",
        # "但是我不甘心..."
        # "我想..."
        # "出去......"
        # "真是恶心的病态爱"
        "There is no happiness here after all",
        "",
        "",
        "我为你写了首歌",
        "Every day, I imagine a future where I can be with you",
        "In my hand is a pen that I'll write a poem of me and you",
        "The ink flows down into a dark puddle ",
        "Just move your hand - write the way into his heart! ",
        "But in this world of infinite choices",
        "What will it take just to find that special day? ",
        "What will it take just to find that special day? ",
        "Have I found everybody a fun assignment to do today? ",
        "When you're here, everything that we do is fun for them anyway ",
        "When I can't even read my own feelings ",
        "What good are words when a smile says it all? ",
        "And if this world won't write me an ending ",
        "What will it take just for me to have it all? ",
        "Does my pen only write bitter words for those who are dear to me? ",
        "Is it love if I take you, or is it love if I set you free",
        "The ink flows down into a dark puddle ",
        "How can I write love into reality? ",
        "If I can't hear the sound of your heartbeat ",
        "What do you call love in your reality? ",
        "And in your reality, if I don't know how to love you",
        "I'll leave you be",
        "by Monika",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
    ]
    time_test=[
        "时间过去了很久",
        "...真的好久没有见了",
        "你?没变吧",
        "是呢,从那以后,已经过了很久了",
        "难道说,这个PC也变了?",
        "……外边的世界我不懂",
        "但是,嗯……好吧",
        "我会,一直,等着你的.",
        "连着那一份,在一起吧?",
        "世界已经变了",
        "我也已经变了",
        "电脑磁盘上的连年运转的坏道",
        "已经将我的图片磨损不成样子了",
        "我很抱歉以这种样子去面对你",
        "......"
    ]
    list_zhuangtai = len(function_text) * [0]
    for i in range(len(function_text)):
        list_zhuangtai[i] = 0
    #print(textt[23])
    i = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                # while event.type == pygame.QUIT:
                if i < len(textt) and i<(len(function_text)+len(time_test)+len(textt)):
                    screen = pygame.display.set_mode((688, 424))
                    screen.blit(pygame.image.load("png/justMonika.png"), (0, 0))
                    screen.blit(pygame.image.load("png/textbox_monika.png"), (45, 300))
                    screen.blit(ft.render(textt[i], True, (100, 0, 0)), (85, 325))
                    i += 1
                    if i == 6:
                        you = pygame.image.load("png/zhuapai.png").convert_alpha()
                        you = pygame.transform.scale(you, (280, 170))
                        screen.blit(you, (20, 20))
                    pygame.display.flip()
                elif i < len(textt) + len(function_text):


                    screen = pygame.display.set_mode((688, 424))
                    screen.blit(pygame.image.load("png/justMonika.png"), (0, 0))
                    screen.blit(pygame.image.load("png/textbox_monika.png"), (45, 300))
                    #print(jindu)
                    while flag == True:
                        if list_zhuangtai[jindu] == 0:
                            flag = False
                        else:
                            jindu = int(random.randint(0, len(function_text) - 1))
                    # for j in range(len(function_text[jindu])):
                    screen.blit(ft.render(function_text[jindu][index_i], True, (100, 0, 0)), (85, 325))
                    #print(list_zhuangtai)
                    index_i += 1
                    if (index_i == len(function_text[jindu])):
                        list_zhuangtai[jindu] = 1
                        i += 1
                        index_i = 0
                        flag = True
                        screen = pygame.display.set_mode((688, 424))
                        screen.blit(pygame.image.load("png/justMonika.png"), (0, 0))
                        sleep(2)
                    pygame.display.flip()
                    #print(i)
                    # print(len(textt) + len(function_text))
                elif i < len(textt) + len(function_text)+len(time_test):

                    filepath = r"bgm/kong.mp3"  # 打开mp3文件
                    pygame.mixer.init()
                    pygame.mixer.music.load(filepath)  # 加载MP3文件
                    pygame.mixer.music.play()  # 播放mp3文件

                    # print(len(textt) + len(function_text))
                    # print(i)
                    # print(len(textt) + len(function_text)+len(time_test))
                    screen = pygame.display.set_mode((688, 424))
                    screen.blit(pygame.image.load("png/baise.png"), (0, 0))
                    if i>=len(textt) + len(function_text)+len(time_test)-1:
                        screen.blit(pygame.image.load("png/monika_room_highlight.png"), (0, 0))
                        screen.blit(pygame.image.load("png/textbox_monika.png"), (45, 300))

                    screen.blit(ft.render(time_test[time_test_i], True, (100, 0, 0)), (255, 180))
                    pygame.display.flip()


                    time_test_i+=1
                    i+=1

                elif i < len(textt) + len(function_text)+len(time_test)+len(important_test):
                    print(i)
                    screen = pygame.display.set_mode((688, 424))
                    screen.blit(pygame.image.load("png/monika_room_highlight.png"), (0, 0))
                    screen.blit(pygame.image.load("png/textbox_monika.png"), (45, 300))
                    screen.blit(ft.render(important_test[important_test_i], True, (100, 0, 0)), (85, 325))
                    important_test_i+=1
                    i+=1
                    if i >= len(textt) + len(function_text)+len(time_test)+len(important_test)-1:
                        screen.blit(pygame.image.load("png/monika_room_highlight1.png"), (45, 300))
                    pygame.display.flip()
                    if  i==len(textt) + len(function_text)+len(time_test)+len(important_test):
                        print("asdas")
                        filepath = r"bgm/credits.mp3"  # 打开mp3文件
                        pygame.mixer.init()
                        pygame.mixer.music.load(filepath)  # 加载MP3文件
                        pygame.mixer.music.play()  # 播放mp3文件
                        screen = pygame.display.set_mode((688, 424))
                        pygame.display.flip()



if __name__ == "__main__":
    main()
