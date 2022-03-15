from app import form_response 

class  NotANumber(Exception):
    def __init__(self, message="Values entered are not Numerical"):
        self.message = message
        super().__init__(self.message)

input_data = {
    "incorrect_values": 
    {"CustomerId": 15701354, 
    "CreditScore": 850, 
    "Age": 'as', 
    "Tenure": 9, 
    "Balance": 125510.82, 
    "NumOfProducts": 'ab',
    "HasCrCard": 0,
    "IsActiveMember": 1,
    "EstimatedSalary": 190857.79,
    },

    "correct_values": 
    {"CustomerId": 15701354, 
    "CreditScore": 850, 
    "Age": 42, 
    "Tenure": 9, 
    "Balance": 125510.82, 
    "NumOfProducts": 2,
    "HasCrCard": 0,
    "IsActiveMember": 1,
    "EstimatedSalary": 190857.79, 
    }
}

def test_form_response_incorrect_values(data=input_data["incorrect_values"]):
    res=form_response(data)
    assert res == NotANumber().message