####图像拼接工具
将一个全景中的相机的六个面渲染出的图片拼接成一张图。
这张图的上下左右前后的安排顺序取决于前端的WebGL里的纹理坐标顺序。

#### 2015-03-24 ImageMerge程序需求更新
- 将渲染图片文件夹路径Path = xxx\xxx\xx\xx:xx:xx\赋给ImageMerge程序
- 程序通过os.walk自动检测文件夹中所有路径下的图片名，检测到一个文件夹下含有六个面全部渲好的场景（即f,l,r,b,d,u全有），自动merge六张图片为一张。
- Merge后的图片存储在OutputPath之下。
- Merge后的图片命名：C1_LG1_IES1.png
- Merge完成后print出工作清单（已merge图片的list和未merge图片缺失哪(几个)个面）

