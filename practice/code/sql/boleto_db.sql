drop database boleto_db;
CREATE DATABASE IF NOT EXISTS boleto_db; 
USE boleto_db;

CREATE TABLE IF NOT EXISTS usuario(
	id_usuario INT NOT NULL AUTO_INCREMENT,
	u_name VARCHAR(35) NOT NULL,
    u_apellidop VARCHAR(35) NOT NULL,
    u_apellidom VARCHAR(35) NOT NULL,
    u_edad INT,
    u_tel VARCHAR(13),
    PRIMARY KEY(id_usuario)
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS administrador(
	id_administrador INT NOT NULL AUTO_INCREMENT,
	a_name VARCHAR(35) NOT NULL,
    a_apellidop VARCHAR(35) NOT NULL,
    a_apellidom VARCHAR(35) NOT NULL,
    a_edad INT,
    a_tel VARCHAR(13),
    PRIMARY KEY(id_administrador)
)ENGINE = INNODB;

create table if not exists pelicula(
	id_pelicula INT NOT NULL auto_increment,
	p_titulo VARCHAR(25) NOT NULL,
	p_genero VARCHAR(25) NOT NULL,
	p_sinopsis VARCHAR(25) NOT NULL,
	p_duracion INT NOT NULL,
	p_idioma VARCHAR(20) NOT NULL,
	p_clasificacion VARCHAR(5),
	primary key(id_pelicula)
)engine = InnoDB;

create table if not exists sala(
	id_sala INT NOT NULL,
	p_fila INT NOT NULL,
	p_afila INT NOT NULL,
	primary key(id_sala)
)engine = InnoDB;

CREATE TABLE IF NOT EXISTS funciones(
	id_funcion INT NOT NULL AUTO_INCREMENT,
	f_id_sala INT NOT NULL,
    f_id_pelicula INT NOT NULL,
    f_fecha DATE NOT NULL,
    f_hora TIME NOT NULL, 
    PRIMARY KEY(id_funcion),
    CONSTRAINT fkpeli_funcion 
    FOREIGN KEY(f_id_pelicula) 
		REFERENCES pelicula(id_pelicula)
       ON DELETE CASCADE
       ON UPDATE CASCADE,
	CONSTRAINT fksala_funcion
    FOREIGN KEY(f_id_sala) 
		REFERENCES sala(id_sala)
       ON DELETE CASCADE
       ON UPDATE CASCADE
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS asientos(
    id_funcion INT NOT NULL,
    id_asiento VARCHAR(3) not null,
    PRIMARY KEY(id_funcion, id_asiento),
    CONSTRAINT fksala_asiento 
    FOREIGN KEY(id_funcion) 
		REFERENCES funciones(id_funcion)
       ON DELETE CASCADE
       ON UPDATE CASCADE
)ENGINE = INNODB;

create table if not exists boleto( 
	id_boleto int not null auto_increment,
    b_id_funcion INT NOT NULL,
    b_id_asiento  VARCHAR(3) not null,
    telefono VARCHAR(35),
    PRIMARY KEY(id_boleto),
	constraint fkb_id_funcion
    foreign key(b_id_funcion, b_id_asiento)
		references asientos(id_funcion, id_asiento)
        ON DELETE CASCADE
        on update cascade
)engine = InnoDB;