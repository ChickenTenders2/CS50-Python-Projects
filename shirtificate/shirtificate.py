from fpdf import FPDF

def PDF(name):
    pdf = FPDF(format="A4")
    pdf.add_page()
    pdf.image("shirtificate.png", x=17.5, y=61, w=175, h=175) #(pg width - img width)/2 = center pos for x

    pdf.set_font("Arial", size=64)
    title_y = 30
    pdf.set_y(title_y)
    pdf.cell(0, 10, "CS50 Shirtificate", 0, 1, "C")

    pdf.set_font("Arial", size=32)
    pdf.set_text_color(255, 255, 255)
    name_y = 139.5
    pdf.set_y(name_y)
    pdf.cell(0, 10, f"{name} took CS50", 0, 1, "C")

    pdf.output("shirtificate.pdf")

def main():
    name = input("Name: ")
    PDF(name)

if __name__ == "__main__":
    main()
