if __name__ == '__main__':
    n = int(input())
    my_list = []
    for i in range(1,n+1):
        my_list.append(i)
        
    print(*my_list, sep = '')
        