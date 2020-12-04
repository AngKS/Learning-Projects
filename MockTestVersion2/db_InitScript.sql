CREATE DATABASE  IF NOT EXISTS `food_db`;
USE `food_db`;
DROP TABLE IF EXISTS `foodmenu`;

CREATE TABLE foodmenu (
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
foodName VARCHAR(50) NOT NULL,
foodDescription VARCHAR(254) NOT NULL,
price DECIMAL(4,2) NOT NULL,
reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

INSERT INTO foodmenu (foodName, foodDescription, price) values 
("Fillet o Dory", "Fillet o Dory, our delicious fish sandwich made with wild-caught fish, cheese and tartar sauce", 6.99), 
("McSpoosy", "Some kind of garlic, spicy goodness that's a hot selling item since 2001", 6.66),
("McDrumlets", "If drumlet’s your thing, our McDrumlets will send you right over the mountain. Coated with a light batter, we guarantee you’ll be Shiok ah!", 4.99),
("Double Chili Burger", "Chili, Spice, and everything nice. These were the ingredients chosen to create the perfect the Double Chili Burger", 8.99);

select * from foodMenu;