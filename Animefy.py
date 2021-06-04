from tkinter import *
import webbrowser as web
            
from tkinter import ttk




window = Tk()
window.title("All Search Anime")


window.resizable(False, False)
#window.iconbitmap("Animefy.ico")   #Works better on windows machine



file_ = open('anime.fav','a+')
file_.close()


def refresh():
    global anime_list
    with open('anime.fav', 'r+') as _file:
        anime_list = _file.readlines()
    _file.close()

    return anime_list

refresh()
#Add functionanlity so to open the browser directly to the site seleced by the user
def Browser():
    if BrowseOption.get() != '' and AnimeVar.get() != '':
        #get the value stored in the varible typed ny the user 
        anime = AnimeVar.get()
        #convert the value typed by the user to a better format to be used to searching 
        anime = anime.lower()
        anime = anime.replace(" ", "-")
        if 'gogoanime' in BrowseOption.get():
            web.open("https://%s/%s/" % (BrowseOption.get(), anime))
        else:
            web.open("https://%s/%s" % (BrowseOption.get(), anime))
    else:
        msg.showerror('Error','Please input a anime and choose a site\nbefore pressing search')
        # label = Label(window, text="Please select a site and browser before clicking search", fg='red')
        # label.grid(row=100,column=0, columnspan=3)


anime = [
    'Naruto',
    'Naruto Shippuden',
    'Keja no Manga',
    'Boruto',
    'Black Clover',
    'Love is war',
    'Demon Slayer'
]




def AddFavorite():
    favourite = open('anime.fav', 'r+')
    list_ = favourite.readlines()
    if AnimeEntry.get() == "":
        favourite.close()
        return msg.showerror('Error', 'Cannot add an Empty Entry to Favorites')
    if AnimeEntry.get() not in list_:
        favourite = open('anime.fav', 'a+')
        favourite.write(AnimeEntry.get()+"\n")
        msg.showinfo('Favourite List', ('%s\nAdded succesfuly to favorite list' % (AnimeEntry.get())))
        msg.showinfo('Favourite List', ('Please Refresh to Update the list'))
    else:
        msg.showinfo('Favourite List', ('%s\nis already in the favorite list' % (AnimeEntry.get())))
    favourite.close()
    refresh()


def RemoveFavorite():
    try:
        favourite = open('anime.fav', 'r+')
        list_ = favourite.readlines()
    except:
        return msg.showinfo('Favorite', 'You have no Favourite List')
    favourite.close()

    if AnimeEntry.get() == "":
        return msg.showerror('Error', 'Cannot Remove an Empty Entry from Favorites')
    
    if AnimeEntry.get() in list_:
        list_.remove(AnimeEntry.get())
        favourite = open('anime.fav', 'w')
        for i in list_:
            favourite.write(i)
        msg.showinfo('Favourite List',('%s\nsuccessfully removed from the Favorite list' % (AnimeEntry.get())))
        msg.showinfo('Favourite List', ('Please Refresh to Update the list'))
        favourite.close()
    else:
        return msg.showinfo('Favorite', ('%s\nis not in the favourite list' % (AnimeEntry.get())))
    favourite.close()
    refresh()


AnimeVar = StringVar()
AnimeEntry  = ttk.Combobox(window ,font=("Caladea", 10), textvar=AnimeVar, value=anime_list)
AnimeEntry.focus()
AnimeEntry.grid(row=0,column=0,ipadx=120, ipady=4, columnspan=2)


SearchButton = Button(window,text="Search",font=('Maiandra GD', 9, 'underline','bold'), relief='raised', command=Browser)
SearchButton.grid(row=0,column=2)
BrowseOption = StringVar()


#Create radio button of the various sites for the user to choose from 
BrOpt1 = Radiobutton(window, variable=BrowseOption, text='GoGoanime', value='www10.gogoanime.io/category', anchor='n')
BrOpt1.grid(sticky=W, row=1, column=0)
BrOpt1.deselect()

BrOpt2 = Radiobutton(window, variable=BrowseOption, text='KissAnime', value='kissanimefree.net', anchor='n')
BrOpt2.grid(sticky=W, row=1, column=1)
BrOpt2.deselect()

BrOpt3 = Radiobutton(window, variable=BrowseOption, text='Anime Freak', value='www.animefreak.tv/watch', anchor='n')
BrOpt3.grid(sticky=W, row=2, column=0)
BrOpt3.deselect()

BrOpt4 = Radiobutton(window, variable=BrowseOption, text='Animepahe', value='animepahe.com/anime', anchor='n')
BrOpt4.grid(sticky=W, row=2, column=1)
BrOpt4.deselect()

BrOpt5 = Radiobutton(window, variable=BrowseOption, text='CrunchyRoll', value='www.crunchyroll.com', anchor='n')
BrOpt5.grid(sticky=W, row=3, column=0)
BrOpt5.deselect()

BrOpt6 = Radiobutton(window, variable=BrowseOption, text='9Anime', value='9anime.xyz/watch', anchor='n')
BrOpt6.grid(sticky=W, row=3, column=1)
BrOpt6.deselect()

FavoritesFrame = ttk.LabelFrame(window, text="Favourites", padding=5) 
FavoritesFrame.grid(row=1, column=2, rowspan=3)

FavouriteButton = Button(FavoritesFrame,text="  Add   ",font=('Maiandra GD', 8,'bold','underline'), relief='flat', command=AddFavorite)
FavouriteButton.grid(row=0,column=0)


FavouriteButton = Button(FavoritesFrame,text="Remove",font=('Maiandra GD', 8,'bold','underline'), relief='flat', command=RemoveFavorite)
FavouriteButton.grid(row=1,column=0)


window.mainloop()
            