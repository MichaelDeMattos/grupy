create table history_imc (
cod_history_imc  integer primary key autoincrement,
name varchar(50) not null,
current_weight float not null,
height float not null,
imc float not null,
imc_result varchar(50) not null,
date_reg timestamp default current_timestamp
);
