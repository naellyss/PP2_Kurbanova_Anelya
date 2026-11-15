-- 1. Procedure: add a new phone number to an existing contact
CREATE OR REPLACE PROCEDURE add_phone(
    p_contact_name VARCHAR,
    p_phone VARCHAR,
    p_type VARCHAR
)
LANGUAGE plpgsql AS $$
DECLARE
    v_contact_id INT;
BEGIN
    SELECT id INTO v_contact_id FROM contacts WHERE name = p_contact_name;

    IF v_contact_id IS NULL THEN
        RAISE EXCEPTION 'Contact "%" does not exist', p_contact_name;
    END IF;

    INSERT INTO phones (contact_id, phone, type)
    VALUES (v_contact_id, p_phone, p_type);
END;
$$;


-- 2. Procedure: move a contact to a group (creates the group if it does not exist)
CREATE OR REPLACE PROCEDURE move_to_group(
    p_contact_name VARCHAR,
    p_group_name VARCHAR
)
LANGUAGE plpgsql AS $$
DECLARE
    v_group_id INT;
BEGIN
    SELECT id INTO v_group_id FROM groups WHERE name ILIKE p_group_name;

    IF v_group_id IS NULL THEN
        INSERT INTO groups (name) VALUES (p_group_name) RETURNING id INTO v_group_id;
    END IF;

    UPDATE contacts
    SET group_id = v_group_id
    WHERE name = p_contact_name;
END;
$$;


-- 3. Function: search contacts across name, email, group, and all phones
CREATE OR REPLACE FUNCTION search_contacts(p_query TEXT)
RETURNS TABLE(
    contact_id INT,
    name VARCHAR,
    email VARCHAR,
    birthday DATE,
    group_name VARCHAR,
    phones TEXT
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        c.id,
        c.name,
        c.email,
        c.birthday,
        g.name AS group_name,
        COALESCE(STRING_AGG(p.phone || ' (' || p.type || ')', ', '), 'No phones') AS phones
    FROM contacts c
    LEFT JOIN groups g ON c.group_id = g.id
    LEFT JOIN phones p ON c.id = p.contact_id
    GROUP BY c.id, c.name, c.email, c.birthday, g.name
    HAVING c.name ILIKE '%' || p_query || '%'
        OR c.email ILIKE '%' || p_query || '%'
        OR g.name ILIKE '%' || p_query || '%'
        OR BOOL_OR(p.phone ILIKE '%' || p_query || '%')
    ORDER BY c.id;
END;
$$ LANGUAGE plpgsql;


-- Paginated contacts query function (from Practice 8 adapted for extended schema)
CREATE OR REPLACE FUNCTION get_contacts_paginated(p_limit INT, p_offset INT)
RETURNS TABLE(
    contact_id INT,
    name VARCHAR,
    email VARCHAR,
    birthday DATE,
    group_name VARCHAR,
    phones TEXT
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        c.id,
        c.name,
        c.email,
        c.birthday,
        g.name AS group_name,
        COALESCE(STRING_AGG(p.phone || ' (' || p.type || ')', ', '), 'No phones') AS phones
    FROM contacts c
    LEFT JOIN groups g ON c.group_id = g.id
    LEFT JOIN phones p ON c.id = p.contact_id
    GROUP BY c.id, c.name, c.email, c.birthday, g.name
    ORDER BY c.id
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;
