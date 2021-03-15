class Patient:
  def __init__(self, name, age, sex, bmi, num_of_children, smoker):
    self.name = name
    self.age = age
    self.sex = sex
    self.bmi = bmi
    self.num_of_children = num_of_children
    self.smoker = smoker

  def estimated_insurance_cost(self):
    estimated_cost = 250 * self.age - 128 * self.sex + 370 * self.bmi + 425 * self.num_of_children + 24000 * self.smoker - 12500
    print("{}'s estimated insurance costs is {} dollars.".format(self.name,estimated_cost))

  def update_age(self, new_age):
    try:
      if isinstance(new_age, int):
        self.age = new_age  
        print("{} is now {} years old.".format(self.name, self.age))
        self.estimated_insurance_cost()
      else:
        raise ValueError("The age has to be an integer")
    except:
      print("ValueError! You have to introduce an integer for the age.")

  def update_num_children(self, new_num_children):
    try:
      if isinstance(new_num_children, int):
        self.num_of_children = new_num_children
        if(self.num_of_children > 1):
          print("{} has {} children.".format(self.name,self.num_of_children))
        else:
          print("{} has {} child.".format(self.name,self.num_of_children))
        self.estimated_insurance_cost()
      else:
        raise ValueError("You have to introduce and integer")
    except:
      print("Value Error! You must introduce an integer for the number of children.")


  def update_bmi(self, new_bmi):
    try:
      if isinstance(new_bmi, float):
        self.bmi = new_bmi
        print("{} has now {} bmi.".format(self.name, self.bmi))
        self.estimated_insurance_cost()
      else:
        raise ValueError("The bmi has to be a float.")
    except:
       print("Value Error! The bmi has to be a float.") 

  def update_smoking_status(self, new_smoker):
    try:
      if (new_smoker == 1 or new_smoker == 0):
        self.smoker = new_smoker
        if (self.smoker == 1):
          print("{} is now a smoker.".format(self.name))
        else:
          print("{} is now a non-smoker.".format(self.name))
        self.estimated_insurance_cost()
      else:
        raise ValueError("Please introduce 1 or 0")
    except:
      print("ValueError! You have to introduce 1 for smoker or 0 for non-smoker.")

  def patient_profile(self):
     patient_information = {}
     patient_information["Name"] = self.name
     patient_information["Age"] = self.age
     patient_information["Sex"] = self.sex
     patient_information["BMI"] = self.bmi
     patient_information["Number of Children"] =   self.num_of_children
     patient_information["Smoker"] = self.smoker
     return patient_information

patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0)
#patient1.estimated_insurance_cost()
patient1.update_age('age')
#patient1.update_num_children(13.3)
#patient1.update_bmi(1)
#patient1.update_smoking_status("Mere")
print(patient1.patient_profile())
