使用scrapy爬取糗事百科的段子，并保存成json文件。
settings.py里：
    ROBOTSTXT_OBEY = False 要是true就是要遵守机器人协议，找到robots.txt才会执行这个项目。
    DOWNLOAD_DELAY = 1  延时1s攫取。
    ITEM_PIPELINES 设置pipelines的优先级，数字越小，优先级越高
    
