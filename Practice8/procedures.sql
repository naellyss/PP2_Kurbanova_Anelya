-- 2. Procedure to insert a new user by name and phone; if the user already exists, update their phone
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


-- 3. Procedure to insert many new users from a list of names and phones
--    Uses a loop and IF inside the procedure, validates phone correctness, and returns all incorrect data
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
    FOR i IN 1 .. COALESCE(array_length(p_names, 1), 0) LOOP
        -- Validate phone: optional '+' followed by 10 to 15 digits
        IF p_phones[i] ~ '^\+?[0-9]{10,15}$' THEN
            IF EXISTS (SELECT 1 FROM phonebook WHERE first_name = p_names[i]) THEN
                UPDATE phonebook SET phone = p_phones[i] WHERE first_name = p_names[i];
            ELSE
                INSERT INTO phonebook(first_name, phone)
                VALUES (p_names[i], p_phones[i])
                ON CONFLICT (phone) DO NOTHING;
            END IF;
        ELSE
            invalid_data := array_append(invalid_data, p_names[i] || ': ' || p_phones[i]);
        END IF;
    END LOOP;
END;
$$;


-- 5. Procedure to delete data from the table by username or phone
CREATE OR REPLACE PROCEDURE delete_contact(p_value VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM phonebook
    WHERE first_name = p_value OR phone = p_value;
END;
$$;
