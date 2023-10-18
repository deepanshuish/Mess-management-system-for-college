import pandas as pd
 
def students_info():
    '''this function stores the database of information of 
    students'''
    
    students = {'Entry_no.':['2021eeb1220','2021eeb1219','2021eeb1217','2020ceb1215'],
                'Name':['Virat','Vaibhav','Srihit','Somya'],
                'Year':[1,1,1,2],
                'Contact no.':[8171828283,7689083332,7404700008,8320792773],
                'Hostel Name':['chenab west','chenab east','satluj','ravi'],
                'Department':['Electrical','Electrical','Electrical','Chemical']                
                }
    '''the above list contains data of student'''
    data= pd.DataFrame(students)
    data.to_csv('student_info.csv')
    '''returning the data to a csv file'''
    return data


def student_details():
    '''this function will give us the information of student which
    is stored in a database'''
    n=input('Enter entry no. : ')
    details=pd.read_csv('student_info.csv')
    a=details.index[details['Entry_no.']==n]
    '''this gives the index in the dataframe corresponding to 
    the entry number'''
    return details.loc[a]
    '''returning  the row of student info''' 
 

def price_per_meal():
    '''this function shows us the price of various meals available at the mess'''
    Menu = {"Meal":['Breakfast','Lunch','Snacks','Dinner','Special Dinner','Full Day'],
            'price':[30,50,20,60,80,150],}
    menu= pd.DataFrame(Menu,index=[1,2,3,4,5,6])
    '''forming a dataframe of menu card'''
    menu.to_csv('Menu_card.csv')
    '''stpring data in a csv file'''
    return menu


def Mess_management(n):
    '''this function will calculate the bill of the students 
    based on the input they will give'''
    Students=[]
    Record=[]
    for j in range (n):
        '''this for loop is for number of students'''
        bill=0
        entry_no=input("Enter your entry no.:")
        print('''1) Breakfast 2) Lunch   3) snacks  4)  Dinner(Y), Special Dinner(S)  5) Full Day''')
        student_choice=input("had Full Day?: ")
        '''using if else statements and taking student input to calculate bill'''
        if student_choice=='Y':
            bill+=150
        else:
            student_choice=input("had breakfast?(Y/N): ")
            if student_choice=='Y':
                bill+=30
            student_choice=input("had lunch(Y/N)?: ")
            if student_choice=='Y':
                bill+=50
            student_choice=input("had snacks(Y/N)?: ")
            if student_choice=='Y':         
                bill+=20
            student_choice=input("had dinner(Y/S/N)?: ")
            if student_choice=='Y':
                bill+=60
            elif student_choice=='S':
                bill+=80
        Record.append(bill)
        '''appending students bill in an empty list'''
        Students.append(entry_no) 
    data={'Entry_no.':Students, 'bill amount':Record}
    table= pd.DataFrame(data)
    '''forming a dataframe of student bill correspond to there entry number'''
    return table


def final_db():
    '''this function will combine the student information
    with there bill amount and will show to us'''
    tab_1=pd.read_csv('student_info.csv')
    tab_3=tab_1.iloc[:,0:3]
    '''taking the student info csv and selecting 3 columns from it'''
    a=tab_3.shape[0]
    '''this gives number of row count'''
    tab_2=Mess_management(a) 
    final_table= tab_3.merge(tab_2[['Entry_no.','bill amount']], on='Entry_no.',how='left')
    '''merging two dataframes of information and bill amount'''
    print(final_table)
    day_sum=final_table['bill amount'].sum() 
    '''calculating per day earning of mess'''
    print('Earning of mess: ', day_sum)


def Mess_analysis():
    '''this function takes input from user regarding number of student ate
    in the mess in a particular day and gives the least amount of the whole week'''
    total_sum=[]
    breakfast=[]
    lunch=[]
    snack=[]
    dinner=[]
    for i in range (7):
        '''using for loop for whole week'''
        s=0
        print('Number of students had breakfast on day ',i+1)
        a=int(input('Enter: '))
        s= a*30+s
        breakfast.append(a*30)
        print('Number of students had lunch on day ',i+1)
        b=int(input('Enter: '))
        s= b*50+s
        lunch.append(b*50)
        print('Number of students had snacks on day ',i+1)
        c=int(input('Enter: '))
        s= c*20+s
        snack.append(c*20)
        print('Number of students had dinner on day ',i+1)
        d=int(input('Enter: '))
        s= d*60+s
        dinner.append(d*60)
        '''taking input from the user and calculating the amount 
        received by the mess'''
        total_sum.append(s)       
    dict_={'Day':['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'],
           'Breakfast':breakfast,'Lunch':lunch,
           'Snacks':snack,'Dinner':dinner,'Total Bill':total_sum}
    db= pd.DataFrame(dict_)
    '''forming a dataframe of the data collected'''
    total_bill_i=db.set_index('Day')
    minvalue1=total_bill_i['Breakfast'].idxmin()
    minvalue2=total_bill_i['Lunch'].idxmin()
    minvalue3=total_bill_i['Snacks'].idxmin()
    minvalue4=total_bill_i['Dinner'].idxmin()
    '''retuning the minimum value of a particular meal for whole week'''
    print(total_bill_i)
    print('Students are not liking breakfast of : ', minvalue1)
    print('Students are not liking lunch of : ', minvalue2)
    print('Students are not liking snacks of : ', minvalue3)
    print('Students are not liking dinner of : ', minvalue4)

    
def suggestions():
    '''this function will take suggestions from the user and store it in 
    a database for further improvement'''
    a=input('Enter Entry_no.: ')
    b= input('Enter Your Sugession: ')
    suggest={'Entry_no':a, 'Suggestions':b}
    sugg=pd.read_csv('suggestions.csv')
    sugg=sugg.append(suggest, ignore_index=True)
    sugg.to_csv('suggestions.csv', index= False)
    return 'Thanks for your suggestion we will work on it'

def new_registeration():
    '''this function adds new registeration to the database'''
    a=input('Enter entry no.: ')
    b=input('Enter name: ')
    c=input('Enter year: ')
    d=input('Enter contact no.: ')
    e=input('Enter Hostel Name: ')
    f=input('Enter department: ')
    '''taking details of the student'''
    info=pd.read_csv('student_info.csv')
    info_1={"Entry_no.": a ,'Name':b ,'Year':c,'Contact no.':d,'Hostel Name':e,
                'Department':f}
    info=info.append(info_1, ignore_index=True)
    '''appending the information of new registeration in thee databbase'''
    info.to_csv('student_info.csv', index=False)
    '''updating the old csv file'''
    return 'New registeration added successfully'
    

def all_func():
    '''this function combins all the functions and gives us an 
    interface'''
    print('Choose a option from the following: ')
    print('''             1)Student Details
             2)Price Menu 
             3)Bill per Day 
             4)Mess Analysis
             5)Suggestions
             6)New Registeration''')
    n=input('Enter your choice: ')
    '''using if else statement to call different function as per user 
    choice'''
    if n=='1' :
        return student_details()
    elif n=='2' :
        return price_per_meal()
    elif n=='3' :
        return final_db()
    elif n=='4' :
        return Mess_analysis()
    elif n=='5' :
        return suggestions()
    elif n== '6':
        return new_registeration()

print(all_func()) 

    
    
    
    
    
    
    
    
    
    