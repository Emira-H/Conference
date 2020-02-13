#creation BDD hotel
CREATEDB hotel
PSQL hotel



CREATE TABLE conferencier(id SERIAL PRIMARY KEY NOT NULL, firstname VARCHAR(20) NOT NULL, name VARCHAR(20) NOT NULL, description VARCHAR(250), profession VARCHAR(250) NOT NULL, status_actif BOOL NOT NULL);

CREATE TABLE conference(id SERIAL PRIMARY KEY NOT NULL, title VARCHAR(50) NOT NULL, resume VARCHAR(250) , date DATE NOT NULL, hour TIME NOT NULL,date_creation DATE NOT NULL, id_conferencier INTEGER NOT NULL);


ALTER TABLE conference
ADD CONSTRAINT fk_conf_id_conferencier
    FOREIGN KEY (id_conferencier)
    REFERENCES conferencier (id)
    ON DELETE CASCADE;
