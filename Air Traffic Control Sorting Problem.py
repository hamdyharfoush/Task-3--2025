#Name: Rehab Ahmed Sharaf Al-Dein
#Section:4

#-------------------------------------------
#why I selected merge sort?

#I chose Merge Sort because it provides efficient 
# performance with large datasets, operating at O(n log n) 
# time complexity in all cases, whether the data is 
# partially sorted or random. This algorithm is stable, 
# meaning it preserves the order of flights with the same 
# arrival time, which is crucial in air traffic management 
# where flights are scheduled based on priority. 
# Additionally, it ensures consistent performance without 
# slowdowns in the worst case, unlike Quick Sort, which can
# degrade to O(n²) in the worst-case scenario.

#-----------------------------------------------------
#How the sorting method would impact real-time air traffic
# management in a high-traffic scenario?

#In a high-traffic air traffic management scenario, 
# sorting needs to be fast and efficient to prevent 
# delays in scheduling flights. Merge Sort is beneficial 
# as it performs efficiently even with a large number of 
# flights, ensuring flights are sorted by arrival or 
# departure time accurately. Since it is a stable algorithm,
# it ensures that flights with the same arrival time 
# maintain their original order, preserving priority 
# scheduling. Additionally, Merge Sort can be implemented 
# in a parallelized manner, which enhances its speed when 
# dealing with large-scale real-time data.

#-------------------------------------------------


def merge_sort(flights):
    if len(flights) > 1:
        mid = len(flights) // 2  # تقسيم القائمة إلى نصفين
        left_half = flights[:mid]
        right_half = flights[mid:]

        # استدعاء Merge Sort لكل نصف
        merge_sort(left_half)
        merge_sort(right_half)

        # دمج النصفين
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i]["Arrival Time"] <= right_half[j]["Arrival Time"]:
                flights[k] = left_half[i]
                i += 1
            else:
                flights[k] = right_half[j]
                j += 1
            k += 1

        # إضافة العناصر المتبقية في كل نصف
        while i < len(left_half):
            flights[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            flights[k] = right_half[j]
            j += 1
            k += 1
            
            
flights = [
    {"Flight ID": "A101", "Arrival Time": "12:30", "Altitude": 30000, "Speed": 550},
    {"Flight ID": "B202", "Arrival Time": "11:45", "Altitude": 28000, "Speed": 600},
    {"Flight ID": "C303", "Arrival Time": "13:15", "Altitude": 32000, "Speed": 500},
    {"Flight ID": "D404", "Arrival Time": "10:10", "Altitude": 29000, "Speed": 530}
]

print("قبل الترتيب:")
for flight in flights:
    print(flight)

merge_sort(flights)

print("\nبعد الترتيب حسب وقت الوصول:")
for flight in flights:
    print(flight)