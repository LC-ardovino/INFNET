import threading


def trabalhador():
    """thread do trabalhador"""
    print('trabalhador')
    return


threads = []
for i in range(5):
    t = threading.Thread(target=trabalhador)
    threads.append(t)

for t in threads:
    t.start()