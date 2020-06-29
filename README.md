
===========================
###########框架简介
框架组成：Python + Appium + PyUnit + HtmlTestRunner
框架说明：一个安卓客户端的UI自动化框架，基本事务性操作都是使用的Appium中的方法进行的二次封装的，框架可同时兼容多个不同项目，基本上所有文件都有两个层次（全局文件、局部文件），全局文件用于所有项目，局部文件只用于当前项目；

###########环境依赖
node v10.15.3
Python 3.7.3
jdk 1.8.0_131
Android SDK
appium

###########目录结构描述
├── Readme.md                   // help
├── config                      
│   └── config.py				// 全局配置文件
├── lib                      
│   ├── LogLib.py               // 框架日志输入文件
│   ├── SysLib.py         		// 框架系统方法文件（非自动化操作）
│   └── UiautomatorLib.py       // UIautomator事务性方法文件
├── logs                      
│   ├── UIautomatorPng          // 截图、uix文件存放目录（用例执行失败时，会截图，可以使用ui工具打开，查看错误定位）
│   └── log.txt         		// 日志存放文件
├── suite                      
│   └── douyin         			// 项目（抖音）
│	    ├── projectconfig       // 项目配置文件
│	    ├── projectlib         	// 项目的系统方法
│	    ├── projectresource     // 用例步骤存放
│	    ├── projectvaible       // 项目中的locator定位
│	    └── testcase            // 测试用例存放
├── tools                      
│   ├── HTMLTestRunner.py       // html测试报告生成
│   └── Run.py       			// 批量执行
├── varible                      
│   ├── global_varible.py       // 全局变量存放
│   └── locator.py       		// 全局的locator定位
└── 安装包                      // 自动化测试apk存放

ps：这只是一个初步的版本，还有很多问题存在，大家对于这个框架有什么疑问，麻烦给我留言，我希望能够将框架做的更简洁、更通用；