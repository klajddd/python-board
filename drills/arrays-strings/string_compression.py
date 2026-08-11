class Solution:


    # // time: O(p) where p is the size of the original string
    def stringCompression_efficient_but_long_duplicated(self, string):
        
        final_length = self.count_compression(string)
        if final_length >= len(string):
            return string

        compressed_string = []

        count = 0

        for i in range(len(string)):
            count += 1

            if i + 1 >= len(string) or string[i] != string[i+1]:
                compressed_string.append(string[i])
                compressed_string.append(str(count))

                count = 0
        return ''.join(compressed_string)


    def count_compression(self, string):
        compressed_length = 0
        count = 0

        for i in range(len(string)):
            
            count += 1

            if i + 1 >= len(string) or string[i] != string[i+1]:
                
                compressed_length += 1 + len(str(count))
                count = 0

        return compressed_length






    
    # // time: O(p) where p is the size of the original string

    # // negatives:
    # // 1. compressed string list will be created and may be never used as its length could be longer than the original string, this raises costs for very very long strings
    # // 2. NOT SURE IF APPLIES TO PYTHON - compressed string list builder is not initialized at the neccessary capacity, without this it will need to double its capacity everytime it is full, 
    # //    the end capacity could be double to what we ultimately need

    # // more efficient solution below
    def stringCompression(self, string):
        
        count = 0

        compressed_string = []

        for i in range(len(string)):
            
            count += 1

            if i + 1 >= len(string) or string[i] != string[i + 1]:
                
                compressed_string.append(string[i])
                compressed_string.append(str(count))
                count = 0
        
        if len(''.join(compressed_string)) < len(string):
            return ''.join(compressed_string)
        
        return string



s = Solution()

print(s.stringCompression("kllllllajddddddd"))
print(s.stringCompression_efficient_but_long_duplicated("kllllllajddddddd"))
print(s.stringCompression("aabcccccaaa"))
print(s.stringCompression_efficient_but_long_duplicated("aabcccccaaa"))
