CREATE TABLE IF NOT EXISTS `Zoo` (
	`id` integer primary key NOT NULL UNIQUE,
	`nombre` TEXT NOT NULL,
	`direccion` TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS `Habitat` (
	`id` integer primary key NOT NULL UNIQUE,
	`nombre` TEXT NOT NULL,
	`clima` TEXT NOT NULL,
	`tamano` REAL NOT NULL
);
CREATE TABLE IF NOT EXISTS `Empleado` (
	`id` integer primary key NOT NULL UNIQUE,
	`nombre` TEXT NOT NULL,
	`apellido` TEXT NOT NULL,
	`posicion` TEXT NOT NULL,
	`anos_experiencia` INTEGER NOT NULL,
	`zoo_id` INTEGER NOT NULL,
FOREIGN KEY(`zoo_id`) REFERENCES `Zoo`(`id`)
);
CREATE TABLE IF NOT EXISTS `1716003382` (

);
CREATE TABLE IF NOT EXISTS `Visitante` (
	`id` integer primary key NOT NULL UNIQUE,
	`nombre` TEXT NOT NULL,
	`apellido` TEXT NOT NULL,
	`cedula` TEXT NOT NULL,
	`fecha_visita` REAL NOT NULL,
	`zoo_id` INTEGER NOT NULL,
FOREIGN KEY(`zoo_id`) REFERENCES `Zoo`(`id`)
);
CREATE TABLE IF NOT EXISTS `Animal` (
	`id` integer primary key NOT NULL UNIQUE,
	`nombre` TEXT NOT NULL,
	`edad` INTEGER NOT NULL,
	`especie` TEXT NOT NULL,
	`zoo_id` INTEGER NOT NULL,
	`habitat_id` INTEGER NOT NULL,
FOREIGN KEY(`zoo_id`) REFERENCES `Zoo`(`id`),
FOREIGN KEY(`habitat_id`) REFERENCES `Habitat`(`id`)
);


FOREIGN KEY(`zoo_id`) REFERENCES `Zoo`(`id`)

FOREIGN KEY(`zoo_id`) REFERENCES `Zoo`(`id`)
FOREIGN KEY(`zoo_id`) REFERENCES `Zoo`(`id`)
FOREIGN KEY(`habitat_id`) REFERENCES `Habitat`(`id`)