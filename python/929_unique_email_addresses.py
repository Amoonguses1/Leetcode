# Time: O(NM)
# Space: O(NM)
# N = len(emails), M = max length of emails[i], i from 0 to N
from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.', "")
            seen.add(local+"@"+domain)
        return len(seen)
