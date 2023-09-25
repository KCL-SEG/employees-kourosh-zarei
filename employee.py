"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""


class Employee:
    def __init__(
        self,
        name,
        monthly_salary=None,
        contract_per_hour=None,
        commission=None,
        bonus=None,
    ):
        self.name = name
        self.m_salary = monthly_salary
        self.contract = contract_per_hour
        self.commission = commission
        self.bonus = bonus

    def get_pay(self):
        total_pay = 0
        if self.m_salary:
            total_pay += self.m_salary
        if self.contract:
            total_pay += self.contract[0] * self.contract[1]
        if self.commission:
            total_pay += self.commission[0] * self.commission[1]
        if self.bonus:
            total_pay += self.bonus
        return total_pay

    def __str__(self):
        out_sentence = f"{self.name} works on a "
        if self.m_salary:
            out_sentence += f"monthly salary of {self.m_salary}"
        if self.contract:
            out_sentence += f"contract of {self.contract[1]} hours at {self.contract[0]}/hour"
        if self.commission:
            out_sentence += f" and receives a commission for {self.commission[1]} contract(s) at {self.commission[0]}/contract"
        if self.bonus:
            out_sentence += f" and receives a bonus commission of {self.bonus}"
        out_sentence += f".  Their total pay is {self.get_pay()}."
        return out_sentence


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee("Billie", monthly_salary=4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee("Charlie", contract_per_hour=(25, 100))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee("Renee", monthly_salary=3000, commission=(200, 4))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee("Jan", contract_per_hour=(25, 150), commission=(220, 3))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee("Robbie", monthly_salary=2000, bonus=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee("Ariel", contract_per_hour=(30, 120), bonus=600)


if __name__ == '__main__':
    print(billie)
    print(charlie)
    print(renee)
    print(jan)
    print(robbie)
    print(ariel)