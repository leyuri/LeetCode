class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        i = 0
        j = 0
        result = []
        nums1.sort()
        nums2.sort()
        # for i in (i, len(nums1)) and j in (j, len(nums2)):
        while i < len(nums1) and j < len(nums2) :
            if nums1[i] < nums2[j]:
                i = i + 1
            elif nums1[i] > nums2[j]:
                j = j + 1
            else :
                result.append(nums1[i])
                i = i + 1
                j = j + 1
        return result