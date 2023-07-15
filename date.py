### custom date class
class date:
    months = ['default','January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October'\
             ,'November', 'December']
    
    def __init__(self,day=0,month=0,year=0,format='%d/%m/%y', word=False):
        self.__day, self.__month, self.__year = self.__validate(day,month,year)
        self.format = format
        self.__word = word
        
        self.__evaluate_date()
    
    
    def __dayh(self, digit):
        if int(digit) == 1:
            return 'st'
        elif int(digit) == 2:
            return 'nd'
        elif int(digit) == 3:
            return 'rd'
        else:
            return 'th'
    
    def __str__(self):
        
        if self.__day == 0 and self.__month == 0 and self.__year == 0:
            return '0 CE'
        
        if self.__word:
            return self.months[int(self.__month)] + ' ' + self.__day + self.__dayh(str(self.__day)[-1]) + ', ' + self.__year
        return self.__day + self.format[2] + self.__month + self.format[5] +self.__year
    
    def __validate(self,dd,mm,yy):
        dd, mm, yy = dd,mm,yy
        
        ####validations follow####
        if len(str(dd)) > 2:
            raise ValueError('Invalid day value. Length exceeded.')
        
        if len(str(mm)) > 2:
            raise ValueError('Invalid month value. Length exceeded.')
        
        if len(str(yy)) < 4:
            raise ValueError('Invalid year value. Length exceeded.')
            
        max1=0
        if(mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12):
            max1=31
        elif(mm==4 or mm==6 or mm==9 or mm==11):
            max1=30
        elif(yy%4==0 and yy%100!=0 or yy%400==0):
            max1=29
        else:
            max1=28
        
        if mm<1 or mm>12:
            raise ValueError('Invalid month value. Accepted range [1,12]')
        elif dd<1 or dd>max1:
            raise ValueError('Invalid day value.')
        
        ####Validations end here#####
        return str(dd),str(mm),str(yy)
        
    
    def __evaluate_date(self):
        if len(self.__day) != 2:
            self.__day = '0' + self.__day
        if len(self.__month) != 2:
            self.__month = '0' + self.__month
    
    
    def toggle_word(self):
        if self.__word:
            self.__word = False
        else:
            self.__word = True
            
        return self
    
    def __getitem__(self, key):
        """
        Key reference:-
            name  | key 
            -------------
            day   | 'd', 'day', 0
            month | 'm', 'month', 1
            year  | 'y', 'year', 2
        """
        if key in ['d', 0, 'day', -3]:
            return self.__day
        elif key in ['m', 1, 'month', -2]:
            return self.__month
        elif key in ['y', 2, 'year', -1]:
            return self.__year
        else:
            raise ValueError("Key value is wrong.")
        
        
    def __setitem__(self, key, value):
        """
         Key reference:-
            name  | key 
            -------------
            day   | 'd', 'day', 0
            month | 'm', 'month', 1
            year  | 'y', 'year', 2
        """
        d = int(self.__day)
        m = int(self.__month)
        y = int(self.__year)
        
        if key in ['d', 0, 'day', -3]:
            self.__day, self.__month, self.__year = self.__validate(value, m, y)
        elif key in ['m', 1, 'month', -2]:
            self.__day, self.__month, self.__year = self.__validate(d, value, y)
        elif key in ['y', 2, 'year', -1]:
            self.__day, self.__month, self.__year = self.__validate(d, m, value)
        else:
            raise ValueError("Key value is wrong.")
        
        self.__evaluate_date()
        