from tkinter import*
import mysql.connector
from PIL import ImageTk, Image
import requests
from io import BytesIO
import os
class NEWS:

            
      ##main class programee creating the 1st GUI
            
      def  __init__(self):
            self.conn=mysql.connector.connect(host="remotemysql.com",user="5bw7baLgbq",password="SpTDVAT9r9",database="5bw7baLgbq")
            self.mycursor=self.conn.cursor()
            self.root1=Tk()                
            #self.user_menu()
            
            self.index=0
            self.root1.title("web Form")
            self.root1.minsize(600,600)
            #self.root.maxsize(600,600)
            self.root1.configure(background="#00a65a")



            #font editing of the title
            self.Label1=Label(self.root1,text="WELCOME",bg="#00a65a",fg="#FFF")
            self.Label1.configure(font=("Algerian",22,"bold"))
            self.Label1.pack(pady=(30,10))

            temp="CHOSE ANY ONE OF THE FOLLOWING::"


            self.Label2=Label(self.root1,text=temp,bg="#00a65a",fg="#FFF")
            self.Label2.configure(font=("Garamond",15))
            self.Label2.pack(pady=(30,5))

            
            self.Label3=Label(self.root1,text="""1. REGISTER\n2. LOGIN\n3.EXIT\nEnter your choice""",bg="#00a65a",fg="#FFF")
            self.Label3.configure(font=("Garamond",15))
            self.Label3.pack(pady=(10,10))


            #input entry box
            self.user_input=Entry(self.root1)
            self.user_input.pack(ipadx=6,ipady=6)
           # print(self.user_input)

            self.email_save="ad"
            #button constrains
            self.click=Button(self.root1,text="OK",bg="#FFF",fg="#000",width=5,height=1,command=lambda:self.user_menu())
            self.click.pack(pady=(5,5))

            self.root1.mainloop()


      def __increment(self):
        self.index+=1
        if self.index > len(self.data['articles'])-1:
            self.index=len(self.data['articles'])
            self.result.configure(text="No more news!!")
            return
       
        self.__fetch()

      def __decrement(self):
            self.index-=1
            if self.index < 0:
                self.index=0
                self.result.configure(text="No more news!!")
                return
            self.__fetch()

      def __saved_list(self):
            self.root5=Tk()
            self.mycursor.execute("SELECT post,date FROM saved WHERE email LIKE '{}'".format(self.email_save))
            self.posts=self.mycursor.fetchall()
            list_items=""
            for i,item in enumerate(self.posts):
                  list_items+=str(i+1)+" : "+item[0]+"\n"
            #print(list_items)
            self.root5.title("Recent News")
            self.root5.minsize(800,600)
            #self.root.maxsize(800,600)
            self.root5.configure(background="#00a65a")
            self.label1=Label(self.root5,text="",bg="#00a65a",fg="#fff")
            self.label1.configure(font=("Constantia",15,"bold"))
            self.label1.pack(pady=(30,10))
            self.label1.configure(text=list_items,wraplength=400)
            self.s_opt=Entry(self.root5)
            self.s_opt.pack(ipadx=6,ipady=6)
            print(self.posts)
            self.click_opt=Button(self.root5,text="Fetch",bg="#fff",fg="#000",width=25,height=2,command=lambda:self.__fetch1(self.posts[int(self.s_opt.get())-1][0],self.posts[int(self.s_opt.get())-1][1]))
            self.click_opt.pack(pady=(10,20))
      

      def __fetch1(self,title,date):
            self.destroy()
            self.root5.destroy()
            self.root=Tk()
            print(title)
            print(date)
            url = ('http://newsapi.org/v2/everything?'
                   'qInTitle={0}&'
                   'from={1}&'
                   'sortBy=relevancy&'
                   'apiKey=459c1308caa3498db0759b2738ac912e').format(title,date)
            
            """
            url = ('http://newsapi.org/v2/top-headlines?'
                   'sources=bbc-news&'
                   'apiKey=459c1308caa3498db0759b2738ac912e')
            """
            response = requests.get(url)
            self.data=response.json()
            print(self.data)
            self.root.title("Recent News")
            self.root.minsize(800,600)
            #self.root.maxsize(800,600)
            self.root.configure(background="#00a65a")
            self.label1=Label(self.root,text=self.data['articles'][0]['publishedAt'][:10],bg="#00a65a",fg="#fff")
            self.label1.configure(font=("Constantia",22,"bold"))
            self.label1.pack(pady=(30,10))

            
            
           

            

            
            #self.click=Button(self.root,text="Fetch",bg="#fff",fg="#000",width=25,height=2,command=lambda:self.__fetch())
            #self.click.pack(pady=(10,20))
            
            
            """
            URL = "http://www.universeofsymbolism.com/images/ram-spirit-animal.jpg"
            u = urlopen(URL)
            raw_data = u.read()
            u.close()

            im = Image.open(BytesIO(raw_data))
            photo = ImageTk.PhotoImage(im)

            self.labelP = tk.Label(image=photo)
            self.labelP.image = photo
            self.labelP.pack()
            """
            print (self.data['articles'][0]['title'])

            self.result=Label(self.root,text="",bg="#00a65a",fg="#fff")
            self.result.configure(font=("Constantia",18,"bold"))
            self.result.pack(pady=(5,10))
        
            self.result.configure(text=self.data['articles'][0]['title']+"\n",wraplength=600)


            img_url = self.data['articles'][0]['urlToImage']
            response2 = requests.get(img_url)
            img_data = response2.content
            self.img = ImageTk.PhotoImage((Image.open(BytesIO(img_data)).resize((500,270),Image.ANTIALIAS)))
            #self.img=self.img.resize(200,200)
            panel = Label(self.root, image=self.img)
            panel.pack( expand="yes")

            self.result2=Label(self.root,text="",bg="#00a65a",fg="#fff")
            self.result2.configure(font=("Constantia",14,"bold"))
            self.result2.pack(pady=(5,10))
            self.result2.configure(text=self.data['articles'][0]['description'],wraplength=600)

            
            self.click1=Button(self.root,text="Back",bg="#fff",fg="#000",width=25,height=2,command=lambda:self.__fetch())
            self.click1.pack(pady=(10,20))
            """
            self.click2=Button(self.root,text="Previous News",bg="#fff",fg="#000",width=25,height=2,command=lambda:self.__decrement())
            self.click2.pack(pady=(10,20))
            self.click_s=Button(self.root,text="Save",bg="#fff",fg="#000",width=25,height=2,command=lambda:self.__save())
            self.click_s.pack(pady=(10,20))
            self.click3=Button(self.root,text="Exit",bg="#fff",fg="#000",width=25,height=2,command=lambda:self.destroy())
            self.click3.pack(pady=(10,20))
            """
      
        
      def __fetch(self):
            self.destroy()

            self.root=Tk()
            url = ('http://newsapi.org/v2/everything?'
                   'sources=bbc-news&'
                   'apiKey=459c1308caa3498db0759b2738ac912e')
            
            """
            url = ('http://newsapi.org/v2/top-headlines?'
                   'sources=bbc-news&'
                   'apiKey=459c1308caa3498db0759b2738ac912e')
            """
            response = requests.get(url)
            self.data=response.json()
            self.root.title("Recent News")
            self.root.minsize(800,600)
            #self.root.maxsize(800,600)
            self.root.configure(background="#00a65a")
            self.label1=Label(self.root,text=self.data['articles'][self.index]['publishedAt'][:10],bg="#00a65a",fg="#fff")
            self.label1.configure(font=("Constantia",22,"bold"))
            self.label1.pack(pady=(30,10))


            
           

            

            
            #self.click=Button(self.root,text="Fetch",bg="#fff",fg="#000",width=25,height=2,command=lambda:self.__fetch())
            #self.click.pack(pady=(10,20))
            
            
            print (self.data['articles'][self.index]['title'])

            self.result=Label(self.root,text="",bg="#00a65a",fg="#fff")
            self.result.configure(font=("Constantia",18,"bold"))
            self.result.pack(pady=(5,10))
        
            self.result.configure(text=self.data['articles'][self.index]['title']+"\n",wraplength=600)


            img_url = self.data['articles'][self.index]['urlToImage']
            response = requests.get(img_url)
            img_data = response.content
            self.img = ImageTk.PhotoImage((Image.open(BytesIO(img_data)).resize((500,270),Image.ANTIALIAS)))
            #self.img=self.img.resize(200,200)
            panel = Label(self.root, image=self.img)
            panel.pack( expand="yes")

            self.result2=Label(self.root,text="",bg="#00a65a",fg="#fff")
            self.result2.configure(font=("Constantia",14,"bold"))
            self.result2.pack(pady=(5,10))
            self.result2.configure(text=self.data['articles'][self.index]['description'],wraplength=600)


            self.click1=Button(self.root,text="Next News",bg="#fff",fg="#000",width=25,height=2,command=lambda:self.__increment())
            self.click1.pack(pady=(2,2))
            self.click2=Button(self.root,text="Previous News",bg="#fff",fg="#000",width=25,height=2,command=lambda:self.__decrement())
            self.click2.pack(pady=(2,2))
            self.click_s=Button(self.root,text="Save",bg="#fff",fg="#000",width=25,height=2,command=lambda:self.__save())
            self.click_s.pack(pady=(2,2))
            self.click3=Button(self.root,text="Exit",bg="#fff",fg="#000",width=25,height=2,command=lambda:self.destroy())
            self.click3.pack(pady=(2,2))
            self.click_test=Button(self.root,text="View Saved News",bg="#fff",fg="#000",width=25,height=2,command=lambda:self.__saved_list())
            self.click_test.pack(pady=(2,2))

      def __save(self):
            self.mycursor.execute("SELECT post FROM saved WHERE email LIKE '{}'".format(self.email_save))
            self.saved_post=self.mycursor.fetchall()
            self.test_title=(' '.join(self.data['articles'][self.index]['title'].split()[0:5])).replace("'","\\'")
            self.saved_post=tuple(map(lambda x:x[0],self.saved_post))
            if not self.data['articles'][self.index]['title'][0:20] in self.saved_post:
                  self.mycursor.execute("INSERT INTO saved (email,post,date) VALUES ('{}','{}','{}')".format(self.email_save , self.test_title , self.data['articles'][self.index]['publishedAt'][:10]))
                  self.conn.commit()


      def user_menu(self):
            x=self.user_input.get()
                        
            if x=="1":
                  self.register()
                 
            elif x=="2":
                  self.login()
             

            else:
                  self.Label2=Label(self.root1,text="BYE",bg="#00a65a",fg="#FFF")
                  self.Label2.configure(font=("Garamond",15))
                  self.Label2.pack(pady=(30,5))
                  self.root1.destroy()



                 
            
      def register(self):

            self.root1.destroy()                                              #destroy the 1st GUI
          
            self.root2=Tk()                                                         #creating the 2nd GUI
           
            

            ##format of 2nd GUI
            self.root2.title("Registration Form")
            self.root2.minsize(600,600)
            #self.root.maxsize(600,600)
            self.root2.configure(background="#00a65a")



            #font editing of the title
            self.Label1=Label(self.root2,text="REGISTRATION FORM",bg="#00a65a",fg="#FFF")
            self.Label1.configure(font=("Algerian",22,"bold"))
            self.Label1.pack(pady=(30,10))


            #creating the name label
            self.Label2=Label(self.root2,text="Enter your name",bg="#00a65a",fg="#FFF")
            self.Label2.configure(font=("Garamond",15))
            self.Label2.pack(pady=(10,5))
            self.user_name=Entry(self.root2)
            self.user_name.pack(ipadx=6,ipady=6)


            #creating the email label
            self.Label2=Label(self.root2,text="Enter your E-mail:",bg="#00a65a",fg="#FFF")
            self.Label2.configure(font=("Garamond",15))
            self.Label2.pack(pady=(10,5))
            self.user_email=Entry(self.root2)
            self.user_email.pack(ipadx=6,ipady=6)


            #creating the password label
            self.Label2=Label(self.root2,text="Enter your password:",bg="#00a65a",fg="#FFF")
            self.Label2.configure(font=("Garamond",15))
            self.Label2.pack(pady=(10,5))
            self.user_password=Entry(self.root2)
            self.user_password.pack(ipadx=6,ipady=6)

            self.click1=Button(self.root2,text="OK",bg="#FFF",fg="#000",width=5,height=1,command=lambda:self.registered())
            self.click1.pack(pady=(5,5))

            self.root2.mainloop()
            

      def registered(self):


            name=self.user_name.get()
            #print(name)
            x=len(name)
            #print(name)
            if (x==0):
                   self.root=Tk()

                   self.root.title("ERROR Form")
                   self.root.minsize(100,100)
                  #self.root.maxsize(600,600)
                   self.root.configure(background="red")
                              
                   self.Label3=Label(self.root,text="INVALID NAME",bg="red",fg="#FFF")
                   self.Label3.configure(font=("Garamond",15))
                   self.Label3.pack(pady=(10,5))
                   #print("x")
                   self.click2=Button(self.root,text="RESET",bg="#FFF",fg="#000",width=5,height=1,command=lambda:self.register1())
                   self.click2.pack(pady=(5,5))
                   self.root.mainloop()
                  
            name1=name.upper()
            email=self.user_email.get()
            f=0
            #print(email)
            for i in email:
                  if(i=="@"  or i=="."):
                        f+=1
            #print(f)
            if f!=2 :
                   self.root=Tk()
                   
                   self.root.title("ERROR Form")
                   self.root.minsize(100,100)
                  #self.root.maxsize(600,600)
                   self.root.configure(background="red")
                              
                   self.Label3=Label(self.root,text="INVALID EMAIL",bg="red",fg="#FFF")
                   self.Label3.configure(font=("Garamond",15))
                   self.Label3.pack(pady=(10,5))
                   #print("x")
                   self.click2=Button(self.root,text="RESET",bg="#FFF",fg="#000",width=5,height=1,command=lambda:self.register1())
                   self.click2.pack(pady=(5,5))
                   self.root.mainloop()
                   
            password=self.user_password.get()
            
            try:
                   self.mycursor.execute("INSERT INTO users (user_id,name,email,password) VALUES (NULL,'{}','{}','{}')".format(name1,email,password))

                   self.conn.commit()

            except Exception as e:
                   self.root=Tk()
                   
                   self.root.title("ERROR Form")
                   self.root.minsize(100,100)
                  #self.root.maxsize(600,600)
                   self.root.configure(background="red")
                              
                   self.Label3=Label(self.root,text="INVALID EMAIL",bg="red",fg="#FFF")
                   self.Label3.configure(font=("Garamond",15))
                   self.Label3.pack(pady=(10,5))
                   #print("x")
                   self.click2=Button(self.root,text="RESET",bg="#FFF",fg="#000",width=5,height=1,command=lambda:self.register1())
                   self.click2.pack(pady=(5,5))
                   self.root.mainloop()
                  



            
            self.root2.destroy()                      #destroyed the 2nd GUI

           
            self.root=Tk()                                  #creating the 3rd GUI


            #initials of 3rd GUI
            self.root.title("Registration Form")
            self.root.minsize(200,100)
            self.root.configure(background="#00a65a")



                  
            self.Label2=Label(self.root,text="Registered succesfully!!!!",bg="#00a65a",fg="#FFF")
            self.Label2.configure(font=("Garamond",20,"bold"))
            self.Label2.pack(pady=(10,5))

            self.click1=Button(self.root,text="OK",bg="#FFF",fg="#000",width=5,height=1,command=lambda:self.destroy())
            self.click1.pack(pady=(5,5))

            self.root.mainloop()


            
      #destroy  the GUI
      def destroy(self):
            self.root.destroy()



      def register1(self):
            #print("x")
            
            self.user_name.delete(first=0,last=100)
            self.user_email.delete(first=0,last=100)
            self.user_password.delete(first=0,last=100)
            
            self.root.destroy()

      def login2(self):
            #print("x")
            
            #self.user_name.delete(first=0,last=100)
            self.user_email.delete(first=0,last=100)
            self.user_password.delete(first=0,last=100)
            
            self.root.destroy()

         

      def login(self):

            self.root1.destroy()                      #destryoing the first GUI
            
            self.root2=Tk()                                 #creating  the 2nd GUI           
                              


            #framework of GUI
            self.root2.title("Login form")
            self.root2.minsize(600,600)
            self.root2.configure(background="#00a65a")



            #font editing of the title
            self.Label1=Label(self.root2,text="LOGIN FORM",bg="#00a65a",fg="#FFF")
            self.Label1.configure(font=("Algerian",22,"bold"))
            self.Label1.pack(pady=(30,10))


            
            #creating the emaillabel
            self.Label2=Label(self.root2,text="Enter your E-mail:",bg="#00a65a",fg="#FFF")
            self.Label2.configure(font=("Garamond",15))
            self.Label2.pack(pady=(10,5))
            self.user_email=Entry(self.root2)
            self.user_email.pack(ipadx=6,ipady=6)

            #creating the password label
            self.Label2=Label(self.root2,text="Enter your password:",bg="#00a65a",fg="#FFF")
            self.Label2.configure(font=("Garamond",15))
            self.Label2.pack(pady=(10,5))
            self.user_password=Entry(self.root2)
            self.user_password.pack(ipadx=6,ipady=6)

            self.click2=Button(self.root2,text="OK",bg="#FFF",fg="#000",width=5,height=1,command=lambda:self.logined())
            self.click2.pack(pady=(5,5))

            self.root2.mainloop()


      def logined(self):
            
            email=self.user_email.get()
            password=self.user_password.get()
            self.email_save=email

            self.mycursor.execute("SELECT * FROM users WHERE email LIKE '{}' and password LIKE '{}'".format(email,password))

            self.x=self.mycursor.fetchall()

            if(len(self.x)==0):
                   self.root=Tk()

                   self.root.title("ERROR Form")
                   self.root.minsize(100,100)
                  #self.root.maxsize(600,600)
                   self.root.configure(background="red")
                              
                   self.Label3=Label(self.root,text="INVALID DATA",bg="red",fg="#FFF")
                   self.Label3.configure(font=("Garamond",15))
                   self.Label3.pack(pady=(10,5))
                   #print("x")
                   self.click2=Button(self.root,text="RESET",bg="#FFF",fg="#000",width=5,height=1,command=lambda:self.login2())
                   self.click2.pack(pady=(5,5))
                   self.root.mainloop()

            self.root2.destroy()          #destroyed the 2nd GUI

            self.root=Tk()                      #creating the GUI

            
            #frame of GUI
            self.root.title("Login Form")
            self.root.minsize(200,100)
            self.root.configure(background="#00a65a")



                  
            self.Label2=Label(self.root,text="LOGIN Successfully!!!",bg="#00a65a",fg="#FFF")
            self.Label2.configure(font=("Garamond",20,"bold"))
            self.Label2.pack(pady=(10,5))

           
            
            self.Label2=Label(self.root,text="WELCOME",bg="#00a65a",fg="#FFF")
            self.Label2.configure(font=("Garamond",25))
            self.Label2.pack(pady=(10,5))
           
            y=self.x[0][1]

            self.Label2=Label(self.root,text=y,bg="#00a65a",fg="#FFF")
            self.Label2.configure(font=("Garamond",20))
            self.Label2.pack(pady=(10,5))

            self.z=self.x[0][0]

            self.Label2=Label(self.root,text="Your ID NO.:",bg="#00a65a",fg="#FFF")
            self.Label2.configure(font=("Garamond",20))
            self.Label2.pack(pady=(10,5))

            
            self.Label2=Label(self.root,text=self.z,bg="#00a65a",fg="#FFF")
            self.Label2.configure(font=("Garamond",20))
            self.Label2.pack(pady=(10,5))


            self.click1=Button(self.root,text="OK",bg="#FFF",fg="#000",width=5,height=1,command=lambda:self.__fetch())
            self.click1.pack(pady=(5,5))
            
ob=NEWS()
