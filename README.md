# FindYYeTs
Alfred是OS X最常用的一款增强型工具软件，充分利用了OS X的系统特性，帮助用户通过快捷键完成各种常用操作，属于Mac必备软件。
近期Alfred发布了V2，对原有特性进行了增强和完善，并推出了全新的workflow功能，提供了极为简洁的接口和各种Action，帮助用户定制自己的功能。

FindYYeTs是为Alfred开发的一款workflow，主要功能是通过YYeTs（人人影视）提供的API和RSS检索最新发布的影视作品，同时也可以进行全站搜索。如果你是个影视剧爱好者，你应该需要这个workflow。

# Development
Alfred 2的workflow提供了多种实现方式，比如shell、php、perl、python、ruby和applescript。
FindYYeTs是基于Python2.7开发的。

通过urllib2、xml.dom.minidom、json等原生库解析YYeTs的RSS和API，检索完成后通过python组织成Alfred 2能识别的xml格式。

# Requirements
* Python2.7 （OS X 10.8默认的Python版本）
* Alfred 2（付费版）

# Installation
下载FindYYeTs.alfredworkflow，双击导入Alfred 2即可。

# How to use
* 关键字yyapi用来进行全站影视剧和字幕信息检索，yyrss查询最新发布的影视剧。
* 通过option+space呼出Alfred，输入yyapi 生活大爆炸，可用检索YYeTs网站生活大爆炸剧集和字幕信息
* 通过option+space呼出Alfred，输入yyrss all，查看YYeTs网站最近发布的影视剧
* 输入yyrss 科幻，可以检索标题匹配“科幻”的影视剧，同样是网站最新发布的，不是所有历史数据。
* 用 上下方向键 或 command+数字 选中需要的文件，回车可以直接在默认浏览器打开。

![demo](demo.png)

![demo1](demo1.png)