import flet as ft
import time

def main(page: ft.Page):
    
    page.title="Mi contadior con Flet"
    page.vertical_alignment= ft.MainAxisAlignment.CENTER
    
    text_number=ft.TextField(value=f"0",text_align=ft.TextAlign.CENTER,width=100)

    
    def minus(e):
        text_number.value= str(int(text_number.value)-1)
        page.update()
    def plus(e): 
        text_number.value= str(int(text_number.value)+1)
        page.update()





    page.add(
        ft.Row(
        [
            ft.IconButton(ft.icons.REMOVE,on_click=minus),
            text_number,
            ft.IconButton(ft.icons.ADD,on_click=plus)


        ],
        alignment=ft.MainAxisAlignment.CENTER
          
        
        )
    )

    # for i in range(100):
    #     text_number.value= f"Step {i}"
    #     page.update()
    #     time.sleep(1)

    for i in range(5000):
        page.controls.append(ft.Text(f"Line {i}"))
    page.scroll = "always"
    page.update()    

# ft.app(main)
ft.app(main)


