####图像拼接工具
将一个全景中的相机的六个面渲染出的图片拼接成一张图。
这张图的上下左右前后的安排顺序取决于前端的WebGL里的纹理坐标顺序。

#### 2015-03-24 ImageMerge程序需求更新
- 将渲染图片文件夹路径Path = xxx\xxx\xx\xx:xx:xx\赋给ImageMerge程序
- 程序通过os.walk自动检测文件夹中所有路径下的图片名，检测到一个文件夹下含有六个面全部渲好的场景（即f,l,r,b,d,u全有），自动merge六张图片为一张。
- Merge后的图片存储在OutputPath之下。
- Merge后的图片命名：C1_LG1_IES1.png
- Merge完成后print出工作清单（已merge图片的list和未merge图片缺失哪(几个)个面）

#### 2015-04-9 ImageMerge程序更新
- 增加了日志系统，log, error 和 warning
- 使用正则表达式匹配文件名确定文件名是否合法：
' re = r'c\d{1,}_LG\d{1,}_IES\d{1,}_[f,b,l,r,u,d].png$' '
- 增加了文件整理功能，根据文件名的，例如：“c1_LG1_IES1_u.png”，用下划线作为分隔符号隔离出文件路径，把六个面的文件归档到对应的文件夹下面。
- 整个工作的流程变为先分流到文件夹内，通过os.walk遍历所有的目录之后，确定是否有文件缺失。

#### 2015-04-13 ImageMerge程序Bug修复
- 修复了当log函数输入的消息不是string类型的时候print不出来的bug。
