from MyQR import myqr

if __name__ == '__main__':
    # 一般二维码生成
    myqr.run("http://weixin.qq.com/r/tS7z62DEIj1drSSI93un")

    # 图片二维码生成黑白
    myqr.run(words="http://weixin.qq.com/r/tS7z62DEIj1drSSI93un",
             picture="C:/Users/admin/Documents/GitHub/QRCode/image.jpg",
             save_name="blackQR.jpg")

    # 图片二维码生成彩色
    myqr.run(words="http://weixin.qq.com/r/tS7z62DEIj1drSSI93un",
             picture="C:/Users/admin/Documents/GitHub/QRCode/image.jpg",
             colorized=True,
             save_name="ColorQR.png")

    # 图片二维码生成gif
    myqr.run(words="http://weixin.qq.com/r/tS7z62DEIj1drSSI93un",
             picture="C:/Users/admin/Documents/GitHub/QRCode/jieyi.gif",
             colorized=True,
             save_name="jieyi_gifQR1.gif")

    myqr.run(words="http://weixin.qq.com/r/tS7z62DEIj1drSSI93un",
             picture="C:/Users/admin/Documents/GitHub/QRCode/jieyi2.gif",
             colorized=True,
             save_name="jieyi_gifQR2.gif")
