# application -> University -> approved

#INPUT DATA
UNIVERSITY_MARK     = 7.0 # float
student_SCHOOL_MARK = 6.0 # float

UNIVERSITY_contract = 10000 # int / year
student_MONEY       = 12000 

student_DAD_HAS_CONN = True

#LOGIC
# !!! OPERATOR PRECEDENCE (1 + 2) * 3
approved = student_SCHOOL_MARK >= UNIVERSITY_MARK\
           or\
           student_MONEY >= UNIVERSITY_contract\
           or\
           student_DAD_HAS_CONN == True          

#OUTPUT
print( "Will the student be approved?", approved )