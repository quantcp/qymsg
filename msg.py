import requests,json,base64,hashlib

bot_url='你的地址'
def send_work_msg(content,webhook_url):
    data={
        'msgtype':'markdown',
        'markdown':
            {'content':content}
    }
    r=requests.post(webhook_url,data=json.dumps(data))
    
name,code,price,strategy,buy='亚钾国际','000893',price,'均线策略','买入信号'
mkd_msg='''
    ### 盘中！**{}**\n
           >代码，{}
           >价格，{}
           >交易策略，{}
           >信号类型，{}
    '''.format(name,code,price,strategy,buy)
send_work_msg(mkd_msg,bot_url)
