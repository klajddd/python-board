class One_away:
    
    def one_away(self, first, second):
        
        if len(first) == len(second):
            return self.check_same_length_strings(first, second)
    
        elif abs(len(first) - len(second) == 1):
            # find the shorter string
            s1, s2 = first, second if len(first) < len(second) else second, first
            return self.check_one_step(s1, s2)

        else:
            return False

    
    def check_same_length_strings(self, s1, s2):
        
        at_most_one = True 

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if not at_most_one:
                    return False 
                else:
                    at_most_one = False 

        return True


    def check_one_step(self, s1, s2):
        
        index1, index2 = 0, 0

        while index2 < len(s2) and index1 < len(s1):
            
            if s1[index1] != s2[index2]:

                if index1 != index2:
                    return False 

                index2 += 1

            else:
                index1 += 1
                index2 += 1

        return True 


o = One_away()
print(o.one_away("pale", "pales"))