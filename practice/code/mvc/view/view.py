class View:
    """
    **************************
    * A view for a boletos DB *
    **************************
    """
    def start(self):
        print('==============')
        print('= Bienvenido =')
        print('==============')

    def end(self):
        print('================================')
        print('=        Hasta la vista!       =')
        print('================================')

    def main_menu(self):
        print('================================')
        print('=        Menu Principal        =')
        print('================================')
        print('1. Películas')
        print('2. Cliente')
        print('3. Administrador')
        print('4. Sala')
        print('5. Asiento')
        print('6. Funciones')
        print('7. Boleto')
        print('8. Salir')

    def client_main_menu(self):
        print('================================')
        print('=        Menu Principal        =')
        print('================================')
        print('1. Películas')
        print('2. Sala')
        print('3. Funciones')
        print('4. Boleto')
        print('5. Salir')

    def sesion_menu(self):
        print('================================')
        print('=        Menu Principal        =')
        print('================================')
        print('1. Login admin')
        print('2. Login clinet')
        print('3. Create admin')
        print('4. Create user')
        print('5. Salir')

    def option(self,last):
        print('Selecciona un opcion (1-'+last+'): ', end = '')

    def not_valid_option(self):
        print('Opcion no valida!\nIntenta de nuevo')
    
    def ask(self, output):
        print(output, end = '' )
    
    def msg(self, output):
        print(output)

    def ok(self, id, op):
        print('+'*(len(str(id))+len(op)+24))
        print('+'+str(id)+' se '+op+' correctamente! +')
        print('+'*(len(str(id))+len(op)+24))
    
    def error(self, err):
        print(' Error! '.center(len(err)+4,'-'))
        print('-'+err+'-')
        print('-'*(len(err)+4))
    

    """
    *********************
    * A view for movies *
    *********************
    """
    def movies_menu(self):
        print('************************')
        print('* -- Submenu Movies -- *')
        print('************************')
        print('1. Agregar Pelicula')
        print('2. Mostrar Pelicula')
        print('3. Mostrar todas las Peliculas')
        print('4. Modificar Pelicula')
        print('5  Borrar pelicula')
        print('6. Regresar')
    
    def movies_client_menu(self):
        print('************************')
        print('* -- Submenu Movies -- *')
        print('************************')
        print('1. Mostrar Pelicula')
        print('2. Mostrar todas las Peliculas')
        print('3. Regresar')

    def show_a_movie(self, record):
        if record[3] == None:
            print(f'{record[0]:<3}|{record[1]:<28}|{record[2]:<19}|'+'                    '+f'|{record[4]:<5}')
        else:
            print(f'{record[0]:<3}|{record[1]:<28}|{record[2]:<19}|{record[3]:<20}|{record[4]:<8}|{record[5]:<25}|{record[6]:<6}')
    
    def show_movie_header(self, header):
        print(header.center(120,'*'))
        print('ID'.ljust(3)+'|'+'Titulo'.ljust(28)+'|'+'Genero'.ljust(19)+'|'+'Sinopsis'.ljust(20)+'|'+'Duracion'.ljust(8)+'|'+'Idioma'.ljust(25)+'|'+'Clasificacion'.ljust(8))
        print('-'*120)

    def show_movie_midder(self):
        print('-'*120)
    
    def show_movie_footer(self):
        print('-'*120)

    def show_a_detail(self, record):
        print(f'{record[0]:<3}|{record[1]:<19}|{record[2]:<19}|{record[3]:<100}|{record[4]:<8}|{record[5]:<5}|{record[6]:<6}   ')
    
    #def show_detail_header(self, header):
    #    print(header.center(92,'*'))
    #    print('ID'.ljust(3)+'|'+'Pelicula'.ljust(20)+'|'+'Director'.ljust(20)+'|'+'Descripcion'.ljust(100)+'|'+'Duracion'.ljust(8))
    #    print('-'*156)

    def show_detail_midder(self):
        print('-'*156)
    
    def show_detail_footer(self):
        print('-'*156)

    """
    *********************
    * Views for clients *
    *********************
    """
    def client_menu(self):
        print('**************************')
        print('* -- Submenu Clientes -- *')
        print('**************************')
        print('1. Agregar cliente')
        print('2. Leer cliente')
        print('3. Leer todos los clientes')
        print('4. Actualizar cliente')
        print('5. Borrar cliente')
        print('6. Regresar')

    def client_client_menu(self):
        print('**************************')
        print('* -- Submenu Clientes -- *')
        print('**************************')
        print('1. Agregar cliente')
        print('2. Leer cliente')
        print('3. Leer todos los clientes')
        print('4. Actualizar cliente')
        print('5. Borrar cliente')
        print('6. Regresar')


    def show_a_client(self, record):
        print('ID', record[0])
        print('Nombre:', record[1])
        print('Apellido paterno:', record[2])
        print('Apellido materno:', record[3])
        print('Edad:', record[4])
        print('Telefono:', record[5])

    def show_a_client_brief(self, record):
        print('ID', record[0])
        print('Nombre:', record[1]+' '+record[2]+' '+record[3])
        print('Edad:', record[4])
        print('Telefono:', record[5])

    def show_client_header(self, header):
        print(header.center(53, '*'))
        print('-'*53)

    def show_client_midder(self):
        print('-'*53)

    def show_client_footer(self):
        print('*'*53)

    """
    *****************************
    * Views for administradores *
    *****************************
    """
    def administrador_menu(self):
        print('*********************************')
        print('* -- Submenu Administradores -- *')
        print('*********************************')
        print('1. Agregar administrador')
        print('2. Leer administrador')
        print('3. Leer todos los administrador')
        print('4. Actualizar administrador')
        print('5. Borrar administrador')
        print('6. Regresar')

    def show_a_administrador(self, record):
        print('ID', record[0])
        print('Nombre:', record[1])
        print('Apellido paterno:', record[2])
        print('Apellido materno:', record[3])
        print('Edad:', record[4])
        print('Telefono:', record[5])

    def show_a_administrador_brief(self, record):
        print('ID', record[0])
        print('Nombre:', record[1]+' '+record[2]+' '+record[3])
        print('Edad:', record[4])
        print('Telefono:', record[5])

    def show_administrador_header(self, header):
        print(header.center(53, '*'))
        print('-'*53)

    def show_administrador_midder(self):
        print('-'*53)

    def show_administrador_footer(self):
        print('*'*53)

    """
    *****************************
    * Views for salas *
    *****************************
    """
    def sala_menu(self):
        print('*********************************')
        print('* -- Submenu salas -- *')
        print('*********************************')
        print('1. Agregar sala')
        print('2. Leer sala')
        print('3. Leer todos los salas')
        print('4. Actualizar sala')
        print('5. Borrar sala')
        print('6. Regresar')

    def sala_client_menu(self):
        print('*********************************')
        print('* -- Submenu salas -- *')
        print('*********************************')
        print('1. Leer sala')
        print('2. Leer todos los salas')
        print('3. Regresar')

    def show_a_sala(self, record):
        print('Sala', record[0])
        print('Fila:', record[1])
        print('Asientos Fila:', record[2])
        print('Caácidad: ',record[2]*record[1], ' personas')

    def show_a_sala_brief(self, record):
        print('Sala', record[0])
        print('Fila:', record[1])
        print('Asientos Fila:', record[2])

    def show_sala_header(self, header):
        print(header.center(53, '*'))
        print('-'*53)

    def show_sala_midder(self):
        print('-'*53)

    def show_sala_footer(self):
        print('*'*53)

    """
    *****************************
    * Views for asiento *
    *****************************
    """
    def asiento_menu(self):
        print('*********************************')
        print('* -- Submenu asiento -- *')
        print('*********************************')
        print('1. Agregar asiento')
        print('2. Leer asiento')
        print('3. Leer todos los asiento')
        print('4. Actualizar asiento')
        print('5. Borrar asiento')
        print('6. Regresar')

    def show_a_asiento(self, record):
        print('Funcion', record[0])
        print('Asiento:', record[1])

    def show_a_asiento_brief(self, record):
        print('Funcion', record[0])
        print('Asiento:', record[1])

    def show_asiento_header(self, header):
        print(header.center(53, '*'))
        print('-'*53)

    def show_asiento_midder(self):
        print('-'*53)

    def show_asiento_footer(self):
        print('*'*53)

    """
    *****************************
    * Views for funcion *
    *****************************
    """
    def funcion_menu(self):
        print('*********************************')
        print('* -- Submenu Funcion -- *')
        print('*********************************')
        print('1. Agregar funcion')
        print('2. Leer funcion')
        print('3. Leer todos las funciones')
        print('4. Actualizar funcion')
        print('5. Borrar funcion')
        print('6. Regresar')

    def funcion_client_menu(self):
        print('*********************************')
        print('* -- Submenu Funcion -- *')
        print('*********************************')
        print('1. Leer funcion')
        print('2. Leer todos las funciones')
        print('3. Regresar')

    def show_a_funcion(self, record):
        print(f'{record[0]:<7}|{record[1]:<5}|{record[2]:<23}|{record[3]}|{record[4]}')

    def show_funcion_header(self, header):
        print(header.center(80,'*'))
        print('Funcion'.ljust(7)+'|'+'Sala'.ljust(5)+'|'+'Pelicula'.ljust(23)+'|'+'Fecha'.ljust(10)+'|'+'Hora'.ljust(8))
        print('-'*80)

    def show_funcion_midder(self):
        print('-'*80)

    def show_funcion_footer(self):
        print('*'*80)

    """
    *****************************
    * Views for Boleto *
    *****************************
    """
    def boleto_menu(self):
        print('*********************************')
        print('* -- Submenu Boleto -- *')
        print('*********************************')
        print('1. Comprar boleto')
        print('2. Leer boleto')
        print('3. Leer todos los boletos')
        print('4. Actualizar boleto')
        print('5. Borrar boleto')
        print('6. Regresar')
    
    def boleto_client_menu(self):
        print('*********************************')
        print('* -- Submenu Boleto -- *')
        print('*********************************')
        print('1. Comprar boleto')
        print('2. Leer boleto')
        print('3. Leer todos los boletos')
        print('4. Regresar')

    def show_a_boleto(self, record):
        print(record)
        print('ID boleto', record[0])
        print('Sala:', record[1])
        print('Asiento:', record[2])
        print('Telefono:', record[4])

    def show_a_print_boleto(self, record):
        print('\t________________________________')
        print('\n\t   ¡¡DISFURUTE SU PELICULA!!')
        print('\t________________________________')
        print('\t|>Pelicula', record[0],'\t\t|')
        print('\t|>Asiento:', record[5],'\t\t\t|')
        print('\t|>Sala:', record[1],'\t\t\t|')
        print('\t|>Hora:', record[2],'\t\t|')
        print('\t|>Dia', record[3],'\t\t|')
        print('\t|>Telefono:', record[4],'\t\t|')
        print('\t|_______________________________|')
        print('\n\t ¡¡Gracias, Vuelva Pronto :D!!')
        print('\t________________________________\n')

    def show_a_boleto_brief(self, record):
        print('Funcion', record[0])
        print('Asiento:', record[1])
        print('Telefono:', record[2])

    def show_boleto_header(self, header):
        print(header.center(53, '*'))
        print('-'*53)

    def show_boleto_midder(self):
        print('-'*53)

    def show_boleto_footer(self):
        print('*'*53)