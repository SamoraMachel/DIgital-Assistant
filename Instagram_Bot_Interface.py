from tkinter import *
from  Instagram_Bot import InstaBot as Bot
from tkinter import messagebox as msg

class Interface:
    def __init__(self):
        self.app = Tk()
        self.app.title("Instagram Bot")
        self.app.resizable(False, False)
    
    def main(self):
        self.max_people = IntVar()
        self.max_likes = IntVar()
        self.people_over = IntVar()
        
        # Sector for entering the maximum amount of people to follow
        Label(self.app, text="Maximum people to follow: ").grid(row=0, column=0, sticky='w')
        Entry(self.app, textvariable=self.max_people).grid(row=1, column=0, pady=4, sticky='w')

        # Sector for entering the maximum likes
        # to give a single person
        Label(self.app, text="Maximum likes for a single person: ").grid(row=2, column=0, sticky='w')
        Entry(self.app, textvariable=self.max_likes).grid(row=3, column=0, pady=4, sticky='w')


        # Sector for disallowing follow of people
        # past 
        Label(self.app, text="Disallow follow of people past: ").grid(row=4, column=0, sticky='w')
        Entry(self.app, textvariable=self.people_over).grid(row=5, column=0, pady=4, sticky='w')
    
        Button(self.app, text="Start ", command=self.follow).grid(row=6, column=1, pady=3, sticky='e')
        Button(self.app, text="Close", command=lambda :exit(4) ).grid(row=7, column=1, pady=3, sticky='e')

    def follow(self):
        try:
            max_people = self.max_people.get()
            max_likes = self.max_likes.get()
            people_over = self.people_over.get()
        except Exception as e:
            print(e)
            msg.showerror("InputError", "{error}".format(error=e))
            exit(4)
        
        if max_people > 200: 
            msg.showinfo("Risk 101", "Following past 200 people \nmight put your account at \nrisk of being blocked \nfor some days")
            torisk = msg.askyesno("Risk 101", "Are you willing to \n take the risk?")
            if torisk:
                InstaBot = Bot()
                InstaBot.LogIn()
                InstaBot.Suggested_Nav()
                InstaBot.people(max_people)
                InstaBot.Follow_and_view_people(max_likes, people_over)
            else:
                pass
        else:
            InstaBot = Bot()
            InstaBot.LogIn()
            InstaBot.Suggested_Nav()
            InstaBot.people(max_people)
            InstaBot.Follow_and_view_people(max_likes, people_over)
        


if __name__ == '__main__':
    bot = Interface()
    bot.main()
    bot.app.mainloop()


