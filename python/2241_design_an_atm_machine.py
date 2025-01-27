

class ATM:

    def __init__(self):
        self.banknotes = [500, 200, 100, 50, 20]
        self.banknotesCount = [0, 0, 0, 0, 0]
        self.types = 5

    def deposit(self, banknotesCount: list[int]) -> None:
        for i, count in enumerate(banknotesCount):
            self.banknotesCount[len(self.banknotesCount)-i-1] += count

    def withdraw(self, amount: int) -> list[int]:
        drawBanknotesCount = [0] * self.types
        for i, banknote in enumerate(self.banknotes):
            if amount == 0:
                break
            currentCount = min(amount // banknote, self.banknotesCount[i])
            drawBanknotesCount[i] = currentCount
            amount -= banknote * currentCount

        if amount != 0:
            return [-1]

        for i, count in enumerate(drawBanknotesCount):
            self.banknotesCount[i] -= count

        return drawBanknotesCount[::-1]

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
