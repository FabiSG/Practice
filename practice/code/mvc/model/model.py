from mysql import connector

class Model:
    """
    *****************************************
    * a data model with MySQL for a boleto DB*
    *****************************************
    """
    def __init__(self, config_db_file='config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()

    def read_config_db(self):
        d={}
        with open(self.config_db_file ) as f_r:
            for line in f_r: 
                (key, val) = line.strip().split(':')
                d[key] = val
        return d

    def connect_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor()

    def close_db(self):
        self.cnx.close()

    """
    *********************
    * peliculas metodos*
    *********************
    """
    def create_movie(self,titulo, genero,sinopsis,duracion,idioma,clasificacion):
        try:
            sql = 'INSERT INTO pelicula(`p_titulo`, `p_genero`,`p_sinopsis`,`p_duracion`,`p_idioma`,`p_clasificacion`) VALUES (%s,%s,%s,%s,%s,%s)'
            vals = (titulo, genero,sinopsis,duracion,idioma,clasificacion)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print (err)
            return err

    def read_a_movie(self,id_pelicula):
        try:
            sql = 'SELECT * FROM pelicula WHERE id_pelicula = %s'
            vals = (id_pelicula,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_movies(self):
        try:
            sql = 'SELECT * FROM pelicula'
            self.cursor.execute(sql)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err
    
    def update_movie(self,fields,vals):
        try:
            sql = 'UPDATE pelicula SET '+','.join(fields)+'WHERE id_pelicula = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_movie(self, id_pelicula):
        try:
            sql = 'DELETE FROM pelicula WHERE id_pelicula = %s'
            vals = (id_pelicula,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    *********************
    * usuario metodos*
    *********************
    """
    def create_client(self,nombre, apellidop,apellidom,edad,tel):
        try:
            sql = 'INSERT INTO usuario (`u_name`, `u_apellidop`,`u_apellidom`,`u_edad`,`u_tel`) VALUES (%s,%s,%s,%s,%s)'
            vals = (nombre, apellidop,apellidom,edad,tel)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return err

    def read_a_client(self,id_usuario):
        try:
            sql = 'SELECT * FROM usuario WHERE id_usuario = %s'
            vals = (id_usuario,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_clients(self):
        try:
            sql = 'SELECT * FROM usuario'
            self.cursor.execute(sql)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err
    
    def update_client(self,fields,vals):
        try:
            sql = 'UPDATE usuario SET '+','.join(fields)+'WHERE id_usuario = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_client(self, id_usuario):
        try:
            sql = 'DELETE FROM usuario WHERE id_usuario = %s'
            vals = (id_usuario,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    """
    *********************
    * administrador metodos*
    *********************
    """
    def create_administrador(self,nombre, apellidop, apellidom,edad,tel):
        try:
            sql = 'INSERT INTO administrador (`a_name`, `a_apellidop`,`a_apellidom`,`a_edad`,`a_tel`) VALUES (%s,%s,%s,%s,%s)'
            vals = (nombre, apellidop, apellidom,edad,tel)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_administrador(self,id_administrador):
        try:
            sql = 'SELECT * FROM administrador WHERE id_administrador = %s'
            vals = (id_administrador,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_administrador(self):
        try:
            sql = 'SELECT * FROM administrador'
            self.cursor.execute(sql)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err
    
    def update_administrador(self,fields,vals):
        try:
            sql = 'UPDATE administrador SET '+','.join(fields)+'WHERE id_administrador = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_administrador(self, id_administrador):
        try:
            sql = 'DELETE FROM usuario WHERE id_usuario = %s'
            vals = (id_administrador,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ***********************
    * SALA metodos*
    ***********************
    """
    def create_sala(self, sala,p_fila, p_afila):
        try:
            sql = 'INSERT INTO sala (`id_sala`, `p_fila`, `p_afila`) VALUES (%s,%s, %s)'
            vals = (sala, p_fila, p_afila)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_sala(self,id_sala):
        try:
            sql = 'SELECT * FROM sala WHERE id_sala = %s'
            vals = (id_sala,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_sala(self):
        try:
            sql = 'SELECT * FROM sala'
            self.cursor.execute(sql)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err
    
    def update_sala(self,fields,vals):
        try:
            sql = 'UPDATE sala SET '+','.join(fields)+'WHERE id_sala = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_sala(self, id_sala):
        try:
            sql = 'DELETE FROM sala WHERE id_sala = %s'
            vals = (id_sala,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ***********************
    * asientos metodos*
    ***********************
    """
    def create_asiento(self,funcion, asiento):
        try:
            sql = 'INSERT INTO asientos (`id_funcion`, `id_asiento`) VALUES (%s, %s )'
            vals = (funcion, asiento)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_asiento(self,id_asiento):
        try:
            sql = 'SELECT * FROM asientos WHERE id_asiento = %s'
            vals = (id_asiento,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_asientos(self):
        try:
            sql = 'SELECT * FROM asientos'
            self.cursor.execute(sql)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err

    def read_all_asientos_ven(self,fun):
        try:
            sql = 'SELECT * FROM asientos WHERE id_funcion = %s'
            vals = (fun,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err
    
    def update_asiento(self,fields,vals):
        try:
            sql = 'UPDATE asientos SET '+','.join(fields)+'WHERE id_asiento = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_asiento(self, id_funcion, id_asiento):
        try:
            sql = 'DELETE FROM asientos WHERE id_funcion = %s AND id_asiento = %s'
            vals = (id_asiento,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ***********************
    * funcion metodos*
    ***********************
    """
    def create_funcion(self, sala, pelicula, fecha, hora):
        try:
            sql = 'INSERT INTO funciones(`f_id_sala`,`f_id_pelicula`, `f_fecha`, `f_hora`) VALUES (%s,%s,%s, %s )'
            vals = (sala, pelicula, fecha, hora)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return err

    def read_a_funcion(self,id_funcion):
        try: 
            sql = 'SELECT funciones.id_funcion, funciones.f_id_sala, pelicula.p_titulo, funciones.f_fecha, funciones.f_hora FROM funciones join pelicula on f_id_pelicula = id_pelicula where funciones.id_funcion = %s'
            vals = (id_funcion,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_funciones(self):
        try:
            sql = 'SELECT funciones.id_funcion, funciones.f_id_sala, pelicula.p_titulo, funciones.f_fecha, funciones.f_hora FROM funciones join pelicula on f_id_pelicula = id_pelicula'
            self.cursor.execute(sql)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err

    def read_funciones_date(self, date):
        try:
            sql = 'SELECT funciones.id_funcion, funciones.f_id_sala, pelicula.p_titulo, funciones.f_fecha, funciones.f_hora FROM funciones join pelicula on f_id_pelicula = id_pelicula WHERE f_fecha = %s'
            vals = (date,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err
    
    def update_funcion(self,fields,vals):
        try:
            sql = 'UPDATE funciones SET '+','.join(fields)+'WHERE id_funcion = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_funcion(self, id_funcion):
        try:
            sql = 'DELETE FROM funciones WHERE id_funcion= %s'
            vals = (id_funcion,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ***********************
    * boleto metodos*
    ***********************
    """
    def create_boleto(self,usuario, funcion, asiento):
        try:
            sql = 'INSERT INTO boleto(`telefono`, `b_id_funcion`, `b_id_asiento`) VALUES (%s, %s,%s )'
            vals = (usuario, funcion, asiento)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_boleto(self,id_boleto):
        try:
            sql = 'SELECT * FROM boleto WHERE id_boleto = %s'
            vals = (id_boleto,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_a_boleto_fun(self,id_fun):
        try:
            sql = 'SELECT * FROM boleto WHERE id_funcion = %s'
            vals = (id_fun,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err


    def read_all_boletos(self):
        try:
            sql = 'SELECT * FROM boleto'
            self.cursor.execute(sql)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err

    def read_all_boletos_client(self,telefono):
        try:
            sql = 'SELECT * FROM boleto WHERE telefono = %s'
            vals = (telefono,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err
    
    def update_boleto(self,fields,vals):
        try:
            sql = 'UPDATE boleto SET '+','.join(fields)+'WHERE id_boleto = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_boleto(self, id_boleto):
        try:
            sql = 'DELETE FROM boleto WHERE id_boleto= %s'
            vals = (id_boleto,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err