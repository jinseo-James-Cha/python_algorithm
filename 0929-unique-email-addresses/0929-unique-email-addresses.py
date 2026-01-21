# local name and a domain name
# localname@domain.name
# . or +

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def getForwardEmail(email):
            email_list = email.split('@')
            local_name, domain_name = email_list[0], email_list[1]
            
            # we do think only local name
            # 1. remove after @
            if '+' in local_name:
                local_name = local_name[:local_name.index('+')]
            local_name = local_name.replace('.', '')
            
            return local_name + '@' + domain_name
        
        receive_emails = set()
        for email in emails:
            forward_email = getForwardEmail(email)
            receive_emails.add(forward_email)
        
        return len(receive_emails)
        # split by @
        # remove after +
        # replace . to ""
        # save localname + @ + domain name into set -> no duplication
        s = set()
        for email in emails:
            localName, domainName = email.split('@')
            localName = localName.replace('.', "")
            if '+' in localName:
                localName = localName[:localName.index('+')]

            s.add(localName + '@' + domainName)
        return len(s)
        
        