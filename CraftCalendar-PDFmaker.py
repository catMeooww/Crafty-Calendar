from fpdf import FPDF
from tkinter import *

window = Tk()
window.title("Crafty Calendar - Minecraft Projects to PDF")

photo = PhotoImage(file = 'CraftyIcon.png')
window.wm_iconphoto(False, photo)

def saveProjectData():
    #Getting the Data
    project = inputName.get()
    world = inputWorld.get()
    dimension = inputDimension.get()
    coordinates = inputCoordinates.get()
    resources = inputResources.get()
    print("Saving Data")
    print(f"- {project} - {world} - {dimension} - {coordinates} - {resources};")
    pdfFont = selectedFont.get()
    pdfColor = selectedColor.get()
    print(f"- {pdfFont} - {pdfColor}.")

    if project != "" and world != "" and dimension != "" and coordinates != "" and resources != "":
        #creating PDF
        pdf = FPDF()

        pdf.add_page()
        pdf.set_font(pdfFont, 'B', 50)
        pdf.set_text_color(255,255,255)

        pdf.image("PDF_background.png",x=0,y=0)
        pdf.text(10,20,project)

        if pdfColor == "Green":
            pdf.image("GreenTable.png",x=40,y=80)
            pdf.set_text_color(0,153,0)
        elif pdfColor == "Red":
            pdf.image("RedTable.png",x=40,y=80)
            pdf.set_text_color(204,102,0)
        elif pdfColor == "Blue":
            pdf.image("BlueTable.png",x=40,y=80)
            pdf.set_text_color(0,102,204)
        else:
            pdf.image("WhiteTable.png",x=40,y=80)
        pdf.set_font(pdfFont, 'B', 17)

        pdf.text(50,100,project)
        pdf.text(50,125,world)
        pdf.text(50,150,dimension)
        pdf.text(50,175,coordinates)
        pdf.text(50,200,resources)

        pdf.output(project + ".pdf")
        print("PDF gerado com sucesso!")
        createLabel["fg"] = "green"
        createLabel["text"] = "PDF generating susccessful!"
    else:
        createLabel["fg"] = "red"
        createLabel["text"] = "Every box must be filled!"

#header
header = Frame(window,relief='raised',borderwidth=8)
header.pack(side=TOP)

topLabel = Label(header,text="CRAFTY CALENDAR",font=("Arial", 20),width=71)
topLabel2 = Label(header,text="Crafty Calendar PDF Maker - Minecraft projects to PDF!",height=5)
topLabel.pack()
topLabel2.pack()

mainFrame = Frame(window)
mainFrame.pack()

#dataframe
dataFrame = Frame(mainFrame,relief="sunken",borderwidth=5)
dataFrame.pack(side=LEFT,pady=2)

helpLabel = Label(dataFrame,text="Put here your project basic data:",font=("Arial", 14),width=80)
extraInfo = Label(dataFrame,text="(Your PDF will be generated in the same folder this program is)",height=4)
helpLabel.pack()
extraInfo.pack()

labelName = Label(dataFrame,text="Project Name:")
inputName = Entry(dataFrame,width=50)
labelWorld = Label(dataFrame,text="World project is:")
inputWorld = Entry(dataFrame,width=50)
labelDimension = Label(dataFrame,text="Dimension project is:")
inputDimension = Entry(dataFrame,width=50)
labelCoordinates = Label(dataFrame,text="Coordinates (X,Y,Z):")
inputCoordinates = Entry(dataFrame,width=50)
labelResources = Label(dataFrame,text="Main resource(s) to collect (ex:wood):")
inputResources = Entry(dataFrame,width=50)
labelName.pack()
inputName.pack()
labelWorld.pack()
inputWorld.pack()
labelDimension.pack()
inputDimension.pack()
labelCoordinates.pack()
inputCoordinates.pack()
labelResources.pack()
inputResources.pack()
spacing = Label(dataFrame,text="----------")
spacing.pack()

#styleFrame
styleFrame = Frame(mainFrame,relief="solid",borderwidth=3)
styleFrame.pack(side=RIGHT,pady=2)

labelStyle = Label(styleFrame,text="Your PDF style",font=("Arial", 14),width=23,height=5)
labelStyle.pack()

selectedFont = StringVar(window, "Arial")
labelChooseFont = Label(styleFrame,text="PDF Font:")
chooseArial = Radiobutton(styleFrame,text="Arial",variable=selectedFont,value="Arial")
chooseTimesNewRoman = Radiobutton(styleFrame,text="Times new Roman",variable=selectedFont,value="Times")
labelChooseFont.pack()
chooseArial.pack()
chooseTimesNewRoman.pack()

selectedColor = StringVar(window, "White")
labelChooseColor = Label(styleFrame,text="PDF Table Color:")
chooseWhite = Radiobutton(styleFrame,text="White",variable=selectedColor,value="White")
chooseRed = Radiobutton(styleFrame,text="Red",variable=selectedColor,value="Red")
chooseGreen = Radiobutton(styleFrame,text="Green",variable=selectedColor,value="Green")
chooseBlue = Radiobutton(styleFrame,text="Blue",variable=selectedColor,value="Blue")
labelChooseColor.pack()
chooseWhite.pack()
chooseRed.pack()
chooseGreen.pack()
chooseBlue.pack()

#createFrame
createFrame = Frame(window,relief="flat",borderwidth=1)
createFrame.pack(side=BOTTOM)
labelInfo = Label(createFrame,text="Create the Project PDF:")
labelInfo.pack()
createBtn = Button(createFrame,text="Generate PDF",command=saveProjectData)
createBtn.pack()
createLabel = Label(createFrame,text=" ",fg="green")
createLabel.pack()
copyrightLabel = Label(createFrame,text="Crafty Calendar by CatMeooww10",height=2)
copyrightLabel.pack()

window.mainloop()