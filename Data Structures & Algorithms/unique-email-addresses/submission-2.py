class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
    #method 1st:-

        # unique=set()

        # for e in emails:
        #     i,local=0,""

        #     while e[i] not in ["@","+"]:
        #         if e[i]!=".":
        #             local+=e[i]

        #         i+=1

        #     while e[i]!="@":
        #         i+=1

        #     domain =e[i+1:]
        #     unique.add((local,domain))

        # return len(unique)



        #method 2nd:-
        unique=set()

        for e in emails:
            local,domain=e.split('@')
            local=local.split("+")[0]
            local=local.replace(".","")
            final_email=local+"@"+domain
            unique.add(final_email)
        return len(unique)


