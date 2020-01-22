class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        
        
        version1 = list(map(int,version1.split('.')))
        version2 = list(map(int,version2.split('.')))
        if version1 == version2:
            return 0
        
        n = len(version1) if len(version1) < len(version2) else len(version2)
        
        for i in range(n):
            if version1[i] > version2[i]:
                return 1
            elif version1[i] < version2[i]:
                return -1
            else:
                continue
        
        if not any(version1[n:]) and not any(version2[n:]):
            return 0
        
        return 1 if len(version1)>len(version2) else -1
        
        
        