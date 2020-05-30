from model.model import Model
from view.view import View
from datetime import date
from datetime import datetime

 
class Controller:
    """
    *******************************
    * A controller for a store DB *
    *******************************
    """
    def __init__(self):
        self.model = Model()
        self.view = View()
    
    def start(self):
        self.view.start()
        self.login()
        #self.main_menu()
    
    """
    ***********************
    * General controllers *
    ***********************
    """   

    def login(self):
        o = 0
        while o != '5':
            self.view.sesion_menu()
            self.view.option('5')
            o = input()
            if o == '1':
                self.login_admin()
            elif o == '2':
                self.login_user()
            elif o == '3':
                self.create_administrador()
            elif o == '4':
                self.create_client()
            elif o == '5':
                self.view.end()
            else:
                self.view.not_valid_option()
        return
            


    def login_admin(self):
        self.view.ask('Telefono: ')
        telefono = input()
        o = 0
        admins = self.model.read_all_administrador()
        while o == 0:
            for i in (range(len(admins))):
                if admins[i][5] == telefono:
                    o = 1
                    self.main_menu()
        if o == 0:
            self.view.error(' Error al inciar sesion ')
        return


    def login_user(self):
        self.view.ask('Telefono: ')
        telefono = input()
        o = 0
        admins = self.model.read_all_clients()
        while o == 0:
            for i in (range(len(admins))):
                if admins[i][5] == telefono:
                    o = 1
                    self.client_menu()
        if o == 0:
            self.view.error(' Error al inciar sesion ')
        return



    def client_menu(self):
        o = '0'
        while o != '5':
            self.view.client_main_menu()
            self.view.option('5')
            o = input()
            if o == '1':
                self.movies_client_menu()
            elif o == '2':
                self.sala_cliente_menu()
            elif o == '3':
                self.funcion_client_menu()
            elif o == '4':
                self.boleto_client_menu()
            elif o == '5':
                self.view.end()
            else:
                self.view.not_valid_option()
        return
    def main_menu(self):
        o = '0'
        while o != '8':
            self.view.main_menu()
            self.view.option('8')
            o = input()
            if o == '1':
                self.movies_menu()
            elif o == '2':
                self.client_menu()
            elif o == '3':
                self.administrador_menu()
            elif o == '4':
                self.sala_menu()
            elif o == '5':
                self.asiento_menu()
            elif o == '6':
                self.funcion_menu()
            elif o == '7':
                self.boleto_menu()
            elif o == '8':
                self.view.end()
            else:
                self.view.not_valid_option()
        return

    def update_lists(self, fs , vs):
        fields = []
        vals = []
        for f,v in zip(fs,vs):
            if v != '':
                fields.append(f+' = %s')
                vals.append(v)
        return fields, vals


    """
    **********************
    * Controllers for movies *
    **********************
    """
    def movies_client_menu(self):
        o = '0'
        while o != '3':
            self.view.movies_client_menu()
            self.view.option('3')
            o = input()
            if o == '1':
                self.read_a_movie()
            elif o == '2':
                self.read_all_movies()
            elif o == '3':
                return
            else:
                self.view.not_valid_option()
        return

    def movies_menu(self):
        o = '0'
        while o != '6':
            self.view.movies_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.create_a_movie()
            elif o == '2':
                self.read_a_movie()
            elif o == '3':
                self.read_all_movies()
            elif o == '4':
                self.update_pelicula()
            elif o == '5':
                self.delete_movie()
            elif o == '6':
                return
            else:
                self.view.not_valid_option()
        return
    def ask_movie(self):
        self.view.ask('Titulo: ')
        Titulo = input()
        self.view.ask('Genero: ')
        Genero = input()
        self.view.ask('Sinopsis: ')
        Sinopsis = input()
        self.view.ask('Duracion: ')
        Duracion = input()
        self.view.ask('Idioma: ')
        Idioma = input()
        self.view.ask('Casificacion: ')
        Clasificacion = input()
        return [Titulo,Genero,Sinopsis,Duracion,Idioma,Clasificacion]

    def create_a_movie(self):
        Titulo,Genero,Sinopsis,Duracion,Idioma,Clasificacion = self.ask_movie()
        out = self.model.create_movie(Titulo,Genero,Sinopsis,Duracion,Idioma,Clasificacion)
        if out == True:
            self.view.ok(Titulo, 'agrego')
        else:
            self.view.error('No se pudo agregar la pelicula')
        return

    def read_a_movie(self):
        self.view.ask('ID de pelicula: ')
        id_pelicula = input()
        pelicula = self.model.read_a_movie(id_pelicula)
        if type(pelicula) == tuple:
            self.view.show_movie_header('Datos de la pelicula  '+id_pelicula+' ')
            self.view.show_a_movie(pelicula)
            self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            if pelicula == None:
                self.view.error('La pelicula no existe')
            else:
                self.view.error(' Hay un problema al leer la pelicula ')
        return
    
    def read_all_movies(self):
        movies = self.model.read_all_movies()
        if type(movies) ==  list:
            self.view.show_movie_header(' Todos las peliculas ')
            for movie in movies:
                self.view.show_a_movie(movie)
            self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            self.view.error('Hay un problema todas las peliculas ')

    """
    def read_movie_year(self):
        self.view.ask('año de la pelicula: ')
        year = input()
        movies = self.model.read_a_movies_year(year)
        if type(movies) == list:
            self.view.show_movie_header('Peliculas del año  '+year+' ')
            for movie in movies:
                self.view.show_a_movie(movie)
            self.view.show_movie_footer()
        else:
            if movies == []:
                self.view.error('No hay pelicula del año '+year)
            else:
                self.view.error(' Hay un problema al leer las peliculas del año '+year)
        return"""

    def update_pelicula(self):
        self.view.ask(' ID de pelicula a modificar: ')
        id_pelicula = input()
        movie = self.model.read_a_movie(id_pelicula)
        if type(movie) == tuple:
            self.view.show_movie_header('Datos de la pelicula  '+id_pelicula+' ')
            self.view.show_a_movie(movie)
            self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            if movie == None:
                self.view.error('La pelicula no existe')
            else:
                self.view.error('Problema al leer la pelicula')
            return
        self.view.msg('Ingresa los valores a modificar ( vacio para dejarlo igual ):')
        whole_vals = self.ask_movie()
        fields, vals = self.update_lists(['p_titulo', 'p_genero', 'p_sinopsis','p_duracion','p_idioma', 'p_clasificacion'],whole_vals)
        vals.append(id_pelicula)
        vals = tuple(vals)
        out = self.model.update_movie(fields,vals)
        if out == True:
            self.view.ok(id_pelicula, 'atualizo')
        else:
            self.view.error('No se pudo actualizar')
        return

    def delete_movie(self):
        self.view.ask('ID de pelicula a borrar: ')
        id_pelicula = input()
        count = self.model.delete_movie(id_pelicula)
        if count != 0:
            self.view.ok(id_pelicula, 'Borro')
        else:
            if count == 0:

                self.view.error('La pelicula no exite')
            else:
                self.view.error('Prblema al borrar la pelicula')
        return


    """
    ***********************************
    * Controllers for clientes  *
    ***********************************
    """
    # def client_client_menu(self):
    #     o = '0'
    #     while o != '6':
    #         self.view.client_menu()
    #         self.view.option('2')
    #         o = input()
    #         if o == '1':
    #             self.create_client()
    #         elif o == '2':
    #             return
    #         else:
    #             self.view.not_valid_option()
    #     return
        
    # def client_menu(self):
    #     o = '0'
    #     while o != '6':
    #         self.view.client_menu()
    #         self.view.option('6')
    #         o = input()
    #         if o == '1':
    #             self.create_client()
    #         elif o == '2':
    #             self.read_a_client()
    #         elif o == '3':
    #             self.read_all_clients()
    #         elif o == '4':
    #             self.update_client()
    #         elif o == '5':
    #             self.delete_client()
    #         elif o == '6':
    #             return
    #         else:
    #             self.view.not_valid_option()
    #     return

    def ask_client(self):
        self.view.ask('Nombre: ')
        name = input()
        self.view.ask('Apellido paterno: ')
        sname1 = input()
        self.view.ask('Apellido materno: ')
        sname2 = input()
        self.view.ask('Edad: ')
        edad = input()
        self.view.ask('Telefono: ')
        tel = input()
        return [name,sname1,sname2,edad,tel]
    
    def create_client(self):
        name,sname1, sname2, edad, tel = self.ask_client()
        out = self.model.create_client(name, sname1, sname2, edad, tel)
        if out == True:
            self.view.ok(name+' '+sname2, 'agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR EL CLIENTE. REVISA.')
        return
    
    def read_a_client(self):
        self.view.ask('ID cliente: ')
        id_client = input()
        client = self.model.read_a_client(id_client)
        if type(client) == tuple:
            self.view.show_client_header(' Datos del cliente '+id_client+' ')
            self.view.show_a_client(client)
            self.view.show_client_midder()
            self.view.show_client_footer()
        else:
            if client == None:
                self.view.error('EL CLIENTE NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL CLIENTE. REVISA.')
        return

    def read_all_clients(self):
        clients = self.model.read_all_clients()
        if type(clients) == list:
            self.view.show_client_header( 'Todos los clientes ')
            for client in clients:
                self.view.show_a_client(client)
                self.view.show_client_midder()
            self.view.show_client_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS CLIENTES. REVISA.')
        return

    def update_client(self):
        self.view.ask('ID de cliente a modificar: ')
        id_client = input()
        client = self.model.read_a_client(id_client)
        if type(client) == tuple:
            self.view.show_client_header(' Datos del cliente '+id_client+' ')
            self.view.show_a_client(client)
            self.view.show_client_midder()
            self.view.show_client_footer()
        else:
            if client == None:
                self.view.error('EL CLIENTE NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL CLIENTE. REVISA')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_client()
        fields, vals = self.update_lists(['q_name', 'a_apellidop','a_apellidop','a_edad','a_tel'], whole_vals)
        vals.append(id_client)
        vals = tuple(vals)
        out = self.model.update_client(fields, vals)
        if out == True:
            self.view.ok(id_client, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL CLIENTE. REVISA')
        return
    
    def delete_client(self):
        self.view.ask('Id de cliente a borrar: ')
        id_client = input()
        count = self.model.delete_client(id_client)
        if count != 0:
            self.view.ok(id_client, 'borro')
        else:
            if count == 0:
                self.view.error('EL CLIENTE NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL CLIENTE. REVISA.')
        return

    """
    ****************************
    * Controllers for administrador  *
    ****************************
    """
    def administrador_menu(self):
        o = '0'
        while o != '6':
            self.view.administrador_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.create_administrador()
            elif o == '2':
                self.read_a_administrador()
            elif o == '3':
                self.read_all_administrador()
            elif o == '4':
                self.update_administrador()
            elif o == '5':
                self.delete_administrador()
            elif o == '6':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_administrador(self):
        self.view.ask('Nombre: ')
        name = input()
        self.view.ask('Apellido paterno: ')
        sname1 = input()
        self.view.ask('Apellido materno: ')
        sname2 = input()
        self.view.ask('Edad: ')
        edad = input()
        self.view.ask('Telefono: ')
        tel = input()
        return [name,sname1,sname2,edad,tel]
    
    def create_administrador(self):
        name,sname1, sname2, edad, tel = self.ask_client()
        out = self.model.create_administrador(name, sname1, sname2, edad, tel)
        if out == True:
            self.view.ok(name+' '+sname2, 'agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR EL ADMINISTRADOR. REVISA.')
        return
    
    def read_a_administrador(self):
        self.view.ask('ID administrador: ')
        id_administrador = input()
        administrador = self.model.read_a_administrador(id_administrador)
        if type(administrador) == tuple:
            self.view.show_administrador_header(' Datos del administrador '+id_administrador+' ')
            self.view.show_a_administrador(administrador)
            self.view.show_administrador_midder()
            self.view.show_administrador_footer()
        else:
            if administrador == None:
                self.view.error('EL ADMINISTRADOR NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL ADMINISTRADOR. REVISA.')
        return

    def read_all_administrador(self):
        administrador = self.model.read_all_administrador()
        if type(administrador) == list:
            self.view.show_administrador_header( 'Todos los administradores ')
            for administrador in administrador:
                self.view.show_a_administrador(administrador)
                self.view.show_administrador_midder()
            self.view.show_administrador_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS ADMINISTRADORES. REVISA.')
        return

    def update_administrador(self):
        self.view.ask('ID de administrador a modificar: ')
        id_administrador = input()
        administrador = self.model.read_a_administrador(id_administrador)
        if type(administrador) == tuple:
            self.view.show_administrador_header(' Datos del administrador '+id_administrador+' ')
            self.view.show_a_administrador(administrador)
            self.view.show_administrador_midder()
            self.view.show_administrador_footer()
        else:
            if administrador == None:
                self.view.error('EL ADMINISTRADOR NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL ADMINISTRADOR. REVISA')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_administrador()
        fields, vals = self.update_lists(['q_name', 'a_apellidop','a_apellidop','a_edad','a_tel'], whole_vals)
        vals.append(id_administrador)
        vals = tuple(vals)
        out = self.model.update_administrador(fields, vals)
        if out == True:
            self.view.ok(id_administrador, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL ADMINISTRADOR. REVISA')
        return
    
    def delete_administrador(self):
        self.view.ask('Id de administrador a borrar: ')
        id_administrador = input()
        count = self.model.delete_administrador(id_administrador)
        if count != 0:
            self.view.ok(id_administrador, 'borro')
        else:
            if count == 0:
                self.view.error('EL ADMINISTRADOR NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL ADMINISTRADOR. REVISA.')
        return

    """
    ****************************
    * Controllers for SALA  *
    ****************************
    """
    def sala_menu(self):
        o = '0'
        while o != '6':
            self.view.sala_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.create_sala()
            elif o == '2':
                self.read_a_sala()
            elif o == '3':
                self.read_all_sala()
            elif o == '4':
                self.update_sala()
            elif o == '5':
                self.delete_sala()
            elif o == '6':
                return
            else:
                self.view.not_valid_option()
        return
    def sala_cliente_menu(self):
        o = '0'
        while o != '6':
            self.view.sala_client_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.read_a_sala()
            elif o == '2':
                self.read_all_sala()
            elif o == '3':
                return
            else:
                self.view.not_valid_option()
        return
    def ask_sala(self):
        self.view.ask('sala: ')
        sala = input()
        self.view.ask('fila: ')
        fila = input()
        self.view.ask('Asiento: ')
        asiento = input()
        return [sala, fila,asiento]
    
    def create_sala(self):
        sala, fila, asiento = self.ask_sala()
        out = self.model.create_sala(sala, fila, asiento)
        if out == True:
            self.view.ok(sala, 'agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR EL ASIENTO. REVISA.')
        return
    
    def read_a_sala(self):
        self.view.ask('ID sala: ')
        id_sala = input()
        sala = self.model.read_a_sala(id_sala)
        if type(sala) == tuple:
            self.view.show_sala_header(' Datos del sala '+id_sala+' ')
            self.view.show_a_sala(sala)
            self.view.show_sala_midder()
            self.view.show_sala_footer()
        else:
            if sala == None:
                self.view.error('EL SALA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL SALA. REVISA.')
        return

    def read_all_sala(self):
        sala = self.model.read_all_sala()
        if type(sala) == list:
            self.view.show_sala_header( 'Todos los sala ')
            for sala in sala:
                self.view.show_a_sala(sala)
                self.view.show_sala_midder()
            self.view.show_sala_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS salaS. REVISA.')
        return

    def update_sala(self):
        self.view.ask('ID de salas a modificar: ')
        id_sala = input()
        sala = self.model.read_a_sala(id_sala)
        if type(sala) == tuple:
            self.view.show_sala_header(' Datos del sala '+id_sala+' ')
            self.view.show_a_sala(sala)
            self.view.show_sala_midder()
            self.view.show_sala_footer()
        else:
            if sala == None:
                self.view.error('LA sala NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL sala. REVISA')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_sala()
        fields, vals = self.update_lists(['q_name', 'a_apellidop','a_apellidop','a_edad','a_tel'], whole_vals)
        vals.append(id_sala)
        vals = tuple(vals)
        out = self.model.update_sala(fields, vals)
        if out == True:
            self.view.ok(id_sala, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL sala. REVISA')
        return
    
    def delete_sala(self):
        self.view.ask('Id de sala a borrar: ')
        id_sala = input()
        count = self.model.delete_sala(id_sala)
        if count != 0:
            self.view.ok(id_sala, 'borro')
        else:
            if count == 0:
                self.view.error('EL sala NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL sala. REVISA.')
        return

    """
    ****************************
    * Controllers for ASIENTOS  *
    ****************************
    """
    def asiento_menu(self):
        
        o = '0'
        while o != '6':
            self.view.asiento_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.create_asiento()
            elif o == '2':
                self.read_a_asiento()
            elif o == '3':
                self.read_all_asiento()
            elif o == '4':
                self.update_asiento()
            elif o == '5':
                self.delete_asiento()
            elif o == '6':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_asiento(self):
        self.view.ask('Asiento: ')
        asiento = input()
        self.view.ask('funcion: ')
        funcion = input()
        return [asiento, funcion]

    def create_asiento(self):
        asiento, funcion = self.ask_asiento()
        out = self.model.create_asiento(funcion,asiento)
        if out == True:
            self.view.ok(asiento, 'agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR EL ASIENTO. REVISA.')
        return
    
    def read_a_asiento(self):
        self.view.ask('ID asiento: ')
        id_asiento = input()
        asiento = self.model.read_a_asiento(id_asiento)
        if type(asiento) == tuple:
            self.view.show_asiento_header(' Datos del asiento '+id_asiento+' ')
            self.view.show_a_asiento(asiento)
            self.view.show_asiento_midder()
            self.view.show_asiento_footer()
        else:
            if asiento == None:
                self.view.error('EL ASIENTO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL ASIENTO. REVISA.')
        return

    def read_all_asiento(self):
        asiento = self.model.read_all_asientos()
        if type(asiento) == list:
            self.view.show_asiento_header( 'Todos los asientos ')
            for asiento in asiento:
                self.view.show_a_asiento(asiento)
                self.view.show_asiento_midder()
            self.view.show_asiento_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS ASIENTOS. REVISA.')
        return

    def update_asiento(self):
        self.view.ask('asiento a modificar: ')
        id_asiento = input()
        self.view.ask('funcion a modificar: ')
        id_funcion= input()

        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_asiento()
        fields, vals = self.update_lists(['a_id_sala', 'a_apellidop'], whole_vals)
        vals.append(id_funcion)
        vals.append(id_asiento)
        vals = tuple(vals)
        out = self.model.update_asiento(fields, vals)
        if out == True:
            self.view.ok(id_asiento, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL ASIENTO. REVISA')
        return
    
    def delete_asiento(self):
        self.view.ask('Id de asiento a borrar: ')
        id_asiento = input()
        self.view.ask('Id de funcion a borrar: ')
        id_funcion = input()
        count = self.model.delete_asiento(id_asiento, id_funcion)
        if count != 0:
            self.view.ok(id_asiento, 'borro')
        else:
            if count == 0:
                self.view.error('EL ASIENTO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL ASIENTO. REVISA.')
        return

    """
    ****************************
    * Controllers for FUNCION  *
    ****************************
    """
    def funcion_menu(self):
        o = '0'
        while o != '6':
            self.view.funcion_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.create_funcion()
            elif o == '2':
                self.read_a_funcion()
            elif o == '3':
                self.read_all_funciones()
            elif o == '4':
                self.update_funcion()
            elif o == '5':
                self.delete_funcion()
            elif o == '6':
                return
            else:
                self.view.not_valid_option()
        return
    
    def funcion_client_menu(self):
        o = '0'
        while o != '3':
            self.view.funcion_client_menu()
            self.view.option('3')
            o = input()
            if o == '1':
                self.read_a_funcion()
            elif o == '2':
                self.read_all_funciones()
            elif o == '3':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_funcion(self):
        self.view.ask('Sala: ')
        sala = input()
        self.view.ask('Pelicula: ')
        pelicula = input()
        self.view.ask('Fecha: ')
        fecha = input()
        self.view.ask('Hora: ')
        hora = input()
        return [sala, pelicula, fecha, hora]
    
    def create_funcion(self):
        self.read_all_funciones()
        self.read_all_sala()
        self.read_all_movies()
        sala, pelicula, fecha, hora = self.ask_funcion()
        out = self.model.create_funcion(sala, pelicula, fecha, hora)
        if out == True:
            self.view.ok(sala+' '+pelicula, 'agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR LA FUNCION. REVISA.')
        return
    
    def read_a_funcion(self):
        self.view.ask('ID funcion: ')
        id_funcion = input()
        funcion = self.model.read_a_funcion(id_funcion)
        if type(funcion) == tuple:
            self.view.show_funcion_header(' Datos de la funcion '+id_funcion+' ')
            self.view.show_a_funcion(funcion)
            self.view.show_funcion_midder()
            self.view.show_funcion_footer()
        else:
            if funcion == None:
                self.view.error('LA FUNCION NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL FUNCION. REVISA.')
        return

    def read_all_funciones(self):
        funcion = self.model.read_all_funciones()
        if type(funcion) == list:
            self.view.show_funcion_header( 'Todos las funciones ')
            for funcion in funcion:
                self.view.show_a_funcion(funcion)
                self.view.show_funcion_midder()
            self.view.show_funcion_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS FUNCIONES. REVISA.')
        return

    def read_funciones_date(self):
        self.view.ask('Fecha de cartelera: ')
        fecha = input()
        funcion = self.model.read_funciones_date(fecha)
        
        if type(funcion) == list:
            #self.view.show_asiento_header( )
            self.view.show_funcion_header('Todos las funciones ')
            for funcion in funcion:
                self.view.show_a_funcion(funcion)
                self.view.show_funcion_midder()
            self.view.show_funcion_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS FUNCIONES. REVISA.')
        return

    def update_funcion(self):
        self.view.ask('ID de funcion a modificar: ')
        id_funcion = input()
        funcion = self.model.read_a_funcion(id_funcion)
        if type(funcion) == tuple:
            self.view.show_funcion_header(' Datos de la funcion '+id_funcion+' ')
            self.view.show_a_funcion(funcion)
            self.view.show_funcion_midder()
            self.view.show_funcion_footer()
        else:
            if funcion == None:
                self.view.error('LA FUNCION NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL FUNCION. REVISA')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_funcion()
        fields, vals = self.update_lists(['a_id_sala', 'a_apellidop'], whole_vals)
        vals.append(id_funcion)
        vals = tuple(vals)
        out = self.model.update_funcion(fields, vals)
        if out == True:
            self.view.ok(id_funcion, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR LA FUNCION. REVISA')
        return
    
    def delete_funcion(self):
        self.view.ask('Id de funcion a borrar: ')
        id_funcion = input()
        count = self.model.delete_funcion(id_funcion)
        if count != 0:
            self.view.ok(id_funcion, 'borro')
        else:
            if count == 0:
                self.view.error('LA FUNCION NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR LA FUNCION. REVISA.')
        return

    """
    ****************************
    * Controllers for BOLETOS  *
    ****************************
    """
    def boleto_menu(self):
        o = '0'
        while o != '6':
            self.view.boleto_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.create_boleto()
            elif o == '2':
                self.read_a_boleto()
            elif o == '3':
                self.read_all_boletos()
            elif o == '4':
                self.update_boleto()
            elif o == '5':
                self.delete_boleto()
            elif o == '6':
                return
            else:
                self.view.not_valid_option()
        return
    
    def boleto_client_menu(self):
        o = '0'
        while o != '3':
            self.view.boleto_client_menu()
            self.view.option('3')
            o = input()
            if o == '1':
                self.create_boleto()
            elif o == '2':        
                self.read_a_boleto()
            elif o == '3':
                self.read_all_boletos_client()
            elif o == '4':
                return
            else:
                self.view.not_valid_option()
        return
    def ask_boleto(self):

        self.view.ask('fila de asiento: ')
        fila = input()
        self.view.ask('numero de asiento: ')
        numero = input()
        self.view.ask('telefono: ')
        telefono = input()
        return [fila, numero, telefono]
    
    def create_view_asientos(self,filas,columnas):
        asientos = []
        for i in range(filas):
            coli = []
            for j in range(columnas):
                A=[]
                A.append(chr(i+97))
                A.append(str(j))
                Num = "".join(A)
                coli.append(Num)
            asientos.append(coli)
        return asientos
                
    def create_boleto(self):
        self.read_funciones_date()
        self.view.ask('Funcion: ')
        funcion = input()
        sala = self.model.read_a_funcion(funcion)

        asientos = self.model.read_a_sala(sala[1])
        filas=asientos[1]
        columnas=asientos[2]
        vendidos=self.model.read_all_asientos_ven(funcion)
        fun = self.create_view_asientos(filas, columnas)
        
        for h in vendidos:
            fi = int(ord(h[1][0])-97)
            co = int(h[1][1])
            fun[fi][co]='-'


        for k in fun:
            print(k)

        fila, numero, telefono = self.ask_boleto()
        fun = self.create_view_asientos(filas, columnas)

        A = [fila,numero]
        ubicaicon = "".join(A)

        out = self.model.create_asiento(funcion,ubicaicon)
        if out == True:
            self.view.ok(ubicaicon, 'agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR EL ASIENTO. REVISA.')

        
        out = self.model.create_boleto(telefono,funcion,ubicaicon)
        #print(out)
        if out == True:
            self.view.ok('Boleto de usuario '+telefono, 'agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR EL BOLETO. REVISA.')

        informacion=[sala[2],sala[1],sala[4],sala[3],telefono,ubicaicon]
        self.view.show_a_print_boleto(informacion)
        
        return
    
    def read_a_boleto(self):
        self.view.ask('ID boleto: ')
        id_boleto = input()
        boleto = self.model.read_a_boleto(id_boleto)
        if type(boleto) == tuple:
            self.view.show_boleto_header(' Datos del boleto '+id_boleto+' ')
            self.view.show_a_boleto(boleto)
            self.view.show_boleto_midder()
            self.view.show_boleto_footer()
        else:
            if boleto == None:
                self.view.error('EL BOLETO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL BOLETO. REVISA.')
        return

    def read_all_boletos(self):
        boleto = self.model.read_all_boletos()
        if type(boleto) == list:
            self.view.show_boleto_header( 'Todos los boletos ')
            for boleto in boleto:
                self.view.show_a_boleto(boleto)
                self.view.show_boleto_midder()
            self.view.show_boleto_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS BOLETOS. REVISA.')
        return

    def read_all_boletos_client(self):
        self.view.ask('telefono: ')
        telefono = input()
        boleto = self.model.read_all_boletos_client(telefono)
        if type(boleto) == list:
            self.view.show_boleto_header( 'Todos los boletos ')
            for boleto in boleto:
                self.view.show_a_boleto(boleto)
                self.view.show_boleto_midder()
            self.view.show_boleto_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS BOLETOS. REVISA.')
        return

    def update_boleto(self):
        self.view.ask('ID de boleto a modificar: ')
        id_boleto = input()
        boleto = self.model.read_a_boleto(id_boleto)
        if type(boleto) == tuple:
            self.view.show_boleto_header(' Datos del boleto '+id_boleto+' ')
            self.view.show_a_boleto(boleto)
            self.view.show_boleto_midder()
            self.view.show_boleto_footer()
        else:
            if boleto == None:
                self.view.error('EL BOLETO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL BOLETO. REVISA')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_funcion()
        fields, vals = self.update_lists(['a_id_sala', 'a_apellidop'], whole_vals)
        vals.append(id_boleto)
        vals = tuple(vals)
        out = self.model.update_boleto(fields, vals)
        if out == True:
            self.view.ok(id_boleto, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL BOLETO. REVISA')
        return
    
    def delete_boleto(self):
        self.view.ask('Id de boleto a borrar: ')
        id_boleto = input()
        count = self.model.delete_boleto(id_boleto)
        if count != 0:
            self.view.ok(id_boleto, 'borro')
        else:
            if count == 0:
                self.view.error('EL BOLETO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL BOLETO. REVISA.')
        return