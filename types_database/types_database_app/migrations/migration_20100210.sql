CREATE TABLE `types_database_app_expertregex` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(45) NOT NULL UNIQUE,
    `data_type_id` integer NOT NULL,
    `content` varchar(180) NOT NULL,
    `regexp_type` varchar(20) NOT NULL
)
;
ALTER TABLE `types_database_app_expertregex` ADD CONSTRAINT `data_type_id_refs_id_5283378d` FOREIGN KEY (`data_type_id`) REFERENCES `types_database_app_datatype` (`id`);
COMMIT;
