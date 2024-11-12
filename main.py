import flet as ft

def main(page: ft.Page):
    page.title = "Product Calculator"
    page.window_left = 942
    page.window_top = 96
    page.window.width = 390
    page.window.height = 542
    page.window.resizable = False
    page.window.maximizable = False
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    gross_weight = ft.TextField(
        label="Gross weight",
        autofill_hints=ft.AutofillHint.NAME,
        min_lines=1
    )
    net_weight = ft.TextField(
        label="Net weight",
        autofill_hints=[ft.AutofillHint.NAME],
        min_lines=1
    )
    
    result_text = ft.Text()

    def clear_fields_click(e):
        gross_weight.value = ""
        net_weight.value = ""
        result_text.value = ""
        page.update()

    def calculate_click(e):
        try:
            gross = float(gross_weight.value)
            net = float(net_weight.value)

            wrapper_weight = gross - net
            sample = net - 2

            result_text.value = f"Wrapping weight: {wrapper_weight} grams \nSample: {sample} grams"
        except ValueError:
            result_text.value = "Please enter valid numerical values."
        page.update()

    group_buttons = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.ElevatedButton("Calculate", on_click=calculate_click),
            ft.ElevatedButton("Clear fields", on_click=clear_fields_click),
        ]
    )
    
    page.add(
        ft.AutofillGroup(
            ft.Column(
                controls=[
                    gross_weight,
                    net_weight,
                    group_buttons,
                    result_text
                ]
            )
        )
    )

ft.app(main)