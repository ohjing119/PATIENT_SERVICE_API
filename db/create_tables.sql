
CREATE TABLE IF NOT EXISTS public.physician
(
	physician_id SERIAL PRIMARY KEY,
    first_name character varying COLLATE pg_catalog.default,
    last_name character varying COLLATE pg_catalog.default,
    ssn character varying COLLATE pg_catalog.default NOT NULL,  
    title character varying COLLATE pg_catalog.default NOT NULL
);

CREATE TABLE IF NOT EXISTS public.patient
(
    patient_record_number SERIAL PRIMARY KEY,
    first_name character varying  NOT NULL COLLATE pg_catalog.default,
    last_name character varying  NOT NULL COLLATE pg_catalog.default,
    ssn character varying COLLATE pg_catalog.default NOT NULL,
    dob date NOT NULL,
    gender character varying COLLATE pg_catalog.default,
    mailing_address character varying COLLATE pg_catalog.default,
    physician_id bigint NOT NULL,
    insurance_id bigint    
);

CREATE TABLE IF NOT EXISTS Public.room_type (	
	room_type_id SERIAL PRIMARY KEY,
	room_type_name character varying UNIQUE
);
INSERT INTO room_type(room_type_name) VALUES ('surgery');
INSERT INTO room_type(room_type_name) VALUES ('ICU');
INSERT INTO room_type(room_type_name) VALUES ('maternity');
INSERT INTO room_type(room_type_name) VALUES ('mental_health');
INSERT INTO room_type(room_type_name) VALUES ('examine');


CREATE TABLE IF NOT EXISTS Public.room (
    room_id SERIAL PRIMARY KEY,
    room_type_name character varying NOT NULL REFERENCES room_type(room_type_name),
    available BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS public.medication
(
	medication_id SERIAL PRIMARY KEY,
	medication_name character varying  NOT NULL COLLATE pg_catalog.default,
	brand character varying COLLATE pg_catalog.default,
	medication_desc character varying COLLATE pg_catalog.default
);


CREATE TABLE IF NOT EXISTS public.appointment
(
	appointment_id SERIAL PRIMARY KEY,
	patient_record_number int NOT NULL REFERENCES public.patient(patient_record_number),
	nurse_id int,
	physician_id int NOT NULL REFERENCES physician(physician_id),
	start_date_time timestamptz NOT NULL ,
	end_date_time timestamptz NOT NULL ,
	exam_room_id int
);

CREATE TABLE IF NOT EXISTS public.prescription
(
	prescription_id SERIAL PRIMARY KEY,
	physician_id int  NOT NULL REFERENCES physician(physician_id),
	patient_record_number int  NOT NULL REFERENCES patient(patient_record_number),
	medication_id int  NOT NULL REFERENCES medication(medication_id),
	prescribed_on date NOT NULL,
	appointment_id int  NOT NULL REFERENCES appointment(appointment_id),
	dosage character varying NOT NULL,
    -- frequency? daily, weekly, monthly
    -- times? 1 / day? 
	refill int  	
);

-- hospital
CREATE TABLE IF NOT EXISTS public.hospital
(
	hospital_id SERIAL PRIMARY KEY,
	hospital_name character varying UNIQUE NOT NULL COLLATE pg_catalog.default
);

-- department
CREATE TABLE IF NOT EXISTS public.department
(
	department_id SERIAL PRIMARY KEY,
	department_name character varying UNIQUE NOT NULL COLLATE pg_catalog.default,
	hospital_id int REFERENCES hospital(hospital_id)
);

-- employee 
CREATE TABLE IF NOT EXISTS public.employee
(
	employee_id SERIAL PRIMARY KEY,
    first_name character varying  NOT NULL COLLATE pg_catalog.default,
    last_name character varying  NOT NULL COLLATE pg_catalog.default,
    ssn character varying  NOT NULL COLLATE pg_catalog.default,  
    title character varying COLLATE pg_catalog.default NOT NULL,
	-- separate gender table?
	gender character varying  COLLATE pg_catalog.default NOT NULL,
	email character varying COLLATE pg_catalog.default,
	hire_date DATE,
	department_id int REFERENCES department(department_id),
	-- employee type ? 
	-- manager_id int REFERENCES manager(manager_id)
	salary DECIMAL(10)
);

-- manager
CREATE TABLE IF NOT EXISTS public.manager
(
	manager_id SERIAL PRIMARY KEY,
	manager_emp_id INT NOT NULL REFERENCES employee(employee_id)	
);

-- nurse (nurse_patient table?)
CREATE TABLE IF NOT EXISTS public.nurse
(
	nurse_id SERIAL PRIMARY KEY,
    employee_id INT NOT NULL REFERENCES employee(employee_id)
	-- nurse_type ?
);


