create table usuario
(
    nick      text not null
        constraint "Usuario_pkey"
            primary key,
    password  text not null,
    email     text,
    pais      text,
    name1     text,
    name2     text,
    lastname1 text,
    lastname2 text
);

create table jugador
(
    baneado_s_n boolean default false,
    nick        text not null
        constraint jugador_pk
            primary key
        constraint fk_nick
            references usuario
);

create table administrador
(
    nick text not null
        constraint administrador_pk
            primary key
        constraint nick_fk
            references usuario
);

create table reporta_jugador
(
    "nickReportado" text not null
        constraint nick_reportado_fk
            references jugador,
    "nickReporta"   text not null
        constraint nick_reporta_fk
            references jugador,
    constraint reporta_jugador_pkey
        primary key ("nickReportado", "nickReporta")
);

create table avatar
(
    nick            text    not null
        constraint avatar_pk
            primary key
        constraint nick_fk
            references jugador,
    "ptosExp"       integer not null,
    "ptosVelocidad" integer not null,
    "ptosVida"      integer not null,
    "ptosAtaque"    integer not null
);


