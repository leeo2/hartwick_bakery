# Olivia Lee
# 10-14-19
# Hartwick Bakery

cookies = []
candies = []


def cookies_input():
    for i in range(0, 6):
        cookies_monthly = int(input("Cookies:"))
        cookies.insert(i, cookies_monthly)
    return cookies_monthly


def candies_input():
    for i in range(0, 6):
        candies_monthly = int(input("Candies:"))
        candies.insert(i, candies_monthly)
    return candies_monthly


def avg_cookie_sales():
    sum = 0
    for cookie in cookies:
        sum = sum + cookie
    avg = sum/6
    return avg


def avg_candy_sales():
    sum_2 = 0
    for candy in candies:
        sum_2 = sum_2 + candy
    avg_2 = sum_2/6
    return avg_2


def max_cookie():
    max_cookies = 0
    if cookies[0] >= cookies[1] and cookies[0] >= cookies[2] and cookies[0] >= cookies[3] and cookies[0] >= cookies[4] and cookies[0] >= cookies[5]:
        max_cookies = cookies[0]
    elif cookies[1] >= cookies[0] and cookies[1] >= cookies[2] and cookies[1] >= cookies[3] and cookies[1] >= cookies[4] and cookies[1] >= cookies[5]:
        max_cookies = cookies[1]
    elif cookies[2] >= cookies[0] and cookies[2] >= cookies[1] and cookies[2] >= cookies[3] and cookies[2] >= cookies[4] and cookies[2] >= cookies[5]:
        max_cookies = cookies[2]
    elif cookies[3] >= cookies[0] and cookies[3] >= cookies[1] and cookies[3] >= cookies[2] and cookies[3] >= cookies[4] and cookies[3] >= cookies[5]:
        max_cookies = cookies[3]
    elif cookies[4] >= cookies[0] and cookies[4] >= cookies[1] and cookies[4] >= cookies[2] and cookies[4] >= cookies[3] and cookies[4] >= cookies[5]:
        max_cookies = cookies[4]
    elif cookies[5] >= cookies[0] and cookies[5] >= cookies[1] and cookies[5] >= cookies[2] and cookies[5] <= cookies[3] and cookies[5] <= cookies[4]:
        max_cookies = cookies[5]
    return max_cookies


def max_candy():
    max = 0
    if candies[0] >= candies[1] and candies[0] >= candies[2] and candies[0] >= candies[3] and candies[0] >= candies[4] and candies[0] >= candies[5]:
        max = candies[0]
    elif candies[1] >= candies[0] and candies[1] >= candies[2] and candies[1] >= candies[3] and candies[1] >= candies[4] and candies[1] >= candies[5]:
        max = candies[1]
    elif candies[2] >= candies[0] and candies[2] >= candies[1] and candies[2] >= candies[3] and candies[2] >= candies[4] and candies[2] >= candies[5]:
        max = candies[2]
    elif candies[3] >= candies[0] and candies[3] >= candies[1] and candies[3] >= candies[2] and candies[3] >= candies[4] and candies[3] >= candies[5]:
        max = candies[3]
    elif candies[4] >= candies[0] and candies[4] >= candies[1] and candies[4] >= candies[2] and candies[4] >= candies[3] and candies[4] >= candies[5]:
        max = candies[4]
    elif candies[5] >= candies[0] and candies[5] >= candies[1] and candies[5] >= candies[2] and candies[5] >= candies[3] and candies[5] >= candies[5]:
        max = candies[5]
    return max


def min_cookies():
    min_cookie = 0
    if cookies[0] <= cookies[1] and cookies[0] <= cookies[2] and cookies[0] <= cookies[3] and cookies[0] <= cookies[4] and cookies[0] <= cookies[5]:
        min_cookie = cookies[0]
    elif cookies[1] <= cookies[0] and cookies[1] <= cookies[2] and cookies[1] <= cookies[3] and cookies[1] <= cookies[4] and cookies[1] <= cookies[5]:
        min_cookie = cookies[1]
    elif cookies[2] <= cookies[0] and cookies[2] <= cookies[1] and cookies[2] <= cookies[3] and cookies[2] <= cookies[4] and cookies[2] <= cookies[5]:
        min_cookie = cookies[2]
    elif cookies[3] <= cookies[0] and cookies[3] <= cookies[1] and cookies[3] <= cookies[2] and cookies[3] <= cookies[4] and cookies[3] <= cookies[5]:
        min_cookie = cookies[3]
    elif cookies[4] <= cookies[0] and cookies[4] <= cookies[1] and cookies[4] <= cookies[2] and cookies[4] <= cookies[3] and cookies[4] <= cookies[5]:
        min_cookie = cookies[4]
    elif cookies[5] <= cookies[0] and cookies[5] <= cookies[1] and cookies[5] <= cookies[2] and cookies[5] <= cookies[3] and cookies[5] <= cookies[4]:
        min_cookie = cookies[5]
    return min_cookie


def min_candies():
    min = 0
    if candies[0] <= candies[1] and candies[0] <= candies[2] and candies[0] <= candies[3] and candies[0] <= candies[4] and candies[0] <= candies[5]:
        min = candies[0]
    elif candies[1] <= candies[0] and candies[1] <= candies[2] and candies[1] <= candies[3] and candies[1] <= candies[4] and candies[1] <= candies[5]:
        min = candies[1]
    elif candies[2] <= candies[0] and candies[2] <= candies[1] and candies[2] <= candies[3] and candies[2] <= candies[4] and candies[2] <= candies[5]:
        min = candies[2]
    elif candies[3] <= candies[0] and candies[3] <= candies[1] and candies[3] <= candies[2] and candies[3] <= candies[4] and candies[3] <= candies[5]:
        min = candies[3]
    elif candies[4] <= candies[0] and candies[4] <= candies[1] and candies[4] <= candies[2] and candies[4] <= candies[3] and candies[4] <= candies[5]:
        min = candies[4]
    elif candies[5] <= candies[0] and candies[5] <= candies[1] and candies[5] <= candies[2] and candies[5] <= candies[3] and candies[5] <= candies[4]:
        min = candies[5]
    return min


def most_popular():
    sum_cookie = 0
    sum_candy = 0
    for cookie in cookies:
        sum_cookie = sum_cookie + cookie
    for candy in candies:
        sum_candy = sum_candy + candy
    if sum_cookie > sum_candy:
        print("Cookies are more popular than candy in the Hartwick bakery.")
    elif sum_candy > sum_cookie:
        print("Candy is more popular than the cookies in the Hartwick bakery.")
    else:
        print("Candy and Cookie sales are equal in the Hartwick bakery.")


cookies_input()
candies_input()
print("Avg. cookie sales:")
print(avg_cookie_sales())
print("Avg. candy sales")
print(avg_candy_sales())
print("Maximum cookies sold in one month:")
print(max_cookie())
print("Maximum candies sold in one month:")
print(max_candy())
print("Minimum cookies sold in one month:")
print(min_cookies())
print("Minimum candies sold in one month:")
print(min_candies())
most_popular()

