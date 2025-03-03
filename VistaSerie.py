import tkinter as tk
from tkinter import ttk

root = tk.Tk()

usuarios = {"Karling": "060301"}

contenido = (
    # Ciencia Ficcion 
    {"tipo": "pelicula", "titulo": "Inception", "genero": "Ciencia Ficcion"},
    {"tipo": "pelicula", "titulo": "The Matrix", "genero": "Ciencia Ficcion"},
    {"tipo": "pelicula", "titulo": "Interstellar", "genero": "Ciencia Ficcion"},
    {"tipo": "pelicula", "titulo": "Avatar", "genero": "Ciencia Ficcion"},
    {"tipo": "pelicula", "titulo": "Dune", "genero": "Ciencia Ficcion"},
    {"tipo": "serie", "titulo": "Stranger Things", "genero": "Ciencia Ficcion"},
    {"tipo": "serie", "titulo": "Black Mirror", "genero": "Ciencia Ficcion"},
    {"tipo": "serie", "titulo": "The Mandalorian", "genero": "Ciencia Ficcion"},
    {"tipo": "serie", "titulo": "Star Trek: Discovery", "genero": "Ciencia Ficcion"},
    {"tipo": "serie", "titulo": "Westworld", "genero": "Ciencia Ficcion"},

    # Romance
    {"tipo": "pelicula", "titulo": "Titanic", "genero": "Romance"},
    {"tipo": "pelicula", "titulo": "The Notebook", "genero": "Romance"},
    {"tipo": "pelicula", "titulo": "Pride and Prejudice", "genero": "Romance"},
    {"tipo": "pelicula", "titulo": "A Star is Born", "genero": "Romance"},
    {"tipo": "pelicula", "titulo": "La La Land", "genero": "Romance"},
    {"tipo": "serie", "titulo": "Outlander", "genero": "Romance"},
    {"tipo": "serie", "titulo": "Bridgerton", "genero": "Romance"},
    {"tipo": "serie", "titulo": "Jane the Virgin", "genero": "Romance"},
    {"tipo": "serie", "titulo": "Poldark", "genero": "Romance"},
    {"tipo": "serie", "titulo": "The Time Traveler's Wife", "genero": "Romance"},

    # Accion 
    {"tipo": "pelicula", "titulo": "The Dark Knight", "genero": "Accion"},
    {"tipo": "pelicula", "titulo": "Mad Max: Fury Road", "genero": "Accion"},
    {"tipo": "pelicula", "titulo": "John Wick", "genero": "Accion"},
    {"tipo": "pelicula", "titulo": "Gladiator", "genero": "Accion"},
    {"tipo": "pelicula", "titulo": "Die Hard", "genero": "Accion"},
    {"tipo": "serie", "titulo": "24", "genero": "Accion"},
    {"tipo": "serie", "titulo": "Arrow", "genero": "Accion"},
    {"tipo": "serie", "titulo": "The Punisher", "genero": "Accion"},
    {"tipo": "serie", "titulo": "Vikings", "genero": "Accion"},
    {"tipo": "serie", "titulo": "The Boys", "genero": "Accion"},

    # Drama 
    {"tipo": "pelicula", "titulo": "Parasite", "genero": "Drama"},
    {"tipo": "pelicula", "titulo": "The Godfather", "genero": "Drama"},
    {"tipo": "pelicula", "titulo": "Schindler's List", "genero": "Drama"},
    {"tipo": "pelicula", "titulo": "Forrest Gump", "genero": "Drama"},
    {"tipo": "pelicula", "titulo": "The Shawshank Redemption", "genero": "Drama"},
    {"tipo": "serie", "titulo": "Breaking Bad", "genero": "Drama"},
    {"tipo": "serie", "titulo": "The Crown", "genero": "Drama"},
    {"tipo": "serie", "titulo": "This Is Us", "genero": "Drama"},
    {"tipo": "serie", "titulo": "The Handmaid's Tale", "genero": "Drama"},
    {"tipo": "serie", "titulo": "Ozark", "genero": "Drama"},

    # Fantasia 
    {"tipo": "pelicula", "titulo": "The Lord of the Rings: The Fellowship of the Ring", "genero": "Fantasia"},
    {"tipo": "pelicula", "titulo": "Harry Potter and the Sorcerer's Stone", "genero": "Fantasia"},
    {"tipo": "pelicula", "titulo": "Pan's Labyrinth", "genero": "Fantasia"},
    {"tipo": "pelicula", "titulo": "The Chronicles of Narnia: The Lion, the Witch and the Wardrobe", "genero": "Fantasia"},
    {"tipo": "pelicula", "titulo": "Alice in Wonderland", "genero": "Fantasia"},
    {"tipo": "serie", "titulo": "Game of Thrones", "genero": "Fantasia"},
    {"tipo": "serie", "titulo": "The Witcher", "genero": "Fantasia"},
    {"tipo": "serie", "titulo": "His Dark Materials", "genero": "Fantasia"},
    {"tipo": "serie", "titulo": "Merlin", "genero": "Fantasia"},
    {"tipo": "serie", "titulo": "Shadow and Bone", "genero": "Fantasia"},

    # Comedia 
    {"tipo": "pelicula", "titulo": "The Grand Budapest Hotel", "genero": "Comedia"},
    {"tipo": "pelicula", "titulo": "Superbad", "genero": "Comedia"},
    {"tipo": "pelicula", "titulo": "The Hangover", "genero": "Comedia"},
    {"tipo": "pelicula", "titulo": "Juno", "genero": "Comedia"},
    {"tipo": "pelicula", "titulo": "Deadpool", "genero": "Comedia"},
    {"tipo": "serie", "titulo": "Friends", "genero": "Comedia"},
    {"tipo": "serie", "titulo": "The Office", "genero": "Comedia"},
    {"tipo": "serie", "titulo": "Brooklyn Nine-Nine", "genero": "Comedia"},
    {"tipo": "serie", "titulo": "Parks and Recreation", "genero": "Comedia"},
    {"tipo": "serie", "titulo": "How I Met Your Mother", "genero": "Comedia"}
)

generos_disponibles = ["Accion", "Ciencia Ficcion", "Comedia", "Drama", "Fantasia", "Romance"]

def limpiar_ventana():
    for widget in root.winfo_children():
        widget.destroy()

def guardar_usuarios(txtusuario, txtcontraseña):
    usuario = txtusuario.get()
    contraseña = txtcontraseña.get()
    
    if usuario in usuarios:
        lblerror = tk.Label(root, text="El usuario ya existe.", fg="red", bg="white")
        lblerror.place(relx=0.5, rely=0.66, anchor="center")
    elif not usuario or not contraseña:
        lblerror = tk.Label(root, text="Debe llenar ambos campos.", fg="red", bg="white")
        lblerror.place(relx=0.5, rely=0.66, anchor="center")
    else:
        usuarios[usuario] = contraseña
        print(f"Usuario registrado con exito: {usuarios}")
        menu_Bienvenida()

def mostrar_mensaje(mensaje, color="red"):
    mensaje_label.config(text=mensaje, fg=color, bg="white")

def buscar():
    tipo = tipo_var.get().lower()
    genero = genero_var.get().strip().lower()

    resultado_list.delete(0, tk.END)
    encontrados = [item for item in contenido if item["tipo"] == tipo and item["genero"].lower() == genero]

    if not encontrados:
        mostrar_mensaje("No se encontraron resultados.", "red")
    else:
        mostrar_mensaje("Resultados encontrados.", "green")
        for item in encontrados:
            resultado_list.insert(tk.END, item["titulo"])

def agregar_calificacion():
    seleccion = resultado_list.curselection()
    if not seleccion:
        mostrar_mensaje("Selecciona un titulo para calificar.", "red")
        return

    titulo = resultado_list.get(seleccion[0])
    comentario = comentario_var.get().strip()
    if not comentario:
        mostrar_mensaje("Debe ingresar un comentario junto con la calificacion.", "red")
        return

    try:
        calificacion = float(calificacion_var.get())
        if not (0 <= calificacion <= 5):
            raise ValueError("La calificacion debe estar entre 0 y 5.")
    except ValueError:
        mostrar_mensaje("Introduce una calificacion valida entre 0 y 5.", "red")
        return

    for item in contenido:
        if item["titulo"] == titulo:
            if "calificaciones" not in item:
                item["calificaciones"] = []
            item["calificaciones"].append({"calificacion": calificacion, "comentario": comentario})
            mostrar_mensaje(f"Se agrego calificacion a '{titulo}'.", "green")
            break
    
    calificacion_var.set("")
    comentario_var.set("")

def ver_comentarios():
    comentarios_text.delete("1.0", tk.END)
    for item in contenido:
        if "calificaciones" in item:
            comentarios_text.insert(tk.END, f"{item['titulo']}:\n")
            for cal in item["calificaciones"]:
                comentarios_text.insert(tk.END, f"  - {cal['comentario']} (Calificacion: {cal['calificacion']})\n")
            comentarios_text.insert(tk.END, "\n")

def inicio_sesion():
    global Fondo
    limpiar_ventana()
    root.geometry("400x400+550+100")
    root.title("VistaSerie - Inicio de Sesion")
    
    Fondo = tk.PhotoImage(file="FondoK23.png")
    lblFondo = tk.Label(root, image=Fondo)
    lblFondo.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    
    bienvenida = tk.Label(root, text="VistaSerie App", font=("Times New Roman", 36), bg="white")
    bienvenida.place(relx=0.5 , rely=0.17, anchor="center")
    
    lbliniciosecion = tk.Label(root, text="Inicio de sesion", font=("Arial", 16, "underline"), bg="white")
    lbliniciosecion.place(relx=0.5, rely=0.29, anchor="center")
    
    lblNuevo_usuario = tk.Label(root, text="Usurario: ", bg="white", font=("calibri", 14))
    lblNuevo_usuario.place(relx=0.5, rely=0.39, anchor="center")
    txtusuario = ttk.Entry(root)
    txtusuario.place(relx=0.5, rely=0.44, anchor="center")
    
    lblNueva_contraseña = tk.Label(root, text="Contraseña:", bg="white",font=("calibri", 14))
    lblNueva_contraseña.place(relx=0.5, rely=0.54, anchor="center")
    txtcontraseña = ttk.Entry(root, show="*")
    txtcontraseña.place(relx=0.5, rely=0.59, anchor="center")
    
    lblError = tk.Label(root, text="", fg="Red", bg="white")
    lblError.place(relx=0.5, rely=0.66, anchor="center")
    
    def validar_inicio():
        usuario = txtusuario.get()
        contraseña = txtcontraseña.get()
        
        if usuario in usuarios and usuarios[usuario] == contraseña:
            ventana_inicio(usuario)
        else:
            lblError.config(text="Usuario o contraseña INCORRECTOS.",fg="Red")
    
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("RedButton.TButton",font=('Arial', 11,'bold'),foreground="white",background="red",borderwidth=2,relief="solid")
    style.map("RedButton.TButton",background=[('active', 'darkred'), ('!active', 'red')],foreground=[('disabled', 'gray')])
    style.configure("GreenButton.TButton", font=('Arial', 11,'bold'), foreground="white", background="green", borderwidth=2, relief="solid")
    style.map("GreenButton.TButton", background=[('active', 'darkgreen'), ('!active', 'green')], foreground=[('disabled', 'gray')])
    
    btnEntrar = ttk.Button(root, text="Entrar", command=validar_inicio, style="GreenButton.TButton")
    btnEntrar.place(relx=0.35, rely=0.74, anchor="center")
    
    btnVolver = ttk.Button(root, text="Volver", command=menu_Bienvenida, style="RedButton.TButton")
    btnVolver.place(relx=0.65, rely=0.74, anchor="center")
    
    lblEmpresa = tk.Label(root, text="By: MajiLing23")
    lblEmpresa.place(relx=0.85, rely=0.95, anchor="center")
    
def registro_Usuarios():
    global Fondo
    limpiar_ventana()
    root.geometry("400x400+550+100")
    root.title("VistaSerie - Registro")
    
    Fondo = tk.PhotoImage(file="FondoK23.png")
    lblFondo = tk.Label(root, image=Fondo)
    lblFondo.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    
    bienvenida = tk.Label(root, text="VistaSerie App", font=("Times New Roman", 36), bg="white")
    bienvenida.place(relx=0.5 , rely=0.17, anchor="center")
    
    lblRegistrarse = tk.Label(root, text="Registrarse", font=("Arial", 16, "underline"), bg="white")
    lblRegistrarse.place(relx=0.5, rely=0.29, anchor="center")
    
    lblNuevo_usuario = tk.Label(root, text="Nuevo Usurario: ", bg="white", font=("calibri", 14))
    lblNuevo_usuario.place(relx=0.5, rely=0.39, anchor="center")
    txtusuario = ttk.Entry(root)
    txtusuario.place(relx=0.5, rely=0.44, anchor="center")
    
    lblNueva_contraseña = tk.Label(root, text="Nueva Contraseña:", bg="white", font=("calibri", 14))
    lblNueva_contraseña.place(relx=0.5, rely=0.54, anchor="center")
    txtcontraseña = ttk.Entry(root, show="*")
    txtcontraseña.place(relx=0.5, rely=0.59, anchor="center")
    
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("RedButton.TButton",font=('Arial', 11,'bold'),foreground="white",background="red",borderwidth=2,relief="solid")
    style.map("RedButton.TButton",background=[('active', 'darkred'), ('!active', 'red')],foreground=[('disabled', 'gray')])
    style.configure("GreenButton.TButton", font=('Arial', 11,'bold'), foreground="white", background="green", borderwidth=2, relief="solid")
    style.map("GreenButton.TButton", background=[('active', 'darkgreen'), ('!active', 'green')], foreground=[('disabled', 'gray')])
    
    btnGuardar = ttk.Button(root, text="Guardar", command=lambda: guardar_usuarios(txtusuario, txtcontraseña), style="GreenButton.TButton")
    btnGuardar.place(relx=0.35, rely=0.74, anchor="center")
    
    btnVolver = ttk.Button(root, text="Volver", command=menu_Bienvenida, style="RedButton.TButton")
    btnVolver.place(relx=0.65, rely=0.74, anchor="center")
    
    lblEmpresa = tk.Label(root, text="By: MajiLing23", bg="white")
    lblEmpresa.place(relx=0.85, rely=0.95, anchor="center")

def menu_Bienvenida():
    global imagen, imagen2, resized_img, resized_img2 , Fondo
    
    limpiar_ventana()
    root.geometry("600x600+450+50")
    root.title("VistaSerie - Recepcion")
    root.resizable(False, False)
    
    Fondo = tk.PhotoImage(file="FondoK1.png")
    lblFondo = tk.Label(root, image=Fondo)
    lblFondo.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    
    bienvenida = tk.Label(root, text="VistaSerie App", font=("Times New Roman", 40), fg="black", bg="white")
    bienvenida.place(relx=0.5, rely=0.195, anchor="center")
    
    lblBienvenida = tk.Label(root, text="🎬Tu Registro de Películas y Series🎬",font=("calibri", 14),fg="black", bg="white")
    lblBienvenida.place(relx=0.5, rely=0.27, anchor="center")
    
    lblDescripcion = tk.Label(root,text="Lleva un control de las peliculas y series que has visto, calificalas y agrega comentarios. \nRevisa tu historial y consulta tus reseñas en cualquier momento. \n¡Organiza tu experiencia cinematografica con VistaSerie! 🍿✨", 
                              bg="white",font=("Arial",10))
    lblDescripcion.place(relx=0.5, rely=0.35, anchor="center")

    imagen = tk.PhotoImage(file="Logokarling.png")
    imagen2 = tk.PhotoImage(file="LogoMajo.png")

    def resize_image(imagen, max_width=150, max_height=75):
        original_width = imagen.width()
        original_height = imagen.height()
        aspect_ratio = original_width / original_height

        if original_width > original_height:
            new_width = min(max_width, original_width)
            new_height = int(new_width / aspect_ratio)
        else:
            new_height = min(max_height, original_height)
            new_width = int(new_height * aspect_ratio)

        resized_img = imagen.subsample(
            max(1, original_width // new_width),  
            max(1, original_height // new_height)
        )
        return resized_img


    resized_img = resize_image(imagen)
    resized_img2 = resize_image(imagen2)

    label = tk.Label(root, image=resized_img)
    label2 = tk.Label(root, image=resized_img2)
    label.place(relx=0.1, rely=0.1, anchor="center")
    label2.place(relx=0.92, rely=0.1, anchor="center")
    
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("GrayButton.TButton", font=('Arial', 12, "bold", "underline"), foreground="black",background="lightgray",borderwidth=2,relief="solid")
    style.map("GrayButton.TButton",background=[('active', 'gray'), ('!active', 'lightgray')],foreground=[('disabled', 'darkgray')])


    button1 = ttk.Button(root, text="Iniciar Sesion", command=inicio_sesion, style="GrayButton.TButton")
    button1.place(relx=0.5, rely=0.65, anchor="center")

    button2 = ttk.Button(root, text="Registarse", command=registro_Usuarios, style="GrayButton.TButton")
    button2.place(relx=0.5, rely=0.72, anchor="center")

    style.configure("RedButton.TButton",font=('Arial', 12,"bold", "underline"),foreground="white",background="red",borderwidth=2,relief="solid")
    style.map("RedButton.TButton",background=[('active', 'darkred'), ('!active', 'red')],foreground=[('disabled', 'gray')])
    
    button3 = ttk.Button(root, text="Salir", command=root.quit, style="RedButton.TButton")
    button3.place(relx=0.5, rely=0.79, anchor="center")
    
    lblEmpresa = tk.Label(root, text="By: MajiLing23", bg="white")
    lblEmpresa.place(relx=0.9, rely=0.98, anchor="center")

def ventana_inicio(usuario):
    global imagen, imagen2, resized_img, resized_img2 , tipo_var, genero_var, calificacion_var, comentario_var, resultado_list, mensaje_label, comentarios_text, Fondo
    limpiar_ventana()
    root.geometry("1280x720+125+40")
    root.title("VistaSerie - App")
    root.configure(bg="white")
    
    Fondo = tk.PhotoImage(file="FondoH3.png")
    lblFondo = tk.Label(root, image=Fondo)
    lblFondo.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    
    bienvenida = tk.Label(root, text="VistaSerie App", font=("Times New Roman", 36), fg="black", bg="white")
    bienvenida.place(relx=0.5, rely=0.182, anchor="center")
    
    imagen = tk.PhotoImage(file="Logokarling.png")
    imagen2 = tk.PhotoImage(file="LogoMajo.png")

    def resize_image(imagen, max_width=150, max_height=75):
        original_width = imagen.width()
        original_height = imagen.height()
        aspect_ratio = original_width / original_height

        if original_width > original_height:
            new_width = min(max_width, original_width)
            new_height = int(new_width / aspect_ratio)
        else:
            new_height = min(max_height, original_height)
            new_width = int(new_height * aspect_ratio)

        resized_img = imagen.subsample(
            max(1, original_width // new_width),  
            max(1, original_height // new_height)
        )
        return resized_img

    resized_img = resize_image(imagen)
    resized_img2 = resize_image(imagen2)

    label = tk.Label(root, image=resized_img)
    label2 = tk.Label(root, image=resized_img2)
    label.place(relx=0.1, rely=0.1, anchor="center")
    label2.place(relx=0.93, rely=0.1, anchor="center")
    
    lblSaludo = tk.Label(root, text=f"🎬¡Bienvenido, {usuario}! Esperamos que disfrutes tu experiencia.🎬", font=("calibri", 16), fg="black", bg="white")
    lblSaludo.place(relx=0.5, rely=0.24, anchor="center")
    
    style = ttk.Style()
    style.theme_use("vista")
    style.configure("MyButton.TButton", font=('Arial', 12,'bold', "underline")) 
    
    frameDetras = tk.Frame(root, bg="red", bd=2)  
    frameDetras.place(relx=0.5, rely=0.9, anchor="center", width=125, height=40)
    
    btnVolver = ttk.Button(root, text="Volver", command=menu_Bienvenida, style="MyButton.TButton")
    btnVolver.place(relx=0.5, rely=0.9, anchor="center")
    
    lblEmpresa = tk.Label(root, text="By: MajiLing23", bg="white")
    lblEmpresa.place(relx=0.94, rely=0.98, anchor="center")
    
    #######################################################################################################################################################################
    tipo_var = tk.StringVar(value="pelicula")
    genero_var = tk.StringVar()
    calificacion_var = tk.StringVar()
    comentario_var = tk.StringVar()
    
    style.theme_use("vista")  
    style.configure("Custom.TFrame", font=("Arial", 16),background="white")  
    style.configure("Custom.TFrame.Label", background="white", borderwidth=2, relief="solid")
    style.configure("Custom.TRadiobutton", background="white", padding=5)
    style.map("Custom.TRadiobutton", background=[("active", "white"), ("!disabled", "white")])
    
    # Frame de búsqueda
    lblIntrucion1 = tk.Label(root,text="\U00000031\U000020E3 Buscar y seleccionar\n-Usa la barra de busqueda para encontrar una película o serie.\n-Seleccionala de la lista de resultados."
                            ,bg="white")
    lblIntrucion1.place(relx=0.17, rely=0.35, anchor="center")
    
    frame_externo = tk.Frame(root, bg="black", bd=2, relief="solid")  # Marco negro de grosor 2
    frame_externo.place(relx=0.2, rely=0.6, anchor="center")
    frame_busqueda = ttk.LabelFrame(frame_externo, text="Buscar Contenido", style="Custom.TFrame")
    frame_busqueda.pack(padx=2, pady=2, fill="both", expand=True)
    
    #frame_busqueda = ttk.LabelFrame(root, text="Buscar Contenido:", style="Custom.TFrame")
    #frame_busqueda.place(relx=0.25, rely=0.5, anchor="center")

    lblBuscar = tk.Label(frame_busqueda, text="Tipo:", bg="white")
    lblBuscar.grid(row=0, column=0)
    btnBusqueda1 = ttk.Radiobutton(frame_busqueda, text="Pelicula", variable=tipo_var, value="pelicula", style="Custom.TRadiobutton")
    btnBusqueda1.grid(row=0, column=1)
    btnBusqueda2 = ttk.Radiobutton(frame_busqueda, text="Serie", variable=tipo_var, value="serie", style="Custom.TRadiobutton")
    btnBusqueda2.grid(row=0, column=2)

    lblBusquedaG = tk.Label(frame_busqueda, text="Género:", bg="white")
    lblBusquedaG.grid(row=1, column=0)
    CmBusqueda = ttk.Combobox(frame_busqueda, textvariable=genero_var, values=generos_disponibles, state="readonly")
    CmBusqueda.grid(row=1, column=1)
    btnBuscar = ttk.Button(frame_busqueda, text="Buscar", command=buscar)
    btnBuscar.grid(row=1, column=2)

    resultado_list = tk.Listbox(frame_busqueda, height=10)
    resultado_list.grid(row=2, column=0, columnspan=3, pady=5)

    # Frame de calificación
    lblIntrucion1 = tk.Label(root,text="\U00000032\U000020E3 Agregar calificacion y comentario\n-Asigna una calificacion (1-5).\n-Escribe tu comentario. ✍\nPulsa ´Agregar´ para guardar."
                            ,bg="white")
    lblIntrucion1.place(relx=0.46, rely=0.35, anchor="center")
    
    frame_externo_calificacion = tk.Frame(root, bg="black", bd=2, relief="solid")  
    frame_externo_calificacion.place(relx=0.46, rely=0.53, anchor="center")
    frame_calificacion = ttk.LabelFrame(frame_externo_calificacion, text="Calificar", style="Custom.TFrame")
    frame_calificacion.pack(padx=2, pady=2, fill="both", expand=True)

    
    #frame_calificacion = ttk.LabelFrame(root, text="Calificar:", style="Custom.TFrame")
    #frame_calificacion.place(relx=0.5, rely=0.5, anchor="center")

    lblCalificacion = tk.Label(frame_calificacion, text="Calificación (0-5):", bg="white")
    lblCalificacion.grid(row=0, column=0, pady=(10, 5))
    txtCalificacion = ttk.Entry(frame_calificacion, textvariable=calificacion_var)
    txtCalificacion.grid(row=0, column=1, pady=(10, 5))

    lblComentario = tk.Label(frame_calificacion, text="Comentario:", bg="white")
    lblComentario.grid(row=1, column=0, pady=(15, 5))
    txtcomentario = ttk.Entry(frame_calificacion, textvariable=comentario_var, width=30)
    txtcomentario.grid(row=1, column=1, pady=(15, 5))

    btnComentario = ttk.Button(frame_calificacion, text="Agregar Calificacion", command=agregar_calificacion)
    btnComentario.grid(row=2, column=0, columnspan=2, pady=10)

    # Frame de comentarios
    lblIntrucion1 = tk.Label(root,text="\U00000033\U000020E3 Ver comentarios\n-Accede al historial para ver tus calificaciones y comentarios previos."
                            ,bg="white")
    lblIntrucion1.place(relx=0.77, rely=0.35, anchor="center")
    
    frame_externo_comentarios = tk.Frame(root, bg="black", bd=2, relief="solid")  # Marco negro
    frame_externo_comentarios.place(relx=0.775, rely=0.575, anchor="center")
    frame_comentarios = ttk.LabelFrame(frame_externo_comentarios, text="Ver Comentarios", style="Custom.TFrame")
    frame_comentarios.pack(padx=2, pady=2, fill="both", expand=True)
    
    #frame_comentarios = ttk.LabelFrame(root, text="Ver Comentarios", style="Custom.TFrame")
    #frame_comentarios.place(relx=0.8, rely=0.5, anchor="center")

    btnMostrarCom = ttk.Button(frame_comentarios, text="Mostrar Comentarios", command=ver_comentarios)
    btnMostrarCom.pack()
    comentarios_text = tk.Text(frame_comentarios, height=10, width=50)
    comentarios_text.pack()

    mensaje_label = tk.Label(root, text="",font=("calibri", 16, "bold") ,fg="red", bg="white")
    mensaje_label.place(relx=0.5, rely=0.8, anchor="center")

menu_Bienvenida()
root.mainloop()

