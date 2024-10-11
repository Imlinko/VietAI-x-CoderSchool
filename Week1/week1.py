
# Ex1: Write a program to count positive and negative numbers in a list
#INPUT
data1 = [-10, -21, -4, -45, -66, 93, 11, -4, -6, 12, 11, 4]
#1.==SOLUTION==O(n)
#KHỞI TẠO 2 ÔNG LÍNH CANH
num_pos = 0
num_neg = 0
#KHỞI TẠO VÒNG LẶP KIỂM TRA TRONG TỪNG PHẦN TỬ TRONG MẢNG
for num in data1:
    if num < 0: #ĐIỀU KIỆN ĐỂ KIỂM TRA XEM PHẦN TỬ LÀ ÂM HAY DƯƠNG
        num_neg+=1
    else:
        num_pos+=1
#IN RA MÀN HÌNH TỔNG SỐ DƯƠNG VÀ ÂM
#OUTPUT
print(f"Tổng số phần tử dương trong data1: {num_pos} ")
print(f"Tổng số phần tử âm trong data1: {num_neg}")

# Ex2: Given a list, extract all elements whose frequency is greater than k.
#INPUT
data2 = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
k = 3
#2.==SOLUTION==
#SOL(O(N^2))
#KHỞI TẠO HÀM TÍNH TẦN SUẤT XUẤT HIỆN CỦA PHẦN TỬ TRONG MẢNG
def find_freq(data,u):
    count_freq= 0 # Khởi tạo ông lính tính số lần xuất hiện của i
    for i in data:
        if i == u:
            count_freq+=1
    return count_freq
#KHỞI TẠO HÀM SO SÁNH TẦN SUẤT CỦA TỪNG PHẦN TỬ VỚI K
def feq_greater_k(data,freq):
    lst_freq = set() #Tạo một set() Tránh lặp lại giá trị
    for i in data: #Khởi tạo một vòng lặp n phần tử
        num_freq = find_freq(data,i)
        if num_freq > freq:
            lst_freq.add(i) #ĐẨY PHẦN TỬ VÀO SET()
    return list(lst_freq)

lst_feq = feq_greater_k(data2,k)
print(lst_feq)


# ==SOL(O(N))==

def find_freq_2(data, feq):
    req = []
    data_dic = {
        # data[i]: feq,
    }  # Hashtable

    for i in data:
        num_str = str(i)
        num_freq = data_dic.get(num_str, 0)  # Lấy giá trị từ key
        data_dic[num_str] = num_freq + 1  # Cộng cho value của key

    # LẤY HẾT CÁC KEY VÀ VALUE TRONG data_dict
    # Nếu value lớn k
    # Đẩy vào mảng req
    # Nếu không thì next
    for v, k in data_dic.items():
        if k > feq:
            req.append(int(v))
    return req


# ==OUTPUT==
lst_num = find_freq_2(data2, k)
print(lst_num)

# Ex3: find the strongest neighbour. Given an array of N positive integers.
# The task is to find the maximum for every adjacent pair in the array.
data3 = [4, 5, 6, 7, 3, 9, 11, 2, 10]
#KHỞI TẠO HÀM TÌM GIÁ TRỊ LIỀN KỀ LỚN NHẤT
def strong_neighbor(data):
    max_seq = [] #Tạo ra một mảng chứa các giá trị max
    for i in range(len(data)-1):
       #Tìm giá trị lớn nhất theo từng cặp i , i+1
       max_seq.append(max(data[i],data[i+1]))
    return max_seq
#==OUTPUT==
max_lst = strong_neighbor(data3)

print(max_lst)
# Ex5: Given two matrices (2 nested lists), the task is to write a Python program
# to add elements to each row from initial matrix.
# For example: Input : test_list1 = [[4, 3, 5,], [1, 2, 3], [3, 7, 4]], test_list2 = [[1], [9], [8]]
# Output : [[4, 3, 5, 1], [1, 2, 3, 9], [3, 7, 4, 8]]
data5_list1 = [[4, 3, 5, ], [1, 2, 3], [3, 7, 4]]
data5_list2 = [[1, 3], [9, 3, 5, 7], [8]]
#==SOLUTION==O(n^2)
#KHỞI TẠO HÀM ADD ELEMENT CỦA LIST_2 VÀO TỪNG PHẦN TỬ CỦA LIST_1
def add_list_2_to_list_1(data_1,data_2) ->list:
    i = 0 #Khởi tạo biến chạy 0 -->len(data1)
    while i < len(data_1):
        for var in data_2[i]:
            data_1[i].append(var) #Với từng phần tử của mảng list_1 ta thêm từng phần tử của list_2
        i+=1
    return data_1
#==OUTPUT==
new_data = add_list_2_to_list_1(data5_list1,data5_list2)
print(new_data)

#==SOLUTON==(2)
#SỬ DỤNG HÀM ZIP()
#LIST1 = [1,2,3,4]
#LIST2 = [6,7,8,9]
#ZIPPED = [(1,6),(2,7),(3,8),(4,9)]
def zipped(d1,d2):
    add_arr = [] #Khởi tạo mảng
    zipp = list(zip(d1,d2)) #zipp = [(data1,data2)]
    for element in zipp: # Quét qua từng phần tử của mảng zipp
        if list(element) not in d2:
            add_arr.append(list(element[0]))#Cast element rồi add từng phần tử thứ nhất của element(tránh lặp lại)
    return add_arr
#==OUTPUT==
z = zipped(data5_list1,data5_list2)
print(z)
# Ex6:  Write a program which will find all such numbers which are divisible by 7
# but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line
#==SOlUTION==

def divide_7_not_5() ->str:
    num_arr = list() #Khởi tạo list
    for n in range(2000,3201): # Không gian tìm kiếm
        if n % 7 == 0 and n %5 != 0: #điều kiện tìm kiếm
            num_arr.append(str(n)) #Cast các phần tử theo kiểm string rồi add nó vào chuỗi
    return ", ".join(num_arr) #Hàm join để add ',' vào từng thành phần của num_arr
#==OUTPUT==
seven_not_five = divide_7_not_5()
print(seven_not_five)

# Ex7: Write a program, which will find all such numbers between 1000 and 3000 (both included)
# such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

#==SOLUTION==O(N)
#KHỞI TẠO HÀM TÌM SỐ MÀ CHỮ SỐ CHIA HẾT CHO 2
def even_num_dig() ->str:
    even_arr = [] #Khởi tạo mảng
    for e in range(1000,3001): #KHÔNG GIAN TÌM KIỂM
        e = str(e) #Cast số thành string
        if ( int(e[0]) %2 ==0 and # Cơ số 1000
             int(e[1]) %2 == 0 and #Cơ số 100 ====> ĐIỀU KIỆN TÌM KIẾM
             int(e[2]) %2 == 0 and #Cơ số 10
             int(e[3]) %2 == 0 #Cơ số 1

          ):
            even_arr.append(e) #Add số vào mảng
    return ", ".join(even_arr)
#==OUTPUT==
even_nums = even_num_dig()
print(even_nums)
# Ex4: print all Possible Combinations from the three Digits
data4 = [1, 2, 3]
#==Solution==
n_arr = []
#Khởi tạo bức tường
visited = [False]*len(data4)
def back_tracking(cur):
    if len(cur) == len(data4):
        n_arr.append(cur.copy()) #Xét điều kiện dừng
    for i in range(len(data4)):
        if not visited[i]:
            cur.append(data4[i])
            visited[i] = True

            back_tracking(cur)

            visited[i] =False

            cur.pop()

back_tracking([])
print(n_arr)

