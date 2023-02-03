import requests
import json
import traceback
print('欢迎使用机器人快捷操作系统，你可以使用此系统完成对机器人的常用操作，每次更新都会有新功能！ 由于时间仓促，代码难免会出现问题，如遇到问题，请给王大哥私信，请保持你的软件版本为最新版本 官网下载：https://eu27770457-12.icoc.ws/ [王大哥 V2.1beta 让机器人控制变得更简单！]')
lingpai=input('请先输入你的机器人的令牌')
url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/getMe'
headers = {'content-type':"application/json;charset=utf-8"}
jsonfile=json.dumps({})
postreturn=requests.post(url,data=jsonfile,headers=headers)
print(postreturn.text)
a=str(postreturn.text)
a=(a[6:10])
if a=='true':#检测返回内容
    input('填写正确,回车键继续')
else:
    input('填写错误，请重启程序后再试')    
print('简介：')
print('发送消息(1)：向频道（包括私聊）发送消息')
print('发送图片(2)：向频道（包括私聊）发送图片，图片链接可通过右键帖子或频道内图片获得')
print('创建私聊频道(3)：和一个用户建立私聊频道')
print('禁言用户(4)：禁言用户，最大30天')
print('创建频道(5)：创建已支持的频道，除过需要官方创建的')
print('通过消息链接获取消息详细信息(6):输入消息链接可以获得用户和消息的详细信息')
print('命令行模式：启动命令行支持其他功能（测试,不建议使用）')
while True:
    try:#检测代码，防止错误闪退
        a=input('请选择模式，1为发送消息(可发送私信消息)，2为发送图片，3为创建私聊频道，4为禁言用户，5为创建频道，6为通过消息链接获取消息详细信息，命令行启动命令行模式，help获取错误码帮助')
        if a=='1':
            pdid=input('请输入频道id（如私信需要私聊id,可通过获取私聊id获取），获取方法：聊天框输入#，然后选择频道，发送后复制刚刚发送的蓝色频道名，复制后例如${#395848618357086556}，填写里面的数字395848618357086556即可')
            xx=input('输入需要发送的消息')
            cis=input('请输入发送消息的次数')
            for i in range(int(cis)):
                url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                headers = {'content-type':"application/json;charset=utf-8"}
                jsonfile=json.dumps({
                "chat_id":int(pdid),
                "text": xx
                })
                postreturn=requests.post(url,data=jsonfile,headers=headers)
                print(postreturn.text)
        elif a=='2':
            pdid=input('请输入频道id（如私信需要私聊id,可通过获取私聊id获取），获取方法：聊天框输入#，然后选择频道，发送后复制刚刚发送的蓝色频道名，复制后例如${#395848618357086556}，填写里面的数字395848618357086556即可')
            tplj=input('输入需要发送的图片链接')
            cis=input('请输入发送消息的次数')
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
                print(postreturn.text)
        elif a=='3':
            yhid=input('请输入需要建立私聊频道用户的id,输出的id为对方私聊id，获取方法：聊天框输入@，然后选择需要私信的用户，发送后复制刚刚发送的蓝色用户名，复制后例如${@!395848618357086556}，填写里面的数字395848618357086556即可')
            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/getPrivateChat'
            headers = {'content-type':"application/json;charset=utf-8"}
            jsonfile=json.dumps({
                "user_id":int(yhid)
                })
            postreturn=requests.post(url,data=jsonfile,headers=headers)
            print(postreturn.text)
        elif a=='4':
            yhid=input('请输入需要禁言的用户id')
            fwqid=input('请输入用户所在的服务器id（设置服务器背景图下面有复制服务器id）')
            jysc=input("禁言时长（以秒为单位)")
            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/forbidUserSpeaking'
            headers={'content-type':"application/json;charset=utf-8"}
            jsonfile=json.dumps({
                "target_uid":yhid,
                "target_guild_id":fwqid,
                "duration_in_second":int(jysc),
                })
            postreturn=requests.post(url,data=jsonfile,headers=headers)
            print(postreturn.text)
        elif a=='5':
            yhid=input('请输入你的id')
            fwqid=input('请输入需要操作服务器id（设置服务器背景图下面有复制服务器id）')
            pdmc=input("请输入频道的名称")
            pdlx=input('请输入频道类型（0  普通文本频道，1	 语音频道，2	 视频频道，6   直播频道）')
            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/v2/channel/create'
            headers={'content-type':"application/json;charset=utf-8"}
            jsonfile=json.dumps({
                "user_id":yhid,
                "guild_id":fwqid,
                "name":pdmc,
                "type":int(pdlx)
                })
            postreturn=requests.post(url,data=jsonfile,headers=headers)
            print(postreturn.text)
        elif a=='6':
            xxlj=input('请输入消息链接')
            xxlj_ld=xxlj.split('/')
            fwqid=xxlj_ld[4]
            pdid=xxlj_ld[5]
            xxid=xxlj_ld[6]
            print('服务器id：',fwqid,'频道id:',pdid,' 消息id：',xxid)
            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/getMessage'
            headers={'content-type':"application/json;charset=utf-8"}
            jsonfile=json.dumps({'chat_id':int(pdid),'message_id':int(xxid)})
            postreturn=requests.post(url,data=jsonfile,headers=headers)
            print(postreturn.text)
            print('主要内容：first_name：发送者昵称，username：发送者短id，avatar：发送者头像，text：发送内容')
        elif a=="命令行":#代码可能有问题，懒改，数据支持2
            print('使用方法:api key1:x key2:xx')
            ml=input(">>>")
            num_spaces= ml.count(' ')
            if num_spaces==1:
                ml1=ml.split(' ')
                ml0=ml1[0]
                ml1=ml1[1]
                sj1=ml1.split(':')
                url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/'+ml0
                headers={'content-type':"application/json;charset=utf-8"}
                jsonfile=json.dumps({ml0:ml1})
                postreturn=requests.post(url,data=jsonfile,headers=headers)
                print(postreturn.text)
            elif num_spaces==2:
                ml1=ml.split(' ')
                ml0=ml1[0]
                ml2=ml1[1]
                ml3=ml1[2]
                sj1=ml2.split(':')
                sj2=ml3.split(':')
                print(ml1,ml0,sj1,ml3,ml2)#打印分离出的数据，测试用，不用管
                url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/'+ml0
                headers={'content-type':"application/json;charset=utf-8"}
                jsonfile=json.dumps({sj1[0]:sj1[1],sj2[0]:sj2[1]})
                postreturn=requests.post(url,data=jsonfile,headers=headers)
                print(postreturn.text)
            else:
                print("'"+ml+"'"+'不是可以识别的命令，参数不全、格式不正确或者长度不支持')
        elif a=='help':
            print('如需帮助，请打开https://open.fanbook.mobi/document/manage/doc/Bot%20API/API%E9%94%99%E8%AF%AF%E7%A0%81')
            print('—————————————————————————————————————————————')
            print('关于：王大哥（#4562997）V2.1测试版')
            print('更新日期：2023/1/13  18：30 ')
            print('下个版本预计更新日期：2023/1/25')
            print('官网： https://eu27770457-12.icoc.ws/ ')
    except Exception as e:#检测错误
        error=traceback.format_exc()#获取错误信息
        input('遇到错误：'+error)
        cw=input('发生错误，请检查参数，是否发送错误报告(报告不包含机器人令牌等敏感数据,王大哥可见)(Y/N)')
        if cw=='Y':
                cwbg='错误模块：'+a+'，返回数据：'+"此段测试后检测到涉及内容信息，版本不支持（新版本为主要变量）"+'，版本：2.1'+'，错误代码：'+error
                xwxx='{\"type\":\"richText\",\"title\":\"错误报告'+'V2.1'+'\",\"document\":\"[{\\\"insert\\\":\\\"'+' '+'\\\"}]\"}'#此段富文本不支持
                url='https://a1.fanbook.mobi/api/bot/0f2de7ac66727cd9fcec1ee43559c561f6abf3f1e202c5a06c2ae4a3f6c***********1a18ad1ff314388d1c/sendMessage'#错误发送到私密频道
                headers = {'content-type':"application/json;charset=utf-8"}
                jsonfile=json.dumps({"chat_id":448843628261933056,"text":cwbg})
                postreturn=requests.post(url,data=jsonfile,headers=headers)
                print('已发送')
        else:
            print('已取消')
#此版本仅为其他开发者开源
#截至2023/1/13最新版本为2.2(内测)