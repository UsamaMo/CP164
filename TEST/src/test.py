"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-02-14"
-------------------------------------------------------
"""
# from Sorted_List_array import Sorted_List
# # key = 30
# # values = [3, 5, 6, 7, 10, 15, 30, 45]
# # left = 0
# # right = len(values) - 1
# #
# # while left < right:
# #     mid = (right + left) // 2
# #     if key > values[mid]:
# #         left = mid + 1
# #     else:
# #         right = mid
# #
# # if left == right and values[left] == key:
# #     i = left
# # else:
# #     i = -1
# #
# # print(i)
#
#
# # values = [1, 2, 3, 4, 5]
# #
# # half = len(values) // 2
# #
# # target1 = Sorted_List()
# # target2 = Sorted_List()
# #
# # for i in range(half - 1, -1, -1):
# #     target2._values.insert(0, values.pop())
# # for j in range(len(values) - 1, -1, -1):
# #     target1._values.insert(0, values.pop())
# #
# # for f in target1:
# #     print(f)
# #
# # for x in target2:
# #     print(x)
# #
# # print(target1)
# # print(target2)
#
#
#
# list array
# # #count method general
# # def count():
# #
# # number = 0:
# # for i in self._values:
# #     if i== key:
# #         number+=1
# # return number
# #
# #
# # #find method
# # def find(self,key):
# #
# # i = self._linear_search(key)
# #
# # if i != -1:
# #     value = deepcopy(self._values[1])
# # else:
# #     value = None
# # return value
# #
# #
# # # index
# # i = self._linear_search(key)
# #
# # return i
#
#
# def insert(self,i,value):
#
#     self._values[i:1] = [value]
#
#     return
#
#
# def intersecton(self,source1,source2):
#     assert len(self._values)==0
#     vals = []
#
#     if len(source1)<len(source2):
#         for i in source1:
#             if i in source2 and i not in vals:
#                 vals.append(i)
#     else:
#         for i in source2:
#             if i in source1 and i not in vals:
#                 vals.append(i)
#     self._values.extend(vals)
#     return
#
# #identical = True
# i = 0
# if len(target) != len(self._values):
#     identical = False
#
# while identical and 1<len(self._values):
#     if target[i] != self._values[i]
#         identical = False
#     i +=1
#     return

# def _linear_search(self, key):
#         """
#         -------------------------------------------------------
#         Searches for the occurrence of key in the set. Skips over None entries.
#         (Private helper method - used only by other ADT methods.)
#         Use: i = self._linear_search(key)
#         -------------------------------------------------------
#         Parameters:
#             key - a partial data element (?)
#         Returns​​‌​‌​​​‌:
#             i - the index of key in the set, -1 if key is not found (int)
#         -------------------------------------------------------
#            """


key = 5
values = [1, 2, 3, 4, 5]
n = len(values)
i = 0

while i < n and values[i] != key:
    i = i + 1
if i == n:
    i = -1

print(i)
