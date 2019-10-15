# Olivia Lee
# 10-14-19
# Hartwick Bakery


def cookies_input():
    for i in range(0, 6):
        cookies_monthly = input("Cookies:")
        cookies.insert(i, cookies_monthly)
    return cookies_monthly


def candies_input():
    for i in range(0, 6):
        candies_monthly = input("Candies:")
        candies.insert(i, candies_monthly)
    return candies


def avg_cookie_sales():
    for cookie in cookies:
        total = total + cookies_input()
    return total


cookies = []
candies = []

avg = total / 6
print(total)
print(cookies_input())
print(candies_input())
print(avg)

# print((candies(0)+candies(1)+candies(2)+candies(3)+candies(4)+candies(5))/6)
