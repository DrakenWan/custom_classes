### custom date class
class date:
    months = ['default','January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October'\
             ,'November', 'December']
    
    def __init__(self,day=0,month=0,year=0,format='%d/%m/%y', word=False):
        self.day, self.month, self.year = self.validate(day,month,year)
        self.format = format
        self.word = word
        
        self.evaluate_date()
    
    
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
        
        if self.day == 0 and self.month == 0 and self.year == 0:
            return '0 CE'
        if self.word:
            return self.months[int(self.month)] + ' ' + self.day + self.__dayh(str(self.day)[-1]) + ', ' + self.year
        return self.day + self.format[2] + self.month + self.format[5] +self.year
    
    def validate(self,dd,mm,yy):
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
        
    
    def evaluate_date(self):
        if len(self.day) != 2:
            self.day = '0' + self.day
        if len(self.month) != 2:
            self.month = '0' + self.month
    #def to_datetime(self,string, format='%d%m%y'):

##x = date(29,2,1992, format='%d.%m.%y', word=True)
##print(x)
