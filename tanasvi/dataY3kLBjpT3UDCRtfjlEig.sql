DROP TABLE IF EXISTS `myTable`;

CREATE TABLE `myTable` (
  `id` mediumint(8) unsigned NOT NULL auto_increment,
  `name` varchar(255) default NULL,
  `phone` varchar(100) default NULL,
  `email` varchar(255) default NULL,
  `time` varchar(255),
  PRIMARY KEY (`id`)
) AUTO_INCREMENT=1;

INSERT INTO `myTable` (`name`,`phone`,`email`,`time`)
VALUES
  ("Otto Pate","(893) 566-2965","condimentum@hotmail.org","8:00 PM"),
  ("Kimberly Gentry","1-232-443-7565","nibh.lacinia.orci@hotmail.com","7:16 PM"),
  ("Lydia Perez","(348) 347-9760","integer@outlook.couk","5:14 AM"),
  ("Regina Good","(337) 981-9436","aliquam.nec@hotmail.com","9:46 AM"),
  ("Dylan Wilkinson","1-565-753-2266","dui.nec@aol.edu","4:47 PM"),
  ("Hasad Wheeler","1-325-825-1812","magna.nec.quam@hotmail.ca","3:35 PM"),
  ("Kaseem Greene","1-751-848-1548","orci@icloud.net","12:08 PM"),
  ("Dara O'donnell","1-610-542-2774","vivamus.sit.amet@outlook.edu","4:08 AM"),
  ("Jessica Blanchard","1-655-296-2862","sed.auctor.odio@hotmail.edu","3:49 AM"),
  ("Buckminster Cleveland","1-364-371-8367","neque.pellentesque@google.org","7:57 AM");
INSERT INTO `myTable` (`name`,`phone`,`email`,`time`)
VALUES
  ("Linda Livingston","1-783-228-5122","at@yahoo.net","11:30 PM"),
  ("Oscar Page","(465) 983-2815","vulputate.risus@google.com","5:40 AM"),
  ("Driscoll Merrill","(463) 449-1863","tincidunt.nunc.ac@yahoo.edu","8:07 AM"),
  ("Zachary Douglas","1-920-167-1251","morbi.accumsan@aol.edu","4:35 PM"),
  ("Sydnee Spence","(634) 321-1678","sociis.natoque.penatibus@protonmail.couk","2:46 AM"),
  ("Ira Guy","1-566-356-5955","odio.vel@icloud.edu","9:34 PM"),
  ("Keegan Middleton","1-901-455-8827","consectetuer@google.edu","7:19 PM"),
  ("Elaine Harrison","(432) 421-2888","at@aol.org","6:57 PM"),
  ("Maris Curry","1-656-244-6357","erat.nonummy@icloud.couk","1:27 AM"),
  ("Hoyt Dillon","1-774-563-6784","nisl.arcu@hotmail.ca","1:13 PM");
