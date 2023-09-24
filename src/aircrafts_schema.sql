create table family (
    id           integer primary key autoincrement not null,
    name         text,
    unique(name)
);



create table company (
    id           integer primary key autoincrement not null,
    name         text,
    unique(name)
);



create table aircraft (
    id           integer primary key autoincrement not null,
    name         text,
    launch       datetime,
    id_family    integer not null references family(id),
    id_company   integer not null references company(id)
);


