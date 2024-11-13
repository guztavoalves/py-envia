import customtkinter as ctk

class CTkinterHelpers:

    def get(self, widget):
        return widget.get()
    
    def select(self, widget):
        widget.select()

    def forget(self, widget):
        widget.pack_forget()

    def place_forget(self, widget):
        widget.place_forget()

    def pack(self, widget, configs):
        widget.pack(**configs)
        
    def place(self, widget, configs):
        widget.place(**configs)

    def delete(self, widget):
        widget.delete('0','end')

    def destroy(self, widget):
        widget.destroy()

    def select(self, widget):
        widget.select()

    def deselect(self, widget):
        widget.deselect()

    def insert(self, widget, val, index=0):
        widget.insert(index,val)

    def is_selected(self, widget):
        return widget.get()

    def make_str_var(self, val):
        return ctk.StringVar(value=val)

    def configure(self, widget, configs):
        widget.configure(**configs)
    
    def update_scrollbar(self, widget):
        widget.update_idletasks()

    def make_frame(self, configs):
        return ctk.CTkFrame(**configs)
    
    def make_scrollabel_frame(self, configs):
        return ctk.CTkScrollableFrame(**configs)
    
    def make_button(self, configs):
        return ctk.CTkButton(**configs)
    
    def make_label(self, configs):
        return ctk.CTkLabel(**configs)
    
    def make_entry(self, configs):
        return ctk.CTkEntry(**configs)
    
    def make_checkbox(self, configs):
        return ctk.CTkCheckBox(**configs)
    
    def make_textbox(self, configs):
        return ctk.CTkTextbox(**configs)

    def generate_font(self, family, size):
        return ctk.CTkFont(family=family, size=size)