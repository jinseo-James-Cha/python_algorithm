class Solution:
    def maskPII(self, s: str) -> str:
        """
        string manipulation

        Email or Phone number

        Email
        - two uppercase and lowercase letters + @ + domain + . 
        - all lowercase and first letter +  * X 5 + last letter 
        """
        
        
        if '@' in s:
            res = s.split('@')
            res[0] = res[0].lower()
            res[1] = res[1].lower()

            res[0] = res[0][0] + '*****' + res[0][-1]
            return "@".join(res)
        else:
            res = [ch for ch in s if ch.isnumeric()]
            phone_len = len(res)
            last_four = res[phone_len-4:]
            country_code_len = phone_len % 10
            country_code = ""
            if country_code_len > 0:
                country_code = "+" + ("*" * country_code_len) + "-"
            
            
            return country_code + "***-***-" + "".join(last_four)