import scrapy
from ..items import AmazonItem
import json

class AmazonSpider(scrapy.Spider):
    name='google'
    allowed_domains=['https://www.mysmartprice.com/computer/pricelist/logitech-computer-keyboard-price-list-in-india.html','https://www.mysmartprice.com/computer/pricelist/hp-computer-keyboard-price-list-in-india.html']
    
    product_list=['keyboard','mouse','pendrive','router','external-hard-disks']
    
    keyboard_list=['logitech','hp','dell','lenovo','zebronics','iball']
    mouse_list=['hp','dell','logitech','lenovo','zebronics']
    pendrive_list=['hp','sandisk']
    router_list=['tp-link','netgear']
    harddisk_list=['seagate','sony','transcend']

    '''
    #product search
    print("choose from the products you can search for")
    print(product_list)
    product=input("enter product:")
    if(product not in product_list):
        print("product not in list")

    #company search
    print("choose from the companies available")
    if(product=='keyboard'):
        print(keyboard_list)
    elif(product=='mouse'):
        print(mouse_list)
    elif(product=='pendrive'):
        print(pendrive_list)
    elif(product=='router'):
        print(router_list)
    elif(product=='external-hard-disks'):
        print(harddisk_list)
    
    company=input("enter company:")
    '''
    start_urls=[]
    for i in keyboard_list:
        domain='https://www.mysmartprice.com/computer/pricelist/'+i+'-computer-keyboard-price-list-in-india.html'
        start_urls.append(domain)
    for i in mouse_list:
        domain='https://www.mysmartprice.com/computer/pricelist/'+i+'-computer-mouse-price-list-in-india.html'
        start_urls.append(domain)
    for i in pendrive_list:
        domain='https://www.mysmartprice.com/computer/pricelist/'+i+'-computer-pendrive-price-list-in-india.html'
        start_urls.append(domain)
    for i in router_list:
        domain='https://www.mysmartprice.com/computer/pricelist/'+i+'-computer-router-price-list-in-india.html'
        start_urls.append(domain)
    for i in harddisk_list:
        domain='https://www.mysmartprice.com/computer/pricelist/'+i+'-computer-external-hard-disks-price-list-in-india.html'
        start_urls.append(domain)

    def parse(self,response):
        item=AmazonItem()
        
        product_name=response.css(".prdct-item__name::text").extract()
        item_cost=response.css(".prdct-item__prc-val::text").extract()
        item['product_name']=product_name
        item['product_price']=item_cost

        #opening the json file
        f=open('google.json')
        initial_data=json.load(f)

        data={}
        data['Logitech_keyboard']={'product_name':[],'product_price':[]}
        data['Logitech_mouse']={'product_name':[],'product_price':[]}
        data['Zebronics_keyboard']={'product_name':[],'product_price':[]}
        data['HP_mouse']={'product_name':[],'product_price':[]}
        data['Lenovo_keyboard']={'product_name':[],'product_price':[]}
        data['I-Ball_keyboard']={'product_name':[],'product_price':[]}
        data['Dell_mouse']={'product_name':[],'product_price':[]}
        data['Lenovo_mouse']={'product_name':[],'product_price':[]}
        data['Sandisk_pendrive']={'product_name':[],'product_price':[]}
        data['TP-link_router']={'product_name':[],'product_price':[]}
        data['HP_pendrive']={'product_name':[],'product_price':[]}
        data['HP_keyboard']={'product_name':[],'product_price':[]}
        data['Seagate_disk']={'product_name':[],'product_price':[]}
        data['Sony_disk']={'product_name':[],'product_price':[]}
        data['Transcend_disk']={'product_name':[],'product_price':[]}
        data['Netgear_router']={'product_name':[],'product_price':[]}
        data['Zebronics_mouse']={'product_name':[],'product_price':[]}
        data['Dell_keyboard']={'product_name':[],'product_price':[]}

        
        index=0
        for i in data:
            for j in range(len(initial_data[index]['product_name'])):
                data[i]['product_name'].append(initial_data[index]['product_name'][j])
                data[i]['product_price'].append(initial_data[index]['product_price'][j])
            index+=1

        json_object = json.dumps(data, indent = 4) 
   
        with open("data.json", "w") as outfile: 
            outfile.write(json_object) 



    '''        
        if(AmazonSpider.product=='keyboard'):
        elif(AmazonSpider.product=='mouse'):
            product_name=response.css(".prdct-item__name::text").extract()
            item_cost=response.css(".prdct-item__prc-val::text").extract()
            item['product_name_mouse']=product_name
            item['product_price_mouse']=item_cost
        elif(AmazonSpider.product=='pendrive'):
            product_name=response.css(".prdct-item__name::text").extract()
            item_cost=response.css(".prdct-item__prc-val::text").extract()
            item['product_name_pendrive']=product_name
            item['product_price_pendrive']=item_cost
        elif(AmazonSpider.product=='router'):
            product_name=response.css(".prdct-item__name::text").extract()
            item_cost=response.css(".prdct-item__prc-val::text").extract()
            item['product_name_router']=product_name
            item['product_price_router']=item_cost
        elif(AmazonSpider.product=='harddisk'):
            product_name=response.css(".prdct-item__name::text").extract()
            item_cost=response.css(".prdct-item__prc-val::text").extract()
            item['product_name_harddisk']=product_name
            item['product_price_harddisk']=item_cost

        match=dict()
        for i in range(len(product_name)):
            match[product_name[i]]=item_cost[i]

        for i in match:
            print(i,"::",match[i])     
    '''


