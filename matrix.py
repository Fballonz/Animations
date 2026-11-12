from tkinter import Frame, Tk, Canvas
from random import choice

class Matrix(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.canvas = Canvas(master, bg='black', highlightthickness=0)
        self.canvas.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.width = master.winfo_screenwidth()
        self.height = master.winfo_screenheight()

        self.velocidad = [i for i in range(5, 30, 5)]
        self.pos = [i for i in range(-200, 200, 20)]
        self.letters = []
        self.green = 0
        self.chars = ['ｱ', 'ｲ', 'ｳ', 'ｴ', 'ｵ',
                      'ｶ', 'ｷ', 'ｸ', 'ｹ', 'ｺ',
                      'ｻ', 'ｼ', 'ｽ', 'ｾ', 'ｿ',
                      'ﾀ', 'ﾁ', 'ﾂ', 'ﾃ', 'ﾄ',
                      'ﾅ', 'ﾆ', 'ﾇ', 'ﾈ', 'ﾉ',
                      'ﾊ', 'ﾋ', 'ﾌ', 'ﾍ', 'ﾎ',
                      'ﾏ', 'ﾐ', 'ﾑ', 'ﾒ', 'ﾓ',
                      'ﾔ', 'ﾕ', 'ﾖ', 'ﾗ', 'ﾘ',
                      'ﾙ', 'ﾚ', 'ﾛ', 'ﾜ', 'ﾝ',
                      '0', '1', '2', '3', '4',
                      '5', '7', '8', '9', 'Z',
                      ':', '.', '=', '*', '+',
                      '-', '<', '>', '¦', '|',
                      '╌', 'ç']

        self.draw()
        self.animate()

    def draw(self):
        for x in range(0, self.width, 20):
            y = choice(self.pos)
            for j in range(0, choice([180, 220, 280]), 20):
                obj = self.canvas.create_text(20 + x, -200 + y + j,
                                              text=choice(self.chars),
                                              fill='green2',
                                              font=('MS Gothic', 14))
                self.letters.append(obj)

    def animate(self):
        for letter in self.letters:
            v = choice(self.velocidad)

            self.green += 5
            if self.green >= 250:
                self.green = 0
            color = '#{:02x}{:02x}{:02x}'.format(0, self.green, 0)

            self.canvas.itemconfig(letter, fill=color, text=choice(self.chars))
            self.canvas.move(letter, 0, v)

            # when a symbol falls off the bottom, send it back above the top
            if self.canvas.coords(letter)[1] >= self.height + 20:
                self.canvas.move(letter, 0, -(self.height + 400))

        self.canvas.after(80, self.animate)

if __name__ == '__main__':
    root = Tk()
    root.title('Matrix Animation')
    root.config(bg='black')
    root.geometry('1200x700')
    root.bind('<Escape>', lambda e: root.destroy())
    app = Matrix(root)
    app.mainloop()