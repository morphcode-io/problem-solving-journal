class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1_i = m - 1
        rigth = len(nums1) - 1
        while nums1_i >= 0:
            nums1[rigth], nums1[nums1_i] = nums1[nums1_i], nums1[rigth]
            rigth -= 1
            nums1_i -= 1 
        curr_index = 0
        nums2_i = 0
        nums1_i = rigth + 1
        
        while nums1_i < len(nums1) and nums2_i < n:
            if nums1[nums1_i] < nums2[nums2_i]:
                nums1[curr_index] = nums1[nums1_i]
                nums1_i += 1
            else:
                nums1[curr_index] = nums2[nums2_i]
                nums2_i += 1
            curr_index += 1
        
        while nums1_i < m:
            nums1[curr_index] = nums1[nums1_i]
            nums1_i += 1
            curr_index += 1

        while nums2_i < n:
            nums1[curr_index] = nums2[nums2_i]
            nums2_i += 1
            curr_index += 1


