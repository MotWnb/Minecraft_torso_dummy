import wx
import uuid
import socket


class Frame(wx.Frame):
    def __init__(self):
        global agree
        wx.Frame.__init__(self, None, title='木锄启动器(WHI)', size=(1050, 700))
        self.label_3 = None
        panel = wx.Panel(self)
        self.SetBackgroundColour('#ADD8E6')

        self.font = wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.font2 = wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.font3 = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.font4 = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.font5 = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.font6 = wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL)

        sizer = wx.BoxSizer(wx.VERTICAL)

        self.label_1 = wx.StaticText(panel, label='欢迎使用木锄启动器\nWelcome to use Wooden Hoe Initiator')

        self.label_1.SetFont(self.font)
        self.label_1.SetForegroundColour('#FF6347')

        sizer.Add(self.label_1, 0, wx.ALL, 10)

        self.label_2 = wx.StaticText(panel, label='木锄启动器是一款基于Python的简单的Minecraft启动器\nWooden Hoe Initiator(WHI) is a '
                                                  'simple Minecraft launcher based on Python')

        self.label_2.SetFont(self.font4)
        self.label_2.SetForegroundColour('#90940a')

        sizer.Add(self.label_2, 0, wx.ALL, 10)

        self.Start = wx.Button(panel, label='启动')
        self.Start.SetForegroundColour('#FF6347')
        self.Start.Bind(wx.EVT_BUTTON, self.OnStart)
        sizer.Add(self.Start, 0, wx.ALL, 10)

        panel.SetSizerAndFit(sizer)
        panel.Layout()  # 刷新

    @staticmethod
    def OnStart(self):
        list1 = read()
        username = list1[0]
        password = list1[1]
        login(username, password)


def read():
    fp = open('data.txt', 'r', encoding='utf-8')
    lines = fp.read().splitlines()
    return lines


def login(username, password):
    print('正在启动...\nStarting...')
    print('正在生成UUID...\nGenerating UUID...')
    UUID = str(uuid.uuid4())
    print('已获得UUID:' + UUID)

    print('正在生成access_token...\nGenerating access_token...')
    access_token = bytes(username, 'UTF-8')
    access_token = access_token.hex()
    print('已获得access_token:' + access_token)

    print('正在生成client_token...\nGenerating client_token...')
    client_token = UUID
    client_token = client_token.replace('-', '')
    print('已获得client_token:' + client_token)

    print('开始连接服务器...\nConnecting to server...')
    server = input('请输入服务器地址:')
    port = input('请输入服务器端口:')
    port = int(port)

    join = socket.socket()
    join.connect((server, port))
    print('已连接服务器:' + server)
    while True:
        message = input('请输入消息:')
        if message == 'exit':
            break
        join.send(bytes(message, 'UTF-8'))
        print('已发送消息:' + message)
        data = join.recv(1024)
        print('已接收消息:' + data.decode('UTF-8'))
    join.close()
    print('已关闭连接')


if __name__ == '__main__':
    app = wx.App()
    frame = Frame()
    frame.Centre()
    frame.Show()
    app.MainLoop()
