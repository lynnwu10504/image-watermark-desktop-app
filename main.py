import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageDraw, ImageFont


# font_name = "Arial.ttf"
# font_size = 20
# texts = "Lynn"


def add_text_watermark():

    image_paths = filedialog.askopenfilenames(initialdir="/Users/lynnwu/Desktop",
                                              title="Select Image",
                                              filetypes=[("Image Files", ".jpeg .jpg .png")]
                                              )

    for img in image_paths:

        image = Image.open(img)
        if image.mode == "P":
            image = image.convert('RGB')
        draw = ImageDraw.Draw(image)

        font_name = font_combobox.get()
        font_size = int(fontsize_combobox.get())
        texts = text_entry.get()

        font = ImageFont.truetype(font_name, font_size)
        text_width, text_height = draw.textsize(texts, font=font)

        x = (image.width - text_width) // 2
        y = (image.height - text_height) // 2

        draw.text((x, y), texts, font=font, fill='white')

        save_path = filedialog.asksaveasfilename(initialdir="/Users/lynnwu/Desktop", title="Save Image", filetypes=[("JPG Files", ".jpeg .jpg"), ("PNG Files", ".png")])

        if save_path:
            image.save(save_path)
            print("Watermark added and image saved successfully!")


def add_logo_watermark():

    logo_path = filedialog.askopenfilename(initialdir="/Users/lynnwu/Desktop",
                                           title="Select Logo",
                                           filetypes=[("Image Files", ".jpeg .jpg .png")]
                                           )

    logo = Image.open(logo_path)
    logo_resized = logo.resize((100, 100), Image.ANTIALIAS)

    if logo_resized:
        image_paths = filedialog.askopenfilenames(initialdir="/Users/lynnwu/Desktop",
                                                  title="Select Image",
                                                  filetypes=[("Image Files", ".jpeg .jpg .png")]
                                                  )

        for img in image_paths:
            image = Image.open(img)
            if image.mode == "P":
                image = image.convert('RGB')

            x = (image.width - 100) // 2
            y = (image.height - 100) // 2

            image.paste(logo_resized, (x, y), logo_resized)

            save_path = filedialog.asksaveasfilename(initialdir="/Users/lynnwu/Desktop", title="Save Image", filetypes=[("JPG Files", ".jpeg .jpg"), ("PNG Files", ".png")])

            if save_path:
                image.save(save_path)
                print("Watermark added and image saved successfully!")


window = tk.Tk()
window.title("Image Watermark Magic")

ttk.Separator(window, orient=tk.VERTICAL).grid(column=2, row=3, rowspan=5, sticky='ns')


label_main = tk.Label(window,
                      text="Welcome to Image Watermark Magic!",
                      font=("Arial.ttf", 36),
                      width=40
                      )
label_main.grid(row=0, column=0, rowspan=2, columnspan=4, padx=50, pady=30)


# Text Watermark
label_text_wm = tk.Label(window,
                         text="Text Watermark: configure your watermark, select\n the image(s), then save the watermarked images.",
                         font=("Arial.ttf", 18)
                         )
label_text_wm.grid(row=3, column=0, columnspan=2, padx=20, pady=20)

text_label = tk.Label(window, text="Enter watermark texts:", font=("Arial.ttf", 14), anchor="w")
text_label.grid(row=4, column=0, padx=20, pady=5)
text_entry = tk.Entry(window, width=22)
text_entry.insert(0, "Lynn")
text_entry.grid(row=4, column=1, padx=20, pady=5)

font_label = tk.Label(window, text="Choose font:", font=("Arial.ttf", 14), anchor="w", width=16)
font_label.grid(row=5, column=0, padx=20, pady=5)
font_combobox = ttk.Combobox(window, state="readonly")
font_combobox['values'] = ('Arial', 'Courier New', 'Helvetica', 'Microsoft Sans Serif', 'Times New Roman', 'Verdana')
font_combobox.current(0)
font_combobox.grid(row=5, column=1, padx=20, pady=5)

fontsize_label = tk.Label(text="Choose font size:", font=("Arial.ttf", 14), anchor="w", width=16)
fontsize_label.grid(row=6, column=0, padx=20, pady=5)
fontsize_combobox = ttk.Combobox(window, state="readonly")
fontsize_combobox['values'] = (12, 14, 16, 18, 20, 22, 24, 26, 28, 30)
fontsize_combobox.current(4)
fontsize_combobox.grid(row=6, column=1, padx=20, pady=5)

select_button_text = tk.Button(window, text="Select Images", command=add_text_watermark, font=("Arial.ttf", 14))
select_button_text.grid(row=7, column=0, columnspan=2, padx=20, pady=40)

# Logo Watermark
label_logo_wm = tk.Label(window,
                         text="Logo Watermark: click the button to select the logo and\n the image(s), then save the watermarked image(s)",
                         font=("Arial.ttf", 18)
                         )
label_logo_wm.grid(row=3, column=3, columnspan=2, padx=20, pady=20)


select_button_logo = tk.Button(window, text="Select Logo and Images", command=add_logo_watermark, font=("Arial.ttf", 14))
select_button_logo.grid(row=7, column=3, columnspan=2, padx=20, pady=40)

window.mainloop()

