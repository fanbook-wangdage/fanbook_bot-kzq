import requests#发送请求
import json#处理数据
import traceback#错误检测
from colorama import init, Fore, Back, Style
import urllib.request
import time

init(autoreset=True)    #  初始化，并且设置颜色设置自动恢复
def addmsg(msg, color="white"):
    if color == "white":
        print(msg)
    elif color == "red":
        print("\033[31m" + msg + "\033[39m")
    elif color == "yellow":
        print("\033[33m" + msg + "\033[39m")
    elif color == "green":
        print("\033[32m" + msg + "\033[39m")
    elif color == "aqua":
        print("\033[36m" + msg + "\033[39m")

def colorprint(smg2,pcolor):
    if pcolor=='red':
      print(Fore.RED + smg2)
    elif pcolor=='bandg':
      print(Back.GREEN + smg2)
    elif pcolor=='d':
      print(Style.DIM + smg2)
    # 如果未设置autoreset=True，需要使用如下代码重置终端颜色为初始设置
    #print(Fore.RESET + Back.RESET + Style.RESET_ALL)  autoreset=True
import random
def generate_random_string(length):
    # 生成一个由数字组成的随机字符串
    return ''.join(random.choices('0123456789', k=length))

addmsg('欢迎使用机器人快捷操作系统，你可以使用此系统完成对机器人的常用操作，每次更新都会有新功能！ 由于时间仓促，代码难免会出现问题，如遇到问题，请给王大哥私信，请保持你的软件版本为最新版本 最新下载：http://fanbook_wdgsys.bailituya.com/ [王大哥 V4.0 让机器人控制变得更简单！]',color='aqua')
url = 'http://fanbook_wdgsys.bailituya.com/data.txt'#获取版本数据
response = urllib.request.urlopen(url)
data = response.read()
datatext = data.decode('utf-8') 
print("最新版本：",datatext)
if float(datatext) > 4.0:
    print("有最新版本,请去 http://fanbook_wdgsys.bailituya.com/ 下载最新版本")

while True:
    colorprint(smg2='请输入你的机器人的令牌',pcolor='bandg')
    lingpai=input()
    url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/getMe'
    headers = {'content-type':"application/json;charset=utf-8"}
    jsonfile=json.dumps({})
    postreturn=requests.post(url,data=jsonfile,headers=headers)
    colorprint(smg2=postreturn.text,pcolor='d')
    a=str(postreturn.text)
    a=(a[6:10])
    if a=='true':#检测返回内容
        colorprint(smg2='填写正确,回车键继续',pcolor='bandg')
        input()
        break
    else:
        colorprint(smg2='填写错误，回车重试(输入1跳过)',pcolor='bandg')
        a=input()
        if a=='1':
            addmsg('已跳过重试',color="yellow")
            break
addmsg('简介：',color='aqua')
addmsg('发送消息(1)：向频道（包括私聊）发送消息',color='aqua')
addmsg('发送图片(2)：向频道（包括私聊）发送图片，图片链接可通过右键帖子或频道内图片获得',color='aqua')
addmsg('创建私聊频道(3)：和一个用户建立私聊频道',color='aqua')
addmsg('禁言用户(4)：禁言用户，最大30天',color='aqua')
addmsg('创建频道(5)：创建已支持的频道，除过需要官方创建的',color='aqua')
addmsg('通过消息链接获取消息详细信息(6):输入消息链接可以获得用户和消息的详细信息',color='aqua')
addmsg('命令行模式：启动命令行支持其他功能（测试,不建议使用）',color='aqua')
addmsg('反馈模式(7)：给王大哥直接发送反馈消息',color='aqua')
addmsg('富文本模式(8):向频道(包括私聊)发送富文本',color='aqua')
addmsg('自定义勋章(9):为成员添加自定义勋章',color='aqua')
addmsg('获取勋章(10):获取成员勋章的详细信息',color='aqua')
addmsg('机器人迎新[自动化](11):有新成员进入时，自动在频道发送欢迎消息',color='aqua')
addmsg('发送定时重复消息[自动化](12): 重复在频道内延时一段时间后发送消息',color='aqua')
while True:
    try:#检测代码，防止错误闪退
        colorprint(smg2='请选择模式，1为发送消息(可发送私信消息)，2为发送图片，3为创建私聊频道，4为禁言用户，5为创建频道，6为通过消息链接获取消息详细信息，7为反馈模式，8为富文本模式，9为为成员添加自定义勋章，10为获取成员勋章的详细信息，11为机器人迎新[自动化]，12为发送定时重复消息[自动化]，命令行启动命令行模式，help获取错误码帮助',pcolor='bandg')
        a=input()
        if a=='1':
            colorprint(smg2='请输入频道id（如私信需要私聊id,可通过获取私聊id获取），获取方法：聊天框输入#，然后选择频道，发送后复制刚刚发送的蓝色频道名，复制后例如${#395848618357086556}，填写里面的数字395848618357086556即可',pcolor='bandg')
            pdid=input()
            colorprint(smg2='输入需要发送的消息',pcolor='bandg')
            xx=input()
            colorprint(smg2='请输入发送消息的次数',pcolor='bandg')
            cis=input()
            for i in range(int(cis)):
                url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                headers = {'content-type':"application/json;charset=utf-8"}
                jsonfile=json.dumps({
                "chat_id":int(pdid),
                "text": xx
                })
                postreturn=requests.post(url,data=jsonfile,headers=headers)
                colorprint(smg2=postreturn.text,pcolor='d')
        elif a=='2':
            colorprint(smg2='请输入频道id（如私信需要私聊id,可通过获取私聊id获取），获取方法：聊天框输入#，然后选择频道，发送后复制刚刚发送的蓝色频道名，复制后例如${#395848618357086556}，填写里面的数字395848618357086556即可',pcolor='bandg')
            pdid=input()
            colorprint(smg2='输入需要发送的图片链接',pcolor='bandg')
            tplj=input()
            colorprint(smg2='请输入发送消息的次数',pcolor='bandg')
            cis=input()
            for i in range(int(cis)):
                url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendPhoto'
                headers = {'content-type':"application/json;charset=utf-8"}
                jsonfile=json.dumps({
                    "photo": {
                    "Url": tplj
                    },
                    "chat_id":int(pdid)
                    })
                postreturn=requests.post(url,data=jsonfile,headers=headers)
                colorprint(smg2=postreturn.text,pcolor='d')
        elif a=='3':
            colorprint(smg2='请输入需要建立私聊频道用户的id,输出的id为对方私聊id，获取方法：聊天框输入@，然后选择需要私信的用户，发送后复制刚才发送的蓝色用户名，复制后例如${@!395848618357086556}，填写里面的数字395848618357086556即可',pcolor='bandg')
            yhid=input()
            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/getPrivateChat'
            headers = {'content-type':"application/json;charset=utf-8"}
            jsonfile=json.dumps({
                "user_id":int(yhid)
                })
            postreturn=requests.post(url,data=jsonfile,headers=headers)
            colorprint(smg2=postreturn.text,pcolor='d')
        elif a=='4':
            colorprint(smg2='请输入需要禁言的用户id',pcolor='bandg')
            yhid=input()
            colorprint(smg2='请输入用户所在的服务器id（设置服务器背景图下面有复制服务器id）',pcolor='bandg')
            fwqid=input()
            colorprint(smg2="禁言时长（以秒为单位)",pcolor='bandg')
            jysc=input()
            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/forbidUserSpeaking'
            headers={'content-type':"application/json;charset=utf-8"}
            jsonfile=json.dumps({
                "target_uid":yhid,
                "target_guild_id":fwqid,
                "duration_in_second":int(jysc),
                })
            postreturn=requests.post(url,data=jsonfile,headers=headers)
            colorprint(smg2=postreturn.text,pcolor='d')
        elif a=='5':
            colorprint(smg2='请输入你的id',pcolor='bandg')
            yhid=input()
            colorprint(smg2='请输入需要操作服务器id（设置服务器背景图下面有复制服务器id）',pcolor='bandg')
            fwqid=input()
            colorprint(smg2="请输入频道的名称",pcolor='bandg')
            pdmc=input()
            colorprint(smg2='请输入频道类型（0  普通文本频道，1	 语音频道，2	 视频频道，6   直播频道）',pcolor='bandg')
            pdlx=input()
            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/v2/channel/create'
            headers={'content-type':"application/json;charset=utf-8"}
            jsonfile=json.dumps({
                "user_id":yhid,
                "guild_id":fwqid,
                "name":pdmc,
                "type":int(pdlx)
                })
            postreturn=requests.post(url,data=jsonfile,headers=headers)
            colorprint(smg2=postreturn.text,pcolor='d')
        elif a=='6':
            colorprint(smg2='请输入消息链接',pcolor='bandg')
            xxlj=input()
            xxlj_ld=xxlj.split('/')
            fwqid=xxlj_ld[4]
            pdid=xxlj_ld[5]
            xxid=xxlj_ld[6]
            colorprint(smg2='服务器id：'+fwqid+'频道id:'+pdid+' 消息id：'+xxid,pcolor='d')
            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/getMessage'
            headers={'content-type':"application/json;charset=utf-8"}
            jsonfile=json.dumps({'chat_id':int(pdid),'message_id':int(xxid)})
            postreturn=requests.post(url,data=jsonfile,headers=headers)
            colorprint(smg2=postreturn.text,pcolor='d')
            print('主要内容：first_name：发送者昵称，username：发送者短id，avatar：发送者头像，text：发送内容')
        elif a=="命令行":
            colorprint(smg2='>>>',pcolor='bandg')
            cmd=input()
            if cmd == 'api':
                colorprint(smg2='api:',pcolor='bandg')
                cmd=input()
                colorprint(smg2='data:',pcolor='bandg')
                cmd2=input()
                cmd2=json.loads(cmd2)
                url='https://a1.fanbook.mobi/api/bot/'+lingpai+cmd
                headers={'content-type':"application/json;charset=utf-8"}
                jsonfile=json.dumps(cmd2)
                postreturn=requests.post(url,data=jsonfile,headers=headers)
                colorprint(smg2=postreturn.text,pcolor='d')
        elif a=='7':
            colorprint(smg2='请输入反馈信息',pcolor='bandg')
            c=input()
            d='{\"type\":\"richText\",\"title\":\"反馈 V4.0'+'\",\"document\":\"[{\\\"insert\\\":\\\"'+c+'\\\"}]\"}'
            url='https://a1.fanbook.mobi/api/bot/0f2de7ac66727cd9fcec1ee43559c561f6abf3f1e202c5a06c2ae4a3f6cf94ab795fbfbe39ad311a18ad1ff314388d1c/sendMessage'
            headers = {'content-type':"application/json;charset=utf-8"}
            jsonfile=json.dumps({"chat_id":448843628261933056,"text":d ,"parse_mode": "Fanbook"})
            postreturn=requests.post(url,data=jsonfile,headers=headers)
            if 'true' in postreturn.text:
                print('发送成功！')
            else:
                colorprint(smg2="'"+c+"'"+'发送失败！',pcolor='red')
        elif a=='help':
            import pygame
            print('弹出的帮助窗口中有详细信息')
            pygame.init()
            pygame.display.set_caption("帮助窗口 回车关闭")
            window_size = (271, 255)
            screen = pygame.display.set_mode(window_size)
            image = pygame.image.load("bztp.png")
            screen.blit(image, (0, 0))
            pygame.display.flip()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        pygame.quit()
                        addmsg('如需其他错误码帮助，请打开https://open.fanbook.mobi/document/manage/doc/Bot%20API/API%E9%94%99%E8%AF%AF%E7%A0%81',color='aqua')
                        addmsg('—————————————————————————————————————————————',color='aqua')
                        addmsg('关于：王大哥（#4562997）V4.0版',color='aqua')
                        addmsg('更新日期：2023/4/7  18：30 ',color='aqua')
        elif a== '8':
            colorprint(smg2='请输入频道id（如私信需要私聊id,可通过获取私聊id获取），获取方法：聊天框输入#，然后选择频道，发送后复制刚刚发送的蓝色频道名，复制后例如${#395848618357086556}，填写里面的数字395848618357086556即可',pcolor='bandg')
            pdid=input()
            colorprint(smg2='输入需要发送的消息标题',pcolor='bandg')
            xxbt=input()
            colorprint(smg2='请输入正文内容',pcolor='bandg')
            xxwb=input()
            colorprint(smg2='请输入发送消息的次数',pcolor='bandg')
            cis=input()
            for i in range(int(cis)):
                url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                headers = {'content-type':"application/json;charset=utf-8"}
                jsonfile=json.dumps({
                "chat_id":int(pdid),
                "text":'{\"type\":\"richText\",\"title\":\"'+xxbt+'\",\"document\":\"[{\\\"insert\\\":\\\"'+xxwb+'\\\"}]\"}',
                "parse_mode": "Fanbook"
                })
                postreturn=requests.post(url,data=jsonfile,headers=headers)
                colorprint(smg2=postreturn.text,pcolor='d')
        elif a=='9':#勋章及其功能（1添加）
            colorprint(smg2='输入需要操作的用户id',pcolor='bandg')
            xzuserid=input()
            colorprint(smg2='输入需要操作的服务器id',pcolor='bandg')
            fwqid=input()
            colorprint(smg2='勋章颁发者图标',pcolor='bandg')
            tb=input()
            colorprint(smg2='勋章颁发者名称',pcolor='bandg')
            mc=input()
            colorprint(smg2='在成员列表中的图标',pcolor='bandg')
            cytb=input()
            colorprint(smg2='文本标题',pcolor='bandg')
            wbbt=input()
            colorprint(smg2='文本内容',pcolor='bandg')
            wbnr=input()
            colorprint(smg2='勋章图标个数（1~3）',pcolor='bandg')
            tbgs=input()
            if tbgs=="2":
                colorprint(smg2='勋章图标1',pcolor='bandg')
                xzbttb=input()
                colorprint(smg2='荣誉图标正文1',pcolor='bandg')
                rysjzw=input()
                colorprint(smg2='勋章图标2',pcolor='bandg')
                xzbttb2=input()
                colorprint(smg2='荣誉图标正文2',pcolor='bandg')
                rysjzw2=input()
                url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/v2/guild/credit'
                headers = {'content-type':"application/json;charset=utf-8"}
                random_string = generate_random_string(11)
                print("此勋章id：",random_string)
                jsonfile=json.dumps({"guild_id":fwqid,"user_id":xzuserid,"card_id":random_string,"guild_credit":{"authority":{"icon":tb,"name":mc},"title":{"img":cytb},"slots":[[{"label":wbbt,"value":wbnr}],[{"img":xzbttb,"value":rysjzw},{"img":xzbttb2,"value":rysjzw2}]]}})
                postreturn = requests.put(url, data=jsonfile, headers=headers)
                colorprint(smg2=postreturn.text,pcolor='d')
            elif tbgs=="3":
                colorprint(smg2='勋章图标1',pcolor='bandg')
                xzbttb=input()
                colorprint(smg2='荣誉图标正文1',pcolor='bandg')
                rysjzw=input()
                colorprint(smg2='勋章图标2',pcolor='bandg')
                xzbttb2=input()
                colorprint(smg2='荣誉图标正文2',pcolor='bandg')
                rysjzw2=input()
                colorprint(smg2='勋章图标3',pcolor='bandg')
                xzbttb3=input()
                colorprint(smg2='荣誉图标正文3',pcolor='bandg')
                rysjzw3=input()
                url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/v2/guild/credit'
                headers = {'content-type':"application/json;charset=utf-8"}
                random_string = generate_random_string(11)
                print("此勋章id：",random_string)
                jsonfile=json.dumps({"guild_id":fwqid,"user_id":xzuserid,"card_id":random_string,"guild_credit":{"authority":{"icon":tb,"name":mc},"title":{"img":cytb},"slots":[[{"label":wbbt,"value":wbnr}],[{"img":xzbttb,"value":rysjzw},{"img":xzbttb2,"value":rysjzw2},{"img":xzbttb3,"value":rysjzw3}]]}})
                postreturn = requests.put(url, data=jsonfile, headers=headers)
                colorprint(smg2=postreturn.text,pcolor='d')
            else:
                colorprint(smg2='勋章图标',pcolor='bandg')
                xzbttb=input()
                colorprint(smg2='荣誉图标正文',pcolor='bandg')
                rysjzw=input()
                url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/v2/guild/credit'
                headers = {'content-type':"application/json;charset=utf-8"}
                random_string = generate_random_string(11)
                print("此勋章id：",random_string)
                jsonfile=json.dumps({"guild_id":fwqid,"user_id":xzuserid,"card_id":random_string,"guild_credit":{"authority":{"icon":tb,"name":mc},"title":{"img":cytb},"slots":[[{"label":wbbt,"value":wbnr}],[{"img":xzbttb,"value":rysjzw}]]}})
                postreturn = requests.put(url, data=jsonfile, headers=headers)
                colorprint(smg2=postreturn.text,pcolor='d')
        elif a=="10":
            colorprint(smg2='服务器id',pcolor='bandg')
            fwqid=input()
            colorprint(smg2='用户id',pcolor='bandg')
            yhid=input()
            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/getGuildCredit'
            headers={'content-type':"application/json;charset=utf-8"}
            jsonfile=json.dumps({
                "guild_id":int(fwqid),
                "user_id":int(yhid)
                })
            postreturn=requests.post(url,data=jsonfile,headers=headers)
            colorprint(smg2=postreturn.text,pcolor='d')
        elif a=="11":
            colorprint(smg2='请输入服务器id',pcolor='bandg')
            guild_id=int(input(''))
            colorprint(smg2='请输入欢迎语投放频道',pcolor='bandg')
            chat_id=int(input(''))
            colorprint(smg2='请输入欢迎消息',pcolor='bandg')
            intext=input('')
            lp=lingpai
            while True:
                url='https://a1.fanbook.mobi/api/bot/'+lp+'/getGuildMembersCount'
                headers = {'content-type':"application/json;charset=utf-8"}
                jsonfile=json.dumps({"guild_id":guild_id})
                postreturn=requests.post(url,data=jsonfile,headers=headers)
                print(postreturn.text)
                usershuliang1=int(postreturn.text[20:-1:])
                print('第一次'+str(usershuliang1))
                time.sleep(1.5)
                url='https://a1.fanbook.mobi/api/bot/'+lp+'/getGuildMembersCount'
                headers = {'content-type':"application/json;charset=utf-8"}
                jsonfile=json.dumps({"guild_id":guild_id})
                postreturn=requests.post(url,data=jsonfile,headers=headers)
                print(postreturn.text)
                usershuliang2=int(postreturn.text[20:-1:])
                print('第二次'+str(usershuliang2))
                if usershuliang1 < usershuliang2:
                    print('发送ing')
                    url='https://a1.fanbook.mobi/api/bot/'+lp+'/sendMessage'
                    headers = {'content-type':"application/json;charset=utf-8"}
                    jsonfile=json.dumps({
                        "chat_id":chat_id,
                        "text": "{\"type\":\"richText\",\"title\":\"欢迎第"+str(usershuliang2)+"位新成员加入！\",\"document\":\"[{\\\"insert\\\":\\\""+intext+"\\\"}]\"}",
                        "parse_mode": "Fanbook"
                    })
                    postreturn=requests.post(url,data=jsonfile,headers=headers)
                    print(postreturn.text)
        elif a=="12":
            colorprint(smg2='请输入频道id（如私信需要私聊id,可通过获取私聊id获取），获取方法：聊天框输入#，然后选择频道，发送后复制刚刚发送的蓝色频道名，复制后例如${#395848618357086556}，填写里面的数字395848618357086556即可',pcolor='bandg')
            pdid=input()
            colorprint(smg2='请输入需要发送的消息',pcolor='bandg')
            xx=input()
            colorprint(smg2='请输入发送消息的间隔时间(分钟)',pcolor='bandg')
            cis=input()
            cis=int(cis)
            cis=cis*60
            while True:
                url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                headers = {'content-type':"application/json;charset=utf-8"}
                jsonfile=json.dumps({
                "chat_id":int(pdid),
                "text": xx,
                })
                postreturn=requests.post(url,data=jsonfile,headers=headers)
                colorprint(smg2=postreturn.text,pcolor='d')
                time.sleep(cis)
    except Exception as e:#检测错误
        error=traceback.format_exc()#获取错误信息
        if 'pygame.error: video system not initialized' in error:#忽略错误
            continue
        elif 'for int()' in error:
            colorprint(smg2='遇到错误，请重试',pcolor='red')
            colorprint(smg2='错误诊断：数据类型错误，请输入整数',pcolor='red')
        elif 'list index out of range' in error:
            colorprint(smg2='遇到错误，请重试',pcolor='red')
            colorprint(smg2='错误诊断：数据处理错误，请输入正确的数据',pcolor='red')
        else:
            colorprint(smg2='遇到错误，请重试',pcolor='red')
            colorprint(smg2='遇到未知错误：'+error,pcolor='red')
            colorprint(smg2='发生错误，请检查参数，是否发送错误报告(报告不包含机器人令牌等敏感数据,王大哥可见)(Y/N)',pcolor='bandg')
            cw=input()
            if cw=='Y':
                    cwbg='错误模块：'+a+' 版本号：4.0'+'，错误代码：'+error
                    xwxx='{\"type\":\"richText\",\"title\":\"错误报告'+'3.1'+'\",\"document\":\"[{\\\"insert\\\":\\\"'+' '+'\\\"}]\"}'#此段富文本不支持
                    url='https://a1.fanbook.mobi/api/bot/0f2de7ac66727cd9fcec1ee43559c561f6abf3f1e202c5a06c2ae4a3f6cf94ab795fbfbe39ad311a18ad1ff314388d1c/sendMessage'#错误发送到私密频道
                    headers = {'content-type':"application/json;charset=utf-8"}
                    jsonfile=json.dumps({"chat_id":448843628261933056,"text":cwbg})
                    postreturn=requests.post(url,data=jsonfile,headers=headers)
                    addmsg('已发送',color='aqua')
            else:
                colorprint(smg2='已取消',pcolor='red')