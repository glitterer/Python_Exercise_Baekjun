#width of new laptop, height of new laptop, width of laptop sticker, height of laptop sticker
wc, hc, ws, hs = map(int, input(). split())

if (wc-2 >= ws) and (hc-2 >= hs):
    print(1)
else:
    print(0)
