CREATE TABLE `bot`.`user` ( 
    `id` INT NOT NULL AUTO_INCREMENT , 
    `channel_id` TEXT NULL DEFAULT NULL , 
    `password` TEXT NOT NULL , 
    `name` TEXT NOT NULL , 
    PRIMARY KEY (`id`)
);

INSERT INTO `user` (`id`, `channel_id`, `password`, `name`)
             VALUES (NULL, '1', '123456', 'chihuahua');