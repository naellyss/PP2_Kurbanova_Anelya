-- 2. Insert new contact or update phone if user exists
CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE first_name = p_name) THEN
        UPDATE phonebook SET phone = p_phone WHERE first_name = p_name;
    ELSE
        INSERT INTO phonebook(first_name, phone) VALUES (p_name, p_phone);
    END IF;
END;
$$;


-- 3. Insert many contacts with phone validation
CREATE OR REPLACE PROCEDURE insert_many_contacts(
    IN p_names VARCHAR[],
    IN p_phones VARCHAR[],
    INOUT invalid_data TEXT[] DEFAULT '{}'
)
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
BEGIN
    invalid_data := '{}';
    FOR i IN 1..array_length(p_names, 1) LOOP
        IF p_phones[i] ~ '^\+?[0-9]{10,15}$' THEN
            IF EXISTS (SELECT 1 FROM phonebook WHERE first_name = p_names[i]) THEN
                UPDATE phonebook SET phone = p_phones[i] WHERE first_name = p_names[i];
            ELSE
                INSERT INTO phonebook(first_name, phone) VALUES (p_names[i], p_phones[i]);
            END IF;
        ELSE
            invalid_data := array_append(invalid_data, p_names[i] || ': ' || p_phones[i]);
        END IF;
    END LOOP;
END;
$$;


-- 5. Delete contact by name or phone
CREATE OR REPLACE PROCEDURE delete_contact(p_value VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM phonebook
    WHERE first_name = p_value OR phone = p_value;
END;
$$;
