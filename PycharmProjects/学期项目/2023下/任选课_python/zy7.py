
# price_dict={"苹果":5.98,  "香蕉":7, "葡萄":9.8,
#             "毛巾":13.8,  "牙刷":24.8,   "香皂":20,
#             "铅笔":1.8,  "尺子":4.5,   "橡皮":3.2}
# #定义查商品价格的函数
# #定义一个函数，求一定数量的某种商品的总价
# shopping_goods_list=["苹果",  "香蕉", "牙刷",  "铅笔"]
# shopping_number_list=[1.5,  2.5, 2, 5]
# #定义一个函数，求多种商品的总价
# #################################################

# fruit_list =["苹果",  "香蕉", "葡萄"]
# #定义一个函数，判断某种商品是否是水果
# #定义一个函数，求某种水果的总价,并考虑水果打折7折的情况
# #定义一个函数，求某一种商品的总价,并考虑如果是水果则打折7折的情况
# #定义一个函数，求多种商品的总价,并考虑如果是水果则打折7折的情况

price_dict={"苹果":5.98,"香蕉":7, "葡萄":9.8, "毛巾":13.8, "牙刷":24.8, "香皂":20, "铅笔":1.8,  "尺子":4.5, "橡皮":3.2}
fruit_list =["苹果",  "香蕉", "葡萄"]

#定义查商品价格的函数
def get_price(name):
    return price_dict.get(name)

#定义一个函数，求一定数量的某种商品的总价
def get_prices(name, quantity):
    sum_prices = get_price(name) * quantity
    return round(sum_prices, 2)

#定义一个函数，求多种商品的总价
def get_all_prices(name_list:list, quantity_list):
    sum_prices = 0
    for i in range(len(name_list)):
        name = name_list[i]
        prices = get_price(name)
        prices = get_prices(name, quantity_list[i])
        sum_prices += prices

    return sum_prices

#定义一个函数，判断某种商品是否是水果
def estimate(name):
    if name in fruit_list:
        return True
    else:
        return False
   
#定义一个函数，求某种水果的总价,并考虑水果打折7折的情况   
def get_discount(name, quantity):
    TotalPrice = get_prices(name, quantity)
    return round(TotalPrice * 0.7, 2)

#定义一个函数，求某一种商品的总价,并考虑如果是水果则打折7折的情况
def get_one_Price(name, quantity):
    if estimate(name):
        return get_discount(name, quantity)
    else:
        return get_prices(name, quantity)

#定义一个函数，求多种商品的总价,并考虑如果是水果则打折7折的情况
def get_TotalPrice(name_list, quantity_list):
    sum_prices = 0
    for i in range(len(name_list)):
        prices = get_one_Price(name_list[i], quantity_list[i])
        sum_prices = sum_prices + prices
    return sum_prices

need = ["苹果", "香蕉", "毛巾", "牙刷"]
need_num = [9, 5, 3, 2]
print(get_one_Price("香蕉", 2))