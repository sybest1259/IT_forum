-- MySQL dump 10.13  Distrib 5.7.23, for Linux (x86_64)
--
-- Host: localhost    Database: blog
-- ------------------------------------------------------
-- Server version	5.7.23-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('5618a28b9237');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `collections`
--

DROP TABLE IF EXISTS `collections`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `collections` (
  `user_id` int(11) DEFAULT NULL,
  `posts_id` int(11) DEFAULT NULL,
  KEY `posts_id` (`posts_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `collections_ibfk_1` FOREIGN KEY (`posts_id`) REFERENCES `posts` (`id`),
  CONSTRAINT `collections_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `collections`
--

LOCK TABLES `collections` WRITE;
/*!40000 ALTER TABLE `collections` DISABLE KEYS */;
INSERT INTO `collections` VALUES (4,42),(2,42),(1,38),(1,31),(1,4),(1,5),(1,10),(1,42),(4,10),(4,11),(4,31),(1,6);
/*!40000 ALTER TABLE `collections` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `course`
--

DROP TABLE IF EXISTS `course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `course` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(23) DEFAULT NULL,
  `abstract` text,
  `pid` int(11) DEFAULT NULL,
  `path` text,
  `timestamp` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_course_title` (`title`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course`
--

LOCK TABLES `course` WRITE;
/*!40000 ALTER TABLE `course` DISABLE KEYS */;
INSERT INTO `course` VALUES (1,'Python基础','<h1>Python&nbsp;简介</h1>\r\n\r\n<p>Python 是一个高层次的结合了解释性、编译性、互动性和面向对象的脚本语言。</p>\r\n\r\n<p>Python 的设计具有很强的可读性，相比其他语言经常使用英文关键字，其他语言的一些标点符号，它具有比其他语言更有特色语法结构。</p>\r\n\r\n<ul>\r\n	<li>\r\n	<p><strong>Python 是一种解释型语言：</strong>&nbsp;这意味着开发过程中没有了编译这个环节。类似于PHP和Perl语言。</p>\r\n	</li>\r\n	<li>\r\n	<p><strong>Python 是交互式语言：</strong>&nbsp;这意味着，您可以在一个Python提示符，直接互动执行写你的程序。</p>\r\n	</li>\r\n	<li>\r\n	<p><strong>Python 是面向对象语言:</strong>&nbsp;这意味着Python支持面向对象的风格或代码封装在对象的编程技术。</p>\r\n	</li>\r\n	<li>\r\n	<p><strong>Python 是初学者的语言：</strong>Python 对初级程序员而言，是一种伟大的语言，它支持广泛的应用程序开发，从简单的文字处理到 WWW 浏览器再到游戏。</p>\r\n	</li>\r\n</ul>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<hr />\r\n<h2>Python 发展历史</h2>\r\n\r\n<p>Python 是由 Guido van Rossum 在八十年代末和九十年代初，在荷兰国家数学和计算机科学研究所设计出来的。</p>\r\n\r\n<p>Python 本身也是由诸多其他语言发展而来的,这包括 ABC、Modula-3、C、C++、Algol-68、SmallTalk、Unix shell 和其他的脚本语言等等。</p>\r\n\r\n<p>像 Perl 语言一样，Python 源代码同样遵循 GPL(GNU General Public License)协议。</p>\r\n\r\n<p>现在 Python 是由一个核心开发团队在维护，Guido van Rossum 仍然占据着至关重要的作用，指导其进展。</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<hr />\r\n<h2>Python 特点</h2>\r\n\r\n<ul>\r\n	<li>\r\n	<p><strong>1.易于学习：</strong>Python有相对较少的关键字，结构简单，和一个明确定义的语法，学习起来更加简单。</p>\r\n	</li>\r\n	<li>\r\n	<p><strong>2.易于阅读：</strong>Python代码定义的更清晰。</p>\r\n	</li>\r\n	<li>\r\n	<p><strong>3.易于维护：</strong>Python的成功在于它的源代码是相当容易维护的。</p>\r\n	</li>\r\n	<li>\r\n	<p><strong>4.一个广泛的标准库：</strong>Python的最大的优势之一是丰富的库，跨平台的，在UNIX，Windows和Macintosh兼容很好。</p>\r\n	</li>\r\n	<li>\r\n	<p><strong>5.互动模式：</strong>互动模式的支持，您可以从终端输入执行代码并获得结果的语言，互动的测试和调试代码片断。</p>\r\n	</li>\r\n	<li>\r\n	<p><strong>6.可移植：</strong>基于其开放源代码的特性，Python已经被移植（也就是使其工作）到许多平台。</p>\r\n	</li>\r\n	<li>\r\n	<p><strong>7.可扩展：</strong>如果你需要一段运行很快的关键代码，或者是想要编写一些不愿开放的算法，你可以使用C或C++完成那部分程序，然后从你的Python程序中调用。</p>\r\n	</li>\r\n	<li>\r\n	<p><strong>8.数据库：</strong>Python提供所有主要的商业数据库的接口。</p>\r\n	</li>\r\n	<li>\r\n	<p><strong>9.GUI编程：</strong>Python支持GUI可以创建和移植到许多系统调用。</p>\r\n	</li>\r\n	<li>\r\n	<p><strong>10.可嵌入:&nbsp;</strong>你可以将Python嵌入到C/C++程序，让你的程序的用户获得&quot;脚本化&quot;的能力。</p>\r\n	</li>\r\n</ul>\r\n',0,'0,','2018-08-02 21:15:20'),(2,'WEB前端基础','<p>学习web前端开发基础技术需要掌握：HTML、CSS、JavaScript语言。下面我们就来了解下这三门技术都是用来实现什么的：&nbsp;<br />\r\n1、HTML是网页内容的载体。内容就是网页制作者放在页面上想要让用户浏览的信息，可以包含文字、图片、视频等。</p>\r\n\r\n<p>2、CSS样式是表现。就像网页的外衣。比如，标题字体、颜色变化，或为标题加入背景图片、边框等。所有这些用来改变内容外观的东西称之为表现。</p>\r\n\r\n<p>3、JavaScript是用来实现网页上的特效效果。如：鼠标滑过弹出下拉菜单。或鼠标滑过表格的背景颜色改变。还有焦点新闻（新闻图片）的轮换。可以这么理解，有动画的，有交互的一般都是用JavaScript来实现的。</p>\r\n',0,'0,','2018-08-02 21:20:31'),(3,'Linux基础','<p>Linux内核最初只是由芬兰人李纳斯&middot;托瓦兹（Linus Torvalds）在赫尔辛基大学上学时出于个人爱好而编写的。&nbsp;<br />\r\nLinux是一套免费使用和自由传播的类Unix操作系统，是一个基于POSIX和UNIX的多用户、多任务、支持多线程和多CPU的操作系统。&nbsp;<br />\r\nLinux能运行主要的UNIX工具软件、应用程序和网络协议。它支持32位和64位硬件。Linux继承了Unix以网络为核心的设计思想，是一个性能稳定的多用户网络操作系统。</p>\r\n',0,'0,','2018-08-02 22:00:52'),(4,'第一章',NULL,1,'0,1,','2018-08-02 22:39:04'),(5,'第一章',NULL,3,'0,3,','2018-08-02 22:39:48'),(6,'第一章',NULL,2,'0,2,','2018-08-03 07:31:43'),(8,'计算机概述',NULL,4,'0,1,4','2018-08-03 07:43:46'),(9,'python概述',NULL,4,'0,1,4','2018-08-03 08:03:24'),(10,'python的优缺点',NULL,4,'0,1,4','2018-08-03 08:05:24'),(11,'python应用场景',NULL,4,'0,1,4','2018-08-03 08:06:08'),(12,'进制的概述和分类',NULL,4,'0,1,4','2018-08-03 08:10:29'),(13,'进制的转换',NULL,4,'0,1,4','2018-08-03 08:11:49'),(14,'python环境安装',NULL,4,'0,1,4','2018-08-03 08:12:13'),(15,'pycharm的使用',NULL,4,'0,1,4','2018-08-03 08:12:46'),(16,'原反补码',NULL,4,'0,1,4','2018-08-03 08:13:43'),(17,'常见的DOS命令',NULL,4,'0,1,4','2018-08-03 08:13:53'),(18,'第二章',NULL,1,'0,1,','2018-08-03 08:15:19'),(19,'注释',NULL,18,'0,1,18','2018-08-03 08:15:53'),(20,'标识符和关键字',NULL,18,'0,1,18','2018-08-03 08:16:03'),(21,'输出',NULL,18,'0,1,18','2018-08-03 08:16:14'),(22,'输入',NULL,18,'0,1,18','2018-08-03 08:16:32'),(23,'常量和变量',NULL,18,'0,1,18','2018-08-03 08:16:43'),(24,'python数据类型',NULL,18,'0,1,18','2018-08-03 08:16:55'),(25,'运算符',NULL,18,'0,1,18','2018-08-03 08:17:06'),(26,'if判断语句',NULL,18,'0,1,18','2018-08-03 08:17:23'),(27,'第三章',NULL,1,'0,1,','2018-08-03 08:19:09'),(28,'while循环格式',NULL,27,'0,1,27','2018-08-03 08:20:03'),(29,'while/else及循环应用',NULL,27,'0,1,27','2018-08-03 08:20:27'),(30,'while循环嵌套及应用',NULL,27,'0,1,27','2018-08-03 08:21:32'),(31,'for循环基本格式和嵌套',NULL,27,'0,1,27','2018-08-03 08:21:52'),(32,'for循环应用',NULL,27,'0,1,27','2018-08-03 08:22:03'),(33,'break和continue',NULL,27,'0,1,27','2018-08-03 08:22:12'),(34,'数据库基础','<p>主流的数据库有：sqlserver，mysql，Oracle、SQLite、Access、MS SQL Server等</p>\r\n\r\n<p>数据库是由一张张表组成，和Excel很像，但是各有所长。</p>\r\n\r\n<ul>\r\n	<li>每一竖行称为列，也叫字段，或者键。</li>\r\n	<li>每一横行称为行，也叫一条结果，或者一条记录。</li>\r\n	<li>一张表里可以设置一个主键或者多个键组成的联合主键，例如学生的学号，人的身份证。用于区分每条结果，方便查询。如果没有唯一标识，那就设置联合主键，比如学号加课程号（一个学生可以学多个课程）。</li>\r\n</ul>\r\n',0,'0,','2018-08-03 08:24:59'),(35,'Flask框架','<p>Flask是当下流行的Web框架，它是用Python实现的。Flask显著的特点是：它是一个&ldquo;微&rdquo;框架。&rdquo;微&rdquo;意味着Flask旨在保持核心的简单，但同时又易于扩展。默认情况下，Flask 不包含数据库抽象层、表单验证，或是其它任何已有多种库可以胜任的功能。然而，Flask 支持用扩展来给应用添加这些功能。众多的扩展提供了数据库集成、表单验证、上传处理、各种各样的开放认证技术等功能。Flask的这些特性，使得它在Web开发方面变得非常流行。</p>\r\n',0,'0,','2018-08-03 08:26:23'),(36,'Django框架','<p>Django是一个开放源代码的Web应用框架，由Python写成。采用了MVC的软件设计模式，即模型M，视图V和控制器C。它最初是被开发来用于管理劳伦斯出版集团旗下的一些以新闻内容为主的网站的。并于2005年7月在BSD许可证下发布。这套框架是以比利时的吉普赛爵士吉他手Django Reinhardt来命名的。</p>\r\n\r\n<p>Django的主要目标是使得开发复杂的、数据库驱动的网站变得简单。Django注重组件的重用性和&ldquo;可插拔性&rdquo;，敏捷开发和DRY法则（Don&#39;t Repeat Yourself）。在Django中Python被普遍使用，甚至包括配置文件和数据模型。</p>\r\n',0,'0,','2018-08-03 08:28:02'),(37,'第一章',NULL,36,'0,36,','2018-08-03 08:28:15'),(38,'第一章',NULL,35,'0,35,','2018-08-03 08:28:24'),(39,'第一章',NULL,34,'0,34,','2018-08-03 08:28:36'),(40,'第四章',NULL,1,'0,1,','2018-08-03 08:29:06'),(41,'Number数据类型',NULL,40,'0,1,40','2018-08-03 08:29:44'),(42,'数据类型转换',NULL,40,'0,1,40','2018-08-03 08:29:58'),(43,'math数据模块',NULL,40,'0,1,40','2018-08-03 08:30:28'),(44,'random数据模块',NULL,40,'0,1,40','2018-08-03 08:30:43'),(45,'字符串的介绍和输入输出',NULL,40,'0,1,40','2018-08-03 08:31:08'),(46,'字符串的下标和切片',NULL,40,'0,1,40','2018-08-03 08:31:19'),(47,'字符串常见运算',NULL,40,'0,1,40','2018-08-03 08:31:27'),(48,'字符串中的转义字符',NULL,40,'0,1,40','2018-08-03 08:31:41'),(49,'字符串常见操作',NULL,40,'0,1,40','2018-08-03 08:32:19'),(50,'字符串的常见操作(续)',NULL,40,'0,1,40','2018-08-03 08:33:01');
/*!40000 ALTER TABLE `course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `posts`
--

DROP TABLE IF EXISTS `posts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `posts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(23) DEFAULT NULL,
  `article` text,
  `pid` int(11) DEFAULT NULL,
  `path` text,
  `fabulous` int(11) DEFAULT NULL,
  `times` int(11) DEFAULT NULL,
  `timestamp` datetime DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  `scan` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `uid` (`uid`),
  KEY `ix_posts_title` (`title`),
  CONSTRAINT `posts_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `posts`
--

LOCK TABLES `posts` WRITE;
/*!40000 ALTER TABLE `posts` DISABLE KEYS */;
INSERT INTO `posts` VALUES (1,'python 计算时间差，时间加减运算代码','<pre>\r\nmport datetime\r\nd1 = datetime.datetime(2009, 3, 23)\r\nd2 = datetime.datetime(2009, 10, 7)\r\ndayCount = (d1 - d2).days</pre>\r\n\r\n<p><strong>python计算两个时间之间的秒数</strong></p>\r\n\r\n<pre>\r\nimport datetime\r\nstarttime = datetime.datetime.now()\r\n#long running\r\nendtime = datetime.datetime.now()\r\nprint (endtime - starttime).seconds</pre>\r\n\r\n<p><strong>计算时间差很简单，我们再看下时间相加</strong></p>\r\n\r\n<pre>\r\nd1 = datetime.datetime.now()\r\nd3 = d1 + datetime.timedelta(days=10)\r\nprint d3.ctime()</pre>\r\n\r\n<p>上例演示了计算当前时间向后10天的时间。参数可以是days, hours，minutes，seconds,microseconds,如果是负数就是向前多少时间其本上常用的类：&nbsp;<code>datetime</code>和<code>timedelta</code>两个。它们之间可以相互加减。每个类都有一些方法和属性可以查看具体的值，如 datetime可以查看：天数(day)，小时数(hour)，星期几(weekday())等;timedelta可以查看：天数(days)，秒数 (seconds)等</p>\r\n',0,'0,',0,0,'2018-07-28 10:47:59',1,NULL),(2,'一、flask框架概述','<p>flask是一个非常小的python web框架,被称为微型框架,只提供了一个强健的核心,其它功能都是通过第三方扩展库来实现<br />\r\n&nbsp;</p>\r\n',0,'0,',0,0,'2018-07-28 13:18:28',1,NULL),(3,'flask框架分类','<p>1. MVC<br />\r\n&nbsp; &nbsp;M &nbsp;: 模型 &nbsp;（数据的操作）<br />\r\n&nbsp; &nbsp;V &nbsp;: 视图<br />\r\n&nbsp; &nbsp;C &nbsp;: 控制器<br />\r\n2. python中 MVT<br />\r\n&nbsp; &nbsp;M &nbsp;: 模型 &nbsp;（数据的操作）<br />\r\n&nbsp; &nbsp;V &nbsp;: 控制器<br />\r\n&nbsp; &nbsp;T &nbsp;: 视图</p>\r\n',0,'0,',0,0,'2018-07-28 13:18:45',1,NULL),(4,'二、flask第三方库','<p>app = Flask(__name__)<br />\r\nFlask构造函数的第一个参数指定一个引入参数/importname<br />\r\nFlask框架使用这个名字进行静态资源、模板、错误信息的定位</p>\r\n\r\n<p>&nbsp;</p>\r\n',0,'0,',0,0,'2018-07-28 13:19:46',1,12),(5,'url_for','<p>@app.route(&#39;/url/&#39;)<br />\r\ndef url():&nbsp;<br />\r\n&nbsp; &nbsp; return url_for(&#39;test1&#39;,x=1,y=2)<br />\r\n通过定位A函数所在的路由，返回该函数所在的路由地址（字符串格式，例如：/test/），若该路由接受传参，x、y将被构造为路由与之前的路由拼接（例如：/test/1/2/），若不接受传参，返回?x=1&amp;y=2（例如：/test/?x=1&amp;y=2）</p>\r\n',0,'0,',0,0,'2018-07-28 13:20:22',1,2),(6,'redirect','<p>@app.route(&#39;/lt/&#39;)<br />\r\ndef lt():<br />\r\n&nbsp; &nbsp; return redirect(url_for(&#39;test1&#39;,x=1,y=2))<br />\r\n访问该路由：127.0.0.1:5000/test/1/2/（test1()函数在@app.route(&#39;/test/&lt;x&gt;/&lt;y&gt;&#39;)中）</p>\r\n',0,'0,',0,0,'2018-07-28 13:20:58',1,NULL),(7,'abort','<p>@app.route(&#39;/test/&#39;)<br />\r\ndef test():<br />\r\n&nbsp; &nbsp; abort(500)<br />\r\n@app.errorhandler(500)<br />\r\ndef page_not_found(e): #e为错误的信息<br />\r\n&nbsp; &nbsp; return &#39;500-------{}&#39;.format(e)</p>\r\n',0,'0,',0,0,'2018-07-28 13:21:12',1,NULL),(8,'make_response','<p>@app.route(&#39;/&#39;)&nbsp;<br />\r\ndef res():<br />\r\n&nbsp; &nbsp; response = make_response(&#39;构造响应&#39;,500)<br />\r\n&nbsp; &nbsp; return response</p>\r\n',0,'0,',0,0,'2018-07-28 13:21:31',1,NULL),(9,'request','<p>@app.route(&#39;/&#39;)<br />\r\ndef index():<br />\r\n&nbsp; &nbsp; print(&#39;获取完整请求的url地址&#39;,request.url)<br />\r\n&nbsp; &nbsp; print(&#39;去掉get传参的url&#39;,request.base_url)<br />\r\n&nbsp; &nbsp; print(&#39; 只有主机地址和端口号&#39;,request.host_url)<br />\r\n&nbsp; &nbsp; print(&#39;请求的路由地址&#39;,request.path)<br />\r\n&nbsp; &nbsp; print(&#39;请求的方法&#39;,request.method)<br />\r\n&nbsp; &nbsp; print(&#39; 请求的get传参&#39;,request.args)<br />\r\n&nbsp; &nbsp; print(&#39; 请求的get传参&#39;,request.args[&#39;name&#39;])<br />\r\n&nbsp; &nbsp; print(&#39; 请求的get传参&#39;,request.args.get(&#39;name&#39;))<br />\r\n&nbsp; &nbsp; print(&#39; 请求的get传参&#39;,request.args.getlist(&#39;name&#39;))<br />\r\n&nbsp; &nbsp; print(&#39; 请求的get传参&#39;,request.args[&#39;age&#39;])<br />\r\n&nbsp; &nbsp; print(&#39; 请求的get传参&#39;,request.args.get(&#39;age&#39;))<br />\r\n&nbsp; &nbsp; print(&#39; 获取表单post传递过来的数据&#39;,request.form)<br />\r\n&nbsp; &nbsp; print(&#39;获取文件上传&#39;,request.files)<br />\r\n&nbsp; &nbsp; print(&#39;请求头信息&#39;,request.headers.get(&#39;User-Agent&#39;))<br />\r\n&nbsp; &nbsp; print(&#39;请求头信息&#39;,request.headers.get(&#39;Host&#39;))<br />\r\n&nbsp; &nbsp; print(&#39;获取请求过来的cookie&#39;,request.cookies)<br />\r\n&nbsp; &nbsp; print(&#39;获取请求过来的cookie&#39;,request.cookies.get(&#39;sessionid&#39;))<br />\r\n&nbsp; &nbsp; print(&#39;获取请求过来的json数据&#39;,request.json)<br />\r\n&nbsp; &nbsp; return &#39;index&#39;</p>\r\n',0,'0,',0,0,'2018-07-28 13:22:20',1,1),(10,' filter() 过滤出你要得','<p>如果没有参数 默认查询所有</p>\r\n\r\n<p>User.query.filter(User.username==&#39;张&#39;,User.sex==True) #查询name为张 并且sex为True<br />\r\n&nbsp;</p>\r\n',0,'0,',0,0,'2018-07-28 16:08:16',2,31),(11,'filter_by() ','<p>#单条件查询<br />\r\n@test.route(&#39;/filter_by/&#39;)<br />\r\ndef filter_by():<br />\r\n&nbsp; &nbsp; data = User.query.filter_by() #查询所有<br />\r\n&nbsp; &nbsp; data = User.query.filter_by(sex=True) #查询sex为True的数据<br />\r\n&nbsp; &nbsp; data = User.query.filter_by(sex=True,age=43) #查询sex为True 并且 age为43的数据<br />\r\n&nbsp; &nbsp; print(data)<br />\r\n&nbsp; &nbsp; return render_template(&#39;show.html&#39;, data=data)</p>\r\n',0,'0,',0,0,'2018-07-28 17:31:03',4,20),(12,'回复王钰清会y按的评论','<p>还不错～～～～～～～～～～～～～～～～</p>\r\n',10,'0,10,',0,0,'2018-07-28 18:46:21',4,NULL),(13,'回复sybest1230的评论','<p>不咋地～～～～～～～～～～～～</p>\r\n',9,'0,9,',0,0,'2018-07-28 19:02:36',4,NULL),(14,'回复sybest1230的评论','<p>这样也行～～～～～～～～～～～～～</p>\r\n',8,'0,8,',0,0,'2018-07-28 19:03:17',4,NULL),(15,'回复王钰清会y按的评论','<p>以前还上去刷下坐骑，一个月卡GG 30好样的！</p>\r\n',10,'0,10,',0,0,'2018-07-28 20:29:30',4,NULL),(16,'回复王钰清会y按的评论','<p>改点卡后，就不玩了，休闲玩家工作没时间，周末感觉不合算，也不是在乎那点钱，总觉得心里不平衡<img src=\"https://tb2.bdstatic.com/tb/editor/images/face/i_f16.png?t=20140803\" style=\"height:30px; width:30px\" /></p>\r\n',10,'0,10,',0,0,'2018-07-28 20:32:54',4,NULL),(17,'回复王钰清会y按的评论','<p>点卡估计回不来了，买了半年卡，每天就晚上下班玩玩</p>\r\n',10,'0,10,',0,0,'2018-07-28 20:33:41',4,NULL),(18,'回复sybest1230的评论','<p>没我写的好～～～～～～～～</p>\r\n',9,'0,9,',0,0,'2018-07-28 20:37:07',4,NULL),(19,'回复Guido1230的评论','<p>在Jinja2模板（1）中的例2中，{{name}}结构表示一个变量，它是一种特殊的占位符，告诉模板引擎这个位置的值从渲染模板时使用的数据中获取。</p>\r\n',11,'0,11,',0,0,'2018-07-28 20:41:31',1,NULL),(20,'回复sybest1230的评论','<p>很好～～～～～～～～～～～～</p>\r\n',9,'0,9,',0,0,'2018-07-28 21:16:19',1,NULL),(21,'回复王钰清会y按的评论','<p>干嘛的～～～～～～～～～～～～～～～</p>\r\n',10,'0,10,',0,0,'2018-07-28 21:50:53',1,NULL),(22,'回复王钰清会y按的评论','<p>还好～～～～～～～～～～～～～</p>\r\n',10,'0,10,',0,0,'2018-07-28 21:51:16',1,NULL),(23,'回复sybest1230的评论','<p>子评论测试</p>',22,'0,10,22,',0,0,'2018-07-29 10:13:31',4,NULL),(24,'回复sybest1230的评论','<p>子评论测试2</p>',22,'0,10,22,',0,0,'2018-07-29 11:03:02',4,NULL),(25,'回复sybest1230的评论','<p>瞅你咋地～～～～～</p>',21,'0,10,21,',0,0,'2018-07-29 12:02:36',4,1),(26,'回复Guido1230的评论','<p>瞅你咋地2</p>',25,'0,10,21,25,',0,0,'2018-07-29 12:03:25',4,NULL),(27,'回复sybest1230的评论','<p>干嘛的______子评论</p>',21,'0,10,21,',0,0,'2018-07-29 12:32:53',4,NULL),(28,'回复sybest1230的评论','<p>子评论测试3</p>',22,'0,10,22,',0,0,'2018-07-29 12:33:37',4,NULL),(29,'回复Guido1230的评论','<p>买点卡的评论</p>',17,'0,10,17,',0,0,'2018-07-29 12:34:06',4,NULL),(30,'回复Guido1230的评论','<p>不怎么样～～～～～～～～～～～～</p>',12,'0,10,12,',0,0,'2018-07-29 15:21:02',4,NULL),(31,'Flask-Login','<p>Flask-Login 为 Flask 提供了用户会话管理。它处理了日常的登入，登出并且长时间记住用户的会话。</p><p>它会:</p><ul><li>在会话中存储当前活跃的用户 ID，让你能够自由地登入和登出。</li><li>让你限制登入(或者登出)用户可以访问的视图。</li><li>处理让人棘手的 &ldquo;记住我&rdquo; 功能。</li><li>帮助你保护用户会话免遭 cookie 被盗的牵连。</li><li>可以与以后可能使用的 Flask-Principal 或其它认证扩展集成。</li></ul><p>但是，它不会:</p><ul><li>限制你使用特定的数据库或其它存储方法。如何加载用户完全由你决定。</li><li>限制你使用用户名和密码，OpenIDs，或者其它的认证方法。</li><li>处理超越 &ldquo;登入或者登出&rdquo; 之外的权限。</li><li>处理用户注册或者账号恢复。</li></ul>',0,'0,',0,0,'2018-07-29 15:59:35',4,59),(32,'回复Guido1230的评论','<p>自己狂顶～～～～～～～～～～～</p>',31,'0,31,',0,0,'2018-07-29 16:00:07',4,NULL),(33,'回复Guido1230的评论','<p>继续顶～～～～～～～～～～～～</p>',32,'0,31,32,',0,0,'2018-07-29 16:00:31',4,NULL),(34,'回复Guido1230：','<p>顶贴～～～～～～～～～～～～</p>',31,'0,31,',0,0,'2018-07-29 16:03:22',4,NULL),(35,'回复Guido1230：','<p>真是不知羞耻～～～～～～～～～～～～</p>',32,'0,31,32,',0,0,'2018-07-29 18:32:33',2,NULL),(36,'回复Guido1230：','<p>快来围观龟哥～～～～</p>',31,'0,31,',0,0,'2018-07-29 18:36:41',2,NULL),(37,'回复sybest1230：','<p>没什么大不了的～～～～～～～</p>',8,'0,8,',0,0,'2018-07-29 18:53:24',2,NULL),(38,'bootstrap设置全局 CSS 样式','<p>设置全局 CSS 样式；基本的 HTML 元素均可以通过 class 设置样式并得到增强效果；还有先进的栅格系统。深入了解 Bootstrap 底层结构的关键部分，包括我们让 web 开发变得更好、更快、更强壮的最佳实践。</p>',0,'0,',0,0,'2018-07-30 09:05:06',4,62),(39,'回复Guido1230：','<p>HTML5 文档类型</p><p>Bootstrap 使用到的某些 HTML 元素和 CSS 属性需要将页面设置为 HTML5 文档类型。在你项目中的每个页面都要参照下面的格式进行设置。</p><p>&lt;!DOCTYPE html&gt; &lt;html lang=&quot;zh-CN&quot;&gt; ... &lt;/html&gt;</p>',38,'0,38,',0,0,'2018-07-30 09:05:37',4,NULL),(40,'回复Guido1230：','<p>移动设备优先</p><p>在 Bootstrap 2 中，我们对框架中的某些关键部分增加了对移动设备友好的样式。而在 Bootstrap 3 中，我们重写了整个框架，使其一开始就是对移动设备友好的。这次不是简单的增加一些可选的针对移动设备的样式，而是直接融合进了框架的内核中。也就是说，<strong>Bootstrap 是移动设备优先的</strong>。针对移动设备的样式融合进了框架的每个角落，而不是增加一个额外的文件。</p><p>为了确保适当的绘制和触屏缩放，需要在&nbsp;&lt;head&gt;&nbsp;之中<strong>添加 viewport 元数据标签</strong>。</p><p>&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;</p><p>在移动设备浏览器上，通过为视口（viewport）设置 meta 属性为&nbsp;user-scalable=no&nbsp;可以禁用其缩放（zooming）功能。这样禁用缩放功能后，用户只能滚动屏幕，就能让你的网站看上去更像原生应用的感觉。注意，这种方式我们并不推荐所有网站使用，还是要看你自己的情况而定！</p><p>&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no&quot;&gt;</p>',38,'0,38,',0,0,'2018-07-30 09:06:08',4,NULL),(41,'回复Guido1230：','<p>排版与链接</p><p>Bootstrap 排版、链接样式设置了基本的全局样式。分别是：</p><ul><li>为&nbsp;body&nbsp;元素设置&nbsp;background-color: #fff;</li><li>使用&nbsp;@font-family-base、@font-size-base&nbsp;和&nbsp;@line-height-base&nbsp;变量作为排版的基本参数</li><li>为所有链接设置了基本颜色&nbsp;@link-color&nbsp;，并且当链接处于&nbsp;:hover&nbsp;状态时才添加下划线</li></ul><p>这些样式都能在&nbsp;scaffolding.less&nbsp;文件中找到对应的源码。</p><p>Normalize.css</p><p>为了增强跨浏览器表现的一致性，我们使用了&nbsp;<a target=\"_blank\" href=\"http://necolas.github.io/normalize.css/\">Normalize.css</a>，这是由&nbsp;<a target=\"_blank\" href=\"https://twitter.com/necolas\">Nicolas Gallagher</a>&nbsp;和&nbsp;<a target=\"_blank\" href=\"https://twitter.com/jon_neal\">Jonathan Neal</a>&nbsp;维护的一个CSS 重置样式库。</p>',38,'0,38,',0,0,'2018-07-30 09:06:58',4,NULL),(42,'浅析MySQL中concat的使用','<h1>一、concat()函数</h1>\r\n\r\n<p>1、功能：将多个字符串连接成一个字符串。</p>\r\n\r\n<p>2、语法：concat(str1, str2,...)</p>\r\n\r\n<p>返回结果为连接参数产生的字符串，如果有任何一个参数为null，则返回值为null。</p>\r\n\r\n<p>3、举例：</p>\r\n\r\n<p>例1:select concat (id, name, score) as info from tt2</p>\r\n',0,'0,',0,0,'2018-07-30 09:41:45',1,97),(43,'回复sybest1230：','<h1>二、concat_ws()函数</h1>\r\n\r\n<p>1、功能：和concat()一样，将多个字符串连接成一个字符串，但是可以一次性指定分隔符～（concat_ws就是concat with separator）</p>\r\n\r\n<p>2、语法：concat_ws(separator, str1, str2, ...)</p>\r\n\r\n<p>说明：第一个参数指定分隔符。需要注意的是分隔符不能为null，如果为null，则返回结果为null。</p>\r\n\r\n<p>3、举例：</p>\r\n\r\n<p>例3:我们使用concat_ws()将 分隔符指定为逗号，达到与例2相同的效果：</p>\r\n',42,'0,42,',0,0,'2018-07-30 09:43:30',1,NULL),(44,'回复sybest1230：','<h1>三、group_concat()函数</h1>\r\n\r\n<p>前言：在有group by的查询语句中，select指定的字段要么就包含在group by语句的后面，作为分组的依据，要么就包含在聚合函数中。（有关group by的知识请戳：<a href=\"http://blog.csdn.net/mary19920410/article/details/76398050\" target=\"_blank\">浅析SQL中Group By的使用</a>）。</p>\r\n',42,'0,42,',0,0,'2018-07-30 09:43:46',1,NULL),(45,'回复sybest1230：','<p>但是这样同一个名字出现多次，看上去非常不直观。有没有更直观的方法，既让每个名字都只出现一次，又能够显示所有的名字相同的人的id呢？&mdash;&mdash;使用group_concat()</p>\r\n\r\n<p>1、功能：将group by产生的同一个分组中的值连接起来，返回一个字符串结果。</p>\r\n\r\n<p>2、语法：group_concat( [distinct] 要连接的字段 [order by 排序字段 asc/desc &nbsp;] [separator &#39;分隔符&#39;] )</p>\r\n\r\n<p>说明：通过使用distinct可以排除重复值；如果希望对结果中的值进行排序，可以使用order by子句；separator是一个字符串值，缺省为一个逗号。</p>\r\n',42,'0,42,',0,0,'2018-07-30 09:44:13',1,NULL),(46,'回复sybest1230：','<p>但是输入sql语句麻烦了许多，三个字段需要输入两次逗号，如果10个字段，要输入九次逗号...麻烦死了啦，有没有什么简便方法呢？&mdash;&mdash;于是可以指定参数之间的分隔符的concat_ws()来了！！！</p>\r\n',43,'0,42,43,',0,0,'2018-07-30 09:50:38',1,NULL),(47,'回复sybest1230：','<p>我们使用concat_ws()将 分隔符指定为逗号，达到与例2相同的效果</p>\r\n',44,'0,42,44,',0,0,'2018-07-30 10:00:12',1,NULL),(48,'回复Guido1230：','<p>haha~~~~~~~</p>\r\n',11,'0,11,',0,0,'2018-07-30 10:01:10',1,NULL),(49,'回复Guido1230：','<p>呵呵～～～～～～～～～～～～</p>\r\n',11,'0,11,',0,0,'2018-07-30 10:04:29',1,NULL),(50,'回复sybest1230：','<p>哈哈～～～～``</p>\r\n',49,'0,11,49,',0,0,'2018-07-30 10:04:38',1,NULL),(51,'回复sybest1230：','<p>顶～～～～～～～～～～～～</p>\r\n',43,'0,42,43,',0,0,'2018-07-31 17:55:48',2,NULL),(52,'回复王钰清会y按：','<p>haha~~~~~~~~~~</p>\r\n',10,'0,10,',0,0,'2018-08-01 20:24:11',4,NULL),(53,'回复Guido1230：','<p>顶贴～～～～～～～～～</p>\r\n',34,'0,31,34,',0,0,'2018-08-01 22:18:23',1,0),(54,'回复Guido1230：','<p>就瞅你了，咋的～～～～～～</p>\r\n',26,'0,10,21,25,26,',0,0,'2018-08-02 11:30:12',1,0);
/*!40000 ALTER TABLE `posts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(15) DEFAULT NULL,
  `password_hash` varchar(128) DEFAULT NULL,
  `sex` tinyint(1) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `icon` varchar(40) DEFAULT NULL,
  `confirm` tinyint(1) DEFAULT NULL,
  `register_date` datetime DEFAULT NULL,
  `lastlogin_date` datetime DEFAULT NULL,
  `lastlogin_date_cache` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_user_username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'admin','pbkdf2:sha256:50000$J3hQwffP$43b83be3d1d2227b7d2ad61537722358177f37a0c18eaf9ac0773b7613301e6e',1,29,'604508260@qq.com','s_v8jQ9hp3.png',1,'2018-07-19 08:27:17','2018-08-03 21:28:42','2018-08-04 09:03:39'),(2,'wangyuqing','pbkdf2:sha256:50000$mcTBBZMS$d7db6dea1de66acbf37f09fa600e3185109dbd7ef6d68fb10168886b91c6d378',0,90,'sybest08407323@163.com','s_Q9zellx3.png',1,'2018-07-28 08:49:58','2018-07-31 17:54:55','2018-07-31 17:54:55'),(4,'Guido1230','pbkdf2:sha256:50000$GiKspg7F$b3705ccba004b509f09a96934e4136a5ba64805f4a40e736e76a22e268ca9f15',1,50,'18635171210@163.com','s_9PumSKk7.png',1,'2018-07-28 15:28:51','2018-08-03 18:14:19','2018-08-03 18:14:19');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-08-04 17:27:45
