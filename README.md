# Scrapy_ex
简单的Scrapy文本爬取示例

### 1.介  绍
	对 quanshuwang.com/map/1.html 中的小说进行爬取，包括主题、文题、章节、内容（2.html-5.html也爬取）

### 2.使用方法：
	cd quanshuwang/quanshuwang/spiders/
	scrapy list #查看spider，共有两个（title爬取索引页，针对标题进行爬取;artcle爬取内容页，针对章节、内容）
	scrapy crawl [spider_name] #[spider_name]处填写相应内容，由于artcle需要用title所生成的.json文件，所以需要先运行title
    
### 3.输出结果
	爬取后会生成相应的.json文件分为两种：其一包含内容{“主题名称”，“文题名称”，“文章对应src”};其二包含{“章节”，“内容”，“文题名称”，“章节对应src”}
