#from model.model import Model

from controller.controller import Controller

c = Controller()

c.start()



#from model.model import Model
##
#m = Model()
#
#m.create_movie('avatar', 'ciencia ficcion', 'Monitos azules', '180', 'ingles-subtitulada E', 'a')
#m.create_movie('cuando te encuentre', 'romantica', 'historia de amor ', '120', 'ingles-subtitulada E', 'a')
#m.create_sala(1,5,5)
#m.create_sala(2,6,8)
#m.create_funcion(1,1,'2020-05-28','13:30')
#m.create_funcion(1,2,'2020-04-28','12:30')

#m.create_funcion(2,2,'2020-05-28','15:00')


#data = m.read_all_asientos_ven(2)
#print(data)
#for h in data:
#    fi = int(ord(h[1][0])-97)
#    co = int(h[1][1])
#    print(fi,co)

#movie=m.read_a_movie(1)
#movie=m.read_all_movies()
#print(movie)

#m.create_client('Fabiola', 'Sierra', 'Gonzalez', '24', '4561292145')
#m.create_client('lola', 'lopez', 'perez', '23', '4561225544')
#usuario=m.read_a_client(1)
#usuario=m.read_all_clients()
#print(usuario)

#m.create_administrador('karla', 'medina', 'servin', '33', '4561778956')
#m.create_administrador('Majo', 'Guzman', 'Valades', '24', '4561885544')
#admin=m.delete_administrador(1)
#admin=m.read_all_administrador()
#print(admin)
#
#m.close_db()


