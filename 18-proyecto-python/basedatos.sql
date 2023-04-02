CREATE DATABASE IF NOT EXISTS master_python;
USE master_python;

CREATE TABLE usuarios(
    id          INT(25) AUTO_INCREMENT NOT NULL,
    nombre      VARCHAR(100),
    apellidos   VARCHAR(255),
    email       VARCHAR(255) NOT NULL,
    password    VARCHAR(255) NOT NULL,
    fecha       DATE NOT NULL,
    CONSTRAINT pk_usuarios PRIMARY KEY(id),
    CONSTRAINT uq_email UNIQUE(email)
)ENGINE=InooDb;

CREATE TABLE notas(
    id              INT(25) AUTO_INCREMENT NOT NULL,
    usuario_id      INT(25) NOT NULL,
    titulo          VARCHAR(255) NOT NULL,
    descripcion     MEDIUMTEXT,
    fecha           DATE NOT NULL,
    CONSTRAINT pk_notas PRIMARY KEY(id)
    CONSTRAINT fk_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
)ENGINE=InooDb;