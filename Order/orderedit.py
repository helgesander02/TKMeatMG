import customtkinter
from tkcalendar import DateEntry
from PIL import Image
from sqlalchemy.orm import Session

from sql_app.database import engine
from sql_app.crud import *
import tkinter as tk
from .floatspinbox import FloatSpinbox,sum_Frame

class edit_order(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        # self.edit_top_=edit_top(self,fg_color = ("#DDDDDD"))
        self.edit_top_=customtkinter.CTkFrame(self,fg_color = ("#DDDDDD"))
        for i in range(7):
            self.edit_top_.columnconfigure(i,weight=1)
        self.ph_label=customtkinter.CTkLabel(self.edit_top_, text="電話",text_color='black')
        self.phone=customtkinter.CTkEntry(self.edit_top_, placeholder_text="電話",fg_color = ("#DDDDDD"),text_color='black')
        self.ph_label.grid(row=0,column=0,padx=30,pady=5)
        self.phone.grid(row=0, column=1,padx=30,pady=5)
        self.path_label=customtkinter.CTkLabel(self.edit_top_, text="通路",text_color='black')
        self.path=customtkinter.CTkComboBox(self.edit_top_,values=["option 1", "option 2"],fg_color = ("#DDDDDD"),text_color='black')
        self.path_label.grid(row=1,column=0,padx=30,pady=5)
        self.path.grid(row=1,column=1,padx=30,pady=5)
        self.pick_up_label=customtkinter.CTkLabel(self.edit_top_, text="取貨方式",text_color='black')
        self.pick_up=customtkinter.CTkComboBox(self.edit_top_,values=["option 1", "option 2"],fg_color = ("#DDDDDD"),text_color='black')
        self.pick_up_label.grid(row=2,column=0,padx=30,pady=5)
        self.pick_up.grid(row=2,column=1,padx=30,pady=5)
        self.date_label=customtkinter.CTkLabel(self.edit_top_, text="日期",text_color='black')
        self.date_=DateEntry(self.edit_top_,selectmode='day')
        self.date_label.grid(row=0,column=2,padx=30,pady=5)
        self.date_.grid(row=0,column=3,padx=30,pady=5)
        self.money_label=customtkinter.CTkLabel(self.edit_top_, text="金額",text_color='black')
        self.money=customtkinter.CTkEntry(self.edit_top_, placeholder_text="",fg_color = ("#DDDDDD"),text_color='black')
        self.money2=customtkinter.CTkEntry(self.edit_top_, placeholder_text="",fg_color = ("#DDDDDD"),text_color='black')
        self.money_label.grid(row=0,column=4,padx=30,pady=5)
        self.money.grid(row=0,column=5,padx=30,pady=5)
        self.money2.grid(row=1,column=5,padx=30,pady=5)
        reset_bt=customtkinter.CTkButton(self.edit_top_,text='重新設定', width=150, height=40,
                                                        fg_color=("#5b5a5a"),
                                                        font=("microsoft yahei", 18, 'bold'),
                                                        )
        reset_bt.grid(row=0,column=6,padx=30,pady=5)
        search=customtkinter.CTkButton(self.edit_top_,text='確定查詢', width=150, height=40,
                                                        fg_color=("#5b5a5a"),
                                                        font=("microsoft yahei", 18, 'bold'),
                                                        command=lambda: self.search_od_list(phone=self.phone.get(),pick_up=self.pick_up.get(),date_=self.date_.get_date(),money1=self.money.get(),money2=self.money2.get()))
        search.grid(row=1,column=6,padx=30,pady=5)  
     
        self.edit_top_.pack(fill='x',padx=30,pady=5)
        self.ol=order_List(self,phone='',pick_up='',date_='',money1='',money2='',fg_color = ("#DDDDDD"))
        self.ol.pack(fill='x',padx=30,pady=5)
    def search_od_list(self,phone,pick_up,date_,money1,money2):
        self.ol.pack_forget()
        self.ol=order_List(self,phone=phone,pick_up=pick_up,date_=date_,money1=money1,money2=money2,fg_color = ("#DDDDDD"))
        self.ol.pack(fill='x',padx=30,pady=5)
    def delete_(self):
        pass
class order_List(customtkinter.CTkFrame):
    def __init__(self, master,phone,pick_up,date_,money1,money2, **kwargs):
        super().__init__(master, **kwargs)
        self.image = customtkinter.CTkImage(light_image=Image.open("image\\user.png"),
                                  dark_image=Image.open("image\\user.png"),
                                  size=(30, 30))
        self.info = customtkinter.CTkImage(light_image=Image.open("image\\information-button.png"),
                                  dark_image=Image.open("image\\information-button.png"),
                                  size=(30, 30))
        self.edit_photo = customtkinter.CTkImage(light_image=Image.open("image\\pencil.png"),
                                  dark_image=Image.open("image\\pencil.png"),
                                  size=(30, 30))
        self.delete_photo = customtkinter.CTkImage(light_image=Image.open("image\\close.png"),
                                  dark_image=Image.open("image\\close.png"),
                                  size=(30, 30))        
        try:
            self.od_l={}
            order_list=search_od_(db=Session(engine),phone=phone,pick_up=pick_up,date_=date_,money1=money1,money2=money2)
            for i in order_list:
                if i.order_number in self.od_l:
                    self.od_l[i.order_number][4]+=f',{i.p_ID_.product_Name}'
                    self.od_l[i.order_number][6]+=i.count*i.p_ID_.product_Price
                else:
                    self.od_l[i.order_number]=[i.M_ID_.Phone,i.od_id,i.pick_up_date,i.pick_up,i.p_ID_.product_Name,i.pick_up_tf,i.count*i.p_ID_.product_Price]
        except:
            self.od_l={}
        self.c=customtkinter.CTkFrame(self,fg_color = ("#DDDDDD"))
        for i in range(9):
            self.c.columnconfigure(i,weight=1)
        self.c.columnconfigure(4,weight=2)
        a=customtkinter.CTkLabel(self.c,text='會員資訊',fg_color = ("#DDDDDD"),text_color='black')
        a.grid(row=0,column=0)
        a=customtkinter.CTkLabel(self.c,text='訂單資訊',fg_color = ("#DDDDDD"),text_color='black')
        a.grid(row=0,column=1)
        a=customtkinter.CTkLabel(self.c,text='取貨日期',fg_color = ("#DDDDDD"),text_color='black')
        a.grid(row=0,column=2) 
        a=customtkinter.CTkLabel(self.c,text='取貨方式',fg_color = ("#DDDDDD"),text_color='black')
        a.grid(row=0,column=3) 
        a=customtkinter.CTkLabel(self.c,text='訂單項目',fg_color = ("#DDDDDD"),text_color='black')
        a.grid(row=0,column=4)
        a=customtkinter.CTkLabel(self.c,text='是否取貨',fg_color = ("#DDDDDD"),text_color='black')
        a.grid(row=0,column=5)
        a=customtkinter.CTkLabel(self.c,text='金額',fg_color = ("#DDDDDD"),text_color='black')
        a.grid(row=0,column=6)
        a=customtkinter.CTkLabel(self.c,text='編輯',fg_color = ("#DDDDDD"),text_color='black')
        a.grid(row=0,column=7)
        a=customtkinter.CTkLabel(self.c,text='刪除',fg_color = ("#DDDDDD"),text_color='black')
        a.grid(row=0,column=8)
        
        i=1
        def gen_cmd1(i,l):return lambda:self.edit_(i,l)
        def gen_cmd(i):return lambda:self.delete(i)
        def get_user(i):return lambda:self.get_u(i)
        def get_od_(i):return lambda:self.get_o(i)
        for key,value in self.od_l.items():
            a=customtkinter.CTkButton(self.c,image=self.image,hover=False,text='',fg_color = ("#DDDDDD"),text_color='black',command=get_user(value[0]))
            # a=customtkinter.CTkLabel(self.c,text=f'{value[0]}',fg_color = ("#DDDDDD"),text_color='black')
            a.grid(row=i,column=0)
            a=customtkinter.CTkButton(self.c,image=self.info,hover=False,text='',fg_color = ("#DDDDDD"),text_color='black',command=get_od_(value[1]))
            a.grid(row=i,column=1)
            a=customtkinter.CTkLabel(self.c,text=f'{value[2]}',fg_color = ("#DDDDDD"),text_color='black')
            a.grid(row=i,column=2) 
            a=customtkinter.CTkLabel(self.c,text=f'{value[3]}',fg_color = ("#DDDDDD"),text_color='black')
            a.grid(row=i,column=3) 
            a=customtkinter.CTkLabel(self.c,text=f'{value[4]}',fg_color = ("#DDDDDD"),text_color='black')
            a.grid(row=i,column=4)
            a=customtkinter.CTkLabel(self.c,text=f'{value[5]}',fg_color = ("#DDDDDD"),text_color='black')
            a.grid(row=i,column=5)
            a=customtkinter.CTkLabel(self.c,text=f'{value[6]}',fg_color = ("#DDDDDD"),text_color='black')
            a.grid(row=i,column=6)
            a=customtkinter.CTkButton(self.c,image=self.edit_photo,hover=False,text='',fg_color = ("#DDDDDD"),text_color='black',command=gen_cmd1(key,value[0]))
            a.grid(row=i,column=7)
            a=customtkinter.CTkButton(self.c,image=self.delete_photo,hover=False,text='',fg_color = ("#DDDDDD"),text_color='black',command=gen_cmd(key))
            a.grid(row=i,column=8)
            i+=1
        self.c.pack(fill='x')
        self.toplevel_window = None
    def get_o(self,i):
        
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = info_ToplevelWindow(self,od=i)  
            self.toplevel_window.attributes('-topmost','true')   
        else:
            self.toplevel_window.focus() 
    def get_u(self,i):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = profile_ToplevelWindow(self,phone=i)  
            self.toplevel_window.attributes('-topmost','true')   
        else:
            self.toplevel_window.focus()        
    def edit_(self,i,l):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = edit_ToplevelWindow(self,key=i,M_Name=l)   
            self.toplevel_window.attributes('-topmost','true')   
        else:
            self.toplevel_window.focus()        
    def delete(self,i):
        delete_od(Session(engine),i)
        del self.od_l[i]
        self.c.pack_forget()
        self.c=customtkinter.CTkFrame(self,fg_color = ("#DDDDDD"))
        for i in range(9):
            self.c.columnconfigure(i,weight=1)
        self.c.columnconfigure(4,weight=2)
        a=customtkinter.CTkLabel(self.c,text='會員資訊',fg_color = ("#DDDDDD"),text_color='black')
        a.grid(row=0,column=0)
        a=customtkinter.CTkLabel(self.c,text='訂單資訊',fg_color = ("#DDDDDD"),text_color='black')
        a.grid(row=0,column=1)
        a=customtkinter.CTkLabel(self.c,text='取貨日期',fg_color = ("#DDDDDD"),text_color='black')
        a.grid(row=0,column=2) 
        a=customtkinter.CTkLabel(self.c,text='取貨方式',fg_color = ("#DDDDDD"),text_color='black')
        a.grid(row=0,column=3) 
        a=customtkinter.CTkLabel(self.c,text='訂單項目',fg_color = ("#DDDDDD"),text_color='black')
        a.grid(row=0,column=4)
        a=customtkinter.CTkLabel(self.c,text='是否取貨',fg_color = ("#DDDDDD"),text_color='black')
        a.grid(row=0,column=5)
        a=customtkinter.CTkLabel(self.c,text='金額',fg_color = ("#DDDDDD"),text_color='black')
        a.grid(row=0,column=6)
        a=customtkinter.CTkLabel(self.c,text='編輯',fg_color = ("#DDDDDD"),text_color='black')
        a.grid(row=0,column=7)
        a=customtkinter.CTkLabel(self.c,text='刪除',fg_color = ("#DDDDDD"),text_color='black')
        a.grid(row=0,column=8)
        
        i=1
        def gen_cmd1(i,l):return lambda:self.edit_(i,l)
        def gen_cmd(i):return lambda:self.delete(i)
        def get_user(i):return lambda:self.get_u(i)
        def get_od_(i):return lambda:self.get_o(i)
        for key,value in self.od_l.items():
            a=customtkinter.CTkButton(self.c,image=self.image,hover=False,text='',fg_color = ("#DDDDDD"),text_color='black',command=get_user(value[0]))
            a.grid(row=i,column=0)
            a=customtkinter.CTkButton(self.c,image=self.info,hover=False,text='',fg_color = ("#DDDDDD"),text_color='black',command=get_od_(value[1]))
            a.grid(row=i,column=1)
            a=customtkinter.CTkLabel(self.c,text=f'{value[2]}',fg_color = ("#DDDDDD"),text_color='black')
            a.grid(row=i,column=2) 
            a=customtkinter.CTkLabel(self.c,text=f'{value[3]}',fg_color = ("#DDDDDD"),text_color='black')
            a.grid(row=i,column=3) 
            a=customtkinter.CTkLabel(self.c,text=f'{value[4]}',fg_color = ("#DDDDDD"),text_color='black')
            a.grid(row=i,column=4)
            a=customtkinter.CTkLabel(self.c,text=f'{value[5]}',fg_color = ("#DDDDDD"),text_color='black')
            a.grid(row=i,column=5)
            a=customtkinter.CTkLabel(self.c,text=f'{value[6]}',fg_color = ("#DDDDDD"),text_color='black')
            a.grid(row=i,column=6)
            a=customtkinter.CTkButton(self.c,text='編輯',fg_color = ("#DDDDDD"),text_color='black',command=gen_cmd1(key,value[0]))
            a.grid(row=i,column=7)
            a=customtkinter.CTkButton(self.c,text='刪除',fg_color = ("#DDDDDD"),text_color='black',command=gen_cmd(key))
            a.grid(row=i,column=8)
            i+=1
        self.c.pack(fill='x')
class info_ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args,od, **kwargs):
        super().__init__(*args, **kwargs)
        self.image = customtkinter.CTkImage(light_image=Image.open("image\\user.png"),
                                  dark_image=Image.open("image\\user.png"),
                                  size=(100, 100))
        self.geometry("400x500")
        self.columnconfigure((0,1),weight=1)
        self.rowconfigure((3,4),weight=2)
        bt=customtkinter.CTkLabel(self,image=self.image,text='')
        
        od_=get_od_info(Session(engine),od_nb=od)    
        edit_n=customtkinter.CTkLabel(self,text='訂單編號：',text_color='black')
        edit_n1=customtkinter.CTkLabel(self,text='通路：',text_color='black')
        edit_n2=customtkinter.CTkLabel(self,text='備註：',text_color='black')
        
        # edit_n4=customtkinter.CTkLabel(self,text='廠商編號',text_color='black')
        edit_nL=customtkinter.CTkLabel(self,text=f'{od_.od_id}',text_color='black')
        edit_n1L=customtkinter.CTkLabel(self,text=f'{od_.pick_up}',text_color='black')
        edit_n2L=customtkinter.CTkLabel(self,text=f'{od_.Remark}',text_color='black')
        
        bt.grid(row=0,column=0,columnspan=2,pady=20)
        edit_n.grid(row=1,column=0)#姓名
        edit_n1.grid(row=2,column=0)#電話
        edit_n2.grid(row=3,column=0)#地址
        
        
        edit_nL.grid(row=1,column=1)#姓名
        edit_n1L.grid(row=2,column=1)#電話
        edit_n2L.grid(row=3,column=1)#地址
class profile_ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args,phone, **kwargs):
        super().__init__(*args, **kwargs)
        self.image = customtkinter.CTkImage(light_image=Image.open("image\\user.png"),
                                  dark_image=Image.open("image\\user.png"),
                                  size=(100, 100))
        self.geometry("400x500")
        self.columnconfigure((0,1),weight=1)
        self.rowconfigure((3,4),weight=2)
        bt=customtkinter.CTkLabel(self,image=self.image,text='')
        user=get_user(db=Session(engine),user_phone=phone)    
        edit_n=customtkinter.CTkLabel(self,text='會員編號：',text_color='black')
        edit_n1=customtkinter.CTkLabel(self,text='會員姓名：',text_color='black')
        edit_n2=customtkinter.CTkLabel(self,text='地址：',text_color='black')
        edit_n3=customtkinter.CTkLabel(self,text='備註：',text_color='black')
        # edit_n4=customtkinter.CTkLabel(self,text='廠商編號',text_color='black')
        edit_nL=customtkinter.CTkLabel(self,text=f'{user.ID}',text_color='black')
        edit_n1L=customtkinter.CTkLabel(self,text=f'{user.Name}',text_color='black')
        edit_n2L=customtkinter.CTkLabel(self,text=f'{user.Address}',text_color='black')
        edit_n3L=customtkinter.CTkLabel(self,text=f'{user.Remark}',text_color='black')
        bt.grid(row=0,column=0,columnspan=2,pady=20)
        edit_n.grid(row=1,column=0)#姓名
        edit_n1.grid(row=2,column=0)#電話
        edit_n2.grid(row=3,column=0)#地址
        edit_n3.grid(row=4,column=0)#備註
        
        edit_nL.grid(row=1,column=1)#姓名
        edit_n1L.grid(row=2,column=1)#電話
        edit_n2L.grid(row=3,column=1)#地址
        edit_n3L.grid(row=4,column=1)#備註
class edit_ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args,key,M_Name, **kwargs):
        super().__init__(*args, **kwargs)
        self.buy_photo = customtkinter.CTkImage(light_image=Image.open("image\\cart.png"),
                                  dark_image=Image.open("image\\cart.png"),
                                  size=(30, 30))        
        od=get_edit_od(Session(engine),key,M_Name)
        self.key=key
        self.M_Name=M_Name
        self.geometry("1000x900")
        self.columnconfigure((0,1),weight=1)
        self.input_top_=customtkinter.CTkFrame(self, fg_color = ("#DDDDDD"))
        self.input_top_.columnconfigure(5,weight=5)
        for i in range(6):
            self.columnconfigure(i,weight=1)
        self.ph_label=customtkinter.CTkLabel(self.input_top_, text="電話",text_color='black')
        self.phone=customtkinter.CTkEntry(self.input_top_, placeholder_text="電話",fg_color = ("#DDDDDD"),text_color='black')
        self.phone.insert(tk.END,'' if od[0].phone==None else od[0].phone)
        self.ph_label.grid(row=0,column=0,padx=30,pady=5)
        self.phone.grid(row=0, column=1,padx=30,pady=5)
        self.path_label=customtkinter.CTkLabel(self.input_top_, text="通路",text_color='black')
        self.path=customtkinter.CTkComboBox(self.input_top_,values=["option 1", "option 2"],fg_color = ("#DDDDDD"),text_color='black')
        self.path_label.grid(row=1,column=0,padx=30,pady=5)
        self.path.grid(row=1,column=1,padx=30,pady=5)
        self.pick_up_label=customtkinter.CTkLabel(self.input_top_, text="取貨方式",text_color='black')
        self.pick_up=customtkinter.CTkComboBox(self.input_top_,values=["現場", "取貨2"],fg_color = ("#DDDDDD"),text_color='black')
        self.pick_up.set(od[0].pick_up)
        self.pick_up_label.grid(row=2,column=0,padx=30,pady=5)
        self.pick_up.grid(row=2,column=1,padx=30,pady=5)
        self.date_label=customtkinter.CTkLabel(self.input_top_, text="取貨日期",text_color='black')
        self.date_=DateEntry(self.input_top_,selectmode='day')
        self.date_.set_date(od[0].pick_up_date)
        self.date_label.grid(row=0,column=2,padx=30,pady=5)
        self.date_.grid(row=0,column=3,padx=30,pady=5)
        self.Remark_label=customtkinter.CTkLabel(self.input_top_, text="備註",text_color='black')
        self.Remark_label.grid(row=0,column=4,padx=30,pady=5)
        self.Remark_textbox = customtkinter.CTkTextbox(self.input_top_, corner_radius=0,fg_color='white',border_color='black',text_color='black',border_width=1)
        self.Remark_textbox.insert(tk.END,'' if od[0].Remark==None else od[0].Remark)
        self.Remark_textbox.grid(row=0, column=5,rowspan=3,padx=30,pady=5,sticky='we')        
        # self.input_top_=input_top(self, fg_color = ("#DDDDDD")) 
        self.input_top_.pack(fill='x',padx=30,pady=5)
        
        self.product_=customtkinter.CTkFrame(self, fg_color = ("#DDDDDD"))
        prodcuts=get_all_products(Session(engine))
        self.toplevel_window = None
        self.bt_group={}
        self.buy_list={}
        for i in od:
            self.buy_list[i.p_ID_.product_Name]=[i.count,i.p_ID_.product_Price]
        self.a_frame=customtkinter.CTkFrame(self.product_,fg_color = ("#DDDDDD"))
        for i in range(len(prodcuts)):
            self.a_frame.columnconfigure(i,weight=1)
        def gen_cmd(i):return lambda:self.buy_bt_click(i)
        for i in range(len(prodcuts)):
            label_Name=customtkinter.CTkLabel(self.a_frame,text=prodcuts[i].product_Name,text_color='black')
            label_Name.grid(row=i,column=0,padx=30,sticky='w')
            label_Weight=customtkinter.CTkLabel(self.a_frame,text=prodcuts[i].product_Weight,text_color='black')
            label_Weight.grid(row=i,column=1,padx=30)
            label_price=customtkinter.CTkLabel(self.a_frame,text=f'{prodcuts[i].product_Price}元',text_color='black')
            label_price.grid(row=i,column=2,padx=30)
            
            spinbox_1 = FloatSpinbox(self.a_frame, width=150, step_size=1)
            self.bt_group[prodcuts[i].product_Name]=[spinbox_1,prodcuts[i].product_Price]
            spinbox_1.grid(row=i,column=4,pady=0)
            buy_button=customtkinter.CTkButton(self.a_frame,image=self.buy_photo,hover=False,  fg_color = ("#DDDDDD"), text="",command=gen_cmd(prodcuts[i].product_Name))
            buy_button.grid(row=i,column=5, padx=30, pady=0)
            
        self.a_frame.pack(side='left',anchor='n',fill='x',expand=1)
        self.sum_frame_=sum_Frame(self.product_,a='',buy_list=self.buy_list,bt_group=self.bt_group,  fg_color = ("#EEEEEE"))
        self.sum_frame_.reset_bt.configure(command=self.reset_)
        self.sum_frame_.confirm_bt.configure(command=self.add_od)
        self.sum_frame_.pack(side='right',anchor='n',fill='both')        
        # self.product_=product_Frame(self, fg_color = ("#DDDDDD"))
        self.product_.pack(fill='both',expand=1,padx=30,pady=5)
    def add_od(self):
        edit_order_(db=Session(engine),phone=self.phone.get(),Pick_up=self.pick_up.get(),remark=self.Remark_textbox.get(1.0,'end'),product_=self.buy_list,m_id='1',date_=self.date_.get_date(),key=self.key,M_name=self.M_Name)
        self.sum_frame_.pack_forget()
        self.sum_frame_=sum_Frame(self.product_,a='',buy_list=self.buy_list,bt_group=self.bt_group,  fg_color = ("#EEEEEE"))
        self.sum_frame_.reset_bt.configure(command=self.reset_)
        self.sum_frame_.pack(side='right',anchor='n',fill='both')
        self.destroy()
    def buy_bt_click(self,a):
        self.sum_frame_.pack_forget()
        self.sum_frame_=sum_Frame(self.product_,a=a,buy_list=self.buy_list,bt_group=self.bt_group,  fg_color = ("#EEEEEE"))
        self.sum_frame_.reset_bt.configure(command=self.reset_)
        self.sum_frame_.confirm_bt.configure(command=self.add_od)
        self.sum_frame_.pack(side='right',anchor='n',fill='both')
        self.buy_list=self.sum_frame_.buy_list   
    def reset_(self):
        self.buy_list={}
        self.sum_frame_.pack_forget()
        self.sum_frame_=sum_Frame(self.product_,a='',buy_list=self.buy_list,bt_group=self.bt_group,  fg_color = ("#EEEEEE"))
        self.sum_frame_.reset_bt.configure(command=self.reset_)
        self.sum_frame_.confirm_bt.configure(command=self.add_od)
        self.sum_frame_.pack(side='right',anchor='n',fill='both')  