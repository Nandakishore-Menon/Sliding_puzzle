from Tkinter import *
from heapq import heappush, heappop
from random import shuffle
import time
import random
import time
count=0
n = 0
p = 0
flag=0
listofstates=[]
l = []
print("Please enter a nuber from 0 to 8\n\n0 denotes a blank space\n1 denotes number 1 and so on...\n")
for i in range(0,9):
    l.append(input())
if l==[1,2,3,4,5,6,7,8,0]:
	print "Already Solved"
	quit()
class Solver:
  def __init__(self, initial_state=None):
    self.initial_state = State(initial_state)
    self.goal = range(1, 9)

  def _rebuildPath(self, end):
    path = [end]
    state = end.parent
    while state.parent:
      path.append(state)
      state = state.parent
    return path

  def solve(self):
    openset = PriorityQueue()
    openset.add(self.initial_state)
    closed = set()
    moves = 0
    #print openset.peek(), '\n\n'
    start = time.time()
    global count
    while openset:
      current = openset.poll()
      if current.values[:-1] == self.goal:
        end = time.time()
        path = self._rebuildPath(current)
        for state in reversed(path):
          # print state
          listofstates.append(state.values)
          count += 1
        print 'Moves made: %d' % len(path)
        break
      moves += 1
      for state in current.possible_moves(moves):
        if state not in closed:
          openset.add(state)
      closed.add(current)
    else:
      print 'No Solution!'
      global flag
      flag=1


class State:
  def __init__(self, values, moves=0, parent=None):
    self.values = values
    self.moves = moves
    self.parent = parent
    self.goal = range(1, 9)
  
  def possible_moves(self, moves):
    i = self.values.index(0)
    if i in [3, 4, 5, 6, 7, 8]:
      new_board = self.values[:]
      new_board[i], new_board[i - 3] = new_board[i - 3], new_board[i]
      yield State(new_board, moves, self)
    if i in [1, 2, 4, 5, 7, 8]:
      new_board = self.values[:]
      new_board[i], new_board[i - 1] = new_board[i - 1], new_board[i]
      yield State(new_board, moves, self)
    if i in [0, 1, 3, 4, 6, 7]:
      new_board = self.values[:]
      new_board[i], new_board[i + 1] = new_board[i + 1], new_board[i]
      yield State(new_board, moves, self)
    if i in [0, 1, 2, 3, 4, 5]:
      new_board = self.values[:]
      new_board[i], new_board[i + 3] = new_board[i + 3], new_board[i]
      yield State(new_board, moves, self)

  def score(self):
    return self._h() + self._g()

  def _h(self):
    return sum([1 if self.values[i] != self.goal[i] else 0 for i in xrange(8)])

  def _g(self):
    return self.moves

  def __cmp__(self, other):
    return self.values == other.values

  def __eq__(self, other):
    return self.__cmp__(other)

  def __hash__(self):
    return hash(str(self.values))

  def __lt__(self, other):
    return self.score() < other.score()

  def __str__(self):
    return '\n'.join([str(self.values[:3]),
        str(self.values[3:6]),
        str(self.values[6:9])]).replace('[', '').replace(']', '').replace(',', '').replace('0', 'x')

class PriorityQueue:
  def __init__(self):
    self.pq = []

  def add(self, item):
    heappush(self.pq, item)

  def poll(self):
    return heappop(self.pq)

  def peek(self):
    return self.pq[0]

  def remove(self, item):
    value = self.pq.remove(item)
    heapify(self.pq)
    return value is not None

  def __len__(self):
    return len(self.pq)

def quitme():
    root.destroy()
    
solver = Solver(l)
solver.solve()
if flag==1:
    root = Tk()
    root.geometry("500x500")
    root.title("Sliding Puzzle")
    myLabel = Label(root, text = "Unsolvable!",font = 100)
    quit = Button(root, text = "Quit", padx = 60, command = quitme)
    myLabel.place(x = 190,y = 100)
    quit.place(x=190,y=250)
    root.mainloop()
if flag==1:
    quit()
    
class slidingpuzzle:
    def __init__(self):
        self.tk = Toplevel()
        self.canvas = Canvas(self.tk,width = 600,height = 400)
        self.canvas.grid(row = 0,column = 0)
        self.images = []
        self.counter = Label(self.tk,font = 100)


        self.counter.place(x = 420,y = 150)
    
    def load_image(self):
        for i in range(0,9):
            img = PhotoImage(file = "photos/%d.gif"%i)
            self.images.append(img)
        #self.blank = PhotoImage(file = "photos/blank.gif")
        #self.images.append(self.blank)
    # counter = Label(tk)
    # counter.pack()
    def first_page(self,l):
        self.draw_imageauto(l)
        #heading = Label(self.tk,text = "Sliding Puzzle")
        #heading.grid(row = 2,column = 8)
        #button1 = Button(self.tk,text = "start")
        #button1.grid(row = 4,column = 8)
        #button1.bind("<Button-1>",self.draw_imageauto(l))
    def first_pagemanual(self,l):
        self.draw_image(l)
        #heading = Label(self.tk,text = "Sliding Puzzle")
        #heading.grid(row = 2,column = 8)
        #button1 = Button(self.tk,text = "start")
        #button1.grid(row = 4,column = 8)
        #button1.bind("<Button-1>",self.draw_image(l))
    def draw_imageauto(self,l):
        i = 0
        yp=0
        global n
        for y in range(0,3):
            xp=5
            yp+=5
            for x in range(0,3):
                self.canvas.create_image(x*130+xp,y*130+yp,image=self.images[l[i]],anchor='nw')
                i+=1
                xp+=5 
        
        # Label(self.tk).pack()
        self.counter['text'] = "count = " + str(n)
        self.tk.update()
        # self.tk.mainloop()
    def draw_image(self,l):
        i = 0
        yp=0
        global n
        for y in range(0,3):
            xp=5
            yp+=5
            for x in range(0,3):
                self.canvas.create_image(x*130+xp,y*130+yp,image=self.images[l[i]],anchor='nw')
                i+=1
                xp+=5 
        self.counter['text'] = "Moves made = " +str(p)
    def startauto(self,l):
        self.load_image()
        self.first_page(l)
        time.sleep(1)
        self.changeauto()
        # self.change()
    def startmanual(self,l):
        self.load_image()
	self.first_pagemanual(l)
        self.changemanual()
    def changeauto(self):
      global l
      global n
      global count
      while(n< count):
        l = listofstates[n]
        n += 1
        num = 0
        self.draw_imageauto(l)
        num += 1
        time.sleep(1)
    def changemanual(self):
      self.tk.bind("<Up>",self.up)
      self.tk.bind("<Down>",self.down)
      self.tk.bind("<Left>",self.left)
      self.tk.bind("<Right>",self.right)
    def up(self, event):  
      global p
      p += 1
      i = l.index(0)
      if(i!=0 and i!=1 and i!=2):
        temp = l[i] 
        l[i] = l[i-3]
        l[i-3] = temp
        self.draw_image(l)
        if l==[1,2,3,4,5,6,7,8,0]:
        	self.tk.destroy()
    def down(self, event):
      global p
      p += 1
      i = l.index(0)
      if(i!=6 and i!=7 and i!=8):
        temp = l[i]
        l[i] = l[i+3]
        l[i+3] = temp
        self.draw_image(l)
        if l==[1,2,3,4,5,6,7,8,0]:
        	self.tk.destroy()
    def left(self, event):
      global p
      p += 1
      i = l.index(0)
      if(i!=0 and i!=3 and i!=6):
        temp = l[i]
        l[i] = l[i-1]
        l[i-1] = temp
        self.draw_image(l)
        if l==[1,2,3,4,5,6,7,8,0]:
        	self.tk.destroy()
    def right(self, event):
      global p
      p += 1
      i = l.index(0)
      if(i!=2 and i!=5 and i!=8):
        temp = l[i]
        l[i] = l[i+1]
        l[i+1] = temp
        self.draw_image(l)
        if l==[1,2,3,4,5,6,7,8,0]:
        	self.tk.destroy()
      

def slidingauto():
	#new.destroy()
	l2=l[:]
	g1 = slidingpuzzle()
	g1.startauto(l2)
	
# g.tk.mainloop()
# print(l.index(0))
#puzzle = range(9)
#shuffle(puzzle)
# print listofstates
# print listofstates[i]
	g1.tk.mainloop()
def slidingmanual():
	#new.destroy()
	l2=l[:]
	g = slidingpuzzle()
	g.startmanual(l2)
	
# g.tk.mainloop()
# print(l.index(0))
#puzzle = range(9)
#shuffle(puzzle)
# print listofstates
# print listofstates[i]
	g.tk.mainloop()
	
def clickStart():
	root.destroy()
	new = Tk()
	new.geometry("500x500")
	new.title("Sliding Puzzle")
	photo1 = PhotoImage(file = "bg.gif")
	bg1 = Label(new, image = photo1)
	bg1.pack()
	solve = Button(new, text = "Solve Yourself", padx = 50,command = slidingmanual)
	solve.place(y=200,x=190)

	solveComp = Button(new, text = "Solve using Computer",command = slidingauto)
	solveComp.place(x=190,y=250)
	# back = Button(new, text = "Go Back", padx = 50, command = Root)
	# back.pack()

def Quit():
	root.destroy()


root = Tk()
root.geometry("500x500")
root.title("Sliding Puzzle")
photo = PhotoImage(file = "bg.gif")
bg = Label(root, image = photo)
bg.pack()
myLabel = Label(root, text = "Sliding Puzzle",font = 100)
myButton = Button(root, text = "Start", padx = 60,command = clickStart)
quit = Button(root, text = "Quit", padx = 60, command = Quit)

myLabel.place(x = 190,y = 100)
myButton.place(x=190,y=200)
quit.place(x=190,y=250)

root.mainloop()

