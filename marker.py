from tkinter import filedialog, colorchooser
from PIL import Image as ImgObj, ImageFont, ImageDraw


class WaterMarker:
    def __init__(self):
        self.img = None
        self.img_select_label = ""
        self.mark = None
        self.mark_select_label = ""
        self.text_select_color = ()

    def open_img_dialog(self):
        # open dialogue window to choose image
        img_file_path = filedialog.askopenfilename(
            title="Select a file to be watermarked",
            filetypes=[("Image files", ["*.gif", "*.jpg", "*.jpeg", "*.png", "*.tiff"]),
                       ("All Files", "*.*")])

        if img_file_path:
            self.img = ImgObj.open(img_file_path)
            # add alpha to image
            self.img.putalpha(255)
            self.img_select_label = img_file_path.split("/")[-1]

    def open_mark_dialog(self):
        # open dialogue window to choose watermark
        mark_file_path = filedialog.askopenfilename(
            title="Select a file as watermark",
            filetypes=[("Image files", ["*.gif", "*.jpg", "*.jpeg", "*.png", "*.tiff"]),
                       ("All Files", "*.*")])

        if mark_file_path:
            self.mark = ImgObj.open(mark_file_path)
            self.mark_select_label = mark_file_path.split("/")[-1]

    def add_img_watermark(self, opacity, position):
        # if watermark is landscape, mark width is 10% of image's width
        if self.mark.size[0] > self.mark.size[1]:
            ratio = self.img.size[0] * 0.1 / self.mark.size[0]
            mark_size = (int(self.img.size[0] * 0.1), int(self.mark.size[1] * ratio))
        # if watermark is portrait, mark height is 10% of image's width
        else:
            ratio = self.img.size[1] * 0.1 / self.mark.size[1]
            mark_size = (int(self.mark.size[0] * ratio), int(self.img.size[1] * 0.1))

        # resize watermark
        mark_resized = self.mark.resize(mark_size)

        # get & set selected watermark opacity
        mark_opa = int((255 / 100) * int(opacity))
        mark_resized.putalpha(mark_opa)

        # watermark coordinates
        mark_coords = {
            "top left": (0, 0),
            "top right": (self.img.size[0] - mark_resized.size[0], 0),
            "bottom left": (0, self.img.size[1] - mark_resized.size[1]),
            "bottom right": (self.img.size[0] - mark_resized.size[0], self.img.size[1] - mark_resized.size[1])
        }

        # get & set selected watermark position
        mark_pos = mark_coords[position]

        # add watermark to image
        self.img.alpha_composite(im=mark_resized, dest=mark_pos)

        # save watermarked image
        file = filedialog.asksaveasfile(mode="w", defaultextension=".png",
                                        filetypes=(("PNG", "*.png"), ("All Files", "*.*")))
        if file:
            self.img.save(file.name)

    def open_color_dialog(self):
        # open dialog window to choose watermark text color
        self.text_select_color = colorchooser.askcolor(title='Watermark text color')

    def add_text_watermark(self, font_size, opacity, position, text):
        # create blank image for watermark text
        txt = ImgObj.new(mode="RGBA", size=self.img.size, color=(255, 255, 255, 0))

        # set font and size of watermark text
        font = ImageFont.truetype(font="arial.ttf", size=int(font_size))

        # watermark text coordinates
        text_mark_coords = {
            "top left": ((0, 0), "la"),
            "top right": ((self.img.size[0], 0), "ra"),
            "bottom left": ((0, self.img.size[1]), "ls"),
            "bottom right": (self.img.size, "rs")
        }

        # get & set selected watermark text position
        mark_pos = text_mark_coords[position]

        # get & combine selected watermark text color and opacity
        text_color = self.text_select_color[0]
        text_opa = int((255 / 100) * int(opacity))
        fill = (*text_color, text_opa)

        # draw watermark text
        text_mark = ImageDraw.Draw(txt)
        text_mark.text(xy=mark_pos[0], text=text, fill=fill, font=font, anchor=mark_pos[1])

        # add watermark to image
        self.img.alpha_composite(txt)

        # save watermarked image
        file = filedialog.asksaveasfile(mode="w", defaultextension=".png",
                                        filetypes=(("PNG", "*.png"), ("All Files", "*.*")))
        if file:
            self.img.save(file.name)
