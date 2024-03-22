from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
from tkinter import messagebox
from datetime import *
import time
from time import strftime
from trangchu import Face_Recognition_System
from trangchu import xuat

class Login(object):
    # hàm khởi tạo giao diện
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')#kích thước giao diện
        self.window.resizable(0, 0) #ko cho giao diện thu nhỏ
        self.window.state('zoomed') #giao diện hiển thị toàn màn hình
        self.window.title('Hệ Thống Đăng Nhập Trung Tâm') #tiêu đề của cửa sổ app
        self.window.iconbitmap('hinhanh\\222.ico')
        today = strftime("%d-%m-%Y")  # thời gian ngày-tháng-năm

        # =============biến kiểu string email,password============
        self.var_email = StringVar()
        self.var_password = StringVar()

        # ============================background image============================
        # ========================================================================
        self.bg_frame = Image.open('hinhanh\\quoc1.png')#khai báo biến bg_frame là ảnh background trong thư mục hinhanh\\background1.png
        photo = ImageTk.PhotoImage(self.bg_frame)# chuyển ảnh về lớp ImageTk
        self.bg_panel = Label(self.window, image=photo)#Khai báo biến bg_panel chứa ảnh photo
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')#Vị trí của lớp Label : chính giữa giao diện
        # ====== Login Frame =========================

        self.lgn_frame = Frame(self.window, bg='#F2C84B', width=950, height=600)
        self.lgn_frame.place(x=500, y=30)

        # ========================================================================
        # ========================================================
        # ======Hiện thị ngày====
        self.txt = today
        self.heading = Label(self.lgn_frame, text=self.txt, font=('times new roman', 25, "bold"), bg="#F2C84B",
                             fg='#006400',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=80, y=30, width=300, height=30)

        # ========================================================================
        # ============ Left Side Image ================================================
        # ========================================================================
        self.side_image = Image.open('hinhanh\\dino.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#F2C84B')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=100)

        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================
        self.sign_in_image = Image.open('hinhanh\\man.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#F2C84B')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=650, y=130)

        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
        self.sign_in_label = Label(self.lgn_frame, text="Đăng nhập", bg="#F2C84B", fg="#006400",
                                    font=("Arial", 25, "bold"))
        self.sign_in_label.place(x=630, y=240)

        # ========================================================================
        # ============================tài khoản====================================
        # ========================================================================
        self.username_label = Label(self.lgn_frame, text="Tài khoản", bg="#F2C84B", fg="#006400",
                                    font=("times new roman", 13, "bold"))
        self.username_label.place(x=550, y=300)

        self.txtuser = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#F2C84B", fg="#6b6a69",
                                    font=("times new roman ", 12, "bold"),textvariable=self.var_email)
        self.txtuser.place(x=580, y=335, width=270)

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#F2C84B", highlightthickness=0)
        self.username_line.place(x=550, y=359)
        # ===== Username icon =========
        self.username_icon = Image.open('hinhanh\\username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#F2C84B')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=332)

        # ========================================================================
        # ============================Nút đăng nhập================================
        # ========================================================================
        self.lgn_button = Image.open('hinhanh\\btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#F2C84B')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=550, y=450)
        self.login = Button(self.lgn_button_label, text='Đăng nhập',command=self.login,
                            font=("times new roman", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white')
        self.login.place(x=20, y=10)


        # =============check_button=============
        self.varcheck = IntVar()
        checkbtn = Checkbutton(self.lgn_frame, variable=self.varcheck,
                               font=("times new roman", 12), onvalue=1, offvalue=0 ,bg="#F2C84B"
                                )
        checkbtn.place(x=550, y=510)

        self.check_label = Label(self.lgn_frame, text="Đăng nhập bằng Admin", bg="#F2C84B", fg="#006400",relief=FLAT,
                                    font=("times new roman", 12, "bold"))
        self.check_label.place(x=580, y=513)

        # ========================================================================
        # ============================Mật khẩu====================================
        # ========================================================================
        self.password_label = Label(self.lgn_frame, text="Mật khẩu", bg="#F2C84B", fg="#006400",
                                    font=("times new roman", 13, "bold"))
        self.password_label.place(x=550, y=380)

        self.txtpass = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#F2C84B", fg="white",
                                    font=("times new roman", 12, "bold"), show="*",textvariable=self.var_password)
        self.txtpass.place(x=580, y=416, width=244)

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#F2C84B", highlightthickness=0)
        self.password_line.place(x=550, y=440)
        # ======== Password icon ================
        self.password_icon = Image.open('hinhanh\\password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#F2C84B')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=414)
        # ========= show/hide password ==================================================================
        #ảnh nút hiển thị password
        self.show_image = ImageTk.PhotoImage \
            (file='hinhanh\\show.png')

        #ảnh  nút ẩn password
        self.hide_image = ImageTk.PhotoImage \
            (file='hinhanh\\hide.png')

        #nút hiển thị password
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.showpass, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)

    def showpass(self):#hàm hiển thị mật khẩu
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=860, y=420)
        self.txtpass.config(show='')
    def show(self):
        """"""
        self.window.update()
        self.window.deiconify()
    def hide(self):#hàm ẩn mật khẩu dưới dạng ***
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.showpass, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)
        self.txtpass.config(show='*')

    #reset thông tin password_tài khoản
    def reset(self):
        self.var_email.set("")
        self.var_password.set("")
        self.varcheck.set(0)

    # hàm đăng nhập
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Lỗi !!","Vui lòng nhập đầy đủ thông tin")
        elif(self.varcheck.get()==1) :
            try:
                conn = mysql.connector.connect(host='localhost', user='root', password='', database='PhamTrongQuoc_2080600990',
                                               port='3306')
                my_cursor = conn.cursor()
                my_cursor.execute("select * from admin where Account=%s and Password=%s", (
                    self.var_email.get(),
                    self.var_password.get()
                ))
                row = my_cursor.fetchone()
                if row==None:
                    messagebox.showerror("Lỗi", "Sai tên đăng nhập, mật khẩu hoặc quyền đăng nhập")
                else:
                    xuat(str(0))
                    # # self.window.destroy()
                    # # import home
                    self.reset()
                    messagebox.showinfo("Thông báo","Bạn đã đăng nhập thành công với quyền chủ trung tâm")
                    self.window.withdraw()
                    # self.new_window = Toplevel(self.window)

                    self.app = Face_Recognition_System(self)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Lỗi", f"Due To:{str(es)}", parent=self)
        else:
            try:
                conn = mysql.connector.connect(host='localhost', user='root', password='', database='PhamTrongQuoc_2080600990',
                                               port='3306')
                my_cursor = conn.cursor()
                my_cursor.execute("select Teacher_id from teacher where Email=%s and Password=%s",(
                                        self.var_email.get(),
                                        self.var_password.get()
                ))
                row=my_cursor.fetchone()

                # print(row[0])
                if row==None:
                    messagebox.showerror("Lỗi", "Sai tên đăng nhập hoặc mật khẩu")
                else:
                    xuat(str(row[0]))
                    # self.window.destroy()
                    # import home
                    self.reset()
                    self.window.withdraw()
                    # self.new_window = Toplevel(self.window)
                    self.app = Face_Recognition_System(self)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Lỗi", f"Due To:{str(es)}", parent=self)





if __name__ == '__main__':
    window = Tk()  # tạo giao diện tkinter Tk() và gán nó vào biến window
    obj = Login(window)
    window.mainloop()  # hiển thị giao diện và bắt đầu nhận các sự kiện để xử lý.