## python与二维码

原创： 十三的小客厅 [程序猿十三](javascript:void(0);) *前天*

> python包MyQR的使用，文末有福利



想必大家平时用到二维码的时候

第一个想到的就是类似于草料二维码的生成网站



![img](https://mmbiz.qpic.cn/mmbiz_png/4dSn5JYzicDfrquJ7ia6ME8COJraiav3gWcy7cV0eodmEmprOJ4V8FNcJUcmd7p9lU1ZnvUImobrF1xibUc5pcglwQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)



方便...快捷...

没得说...

但是个性化设置不够多

![img](data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg==)



python中有一个MyQR的包,可以很快的生成自定义的二维码

python3 环境

使用前需要安装MyQR的包

```
sudo pip3 install MyQR
```

首先生成一个普通的二维码试试

```
# 一般二维码生成
myqr.run("http://weixin.qq.com/r/tS7z62DEIj1drSSI93un")
```



生成好的二维码:

![img](https://mmbiz.qpic.cn/mmbiz_png/4dSn5JYzicDfrquJ7ia6ME8COJraiav3gWcJTDNicnuFwZ5n54v4twbyb3hC5excGsafvDeqYggIejAYS8jNTSa2bQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

可以拿手机扫一扫,或者长按识别,成功会跳转到公众号主页



下面笔者来详细的描述一下 myqr.run()函数里面的参数



| 参数       | 含义           | 详细                                                         |
| ---------- | -------------- | ------------------------------------------------------------ |
| words      | 二维码指向链接 | str，输入链接或者句子作为参数                                |
| version    | 边长           | int，控制边长，范围是1到40，数字越大边长越大,默认边长是取决于你输入的信息的长度和使用的纠错等级 |
| level      | 纠错等级       | str，控制纠错水平，范围是L、M、Q、H，从左到右依次升高，默认纠错等级为'H' |
| picture    | 结合图片       | str，将QR二维码图像与一张同目录下的图片相结合，产生一张黑白图片 |
| colorized  | 颜色           | bool，使产生的图片由黑白变为彩色的                           |
| contrast   | 对比度         | float，调节图片的对比度，1.0 表示原始图片，更小的值表示更低对比度，更大反之。默认为1.0 |
| brightness | 亮度           | float，调节图片的亮度，其余用法和取值与 contrast 相同        |
| save_name  | 输出文件名     | str，默认输出文件名是"qrcode.png"                            |
| save_dir   | 存储位置       | str，默认存储位置是当前目录                                  |



接下来试一下图片个性化处理

首先我们找一个图片:坚强菇



![img](https://mmbiz.qpic.cn/mmbiz_jpg/4dSn5JYzicDfrquJ7ia6ME8COJraiav3gWcUNZWawOnawpdL9E8gcjVeL74NTIex6LaQdgCnLV1YFwESAY8Uic0DeA/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)



这是代码:

```
 # 图片二维码生成黑白
 myqr.run(words="http://weixin.qq.com/r/tS7z62DEIj1drSSI93un",
             picture="C:/Users/admin/PycharmProjects/QRCode/image.jpg",
             save_name="blackQR.jpg")
```



预览:

![img](https://mmbiz.qpic.cn/mmbiz_jpg/4dSn5JYzicDfrquJ7ia6ME8COJraiav3gWcofj09Hf29tb7ic9Wx8ED8uMOacYDichtibexfRXg034L94QlF5ISpDvqA/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

再试试彩色的

```
# 图片二维码生成彩色
myqr.run(words="http://weixin.qq.com/r/tS7z62DEIj1drSSI93un",
             picture="C:/Users/admin/PycharmProjects/QRCode/image.jpg",
             colorized=True,
             save_name="ColorQR.png")
```



预览:

![img](https://mmbiz.qpic.cn/mmbiz_png/4dSn5JYzicDfrquJ7ia6ME8COJraiav3gWcnQK0fSISlkbWJTjsibMkBe0fPiaBPUVttPib2EJ8TAbw9ELHqY3ke1JkA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

接下来我们拿老婆试试

![img](https://mmbiz.qpic.cn/mmbiz_gif/4dSn5JYzicDfrquJ7ia6ME8COJraiav3gWce7h7sqG3fPAibg7ZCCZyF2ASYqeadkNXUCOIgLx7o1fKGoI9CykLNsA/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1)







代码:

```
 # 图片二维码生成gif
myqr.run(words="http://weixin.qq.com/r/tS7z62DEIj1drSSI93un",
             picture="C:/Users/admin/PycharmProjects/QRCode/jieyi.gif",
             colorized=True,
             save_name="gifQR.gif")
```



预览:

![img](https://mmbiz.qpic.cn/mmbiz_gif/4dSn5JYzicDfrquJ7ia6ME8COJraiav3gWcygfOVm5E1mb6683PuLNHSxTpIrP5ohtDNe4VvfhUjQwPf7Z2LK5rzg/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1)

拿手机扫码，或者长按识别二维码，成功将跳转到公众号主页内。如果没有成功跳转到公众号里面，点击关注再扫码试试



下面看一下MyQR的源码内容



**1.**MyQR文件结构



```
 qrcode
│   LICENSE.md  
│   README.md    
│   requirements.txt    #环境依赖文件
|   myqr.py
|
└───MyQR
│   │   __init__.py
│   │   myqr.py     #调用的文件
│   │   terminal.py #设置参数
|   |
│   └───mylibs
│       │   __init__.pt
│       │   constan.py  #数据分析
|       |   data.py     #数据编码
│       │   ECC.py      #纠错编码，Error Correction Codewords 
|       |   structure.py    #数据结构
|       |   matrix.py       #获得QR矩阵
|       |   draw.py         #生成二维码
|       |   theqrmodule.py  #结合函数
│   
└───example
    │   0.png
    │   1.png
    |   2.png
    |   ...
```



**2.**生成二维码的步骤

**2.1** 数据分析`MyQR/mylibs/constan.py`

确定编码的字符类型，按相应的字符集转换成符号字符。

**2.2** 数据编码`MyQR/mylibs/data.py`

将数据字符转换为位流，每8位一个码字，整体构成一个数据的码字序列。

**2.3** 纠错编码`MyQR/mylibs/ECC.py`

按需要将上面的码字序列分块，并根据纠错等级和分块的码字，产生纠错码字，并把纠错码字加入到数据码字序列后面，成为一个新的序列。

**2.4** 构造最终数据信息`MyQR/mylibs/structure.py + matrix.py`

在规格确定的条件下，将上面产生的序列按次序放入分块中，将数据转成能够画出二维码的矩阵。

创建二维码的矩阵

```
# MyQR/mylibs/matrix.py
def get_qrmatrix(ver, ecl, bits):
    num = (ver - 1) * 4 + 21
    qrmatrix = [[None] * num for i in range(num)]
    # 添加查找器模式和添加分隔符
    add_finder_and_separator(qrmatrix)

    # 添加校准模式
    add_alignment(ver, qrmatrix)

    # 添加时间模式
    add_timing(qrmatrix)

    # 添加涂黑模块和保留区域
    add_dark_and_reserving(ver, qrmatrix)

    maskmatrix = [i[:] for i in qrmatrix]

    # 放置数据位
    place_bits(bits, qrmatrix)

    # 蒙版操作
    mask_num, qrmatrix = mask(maskmatrix, qrmatrix)

    # 格式信息
    add_format_and_version_string(ver, ecl, mask_num, qrmatrix)

    return qrmatrix
```



**2.5** 生成二维码`MyQR/mylibs/draw.py`

使用 `draw.py` 画出二维码

```
def draw_qrcode(abspath, qrmatrix):
    unit_len = 3
    x = y = 4*unit_len
    pic = Image.new('1', [(len(qrmatrix)+8)*unit_len]*2, 'white')   #新建一张白色的底图

    '''
    循环矩阵中的单位，在需要涂黑的单位启用dra_a_black_unit()函数涂黑。
    '''
    for line in qrmatrix:
        for module in line:
            if module:
                draw_a_black_unit(pic, x, y, unit_len)  #画出黑单位
            x += unit_len
        x, y = 4*unit_len, y+unit_len

    saving = os.path.join(abspath, 'qrcode.png')
    pic.save(saving)    # 保存二维码图片
    return saving
```



**3.**合并图片的原理 

让我们来看一下 `/MyQR/myqr.py`中的 `combine()` 方法,此方法调用了 Pillow 库

读取图片操作

```
    qr = Image.open(qr_name)    #读取二维码图片
    qr = qr.convert('RGBA') if colorized else qr    #判断二维码是否有色

    bg0 = Image.open(bg_name).convert('RGBA')   #读取要合并的图片
    bg0 = ImageEnhance.Contrast(bg0).enhance(contrast)  # 调节对比度
    bg0 = ImageEnhance.Brightness(bg0).enhance(brightness)  # 调节亮度
```



将新加的图片覆盖原有的二维码图片，生成新的图片并保存



```
for i in range(qr.size[0]-24):
        for j in range(qr.size[1]-24):
            if not ((i in (18,19,20)) or (j in (18,19,20)) or (i<24 and j<24) or (i<24 and j>qr.size[1]-49) or (i>qr.size[0]-49 and j<24) or ((i,j) in aligs) or (i%3==1 and j%3==1) or (bg0.getpixel((i,j))[3]==0)):
                qr.putpixel((i+12,j+12), bg.getpixel((i,j)))
```



更多源码请公众号回复**MyQR**获取













（完）









![img](https://mmbiz.qpic.cn/mmbiz_gif/4dSn5JYzicDfrquJ7ia6ME8COJraiav3gWcfMcG8zjEteUxl3ukvpia5tJy5kEgUAAibxH1JYTKibickV1ZhzC2KDAhEA/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1)





![img](https://mmbiz.qpic.cn/mmbiz_gif/4dSn5JYzicDfrquJ7ia6ME8COJraiav3gWctribwdzLdm9W9ibSOic24FMRRibC4bssED7EJdaiaShg6lhxS6XgDBZibpnA/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1)



