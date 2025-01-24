# Time: O(NlogN)
# Space: O(N)
# N = len(keyTime) = len(keyName)


class Solution:
    def alertNames(self, keyName: list[str], keyTime: list[str]) -> list[str]:

        keyLogs = dict()
        for i, name in enumerate(keyName):
            log = keyLogs.get(name, [])
            log.append(keyTime[i])
            keyLogs[name] = log

        alertPeople = list()
        for name in keyLogs:
            log = sorted(keyLogs[name])
            for i in range(2, len(log)):
                if self.getDiffMinutes(log[i], log[i-2]) <= 60:
                    alertPeople.append(name)
                    break

        return sorted(alertPeople)

    def getDiffMinutes(self, laterTime: str, formerTime: str):
        h1, m1 = laterTime.split(":")
        h2, m2 = formerTime.split(":")
        diffH = int(h1) - int(h2)
        diffMin = int(m1) - int(m2)
        diff = diffH * 60 + diffMin
        return diff
